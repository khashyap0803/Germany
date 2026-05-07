# 📅 WEEK 3 — Jul 13-19 (Mon-Sun): UART — TALK TO YOUR PC

> **Topics**: UART theory, USART2 HAL, USART2 register-level, printf redirect, serial terminal, logic analyzer
> **FastBit MCU1**: UART/USART sections (all)
> **"Mastering STM32" Book**: Chapter 8 (UART/USART)
> **Reference Manual**: RM0383 Section 19 (USART)
> **Hardware**: Black Pill + FT232 USB-UART + Tera Term on PC
> **Programs on hardware**: 4-6
> **German**: Nicos Weg A2 Lessons 9-13

---

## DAY 13 — Monday, Jul 13

### 🔶 Morning Block (5:10 - 6:30 AM) — UART THEORY

#### 📺 WATCH (20 min)
**FastBit MCU1**: USART section intro — theory
**Controllerstech YouTube**: "STM32 UART" basics (~10 min)

#### 📖 STUDY (1h)

**UART fundamentals** (draw on paper):
```
TX ─────┐          ┌───── RX
        │          │
    ┌───┴──────────┴───┐
    │ IDLE  START  D0 D1 D2 D3 D4 D5 D6 D7  STOP │
    │  1     0    LSB ──────────────────── MSB  1  │
    └──────────────────────────────────────────────┘
    
    Baud rate: bits per second (e.g., 115200)
    Frame: 1 start + 8 data + 1 stop = 10 bits per byte
    At 115200 baud: 11,520 bytes/second
```

**Key concepts:**
- **Baud rate**: sender and receiver MUST match exactly
- **Start bit**: always LOW — signals start of transmission
- **Stop bit**: always HIGH — signals end of frame
- **No clock line**: sender and receiver use their own clocks (asynchronous)
- **TX and RX are crossed**: sender's TX → receiver's RX

**Read RM0383 Section 19**: Focus on:
- Section 19.3: USART functional description
- Section 19.3.4: Baud rate generation (BRR register calculation)
- Section 19.6: USART registers

### ✅ Day 13 Checklist
- [ ] UART frame format drawn on paper (start, 8 data, stop)
- [ ] Understand: baud rate, asynchronous, TX/RX crossover
- [ ] Read RM0383 USART section intro
- [ ] Know: USART2 is on APB1, need to enable RCC->APB1ENR

---

## DAY 14 — Tuesday, Jul 14

### 🔶 Morning Block (5:10 - 6:30 AM) — UART WITH HAL

#### 💻 CODE (1h 20m)

**Step 1 — CubeMX UART setup (5:10-5:30):**
1. New project: `08_uart_hal`
2. CubeMX: Enable USART2 → Mode: Asynchronous
3. Pins: PA2 = USART2_TX, PA3 = USART2_RX (should auto-assign)
4. Baud rate: 115200, 8 data bits, 1 stop bit, No parity
5. Generate code

**Step 2 — Send "Hello World" (5:30-5:45):**
```c
// In main(), inside while(1):
char msg[] = "Hello from STM32F411!\r\n";
HAL_UART_Transmit(&huart2, (uint8_t *)msg, strlen(msg), HAL_MAX_DELAY);
HAL_Delay(1000);
```

**Step 3 — Wire FT232 and open terminal (5:45-6:00):**
```
FT232 TX  → PA3 (STM32 RX)
FT232 RX  → PA2 (STM32 TX)
FT232 GND → GND
```
Open **Tera Term** on PC:
- New Connection → Serial → select COM port (check Device Manager)
- Setup → Serial Port → 115200, 8, N, 1
- You should see "Hello from STM32F411!" every second!

**Step 4 — Send formatted data (6:00-6:15):**
```c
char buf[64];
int count = 0;
while (1) {
    int len = snprintf(buf, sizeof(buf), "Count: %d\r\n", count++);
    HAL_UART_Transmit(&huart2, (uint8_t *)buf, len, HAL_MAX_DELAY);
    HAL_Delay(500);
}
```

### ✅ Day 14 Checklist
- [ ] UART transmit working — see data in Tera Term
- [ ] FT232 wired correctly (TX↔RX crossover)
- [ ] Formatted data (counter) streaming over UART
- [ ] Verified baud rate match between STM32 and Tera Term

---

## DAY 15 — Wednesday, Jul 15

### 🔶 Morning Block (5:10 - 6:30 AM) — UART RECEIVE

#### 💻 CODE (1h 20m)

**Exercise 1 — Receive single character (5:10-5:35):**
```c
uint8_t rx_byte;
while (1) {
    HAL_UART_Receive(&huart2, &rx_byte, 1, HAL_MAX_DELAY);  // Blocking!
    
    // Echo back with modification
    char buf[32];
    int len = snprintf(buf, sizeof(buf), "Received: '%c' (0x%02X)\r\n", rx_byte, rx_byte);
    HAL_UART_Transmit(&huart2, (uint8_t *)buf, len, HAL_MAX_DELAY);
}
```

