# 📅 WEEK 4 — Jul 20-26 (Mon-Sun): UART INTERRUPTS + SYSTICK + NVIC

> **Topics**: UART interrupt-driven RX, NVIC interrupt system, SysTick timer, interrupt priorities, non-blocking patterns
> **FastBit MCU1**: Interrupt sections, NVIC, SysTick
> **FastBit ARM Cortex**: NVIC deep dive, exception model, priority
> **"Mastering STM32" Book**: Chapter 7 (Interrupts), Chapter 8 revisit (UART interrupts)
> **Reference Manual**: RM0383 Section 10 (Interrupts/NVIC), Section 19 (USART interrupt mode)
> **Programs on hardware**: 4-6
> **German**: Nicos Weg A2 Lessons 14-18

---

## DAY 20 — Monday, Jul 20

### 🔶 Morning Block (5:10 - 6:30 AM) — INTERRUPT THEORY + NVIC

#### 📺 WATCH (20 min)
**FastBit ARM Cortex**: NVIC section — interrupt basics, vector table, priorities

#### 📖 STUDY (1h)

**What is an interrupt?**
```
Normal execution:      main() → while(1) → process → process → ...
                                                ↑
With interrupt:        main() → while(1) → process → [IRQ!] → ISR() → resume → ...
                                                                  ↑
                                                           Interrupt Service Routine
                                                           (runs automatically)
```

**Key concepts:**
- **IRQ** (Interrupt Request): hardware signal that something happened
- **ISR** (Interrupt Service Routine): function that runs when interrupt fires
- **NVIC** (Nested Vectored Interrupt Controller): manages all interrupts
- **Vector table**: array of ISR addresses at start of flash memory
- **Priority**: 0 = highest, 15 = lowest (on STM32F411, 4 priority bits)
- **Nesting**: higher priority interrupt can preempt lower priority

**Why interrupts matter for UART:**
- `HAL_UART_Receive()` is **BLOCKING** — CPU waits doing nothing
- With interrupt: CPU does useful work, gets notified when data arrives
- This is how ALL professional firmware works

**Draw on paper:**
1. The vector table (addresses 0x00 to 0x1FF)
2. NVIC priority grouping (preemption vs sub-priority)

### ✅ Day 20 Checklist
- [ ] Understand: IRQ, ISR, NVIC, vector table, priority
- [ ] Know why blocking UART is bad (wastes CPU time)
- [ ] Drew vector table on paper
- [ ] Read RM0383 Section 10 (Interrupts)

---

## DAY 21 — Tuesday, Jul 21

### 🔶 Morning Block (5:10 - 6:30 AM) — UART INTERRUPT RX (HAL)

#### 💻 CODE (1h 20m)

Create `10_uart_interrupt_hal`:

**CubeMX setup:**
1. Enable USART2 (same as before)
2. Go to NVIC tab → enable **USART2 global interrupt**
3. Set priority: Preemption = 1, Sub = 0
4. Generate code

**In main.c:**
```c
uint8_t rx_data;

int main(void) {
    // ... init code ...
    
    // Start interrupt-driven receive (1 byte at a time)
    HAL_UART_Receive_IT(&huart2, &rx_data, 1);
    
    printf("STM32 ready! Type something...\r\n");
    
    while (1) {
        // Main loop is FREE to do other work!
        HAL_GPIO_TogglePin(GPIOC, GPIO_PIN_13);
        HAL_Delay(500);
        // LED keeps blinking even while waiting for UART data
    }
}

// This callback fires when a byte is received
void HAL_UART_RxCpltCallback(UART_HandleTypeDef *huart) {
    if (huart->Instance == USART2) {
        // Process received byte
        printf("Received: '%c'\r\n", rx_data);
        
        // IMPORTANT: restart receive for next byte
        HAL_UART_Receive_IT(&huart2, &rx_data, 1);
    }
}
```

**The KEY difference**: The LED keeps blinking! With blocking receive, the LED would stop while waiting. With interrupt, the CPU does useful work and only handles UART when data actually arrives.

