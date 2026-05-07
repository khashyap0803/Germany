# 📅 WEEK 5 — Jul 27-31 (Mon-Fri): TIMERS INTRO + MONTH REVIEW + AUGUST PREP

> **Topics**: Timer basics, timer interrupt, SysTick deep, PLL configuration (100 MHz SYSCLK), month review
> **FastBit MCU1**: Timer sections (intro + basic timer)
> **"Mastering STM32" Book**: Chapter 9 (Timers), Chapter 5 revisit (Clock tree)
> **Reference Manual**: RM0383 Section 11 (General-purpose timers), Section 6 (RCC/PLL)
> **Programs on hardware**: 3-4
> **German**: Nicos Weg A2 Lessons 19-20

---

## DAY 27 — Monday, Jul 27

### 🔶 Morning Block (5:10 - 6:30 AM) — TIMER THEORY

#### 📺 WATCH (20 min)
**FastBit MCU1**: Timer section — introduction + basic timer concepts

#### 📖 STUDY (1h)

**What is a timer?** A counter that counts clock cycles.

```
Timer clock (from RCC) → Prescaler → Counter → Auto-reload → Interrupt/Event
     84 MHz               ÷8400        0→9999     overflow!       [IRQ]
     
     Result: 84,000,000 / 8400 / 10000 = 1 Hz = exactly 1 second
```

**Key registers:**
- **PSC** (Prescaler): divides the input clock
- **ARR** (Auto-Reload Register): counter counts from 0 to ARR, then resets
- **CNT** (Counter): current count value
- **CR1** (Control Register 1): enable/disable, direction
- **SR** (Status Register): overflow flag (UIF)
- **DIER** (DMA/Interrupt Enable): enable timer interrupt

**Timer formula:**
```
Timer frequency = fCLK / (PSC + 1) / (ARR + 1)

Example: 1-second interrupt
fCLK = 16 MHz (HSI, default)
PSC = 15999 → divides to 1000 Hz
ARR = 999  → counts 1000 ticks = 1 second
Verify: 16,000,000 / (15999+1) / (999+1) = 1 Hz ✅
```

**Draw on paper:**
1. Timer block diagram (clock → prescaler → counter → reload → interrupt)
2. Timer formula with your values

### ✅ Day 27 Checklist
- [ ] Timer concepts understood: prescaler, auto-reload, counter
- [ ] Timer formula memorized and can calculate for any frequency
- [ ] Timer block diagram drawn on paper
- [ ] Know which timers exist on STM32F411 (TIM1-5, TIM9-11)

---

## DAY 28 — Tuesday, Jul 28

### 🔶 Morning Block (5:10 - 6:30 AM) — TIMER INTERRUPT (HAL)

#### 💻 CODE (1h 20m)

Create `11_timer_interrupt_hal`:

**CubeMX setup:**
1. Enable TIM2 (32-bit timer on APB1)
2. Clock source: Internal Clock
3. Prescaler: 15999 (divides 16 MHz to 1 kHz)
4. Counter Period (ARR): 999 (1000 counts = 1 second)
5. Enable TIM2 global interrupt in NVIC
6. Generate code

**In main.c:**
```c
int main(void) {
    // ... init ...
    
    // Start timer interrupt
    HAL_TIM_Base_Start_IT(&htim2);
    
    printf("Timer started! LED toggles every 1 second via interrupt.\r\n");
    
    while (1) {
        // Main loop does other work
        process_uart();
        check_buttons();
    }
}

// Timer interrupt callback
void HAL_TIM_PeriodElapsedCallback(TIM_HandleTypeDef *htim) {
    if (htim->Instance == TIM2) {
        HAL_GPIO_TogglePin(GPIOC, GPIO_PIN_13);
    }
}
```

**The LED now toggles at EXACTLY 1 second** — not approximately like `HAL_Delay`. Hardware timers are precise to the clock crystal accuracy.

**Modify**: Change ARR to 499 → LED toggles every 500ms. Change PSC to get 100ms. Experiment.

### ✅ Day 28 Checklist
- [ ] Timer interrupt driving LED toggle — precise 1-second interval
- [ ] PSC and ARR values calculated manually and verified
- [ ] Changed frequency by modifying PSC/ARR
- [ ] Main loop runs freely while timer handles LED

---

## DAY 29 — Wednesday, Jul 29

### 🔶 Morning Block (5:10 - 6:30 AM) — PLL CONFIGURATION (100 MHz)

#### 💻 CODE (1h 20m)

**By default, STM32F411 runs at 16 MHz (HSI).** Let's configure PLL to get full speed.

**CubeMX Clock Configuration tab:**
1. Input: HSI = 16 MHz (or HSE if you have a crystal)
2. PLL Source: HSI
3. PLL M = 8 (16 / 8 = 2 MHz to PLL input)
4. PLL N = 200 (2 × 200 = 400 MHz VCO)
5. PLL P = 4 (400 / 4 = 100 MHz SYSCLK)
6. AHB Prescaler = 1 (HCLK = 100 MHz)
7. APB1 Prescaler = 2 (APB1 = 50 MHz)
8. APB2 Prescaler = 1 (APB2 = 100 MHz)

