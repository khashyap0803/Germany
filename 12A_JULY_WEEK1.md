# 📅 WEEK 1 — Jul 1-5 (Wed-Sun): STM32 SETUP + ARM ARCHITECTURE + FIRST BLINK

> **Topics**: STM32CubeIDE setup, ARM Cortex-M4 architecture, memory map, first project, blink LED (HAL), blink LED (register-level)
> **FastBit MCU1**: Sections 1-3 (Introduction, Development board, IDE setup)
> **FastBit ARM Cortex**: Sections 1-4 (ARM architecture, memory map, bus interfaces)
> **"Mastering STM32" Book**: Chapters 1-4 (Introduction, Setting up the tool chain, Hello World, GPIO)
> **Reference Manual**: RM0383 Section 2 (Memory map), Section 8 (GPIO)
> **Programs on hardware**: 3-5
> **German**: Nicos Weg A2 Lesson 1-3 (start A2!)
> **📚 Full resource details**: See `10_RESOURCES.md`

---

## 📺 PRE-WEEK HOMEWORK (Do June 30 evening if not done)

1. **Install STM32CubeIDE** from st.com (should be done from June Week 4)
2. **Download Reference Manual RM0383** (STM32F411) — bookmark in your browser
3. **Download Datasheet DS10314** (STM32F411xC/E)
4. **Watch FastBit ARM Cortex** — Section 1 (Introduction, 30 min at 1.5×)

---

## DAY 1 — Wednesday, Jul 1 ⭐ FIRST HARDWARE DAY

### 🔶 Morning Block (5:10 - 6:30 AM) — STM32CubeIDE + FIRST PROJECT

#### 📺 WATCH (20 min) — 5:10 to 5:30 AM

**FastBit MCU1**: Section 1 — Course introduction + development board overview
- Watch at 1.5× speed. Note which board they use (likely Nucleo).
- Your board: **STM32F411CEU6 (Black Pill)** — same chip family, different package.

#### 💻 HARDWARE + CODE (40 min) — 5:30 to 6:10 AM

**Step 1 — Create first project (5:30-5:45):**
1. Open **STM32CubeIDE**
2. File → New → STM32 Project
3. Search: **STM32F411CEU6** → select it
4. Name: `01_blink_hal`
5. Targeted Project Type: STM32Cube → Finish
6. CubeMX opens → you see the chip pinout diagram