Type in Tera Term → see the echo.

**Exercise 2 — Simple command menu (5:35-6:10):**
```c
void print_menu(UART_HandleTypeDef *huart) {
    char *menu = "\r\n=== STM32 Menu ===\r\n"
                 "1. Toggle LED\r\n"
                 "2. Read button\r\n"
                 "3. Show uptime\r\n"
                 ">> ";
    HAL_UART_Transmit(huart, (uint8_t *)menu, strlen(menu), HAL_MAX_DELAY);
}
```

Process the received character:
```c
switch (rx_byte) {
    case '1':
        HAL_GPIO_TogglePin(GPIOC, GPIO_PIN_13);
        send_string("LED toggled!\r\n");
        break;
    case '2':
        if (HAL_GPIO_ReadPin(GPIOA, GPIO_PIN_0))
            send_string("Button: NOT pressed\r\n");
        else
            send_string("Button: PRESSED\r\n");
        break;
    case '3': {
        char buf[32];
        snprintf(buf, sizeof(buf), "Uptime: %lu ms\r\n", HAL_GetTick());
        send_string(buf);
        break;
    }
}
```

### ✅ Day 15 Checklist
- [ ] Character echo working (type → see echo)
- [ ] Menu system with 3 commands working
- [ ] Can control LED from PC via UART
- [ ] Understand: HAL_UART_Receive is BLOCKING — stops your main loop

---

## DAY 16 — Thursday, Jul 16

### 🔶 Morning Block (5:10 - 6:30 AM) — PRINTF REDIRECT (RETARGET)

#### 💻 CODE (1h 20m)

**The goal**: Make `printf()` work over UART. Then you can use `printf` for debugging just like on PC.

**Method — Override `_write` syscall:**

Create `retarget.c`:
```c
#include <stdio.h>
#include "stm32f4xx_hal.h"

extern UART_HandleTypeDef huart2;

int _write(int file, char *ptr, int len) {
    HAL_UART_Transmit(&huart2, (uint8_t *)ptr, len, HAL_MAX_DELAY);
    return len;
}
```

Now in `main.c`:
```c
printf("Hello from printf! Count = %d\r\n", count);
printf("HAL_GetTick() = %lu ms\r\n", HAL_GetTick());
printf("sizeof(int) on STM32 = %zu\r\n", sizeof(int));  // 4 bytes!
```

**What to understand**: `printf` calls `_write()` which you redirect to UART. This is the **same** mechanism used in professional firmware. Many companies ban `printf` in production (too slow/big) but it's essential for development.

**Exercise — Also redirect `scanf`:**
```c
int _read(int file, char *ptr, int len) {
    HAL_UART_Receive(&huart2, (uint8_t *)ptr, 1, HAL_MAX_DELAY);
    return 1;
}
```

Now you can use `scanf` to read from Tera Term!

### ✅ Day 16 Checklist
- [ ] printf redirected to UART — working in Tera Term
- [ ] scanf redirected from UART — can read user input
- [ ] Understand: `_write` syscall override mechanism
- [ ] Can use printf for debugging just like on PC

---

## DAY 17 — Friday, Jul 17

### 🔶 Morning Block (5:10 - 6:30 AM) — UART REGISTER LEVEL ⚠️ CRITICAL

#### 💻 CODE (1h 20m)

Create `09_uart_register` — implement UART WITHOUT any HAL:

```c
#include "stm32f4xx.h"

void uart2_init(uint32_t baud) {
    // 1. Enable clocks
    RCC->AHB1ENR |= RCC_AHB1ENR_GPIOAEN;   // GPIOA clock
    RCC->APB1ENR |= RCC_APB1ENR_USART2EN;   // USART2 clock
    
    // 2. Configure PA2 (TX) as AF7
    GPIOA->MODER &= ~(3U << 4);
    GPIOA->MODER |=  (2U << 4);    // AF mode
    GPIOA->AFR[0] &= ~(0xFU << 8);
    GPIOA->AFR[0] |=  (7U << 8);   // AF7 = USART2
    
    // 3. Configure PA3 (RX) as AF7
    GPIOA->MODER &= ~(3U << 6);
    GPIOA->MODER |=  (2U << 6);    // AF mode
    GPIOA->AFR[0] &= ~(0xFU << 12);
    GPIOA->AFR[0] |=  (7U << 12);  // AF7 = USART2
    
    // 4. Configure USART2
    // BRR = fCLK_APB1 / baud_rate
    // At default HSI (no PLL): APB1 prescaler = 1, so APB1 = 16 MHz
    // BRR = 16000000 / 115200 ≈ 139 = 0x8B
    // NOTE: After PLL config (Week 5), APB1 prescaler = 2, and timer
    // clocks double, but USART clock = APB1 = SYSCLK/2. Recalculate!
    USART2->BRR = 16000000UL / baud;  // Hardcoded for HSI default
    
    USART2->CR1 = 0;
    USART2->CR1 |= USART_CR1_TE;    // Transmitter enable
    USART2->CR1 |= USART_CR1_RE;    // Receiver enable
    USART2->CR1 |= USART_CR1_UE;    // USART enable
}

void uart2_send_char(char c) {
    while (!(USART2->SR & USART_SR_TXE));  // Wait until TX buffer empty
    USART2->DR = c;
}

void uart2_send_string(const char *str) {
    while (*str) {
        uart2_send_char(*str++);
    }
}

char uart2_receive_char(void) {
    while (!(USART2->SR & USART_SR_RXNE));  // Wait until RX buffer not empty
    return USART2->DR;
}

int main(void) {
    uart2_init(115200);
    uart2_send_string("Hello from REGISTER-LEVEL UART!\r\n");
    
    while (1) {
        char c = uart2_receive_char();
        uart2_send_string("Got: ");
        uart2_send_char(c);
        uart2_send_string("\r\n");
    }
}
```

