# 📅 WEEK 2 — Jul 6-12 (Mon-Sun): GPIO DEEP — ALL MODES + ALTERNATE FUNCTIONS

> **Topics**: GPIO output modes (push-pull, open-drain), input modes (floating, pull-up, pull-down), alternate function, GPIO speed, multiple LEDs/buttons, LED patterns
> **FastBit MCU1**: GPIO sections (all of them — HAL + register)
> **"Mastering STM32" Book**: Chapter 4 (GPIO Management)
> **Reference Manual**: RM0383 Section 8 (GPIO) — complete mastery
> **Programs on hardware**: 5-7
> **German**: Nicos Weg A2 Lessons 4-8

---

## DAY 6 — Monday, Jul 6

### 🔶 Morning Block (5:10 - 6:30 AM) — GPIO OUTPUT MODES

#### 📺 WATCH (15 min)
**FastBit MCU1**: GPIO output types — push-pull vs open-drain

#### 💻 CODE (1h)

**Exercise 1 — Push-pull vs Open-drain (5:25-5:55):**

Create `05_gpio_output_modes`:
```c
// Push-pull: drives HIGH and LOW (default for LEDs)
// Pin can source AND sink current

// Open-drain: only drives LOW, floats for HIGH
// Needs external pull-up resistor for HIGH
// Used for: I2C (SDA/SCL), driving loads with different voltage
```

Configure two pins: one push-pull, one open-drain.
- Push-pull pin drives LED directly
- Open-drain pin: connect external 10K pull-up to 3.3V, then LED

Observe with multimeter: measure voltage on each pin in HIGH and LOW states.

**Exercise 2 — GPIO speed settings (5:55-6:15):**

Configure same pin at different speeds:
- Low speed → measure rise time on logic analyzer
- Very High speed → measure rise time

> **On STM32, higher speed = faster edge transitions = more EMI noise.** Only use High/Very High for fast protocols (SPI at 10+ MHz). Use Low for LEDs.

Register deep dive: `OSPEEDR` bits per pin:
```
00 = Low speed
01 = Medium speed
10 = Fast speed
11 = High speed
```

### ✅ Day 6 Checklist
- [ ] Push-pull vs open-drain: can explain the difference + when to use each
- [ ] Measured voltage with multimeter on both output types
- [ ] Understand GPIO speed settings and EMI implications
- [ ] Drew output stage diagram on paper (PMOS + NMOS for push-pull)

---

## DAY 7 — Tuesday, Jul 7

### 🔶 Morning Block (5:10 - 6:30 AM) — GPIO INPUT DEEP

#### 💻 CODE (1h 20m)

**Exercise 1 — All input modes (5:10-5:50):**

Create `06_gpio_input_modes`:
```c
// Configure multiple input pins with different settings:
// PA0: Floating input (no pull — for external switch with external pull-up)
// PA1: Internal pull-up (for button connected to GND)
// PA4: Internal pull-down (for button connected to VCC)
```

Wire 3 buttons:
- Button 1: PA0 → GND, external 10K pull-up to 3.3V
- Button 2: PA1 → GND (internal pull-up enabled)
- Button 3: PA4 → 3.3V (internal pull-down enabled)

Read all 3 and display on UART (or toggle different LEDs).

**What to understand**: Internal pull-up/down saves external components. This is configured via `PUPDR` register:
```
00 = No pull-up, no pull-down
01 = Pull-up
10 = Pull-down
11 = Reserved
```

**Exercise 2 — Software debouncing (5:50-6:20):**

```c
// Simple debounce: read twice with delay
uint8_t debounce_read(GPIO_TypeDef *port, uint16_t pin) {
    if (port->IDR & pin) {
        HAL_Delay(50);
        if (port->IDR & pin) {
            return 1;
        }
    }
    return 0;
}
```

Better: state machine debouncer (use your June state machine pattern!):
```c
typedef enum { IDLE, PRESSED_WAIT, PRESSED, RELEASED_WAIT } ButtonState;
```

### ✅ Day 7 Checklist
- [ ] All 3 input modes tested (floating, pull-up, pull-down)
- [ ] PUPDR register understood — drew on paper
- [ ] Debouncing implemented (simple + state machine)
- [ ] Can explain: why does a button bounce? How does debouncing fix it?

---

## DAY 8 — Wednesday, Jul 8

### 🔶 Morning Block (5:10 - 6:30 AM) — ALTERNATE FUNCTION (AF)

#### 📺 WATCH (15 min)
**FastBit MCU1**: Alternate function section

#### 💻 CODE (1h)

