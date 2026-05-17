# 📅 JULY 2026 — MASTER OVERVIEW

> **Period**: July 1 (Wednesday) → July 31 (Friday)
> **Phase**: Jul 1-15: PHASE 1 BUFFER (C catch-up or early STM32 prep) | Jul 16-31: PHASE 2 — STM32 🔧
> **Month Goal**: GPIO + UART + Clock System on real STM32 hardware (HAL AND register level)
> **AI Status**: 🔴 **BANNED for code** — AI only explains concepts, YOU write ALL code
> **Status**: Working at Unistring (9 AM - 7/8 PM, 4hr commute)
>
> ⚠️ **TIMELINE NOTE**: Phase 1 (C Programming) was extended to Jul 15 to absorb the May wedding disruption.
> **Jul 1-15**: Use for Phase 1 catch-up if needed, or begin STM32 setup/prep if Phase 1 exit criteria already met.
> **Jul 16+**: Phase 2 officially starts. All July weekly plans below assume Phase 2 start.
>
> **⚡ THE SHIFT**: You've spent 11 weeks on pure C (including 2-week wedding buffer). Now that code runs on REAL HARDWARE.
> Your circular buffer, state machines, and bitwise ops from May-June → you'll use ALL of them on STM32.
>
> **Primary Course**: FastBit MCU1 "Mastering MCU Driver Development" (28.5h)
> **Primary Book**: "Mastering STM32" by Carmine Noviello (800+ pages)
> **Reference Manual**: RM0383 (STM32F411) + RM0351 (STM32L476RG)
> **Datasheet**: DS10314 (STM32F411xC/E)
>
> **Hardware for July**:
> - STM32F411CEU6 (WeAct Black Pill) — PRIMARY development board
> - Nucleo-L476RG — onboard ST-Link/V2-1 (SWD debugger for BOTH boards)
> - Robocraze ST-Link V2 (metal shell) — portable backup programmer
> - Sipeed SLogic — logic analyzer for UART signal verification
> - Breadboard + LEDs + pushbuttons + 10K resistors + jumper wires
> - FT232 USB-UART — serial communication to PC

---

## ⏰ DAILY TEMPLATES (Modified for Hardware)

### 🟦 WEEKDAY (Mon-Fri)

| Time | Duration | Activity | Tool |
|:---|:---|:---|:---|
| **5:00 AM** | 10 min | Wake up. Water. Wash face. **NO PHONE.** | Alarm |
| **5:10 - 6:30 AM** | 1h 20m | 🔶 **MORNING BLOCK — STM32 study** | STM32CubeIDE + board + FastBit MCU1 |
| **6:30 - 7:00 AM** | 30m | Get ready, breakfast | — |
| **7:00 - 8:30 AM** | 1.5h | 🎧 **COMMUTE IN — German audio** | DW Nicos Weg A2 + AnkiDroid |
| **12:30 - 12:45 PM** | 15m | 📱 **LUNCH ANKI — German cards** | AnkiDroid |
| **7:00 - 8:30 PM** | 1.5h | 🎧 **COMMUTE BACK — German audio** | Easy German / DW podcasts |
| **9:30 - 10:00 PM** | 30m | 📖 **BED READING — "Mastering STM32"** | PDF on tablet/phone |
| **10:00 PM** | — | **SLEEP. Non-negotiable.** | — |

### 🟩 SATURDAY — 9 hour deep study day

| Time | Duration | Activity |
|:---|:---|:---|
| **6:00 AM** | — | Wake up. Coffee/tea. |
| **6:30 - 7:30 AM** | 1h | 💻 STM32 warmup — review yesterday's code, read reference manual section |
| **7:45 - 9:15 AM** | 1.5h | 💻 **STM32 Deep Session 1** — HAL implementation |
| **9:30 - 11:00 AM** | 1.5h | 💻 **STM32 Deep Session 2** — Register-level same feature |
| **11:15 AM - 12:45 PM** | 1.5h | 💻 **STM32 Deep Session 3** — debugging + exercises |
| **12:45 - 2:00 PM** | 1.25h | Lunch + rest |
| **2:00 - 3:30 PM** | 1.5h | 🇩🇪 **German Session 1** — Nicos Weg A2 + writing |
| **3:45 - 5:00 PM** | 1.25h | 🇩🇪 **German Session 2** — speaking with Google AI |
| **5:00 PM+** | — | Free. Gym, family, relax. |