### ✅ Day 21 Checklist
- [ ] UART interrupt receive working — LED blinks while receiving
- [ ] Callback function fires on each received byte
- [ ] Understand: HAL_UART_Receive_IT → callback → restart pattern
- [ ] Can explain: why interrupt-driven is better than blocking

---

## DAY 22 — Wednesday, Jul 22

### 🔶 Morning Block (5:10 - 6:30 AM) — UART RX WITH CIRCULAR BUFFER

#### 💻 CODE (1h 20m)

**The real-world pattern**: Interrupt puts data into circular buffer → main loop processes it.

```c
// Reuse YOUR circular buffer from June!
#include "ringbuf.h"

CircularBuffer uart_rx_buf;
uint8_t rx_byte;

void HAL_UART_RxCpltCallback(UART_HandleTypeDef *huart) {
    if (huart->Instance == USART2) {
        cbuf_write(&uart_rx_buf, rx_byte);
        HAL_UART_Receive_IT(&huart2, &rx_byte, 1);
    }
}

// In main loop:
while (1) {
    uint8_t data;
    while (cbuf_read(&uart_rx_buf, &data) == 0) {
        // Process each buffered byte
        process_command(data);
    }
    
    // Other tasks continue running
    update_leds();
    check_buttons();
}
```

> **⚠️ This is the EXACT pattern used in production firmware.** Interrupt fills buffer, main loop drains it. Your June circular buffer code works UNCHANGED on STM32.

### ✅ Day 22 Checklist
- [ ] Circular buffer integrated with UART interrupt
- [ ] Main loop processes buffered data while doing other tasks
- [ ] June's ringbuf.c/h working on STM32 without modification
- [ ] LED + button + UART all working simultaneously

---

## DAY 23 — Thursday, Jul 23

### 🔶 Morning Block (5:10 - 6:30 AM) — SYSTICK + HAL_DELAY

#### 📺 WATCH (15 min)
**FastBit ARM Cortex**: SysTick timer section

#### 💻 CODE (1h)

**SysTick**: A 24-bit countdown timer built into every ARM Cortex-M core.
- HAL uses it for `HAL_Delay()` and `HAL_GetTick()`
- It fires an interrupt every 1 ms (configured in `HAL_Init()`)

**Exercise 1 — Understand SysTick:**

Open `stm32f4xx_it.c` → find `SysTick_Handler()`:
```c
void SysTick_Handler(void) {
    HAL_IncTick();  // Increments a 32-bit counter every 1 ms
}
```

Open HAL source → find `HAL_Delay()`:
```c
void HAL_Delay(uint32_t Delay) {
    uint32_t tickstart = HAL_GetTick();
    while ((HAL_GetTick() - tickstart) < Delay) {
        // Busy wait — CPU spins here doing nothing!
    }
}
```

**Problem**: `HAL_Delay()` wastes CPU. Better pattern:

```c
uint32_t led_last_toggle = 0;
uint32_t uart_last_send = 0;

while (1) {
    uint32_t now = HAL_GetTick();
    
    // Toggle LED every 500ms (non-blocking!)
    if (now - led_last_toggle >= 500) {
        HAL_GPIO_TogglePin(GPIOC, GPIO_PIN_13);
        led_last_toggle = now;
    }
    
    // Send UART message every 2000ms (non-blocking!)
    if (now - uart_last_send >= 2000) {
        printf("Uptime: %lu ms\r\n", now);
        uart_last_send = now;
    }
    
    // Process UART buffer (non-blocking!)
    process_uart_buffer();
}
```

> **This is called "cooperative multitasking" — you run multiple "tasks" without an RTOS.** When you learn FreeRTOS in Phase 3, it does this scheduling for you.

### ✅ Day 23 Checklist
- [ ] SysTick understood — 1 ms interrupt, HAL_GetTick()
- [ ] HAL_Delay replaced with non-blocking tick comparison
- [ ] Multiple "tasks" running simultaneously without RTOS
- [ ] Can explain: why HAL_Delay is bad in real firmware