**Concept**: Every GPIO pin can do multiple things. For example, PA2 can be:
- Regular GPIO (input or output)
- USART2_TX (alternate function 7)
- TIM5_CH3 (alternate function 2)
- etc.

The AF is selected via `GPIOA->AFR[0]` (pins 0-7) and `GPIOA->AFR[1]` (pins 8-15).
Each pin gets 4 bits to select AF0-AF15.

**Exercise — Find alternate functions in datasheet:**

Open **DS10314** (STM32F411 Datasheet) → Table 9: "Alternate function mapping"

For USART2 on your Black Pill, find:
- PA2 = USART2_TX → AF7
- PA3 = USART2_RX → AF7

**This is prep for next week's UART.** You don't need to code UART yet, just understand HOW alternate functions work:

```c
// To configure PA2 as USART2_TX (AF7):

// 1. Set MODER to Alternate Function (10)
GPIOA->MODER &= ~(3U << 4);   // Clear bits [5:4] for PA2
GPIOA->MODER |=  (2U << 4);   // Set to AF mode (10)

// 2. Set AF7 in AFR[0] for pin 2 (bits [11:8])
GPIOA->AFR[0] &= ~(0xFU << 8);  // Clear AF bits for PA2
GPIOA->AFR[0] |=  (7U << 8);    // Set AF7 (USART2)
```

### ✅ Day 8 Checklist
- [ ] Understand alternate function concept — pins are multipurpose
- [ ] Found USART2 AF mapping in datasheet (PA2=TX, PA3=RX, AF7)
- [ ] Wrote AF configuration code for PA2/PA3 (register level)
- [ ] Can explain: MODER = AF mode, AFR selects which alternate function

---

## DAY 9 — Thursday, Jul 9

### 🔶 Morning Block (5:10 - 6:30 AM) — CLOCK SYSTEM (RCC) INTRO

#### 📺 WATCH (20 min)
**FastBit MCU1**: RCC section — clock tree overview

#### 💻 STUDY (1h)

**The STM32F411 clock tree** (RM0383 Section 6: RCC):

```
                    HSI (16 MHz internal RC)
                    HSE (8-25 MHz external crystal)
                         ↓
                    ┌─────────┐
                    │   PLL   │ → SYSCLK (up to 100 MHz for STM32F411)
                    └─────────┘
                         ↓
                    ┌─────────┐
                    │   AHB   │ → HCLK (CPU, DMA, memory)
                    └────┬────┘
                    ┌────┴────┐
                ┌───┤         ├───┐
            ┌───┴───┐     ┌───┴───┐
            │ APB1  │     │ APB2  │
            │ ≤50MHz│     │≤100MHz│
            └───────┘     └───────┘
            USART2,3      USART1,6
            I2C1,2,3      SPI1,4
            SPI2,3        TIM1,9-11
            TIM2-5        ADC1
            etc.          etc.
```

**KEY**: Before using ANY peripheral, you MUST enable its clock via RCC:
```c
RCC->AHB1ENR |= RCC_AHB1ENR_GPIOAEN;    // Enable GPIOA clock
RCC->APB1ENR |= RCC_APB1ENR_USART2EN;    // Enable USART2 clock
RCC->APB2ENR |= RCC_APB2ENR_ADC1EN;      // Enable ADC1 clock
```

**If you forget this → the peripheral simply doesn't respond. Most common STM32 beginner mistake.**

**Exercise**: Draw the complete clock tree on paper. Label:
- HSI frequency
- SYSCLK after PLL
- AHB prescaler value
- APB1 and APB2 frequencies
- Which bus each peripheral is on

### ✅ Day 9 Checklist
- [ ] Clock tree diagram drawn on paper
- [ ] Know: HSI = 16 MHz, max SYSCLK = 100 MHz (F411)
- [ ] Know: APB1 ≤ 50 MHz, APB2 ≤ 100 MHz
- [ ] Know: MUST enable peripheral clock before using it (RCC->xxxENR)
- [ ] Know which bus USART2 is on (APB1)

---

## DAY 10 — Friday, Jul 10

### 🔶 Morning Block (5:10 - 6:30 AM) — LED PATTERNS + COMBINE EVERYTHING

#### 💻 CODE (1h 20m)

**Exercise 1 — LED chaser (5:10-5:40):**

Create `07_led_chaser`:
- Wire 4 LEDs to PA0, PA1, PA4, PA5 (avoid PA2/PA3 — reserved for UART)
- Create a "Knight Rider" pattern: LEDs light up one at a time, sweeping back and forth
- Use register-level GPIO, not HAL