### 🟨 SUNDAY — 7 hour study + review day

| Time | Duration | Activity |
|:---|:---|:---|
| **7:30 - 9:00 AM** | 1.5h | 💻 STM32 practice — recreate yesterday's project from scratch |
| **9:15 - 10:45 AM** | 1.5h | 💻 Read Reference Manual — deep dive into current peripheral |
| **11:00 AM - 12:30 PM** | 1.5h | 💻 Git push + code cleanup + document in README |
| **2:00 - 3:00 PM** | 1h | 🇩🇪 German review |
| **3:00 - 4:00 PM** | 1h | 🇩🇪 Anki mega review |
| **4:00 - 4:30 PM** | 30m | 📋 Weekly review |

---

## 📚 BOOKS & RESOURCES FOR JULY

### Primary Resources

| Resource | Format | How to Use |
|:---|:---|:---|
| **FastBit MCU1 "Mastering MCU Driver Development"** (28.5h) | Udemy | PRIMARY video. Watch section → code along → then re-implement from scratch WITHOUT the video. |
| **"Mastering STM32" by Carmine Noviello** | PDF/Book | PRIMARY book. Read the relevant chapter BEFORE starting each peripheral. BED READING. |
| **RM0383 (STM32F411 Reference Manual)** | PDF (1700+ pages) | DEEP REFERENCE. Read the specific peripheral section (GPIO, USART, RCC). Don't read cover-to-cover — use it as a dictionary. |
| **RM0351 (STM32L476RG Reference Manual)** | PDF | SECONDARY reference for Nucleo board. |
| **DS10314 (STM32F411 Datasheet)** | PDF | Pin assignments, electrical specs, package info. |
| **FastBit ARM Cortex-M3/M4** (15h) | Udemy | Watch in Week 1 — ARM architecture, memory map, NVIC, bus architecture. |

### YouTube (Free Supplements)

| Channel | Use For |
|:---|:---|
| **Controllerstech** | STM32 tutorials: GPIO, UART, timers. Clear visual explanations. |
| **Phil's Lab** | PCB design + STM32 bare-metal. Professional-grade content. |
| **Fastbit Embedded Brain Academy** (YouTube) | Free previews of the Udemy courses |
| **Embedded Artistry** | Advanced bare-metal patterns |

### Tools

| Tool | When | Purpose |
|:---|:---|:---|
| **STM32CubeIDE** | Every session | IDE: code editor + CubeMX + build + debug |
| **STM32CubeMX** | Inside CubeIDE | Pin/clock/peripheral configuration GUI → generates init code |
| **Tera Term / PuTTY** | UART sessions | Serial terminal to view STM32 output on PC |
| **PulseView + SLogic** | UART debugging | Capture and decode UART signals on logic analyzer |
| **OpenOCD + GDB** | Advanced debugging | Debug via ST-Link when CubeIDE debugger isn't enough |

---

## 🔧 HARDWARE SETUP (Do this Week 1)

### Wiring: Black Pill ↔ Nucleo ST-Link

The Nucleo-L476RG has an onboard ST-Link/V2-1. You can use it to program the Black Pill:

```
Nucleo ST-Link    →    Black Pill (STM32F411)
─────────────          ──────────────────────
CN4 Pin 2 (SWCLK) →    SWCLK (PA14)
CN4 Pin 4 (SWDIO) →    SWDIO (PA13)
CN4 Pin 3 (GND)   →    GND
CN4 Pin 1 (VDD)   →    3.3V (optional — or power Black Pill via USB)
```

**Remove the jumpers** on the Nucleo's CN2 connector to disconnect the onboard STM32L476RG, allowing the ST-Link to target the external Black Pill.