**MANDATORY**: For every register you write:
1. Open RM0383 Section 19.6 (USART registers)
2. Find: CR1, CR2, CR3, BRR, SR, DR registers
3. Verify each bit you set

**Verify with logic analyzer** (Sipeed SLogic + PulseView):
- Connect SLogic CH0 to PA2 (TX line)
- Decode as UART: 115200, 8N1
- See your characters in the decode view!

### ✅ Day 17 Checklist
- [ ] UART init from registers — TX and RX working
- [ ] BRR calculation understood (fCLK / baud)
- [ ] Send and receive characters without HAL
- [ ] Verified on logic analyzer — saw UART waveform + decoded characters
- [ ] Can explain: SR (status), DR (data), BRR (baud rate), CR1 (control)

---

## DAY 18 — Saturday, Jul 18 (DEEP STUDY DAY)

### 💻 Deep Sessions (6:30 AM - 12:45 PM)

**Session 1 (6:30-7:30)**: FastBit MCU1 — complete ALL USART sections

**Session 2 (7:45-9:15)**: "Mastering STM32" Chapter 8 — full read + exercises

**Session 3 (9:30-11:00)**: Build a "Serial Data Logger"
- Combine: button input + UART output
- When button is pressed, send a timestamped message:
  ```
  [00012345] Button pressed! Count: 42
  ```
- Use your circular buffer from June to buffer messages!

**Session 4 (11:15-12:45)**: Interview prep
1. "Explain UART frame format. What is baud rate?"
2. "How do you calculate the BRR value for STM32?"
3. "What is the difference between blocking and interrupt-driven UART?"
4. "What happens if TX and RX baud rates don't match?"
5. "How would you debug a UART communication problem?" (Answer: logic analyzer)

### 🇩🇪 German (2:00-5:00 PM)
- Nicos Weg A2 Lessons 11-13
- Practice: describe your hobbies in German ("Ich programmiere gern.")

### ✅ Day 18 Checklist
- [ ] All FastBit USART content completed
- [ ] "Mastering STM32" Ch 8 read
- [ ] Serial data logger working (button → UART)
- [ ] Circular buffer used on STM32 (reuse from June!)
- [ ] 5 interview answers written

---

## DAY 19 — Sunday, Jul 19 (REVIEW + GIT)

### 💻 Morning (7:30 AM - 12:30 PM)

**7:30-9:00**: From blank project, implement register-level UART from memory.
- Target: init + send string + receive char in < 25 minutes.
- If failed → redo until you can.

**9:15-10:45**: Use Sipeed SLogic to capture and analyze UART traffic
- Measure actual baud rate — does it match 115200?
- Count start/stop/data bits in the waveform
- Take a screenshot for your GitHub README

**11:00-12:30**: Git push all UART projects. Update README with wiring diagram.

### ✅ Day 19 Checklist
- [ ] Register-level UART from memory in < 25 min
- [ ] Logic analyzer capture showing UART waveform
- [ ] All code pushed with README + wiring diagram
- [ ] Weekly review completed

---

## 📋 WEEK 3 CHECKPOINT

- [ ] ✅ UART theory: frame format, baud rate, async communication
- [ ] ✅ UART HAL: transmit, receive, printf redirect, scanf redirect
- [ ] ✅ UART register-level: init, send, receive — all without HAL
- [ ] ✅ BRR calculation from scratch
- [ ] ✅ Logic analyzer used to verify UART signals
- [ ] ✅ Serial data logger with circular buffer working
- [ ] ✅ Can write UART init + send/receive from memory
- [ ] ✅ RM0383 USART section read
- [ ] ✅ Nicos Weg A2 lessons 9-13, 170+ Anki cards
