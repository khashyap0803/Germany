# AUGUST WEEK 5 (Aug 25–31) — PHASE 2 WEEK 1: STM32 BEGINS

> **Phase**: PHASE 2 — STM32 Microcontroller Programming (Week 1 of 13)
> **Topics**: ARM Cortex-M4 architecture, memory map, STM32CubeIDE, first LED blink (HAL), first LED blink (register-level)
> **Primary Course**: FastBit MCU1 "Mastering MCU Driver Development" (28.5h) — Sections 1–3
> **Primary Book**: "Mastering STM32" by Carmine Noviello — Chapters 1–5
> **Reference**: RM0383 (STM32F411 Reference Manual) — Section 2 (Memory Map), Section 8 (GPIO)
> **AI Status**: BANNED for code — Phase 2 maintains no-AI-code rule
> **Dates**: Tuesday August 25 → Monday August 31, 2026
> **REAL CHANGE FROM PHASE 1**: Weekday mornings now shift to STM32 study (hardware + IDE reading). No more pure K.N. King reading.

---

## PHASE 2 DAILY SCHEDULE (Aug 25 onward — new weekday routine)

### Weekday (Mon–Fri)

| Time | Activity |
|:---|:---|
| 5:00–5:25 AM | **PRE-GYM READING** — Mastering STM32 (current chapter) or RM0383 section |
| 5:25–5:30 AM | Gym prep |
| 5:30–6:30 AM | **GYM** |
| 6:30–7:00 AM | Shower, quick breakfast |
| 7:00–8:30 AM | **COMMUTE IN** — German audio (Nicos Weg A2 + AnkiDroid) |
| 12:30–12:45 PM | **LUNCH ANKI** — German cards |
| 6:30–8:30 PM | **COMMUTE BACK** — German audio |
| 8:30–9:30 PM | Dinner, freshen up |
| 9:30–10:00 PM | **BED READING** — Mastering STM32 or FastBit MCU1 course notes |
| 10:00 PM | Sleep |

> All HARDWARE coding (flashing, wiring, debugging real boards) happens on WEEKENDS ONLY.
> Weekdays: read Mastering STM32 + RM0383, watch FastBit MCU1 on phone during gym warm-up if possible.

### Weekend: same time blocks as Phase 1 but content shifts to hardware
- Saturday 7:30 AM–12:30 PM: STM32 hardware coding sessions
- Sunday 7:30 AM–10:30 AM + 2:00–4:00 PM: hardware projects + git push

---

## HARDWARE REQUIRED BY AUG 25 — VERIFY CHECKLIST

| Hardware | Purpose | Have it? |
|:---|:---|:---|
| STM32F411CEU6 (WeAct Black Pill) | Primary dev board | |
| Nucleo-L476RG | Onboard ST-Link/V2-1 debugger | |
| Robocraze ST-Link V2 (metal, USB) | Backup programmer | |
| Sipeed SLogic Combo 8 | Logic analyzer (UART verification) | |
| FT232 USB-UART | Serial monitor to PC | |
| Breadboard + jumper wires | Circuit connections | |
| LEDs (red + green + blue) | Output verification | |
| 330Ω resistors | Current limiting for LEDs | |
| 10KΩ resistors | Pull-up/down for buttons | |
| Pushbuttons | Input testing | |

**Software** (should be done during Deload week):
| Software | Status |
|:---|:---|
| STM32CubeIDE installed and launched | |
| ST-Link/V2 USB drivers installed | |
| Tera Term or PuTTY installed | |
| RM0383 (STM32F411 Reference Manual PDF) downloaded | |
| DS10314 (STM32F411 Datasheet PDF) downloaded | |
| FastBit MCU1 Udemy course accessible | |

---

## WEEKDAY READING SCHEDULE (Aug 25–29)

### Tuesday August 25 — Pre-Gym (5:00–5:25 AM) — FIRST DAY OF PHASE 2
**Read**: Mastering STM32 Chapter 4 (GPIO Management — pages 1–20)
- GPIO port structure: GPIOA through GPIOH (16 pins each on Black Pill)
- Key registers: MODER, OTYPER, OSPEEDR, PUPDR, IDR, ODR, BSRR, LCKR, AFR
- MODER: 2 bits per pin — 00=input, 01=output, 10=alternate function, 11=analog
- Push-pull vs open-drain output types
- No-pull vs pull-up vs pull-down