**After changing clock → recalculate timer values!**
```
Old: 16 MHz / (15999+1) / (999+1) = 1 Hz
New: 50 MHz (APB1 timer clock*) / (49999+1) / (999+1) = 1 Hz

* Note: When APB1 prescaler > 1, timer clock = APB1 × 2 = 100 MHz!
  So: 100 MHz / (99999+1) / (999+1) = 1 Hz
```

**Exercise**: After PLL config, verify:
- `printf("SYSCLK = %lu Hz\r\n", HAL_RCC_GetSysClockFreq());`
- `printf("HCLK   = %lu Hz\r\n", HAL_RCC_GetHCLKFreq());`
- `printf("APB1   = %lu Hz\r\n", HAL_RCC_GetPCLK1Freq());`
- `printf("APB2   = %lu Hz\r\n", HAL_RCC_GetPCLK2Freq());`

Also update UART BRR if using register-level UART.

### ✅ Day 29 Checklist
- [ ] PLL configured — SYSCLK = 100 MHz
- [ ] Verified clock frequencies via printf
- [ ] Timer recalculated for new clock
- [ ] UART still works at 115200 after clock change

---

## DAY 30 — Thursday, Jul 30

### 🔶 Morning Block (5:10 - 6:30 AM) — JULY COMPREHENSIVE REVIEW

**Build a "July Demo" project that combines EVERYTHING:**

Create `12_july_demo`:
```
Features:
1. SYSCLK = 100 MHz via PLL ✅
2. GPIO output: LED on PC13 ✅
3. GPIO input: Button on PA0 with pull-up + debounce ✅
4. UART TX/RX: printf redirect + interrupt receive ✅
5. Circular buffer: UART RX buffered ✅
6. Timer interrupt: LED toggles every 500ms ✅
7. Non-blocking: all tasks run concurrently ✅
8. Command menu: LED ON/OFF, STATUS, TIMER SPEED ✅
```

This single project proves you can:
- Configure GPIO, UART, Timer, Clock, Interrupts
- Use HAL AND understand the registers underneath
- Write non-blocking firmware with interrupt-driven I/O
- Reuse data structures from Phase 1 (circular buffer)

### ✅ Day 30 Checklist
- [ ] July demo project: all 8 features working
- [ ] Clean code: separate .c/.h files, Makefile-style organization
- [ ] Can explain every register configured
- [ ] README documents everything

---

## DAY 31 — Friday, Jul 31 — LAST DAY OF JULY

### 🔶 Morning Block (5:10 - 6:30 AM) — PHASE 2 PROGRESS CHECK

**Self-assessment (answer honestly):**

```
GPIO:
□ Can configure any pin as input/output/AF from registers? 
□ Know push-pull vs open-drain?
□ Can use BSRR for atomic set/reset?

UART:
□ Can init UART from registers (RCC, GPIO AF, BRR, CR1)?
□ Can send/receive with HAL AND registers?
□ Printf redirect working?
□ Interrupt-driven RX with circular buffer?

Clock:
□ Can configure PLL for 100 MHz?
□ Know which bus each peripheral is on?
□ Can recalculate timer/UART values for different clocks?

Timers:
□ Timer formula: fCLK / (PSC+1) / (ARR+1)?
□ Timer interrupt driving LED?

Interrupts:
□ Understand NVIC priorities?
□ Know ISR rules (short, volatile, set flags)?
□ Non-blocking main loop pattern?
```

**If any answer is NO → mark it for August Week 1 review.**

**August preview:** PWM, ADC, SPI, I2C, DMA. The pace accelerates.

### Git push:
```bash
cd /mnt/f/Documents/DEVELOP/STM32-Practice
git add -A
git commit -m "July complete: GPIO, UART, Clock, Timer, Interrupts - Phase 2 Month 1"
git push
```

### ✅ Day 31 Checklist
- [ ] Self-assessment completed honestly
- [ ] Weak areas identified for August review
- [ ] All July code pushed to GitHub
- [ ] July demo project polished with README

---

## 📋 WEEK 5 CHECKPOINT — END OF JULY

- [ ] ✅ Timer basics: prescaler, ARR, interrupt — can calculate for any frequency
- [ ] ✅ PLL configured: SYSCLK = 100 MHz, all peripheral clocks verified
- [ ] ✅ July demo project: GPIO + UART + Timer + Interrupts all working together
- [ ] ✅ Non-blocking firmware pattern mastered
- [ ] ✅ Nicos Weg A2 lessons 19-20, 180+ Anki cards

---

## 🎯 JULY COMPLETE — WHAT YOU'VE BUILT

```
JULY 2026: YOUR FIRST MONTH ON REAL HARDWARE

Week 1:  Setup + first blink → "I can flash code to a microcontroller"
Week 2:  GPIO deep → "I can control ANY pin in ANY mode from registers"
Week 3:  UART → "My STM32 talks to my PC — I have printf debugging"
Week 4:  Interrupts → "My firmware handles events without blocking"
Week 5:  Timers + PLL → "I control time precisely and run at full speed"

You configured real hardware registers.
You debugged with GDB + logic analyzer.
You reused your June C code (circular buffer) on STM32.
You built a multi-peripheral demo without AI.

AUGUST → SPI, I2C, ADC, PWM, DMA. The peripheral collection grows. 🔧
```