**Step 2 — Configure LED pin in CubeMX (5:45-5:55):**
1. Find **PC13** on the pinout (Black Pill's onboard LED)
2. Click PC13 → set to **GPIO_Output**
3. In GPIO configuration: Output type = Push-Pull, Speed = Low, No pull
4. Go to **Project Manager** tab → Generate Code

**Step 3 — Write blink code (5:55-6:10):**
In `main.c`, inside `while(1)`:
```c
/* USER CODE BEGIN WHILE */
while (1)
{
    HAL_GPIO_TogglePin(GPIOC, GPIO_PIN_13);
    HAL_Delay(500);  // 500ms delay
    /* USER CODE END WHILE */
}
```

**Step 4 — Flash and run:**
1. Connect Black Pill to Nucleo's ST-Link (see overview for wiring)
2. Click the green "Run" button (or Debug button)
3. Select "ST-Link" as debugger
4. **THE LED BLINKS!** 🎉

> **You just ran YOUR code on REAL hardware. This is what it's all about.**

#### 📖 READ (6:10 - 6:30 AM)
- Open **RM0383** → Section 2: Memory and bus architecture
- Find the **memory map** diagram. Note where GPIO registers are (0x4002 0000 range)
- Note: FLASH starts at 0x0800 0000, SRAM at 0x2000 0000

### ✅ Day 1 Checklist
- [ ] STM32CubeIDE project created for STM32F411CEU6
- [ ] CubeMX: PC13 configured as GPIO_Output
- [ ] LED blinks at 500ms using HAL
- [ ] Read RM0383 memory map — know where GPIO registers live
- [ ] **First real hardware program running** ⭐

---

## DAY 2 — Thursday, Jul 2

### 🔶 Morning Block (5:10 - 6:30 AM) — ARM ARCHITECTURE OVERVIEW

#### 📺 WATCH (30 min) — 5:10 to 5:40 AM

**FastBit ARM Cortex-M3/M4**: Sections 1-2
- ARM Cortex-M4 processor features
- Bus interfaces: AHB, APB1, APB2
- Memory map: Code, SRAM, Peripheral, External RAM regions
- **KEY CONCEPT**: Every peripheral (GPIO, UART, Timer) is at a FIXED memory address

#### 💻 EXPLORE (30 min) — 5:40 to 6:10 AM

**Exercise 1 — Explore the generated code:**

Open these files in your `01_blink_hal` project and READ every line:
1. `Core/Src/main.c` — your application code
2. `Core/Src/stm32f4xx_hal_msp.c` — MCU-specific init (clock enables)
3. `Core/Src/system_stm32f4xx.c` — system clock configuration
4. `Core/Src/stm32f4xx_it.c` — interrupt handlers (SysTick!)
5. `Drivers/CMSIS/Device/ST/STM32F4xx/Include/stm32f411xe.h` — **THE REGISTER DEFINITIONS**

**Open `stm32f411xe.h` and find:**
```c
// Find the GPIO_TypeDef struct — THIS is what you simulated in June Week 3!
typedef struct {
    __IO uint32_t MODER;    // Mode register        (offset 0x00)
    __IO uint32_t OTYPER;   // Output type           (offset 0x04)
    __IO uint32_t OSPEEDR;  // Output speed          (offset 0x08)
    __IO uint32_t PUPDR;    // Pull-up/pull-down     (offset 0x0C)
    __IO uint32_t IDR;      // Input data            (offset 0x10)
    __IO uint32_t ODR;      // Output data           (offset 0x14)
    __IO uint32_t BSRR;     // Bit set/reset         (offset 0x18)
    __IO uint32_t LCKR;     // Lock                  (offset 0x1C)
    __IO uint32_t AFR[2];   // Alternate function    (offset 0x20-0x24)
} GPIO_TypeDef;

// Find GPIOC base address:
#define GPIOC_BASE  (AHB1PERIPH_BASE + 0x0800UL)
#define GPIOC       ((GPIO_TypeDef *) GPIOC_BASE)
```

> **This is EXACTLY the memory-mapped I/O pattern you built in `week8/memory_mapped_io.c`!**
> The only difference: now `GPIOC` points to REAL hardware at address `0x4002 0800`.

#### 📖 READ (6:10 - 6:30 AM)
- **"Mastering STM32"** — Chapter 1-2 (Introduction, Setting up)

### ✅ Day 2 Checklist
- [ ] Watched ARM Cortex architecture overview
- [ ] Read ALL generated files in blink project
- [ ] Found GPIO_TypeDef in CMSIS header — recognized the pattern from June
- [ ] Know: AHB1, APB1, APB2 bus hierarchy
- [ ] Know: GPIOC base address = 0x4002 0800

---

## DAY 3 — Friday, Jul 3

### 🔶 Morning Block (5:10 - 6:30 AM) — BLINK LED (REGISTER LEVEL) ⚠️ CRITICAL

#### 📺 WATCH (15 min)

**FastBit MCU1**: GPIO section — register-level configuration

#### 💻 CODE (1h) — THE REAL TEST

Create a NEW project: `02_blink_register`

In `main.c`, replace ALL HAL calls with direct register access:

```c
#include "stm32f4xx.h"

int main(void) {
    // 1. Enable GPIOC clock (RCC AHB1 peripheral clock enable register)
    RCC->AHB1ENR |= RCC_AHB1ENR_GPIOCEN;  // Set bit 2
    
    // 2. Configure PC13 as General Purpose Output
    // MODER register: 2 bits per pin. Pin 13 = bits [27:26]
    // 01 = General purpose output mode
    GPIOC->MODER &= ~(3U << 26);   // Clear bits 27:26
    GPIOC->MODER |=  (1U << 26);   // Set bit 26 (output mode)
    
    // 3. Configure output type: push-pull (bit 13 = 0)
    GPIOC->OTYPER &= ~(1U << 13);
    
    // 4. Configure speed: low (bits [27:26] = 00)
    GPIOC->OSPEEDR &= ~(3U << 26);
    
    // 5. No pull-up/pull-down
    GPIOC->PUPDR &= ~(3U << 26);
    
    while (1) {
        // Toggle PC13 using BSRR (atomic set/reset)
        GPIOC->BSRR = (1U << 13);          // Set PC13 (LED OFF — active low!)
        for (volatile int i = 0; i < 500000; i++);  // Crude delay
        
        GPIOC->BSRR = (1U << (13 + 16));   // Reset PC13 (LED ON)
        for (volatile int i = 0; i < 500000; i++);
    }
}
```

**MANDATORY: For every line, open RM0383 Section 8 (GPIO) and find:**
- MODER register layout (Figure 24, Table 24)
- OTYPER register layout
- BSRR register: why bits 0-15 = SET and bits 16-31 = RESET

**Draw on paper**: The MODER register with all 16 pin configurations (32 bits, 2 per pin).

### ✅ Day 3 Checklist
- [ ] Blink LED working WITHOUT any HAL function calls
- [ ] Can explain: RCC clock enable, MODER, OTYPER, OSPEEDR, PUPDR, BSRR
- [ ] Drew MODER register layout on paper
- [ ] Verified register addresses match RM0383
- [ ] **Understand: HAL does exactly this under the hood**

---

## DAY 4 — Saturday, Jul 4 (DEEP STUDY DAY)

### 💻 STM32 Deep Sessions (6:30 AM - 12:45 PM)

**Session 1 (6:30-7:30)**: FastBit ARM Cortex — Sections 3-4
- Bus interfaces deep dive (AHB, APB)
- Vector table, stack pointer, reset sequence
- How does the MCU boot? What happens before `main()`?

**Session 2 (7:45-9:15)**: Debug the blink with GDB
```
1. Click "Debug" button in STM32CubeIDE
2. Step through your register-level blink
3. Open "SFR" (Special Function Register) view
4. Watch GPIOC->MODER change as you step through
5. Watch GPIOC->ODR toggle as LED turns on/off
```

**Session 3 (9:30-11:00)**: Button input (HAL)
- Create `03_button_input_hal`
- Configure PA0 as GPIO_Input with internal pull-up
- Read button state: `HAL_GPIO_ReadPin(GPIOA, GPIO_PIN_0)`
- LED ON when button pressed, OFF when released
- Add debouncing with `HAL_Delay(50)`

**Session 4 (11:15-12:45)**: Button input (Register level)
- Create `04_button_input_register`
- Same button, same LED, but pure register access
- Read IDR register: `if (GPIOA->IDR & (1U << 0))`
- Configure PUPDR for internal pull-up

### 🇩🇪 German (2:00-5:00 PM)
- **Start Nicos Weg A2!** Lesson 1-2
- Review all A1 vocabulary in Anki
- A2 introduces: Perfekt tense, modal verbs (können, müssen, wollen)

### ✅ Day 4 Checklist
- [ ] ARM boot sequence understood (vector table → Reset_Handler → main)
- [ ] Used SFR view in debugger to watch registers change in real-time
- [ ] Button input working with HAL (with debounce)
- [ ] Button input working with register access
- [ ] Started Nicos Weg A2

---

## DAY 5 — Sunday, Jul 5 (REVIEW + GIT)

### 💻 Morning (7:30 AM - 12:30 PM)

**7:30-9:00**: From scratch, write a register-level blink program WITHOUT any reference.
- Time yourself. Target: under 15 minutes.
- If you can't → you don't understand GPIO yet → redo Day 3.

**9:15-10:45**: Read **RM0383 Section 8 (GPIO)** — ALL of it (about 15 pages)
- Draw the GPIO block diagram on paper
- List all GPIO registers with their offsets
- Understand alternate function (AF) — you'll need this for UART

**11:00-12:30**: Push code to GitHub
```bash
# Create a new repo structure for STM32 work
mkdir -p /mnt/f/Documents/DEVELOP/STM32-Practice
cd /mnt/f/Documents/DEVELOP/STM32-Practice
git init
# Copy project folders (or symlink)
```

Write a README explaining:
- What hardware you're using
- How to wire Black Pill to Nucleo ST-Link
- What each project does
- Register-level vs HAL comparison

### 🇩🇪 German (2:00-4:00 PM)
- Nicos Weg A2 Lesson 3
- Anki: add A2 vocabulary (new deck or expand A1 deck)
- Review: "Ich kann... / Ich muss... / Ich will..."

### ✅ Day 5 Checklist
- [ ] Register-level blink from memory in < 15 min
- [ ] RM0383 GPIO section fully read
- [ ] GPIO block diagram drawn on paper
- [ ] All projects pushed to GitHub with README
- [ ] Nicos Weg A2 started (lessons 1-3)

---

## 📋 WEEK 1 CHECKPOINT

- [ ] ✅ STM32CubeIDE installed, working, can flash to Black Pill via Nucleo ST-Link
- [ ] ✅ Blink LED with HAL (understand every generated line)
- [ ] ✅ Blink LED with register access (can write from memory)
- [ ] ✅ Button input with HAL AND register level
- [ ] ✅ ARM Cortex-M4 architecture basics (bus, memory map, boot sequence)
- [ ] ✅ RM0383 GPIO section read completely
- [ ] ✅ GPIO register layout drawn on paper (MODER, ODR, IDR, BSRR)
- [ ] ✅ GDB + SFR view used to watch register changes
- [ ] ✅ Nicos Weg A2 started (lessons 1-3), 160+ Anki cards