```c
uint16_t led_pins[] = {0, 1, 4, 5};  // Pin numbers

void led_on(uint8_t pin_num) {
    GPIOA->BSRR = (1U << pin_num);
}

void led_off(uint8_t pin_num) {
    GPIOA->BSRR = (1U << (pin_num + 16));
}
```

**Exercise 2 — Button-controlled LED brightness (crude PWM) (5:40-6:10):**

Toggle LED very fast with variable on/off ratio:
```c
// Crude PWM using software delays
void crude_pwm(uint16_t on_time, uint16_t off_time) {
    GPIOC->BSRR = (1U << 13);       // LED OFF (active low)
    for (volatile int i = 0; i < off_time; i++);
    GPIOC->BSRR = (1U << (13+16));  // LED ON
    for (volatile int i = 0; i < on_time; i++);
}
```

Button press increases brightness (longer on_time). This previews PWM — you'll do it properly with timers in August.

### ✅ Day 10 Checklist
- [ ] 4-LED chaser working (register-level)
- [ ] Crude software PWM for LED dimming
- [ ] All pins configured without HAL
- [ ] Can set up any GPIO pin for any mode from memory

---

## DAY 11 — Saturday, Jul 11 (DEEP STUDY DAY)

### 💻 Deep Sessions (6:30 AM - 12:45 PM)

**Session 1 (6:30-7:30)**: FastBit MCU1 — GPIO exercises and quizzes
- Complete ALL FastBit GPIO exercises
- Take the section quiz

**Session 2 (7:45-9:15)**: Register map exercise
- Open RM0383 Section 8.4 (GPIO register descriptions)
- For EACH register (MODER, OTYPER, OSPEEDR, PUPDR, IDR, ODR, BSRR, LCKR, AFR):
  - Draw the bit layout
  - Write the reset value
  - Write a 1-line C example setting specific bits

**Session 3 (9:30-11:00)**: "Mastering STM32" Chapter 4 exercises
- Read ALL of Chapter 4 (GPIO Management)
- Do every exercise in the chapter
- Compare HAL functions to your register implementations

**Session 4 (11:15-12:45)**: Interview prep
Write answers for:
1. "What is the difference between push-pull and open-drain?"
2. "Why does STM32 need RCC clock enable before using a peripheral?"
3. "What is an alternate function? How do you configure it?"
4. "What is the BSRR register and why is it better than writing to ODR?"
5. "Draw the STM32F411 memory map from memory."

### 🇩🇪 German (2:00-5:00 PM)
- Nicos Weg A2 Lessons 5-7
- Modal verbs practice: "Ich kann programmieren. Ich muss lernen."
- Anki: 165+ cards total

### ✅ Day 11 Checklist
- [ ] All FastBit GPIO exercises done
- [ ] All 9 GPIO registers drawn on paper with bit layouts
- [ ] "Mastering STM32" Ch 4 read completely
- [ ] 5 interview answers written

---

## DAY 12 — Sunday, Jul 12 (REVIEW + GIT)

### 💻 Morning (7:30 AM - 12:30 PM)

**7:30-9:00**: From blank project, write register-level code that:
1. Configures PA5 as output (push-pull, low speed, no pull)
2. Configures PA0 as input (internal pull-up)
3. LED follows button: pressed = ON, released = OFF
4. All done WITHOUT referencing any notes or RM0383

Target: complete in < 20 minutes. This is your "GPIO from memory" test.

**9:15-10:45**: Read RM0383 Section 6 (RCC) — Clock tree section
- Focus on PLL configuration (you'll configure SYSCLK to 100 MHz next week)
- Find USART2 clock source (APB1)

**11:00-12:30**: Git push all Week 2 projects. Write comprehensive README.

### ✅ Day 12 Checklist
- [ ] GPIO from memory test: complete in < 20 min
- [ ] RCC section read — understand PLL, prescalers
- [ ] All code pushed to GitHub

---

## 📋 WEEK 2 CHECKPOINT

- [ ] ✅ All GPIO output modes mastered (push-pull, open-drain)
- [ ] ✅ All GPIO input modes mastered (floating, pull-up, pull-down)
- [ ] ✅ Alternate function concept understood — AF register configured
- [ ] ✅ RCC clock tree drawn from memory — know which bus each peripheral uses
- [ ] ✅ Software debouncing implemented (simple + state machine)
- [ ] ✅ Multi-LED patterns working (register-level)
- [ ] ✅ Can configure ANY GPIO pin for ANY mode from memory in < 5 min
- [ ] ✅ RM0383 GPIO and RCC sections read
- [ ] ✅ Nicos Weg A2 lessons 4-8, 165+ Anki cards