### Wiring: FT232 USB-UART ↔ Black Pill

```
FT232           →    Black Pill
────────             ──────────
TX              →    PA3 (USART2_RX)
RX              →    PA2 (USART2_TX)
GND             →    GND
```

**⚠️ Do NOT connect VCC from FT232 to 3.3V if Black Pill is USB-powered. Only connect TX, RX, GND.**

---

## 🛡️ PHASE 2 LEARNING PHILOSOPHY

### The "HAL First, Then Register" Pattern

For EVERY peripheral in July, follow this exact pipeline:

```
1. FastBit MCU1 video → watch the section
2. "Mastering STM32" book → read the chapter
3. HAL implementation → use CubeMX-generated code, understand it
4. Register-level implementation → write the SAME thing using only registers
5. Reference Manual → read the peripheral section to verify your understanding
6. GDB debug → step through your code, verify register values
```

**Why both HAL and Register?**
- HAL: what you'll use 80% of the time at work (productivity)
- Register: what you need when HAL fails, when debugging hard bugs, when porting to new chips
- Interview question #1: "Can you configure UART without HAL?" → YES, you can.

### The "What Changed?" Rule

After CubeMX generates code, ALWAYS:
1. Open the generated `main.c`, `stm32f4xx_hal_msp.c`, `system_stm32f4xx.c`
2. Read EVERY line of init code
3. Ask: "What register did this configure? Why?"
4. Open RM0383 and find that register
5. **If you can't explain a line → you don't understand it → study it until you do**

---

## 📊 MONTHLY TARGETS

| Metric | Target |
|:---|:---|
| STM32 programs running on real hardware | **15+** |
| HAL implementations | **8+** (GPIO, UART, clock, button, LED, timer preview) |
| Register-level implementations | **5+** (GPIO, UART, RCC at minimum) |
| Reference Manual sections read | **4+** (GPIO, RCC, USART, NVIC) |
| FastBit MCU1 sections completed | **10-15** |
| "Mastering STM32" chapters read | **Ch 1-10** |
| GitHub commits with hardware code | **15+** |
| German Nicos Weg A2 lessons | **Start (lessons 1-10)** |
| German Anki cards | **170+ total** |
| Days woke at 5 AM | **≥ 25** |
| Total active study hours | **~100 hours** |

---

## 📅 WEEKLY BREAKDOWN — SEE SEPARATE FILES

| File | Dates | Topic |
|:---|:---|:---|
| **`12A_JULY_WEEK1.md`** | Jul 1-5 (Wed-Sun) | STM32 setup + ARM architecture + first blink (HAL + Register) |
| **`12B_JULY_WEEK2.md`** | Jul 6-12 (Mon-Sun) | GPIO deep: modes, pull-up/down, button input, BSRR, ODR |
| **`12C_JULY_WEEK3.md`** | Jul 13-19 (Mon-Sun) | Clock system (RCC) + UART (HAL + Register) |
| **`12D_JULY_WEEK4.md`** | Jul 20-26 (Mon-Sun) | UART deep: receive, printf redirect, interrupts intro |
| **`12E_JULY_WEEK5.md`** | Jul 27-31 (Mon-Fri) | Timers intro + month review + August prep |

---

## 🔑 JULY MINDSET

> **May-June you learned C on a PC. July you learn C on a microcontroller.**
>
> The language is the same. The patterns are the same. But now:
> - `printf()` → `HAL_UART_Transmit()` (no screen, only serial)
> - `int x = 5;` → `GPIOA->BSRR = (1 << 5);` (writing to real hardware)
> - `while(1)` → this loop runs FOREVER on the chip (no Ctrl+C)
> - Debugging = connecting wires, measuring voltages, reading register dumps
>
> **Every bug is harder to find. Every success is more rewarding. Welcome to embedded.** ⚡

---

> **July 16th, 5:00 AM. Wire up your Black Pill. Open STM32CubeIDE. Blink an LED. Begin.**
>
> (If you're using Jul 1-15 for Phase 1 catch-up, start hardware work on Jul 16.)