**Bed Reading**: Mastering STM32 Chapter 4 pages 20–40

### Wednesday August 26 — Pre-Gym (5:00–5:25 AM)
**Read**: RM0383 Section 8 (GPIO — pages 155–185)
- Read the MODER register description — understand each field
- Read BSRR register: bits 0–15 set the pin, bits 16–31 reset the pin — why this is atomic
- Read ODR: direct read/write — NOT atomic (read-modify-write vulnerable to race conditions in ISR)
- Compare: `ODR |= (1<<5)` vs `BSRR = (1<<5)` — BSRR is preferred for embedded

**Bed Reading**: Mastering STM32 Chapter 5 (Clock Tree and RCC — pages 1–20)

### Thursday August 27 — Pre-Gym (5:00–5:25 AM)
**Read**: Mastering STM32 Chapter 5 (RCC — pages 20–40)
- Why the clock system matters: every peripheral runs on a clock. Wrong clock = wrong timing.
- STM32F411 clock sources: HSI (16 MHz internal), HSE (external crystal), PLL (multiply up to 100 MHz)
- AHB, APB1, APB2 buses: peripherals connect to different buses at different max speeds
- GPIO clocks: MUST enable via RCC before using any GPIO pin — `RCC->AHB1ENR |= (1 << 0)` for GPIOA

**Bed Reading**: RM0383 Section 6 (Reset and Clock Control) — GPIO clock enable bits

### Friday August 28 — Pre-Gym (5:00–5:25 AM)
**Read**: FastBit MCU1 course — read the course outline/description carefully
- Which sections cover GPIO? Which cover UART? Which cover Timers?
- Plan: on Saturday watch the intro sections while coding along
- Understand the "HAL First, Then Register" pattern you'll follow for every peripheral

**Bed Reading**: Mastering STM32 Chapter 3 (Hello World — Blink LED) — re-read with fresh eyes before coding

### Monday August 31 — Pre-Gym (5:00–5:25 AM)
**Read**: RM0383 Section 8 (GPIO) — re-read the ODR and BSRR register details
Focus on: why BSRR is preferred over direct ODR write for thread-safety.

**Bed Reading**: Mastering STM32 Chapter 4 — re-read pin configuration section

---

## SATURDAY AUGUST 29 — FIRST STM32 CODING DAY (7:30 AM–12:30 PM)