---

## DAY 24 — Friday, Jul 24

### 🔶 Morning Block (5:10 - 6:30 AM) — INTERRUPT PRIORITIES

#### 💻 CODE (1h 20m)

**Exercise — Priority experiment:**

Set up:
- SysTick (priority 15 — lowest)
- USART2 (priority 1 — high)
- EXTI (button on PA0, priority 0 — highest)

Test nesting:
1. SysTick fires every 1ms → increments counter
2. While SysTick is running, press button → EXTI preempts SysTick
3. While button ISR is running, receive UART → does UART preempt?

```c
void EXTI0_IRQHandler(void) {
    printf("BUTTON ISR start\r\n");
    HAL_Delay(1000);  // Simulate long ISR (BAD practice, but good for learning)
    printf("BUTTON ISR end\r\n");
    HAL_GPIO_EXTI_IRQHandler(GPIO_PIN_0);
}
```

**Rule for ISRs:**
1. Keep ISRs SHORT — set a flag, buffer data, return
2. Do processing in main loop
3. Never use `HAL_Delay` or `printf` in ISR (except for learning)
4. Use volatile for variables shared between ISR and main

### ✅ Day 24 Checklist
- [ ] Interrupt priorities configured — tested nesting
- [ ] Understand: lower number = higher priority
- [ ] Know the golden rule: ISRs must be SHORT
- [ ] Used `volatile` for ISR-shared variables

---

## DAY 25 — Saturday, Jul 25 (DEEP STUDY DAY)

### 💻 Deep Sessions (6:30 AM - 12:45 PM)

**Session 1 (6:30-7:30)**: FastBit MCU1 — complete ALL interrupt sections

**Session 2 (7:45-9:15)**: "Mastering STM32" Chapter 7 (Interrupts) — full read

**Session 3 (9:30-11:00)**: Build a "UART Command Processor"
- Interrupt-driven UART receive with circular buffer
- Command parser: "LED ON", "LED OFF", "STATUS", "HELP"
- Non-blocking LED blink + button check + UART processing
- Print status report on "STATUS" command:
  ```
  === STM32F411 Status ===
  Uptime: 45230 ms
  LED: ON
  Button: Released
  UART RX count: 127
  Buffer usage: 3/16
  ```

**Session 4 (11:15-12:45)**: Interview prep
1. "What is an interrupt? Draw the interrupt lifecycle."
2. "What is NVIC? How does priority work on Cortex-M?"
3. "Why should ISRs be short? What happens if they're too long?"
4. "Explain the difference between polling and interrupt-driven I/O."
5. "What is the volatile keyword and when must you use it with interrupts?"

### 🇩🇪 German (2:00-5:00 PM)
- Nicos Weg A2 Lessons 16-18
- Practice: "Ich arbeite als Ingenieur. Ich studiere Embedded Systems."

---

## DAY 26 — Sunday, Jul 26 (REVIEW + GIT)

### 💻 Morning (7:30 AM - 12:30 PM)

**7:30-9:00**: Implement UART interrupt + circular buffer from memory.
- Target: < 20 minutes for the complete working system.

**9:15-10:45**: Read RM0383 — NVIC + EXTI sections completely.

**11:00-12:30**: Git push. Write comprehensive Week 4 README.

---

## 📋 WEEK 4 CHECKPOINT

- [ ] ✅ NVIC interrupt system understood — priorities, nesting, vector table
- [ ] ✅ UART interrupt RX working (non-blocking)
- [ ] ✅ Circular buffer integrated with UART interrupt
- [ ] ✅ SysTick understood — non-blocking delay pattern
- [ ] ✅ Multiple concurrent tasks without RTOS (cooperative multitasking)
- [ ] ✅ Interrupt priorities tested — preemption verified
- [ ] ✅ ISR golden rules: short, set flags, use volatile
- [ ] ✅ UART Command Processor project complete
- [ ] ✅ Nicos Weg A2 lessons 14-18, 175+ Anki cards