### Warmup (7:30–8:30 AM): FastBit MCU1 — First Sections
Watch FastBit MCU1 sections 1-3 at 1.5× speed:
- Section 1: Course introduction + board overview (~15 min)
- Section 2: STM32CubeIDE project creation + file structure (~20 min)
- Section 3: Blink LED with HAL (~25 min — watch but don't code yet)

Note what CubeMX generates. Note what `MX_GPIO_Init()` does. Ask: what registers does it touch?

### ⭐ FUNDAMENTALS BRIDGE 1 — HANDS-ON (8:30–9:00 AM, before flashing)
> Theory half was done last weekend (deload). This is the hands-on half. See `15_FUNDAMENTALS_BRIDGE.md`.
> Do this on a breadboard with your multimeter BEFORE the LED blink — it makes the GPIO work concrete.
- [ ] Calculate the resistor for an external LED on 3.3V: R = (3.3 − 2.0) / 0.01 ≈ 130Ω → use 220Ω or 330Ω (safe)
- [ ] Wire the external LED + resistor on the breadboard from 3.3V → confirm it lights
- [ ] Build a voltage divider (two equal resistors), measure Vout with multimeter, verify ≈ half of Vin
- [ ] Wire a pushbutton with a pull-up resistor to a pin; measure pin voltage: ~3.3V released, ~0V pressed
- [ ] Confirm you understand: this external LED is what your STM32 GPIO will drive next

### BLOCK 1 (9:00–10:00 AM): LED Blink — HAL Method
Your first program on real STM32 hardware. Drive the EXTERNAL LED you just wired (PA5 → resistor → LED → GND), plus the onboard PC13.

**Setup in STM32CubeIDE + CubeMX**:
1. Create new project → STM32F411CEU6
2. In CubeMX: set PC13 as GPIO_Output (LED on Black Pill)
3. Generate code
4. Open `main.c` — find the `while(1)` loop

**Write this in the `while(1)` loop**:
```c
while (1) {
    HAL_GPIO_WritePin(GPIOC, GPIO_PIN_13, GPIO_PIN_RESET);  // LED ON (active low)
    HAL_Delay(500);
    HAL_GPIO_WritePin(GPIOC, GPIO_PIN_13, GPIO_PIN_SET);    // LED OFF
    HAL_Delay(500);
}
```

**Build**: Ctrl+B → should compile with 0 errors
**Flash**: Run → Debug → should flash to board and start running
**Verify**: LED on PC13 blinks at 1 Hz (500ms ON, 500ms OFF)

If LED does not blink:
1. Check SWD wiring (SWCLK, SWDIO, GND)
2. Check power (Black Pill USB or 3.3V from Nucleo)
3. Check CubeIDE: Project → Properties → Debug → correct ST-Link selected
4. Check Debug console for error messages
5. Use GDB in CubeIDE: set breakpoint in while loop, verify program reaches it

**THIS IS YOUR FIRST EMBEDDED PROGRAM. It took 11 weeks to get here.**

### BREAK (10:00–10:15)

### BLOCK 2 (10:15–11:45 AM): LED Blink — Register Level
Now implement the EXACT same blink LED without using HAL at all. Only register access.

Create a new project `blink_register` in CubeIDE. In `main.c`:

```c
#include "stm32f4xx.h"   // includes all register definitions

int main(void) {
    // Step 1: Enable GPIOC clock via RCC
    RCC->AHB1ENR |= (1 << 2);   // bit 2 = GPIOC clock enable

    // Step 2: Set PC13 as output (MODER bits 27:26 = 01)
    GPIOC->MODER &= ~(3 << 26);  // clear bits 27:26
    GPIOC->MODER |=  (1 << 26);  // set bits 27:26 = 01 (output)

    // Step 3: Set PC13 push-pull output type (OTYPER bit 13 = 0)
    GPIOC->OTYPER &= ~(1 << 13); // 0 = push-pull

    // Step 4: Set PC13 low speed (OSPEEDR bits 27:26 = 00)
    GPIOC->OSPEEDR &= ~(3 << 26);

    // Step 5: No pull-up/pull-down (PUPDR bits 27:26 = 00)
    GPIOC->PUPDR &= ~(3 << 26);

    while (1) {
        // Turn LED ON: reset PC13 via BSRR (active low — logic 0 = LED on)
        GPIOC->BSRR = (1 << (13 + 16));   // write to upper 16 bits = RESET

        // Simple delay (not accurate — just for blinking)
        for (volatile int i = 0; i < 500000; i++) {}

        // Turn LED OFF: set PC13 via BSRR
        GPIOC->BSRR = (1 << 13);           // write to lower 16 bits = SET

        for (volatile int i = 0; i < 500000; i++) {}
    }
}
```

Build and flash. Verify the LED still blinks.

**Open RM0383** while writing this. For each register write:
- Find the register in RM0383
- Read the bit description
- Verify your bit position is correct
- Ask: does the code match the datasheet?

This "verify against reference manual" habit is what makes an embedded engineer reliable.

### BLOCK 3 (11:45 AM–12:30 PM): Document + Reflect
Write in `blink_register/notes.txt`:
1. What does `RCC->AHB1ENR |= (1 << 2)` do? (cite RM0383 section and page)
2. Why must the clock be enabled before configuring GPIO?
3. What is the difference between BSRR and ODR for LED control?
4. Why is `volatile int i` needed in the delay loop? (hint: without volatile, the compiler may optimize it away)
5. What is the numeric address of GPIOC? (check stm32f4xx.h or RM0383 memory map)

### LUNCH (12:30–1:30 PM)

### GERMAN BLOCK 1 (1:30–4:30 PM)
- Nicos Weg A2 Lessons 11–12
- Learn: Konjunktiv II (Wenn ich Zeit hätte, würde ich mehr lernen.)
- Write 10 sentences with Konjunktiv II
- Anki: add 15 new cards

### GERMAN BLOCK 2 (5:00–6:30 PM)
- Nicos Weg A2 Lesson 13
- AnkiDroid: review ALL pending
- Write from memory: what you did today + what you will do tomorrow (German)

---

## SUNDAY AUGUST 30 — LED BLINK REVIEW + GIT (7:30 AM–4:00 PM)

### BLOCK 1 (7:30–9:00 AM): Recreate From Scratch
Close everything. From a blank CubeIDE project, implement LED blink (register level) without looking at yesterday's code.

Goal: understand well enough to recreate without reference.
Time yourself. Target: under 20 minutes.

If you can't do it in 20 min: re-read RM0383 Section 8 (GPIO registers) + your notes from Saturday.

### BLOCK 2 (9:15–10:30 AM): Blink Pattern Variations
Using register-level code only, implement 3 different blink patterns:

1. **SOS pattern**: 3 short, 3 long, 3 short (Morse code)
2. **Heartbeat**: quick double-blink followed by pause
3. **Breathing**: gradually increase then decrease duty cycle (PWM simulation with software delays)

These should be 3 separate functions. `main.c` calls them in sequence.

### GIT PUSH (10:30–11:00 AM)
Create a new GitHub repository: "STM32-Practice" (public)
```bash
# On WSL or in a folder you can access:
cd ~/STM32-Practice
git init
git add .
git commit -m "Phase 2 Week 1: LED blink HAL + register level. First real hardware program."
git push origin main
```

Write `README.md`:
- Board: STM32F411CEU6 (WeAct Black Pill)
- What each project does
- How to build + flash
- Key register: GPIOC MODER + BSRR for LED control

### REST + LUNCH (11:00 AM–12:00 PM)

### GERMAN (12:00–2:00 PM)
- Nicos Weg A2 Lessons 14–15
- Anki mega review (aim for 125+ words total)
- Write from memory: full description of what you're building (C + STM32 + German study)

### EXTENDED CODING (2:00–4:00 PM): Button Input
```
blink_button/
└── main.c   — Toggle LED when button pressed (no debounce yet — just basic GPIO input)
```

Read Mastering STM32 Ch 4 section on GPIO Input configuration. Then implement:

```c
// Configure PC13 as output (LED)
// Configure PA0 as input with pull-up (button — active low)
// In while(1): if (!(GPIOA->IDR & (1 << 0))) → toggle LED
```

This is "polling" (constantly checking the button). In Phase 2 Week 2, you will replace this with interrupt-driven input.

---

## WEEK 1 PHASE 2 CHECKPOINT (Monday August 31, 4:00 PM)

Update PROGRESS.md.

| Checkpoint Item | Done? |
|:---|:---|
| STM32CubeIDE installed and project created | |
| LED blink working with HAL | |
| LED blink working with registers (GPIOC→MODER, →BSRR, RCC→AHB1ENR) | |
| Can explain what each register write does (cited RM0383) | |
| Blink pattern variations (SOS, heartbeat) working | |
| Button input (polling) working | |
| STM32-Practice GitHub repo created with first commit | |
| Mastering STM32 Ch 1–5 read | |
| RM0383 Section 8 (GPIO) read | |
| Nicos Weg A2: Lessons 11–15 done | |
| Anki: 125+ German words total | |

**Self-rating (first STM32 week 1–10)**: ___

> If the LED blinks: you have crossed the threshold from software to hardware.
> Everything you learn in Phase 2 builds on this foundation.
> Phase 2 continues in 14_SEPTEMBER_2026_DAILY_PLAN.md.

---

## PHASE 2 LEARNING PHILOSOPHY (Applies All Remaining Weeks)

### The "HAL First, Then Register" Pattern
For every STM32 peripheral you study:
1. Watch FastBit MCU1 video section
2. Read Mastering STM32 chapter for that peripheral
3. Implement with HAL (using CubeMX-generated init code)
4. Implement with REGISTERS only (using RM0383 register descriptions)
5. Verify both produce IDENTICAL behavior

### The "What Changed?" Rule
Every time CubeMX generates init code:
1. Read every line of the generated code
2. For each HAL function: find the corresponding register in RM0383
3. If you can't explain a line → study it until you can

### AI Policy (Phase 2)
Same as Phase 1: AI may NOT write code.
AI MAY: explain what a register does, explain HAL function behavior, explain error messages.
If you copy AI code: you are stealing your own education.
