# 📅 WEEK 4 — Jun 23-30 (Mon-Tue): PHASE 1 CAPSTONE + MONTH TEST + STM32 PREP

> **Topics**: Final C capstone project, comprehensive month test, Phase 1 exit exam, STM32 prep
> **K.N. King Chapters**: Ch 22 (I/O deep), Ch 24 (Error Handling), review ALL chapters
> **K&R Bed Reading**: Chapter 7 (I/O), Chapter 8 (UNIX System Interface — preview for embedded)
> **Goal**: Prove you're ready for STM32. One polished project. One comprehensive test.
> **German**: Nicos Weg Lessons 41-50 (finish A1!), start A2
> **📚 Full resource details**: See `10_RESOURCES.md`

---

## DAY 22 — Monday, Jun 23

### 🔶 Morning Block (5:10 - 6:30 AM) — CAPSTONE PROJECT PLANNING

#### 💻 PLAN + START (1h 20m)

**Phase 1 Capstone: "Embedded System Simulator"**

Build a complete C project that simulates an embedded system on your PC. This combines EVERYTHING from May + June:

```
week9/embedded_simulator/
├── main.c                 # Main loop + state machine
├── sensor.c / sensor.h    # Simulated sensor (random ADC values)
├── uart.c / uart.h        # Simulated UART (printf to console)
├── gpio.c / gpio.h        # Simulated GPIO (bit manipulation on registers)
├── timer.c / timer.h      # Simulated timer (using time.h)
├── ringbuf.c / ringbuf.h  # Circular buffer for sensor data
├── logger.c / logger.h    # Data logger (writes to CSV file)
├── config.h               # All #defines, constants
├── Makefile               # Build system
└── README.md              # Documentation
```

**What it does:**
1. **State machine** controls the system: INIT → CALIBRATE → RUNNING → ERROR → SHUTDOWN
2. **Simulated sensor** generates random ADC values (0-4095, like 12-bit ADC)
3. **Circular buffer** stores last N sensor readings
4. **Timer** triggers periodic sampling (every "1 second" using `time.h`)
5. **GPIO simulation** — LED status bits (bit manipulation on a `uint32_t` register)
6. **UART simulation** — prints formatted data to console (like printf over UART)
7. **Data logger** — writes timestamped readings to a CSV file
8. **Error handling** — detects out-of-range values, transitions to ERROR state

Today: Plan the architecture. Write ALL header files. Implement `config.h`, `ringbuf.c`, `sensor.c`.

### ✅ Day 22 Checklist
- [ ] Project structure created (all files, all folders)
- [ ] All header files written with function declarations
- [ ] config.h with all constants defined
- [ ] ringbuf.c implemented (re-use your Week 2 circular buffer)
- [ ] sensor.c — random ADC value generator working
- [ ] Makefile started

---

## DAY 23 — Tuesday, Jun 24

### 🔶 Morning Block (5:10 - 6:30 AM) — CAPSTONE: CORE IMPLEMENTATION

#### 💻 CODE (1h 20m)

Implement:
- `gpio.c` — simulated GPIO register with SET/CLEAR/TOGGLE bit macros
- `uart.c` — formatted output function (wraps printf but adds timestamps)
- `timer.c` — periodic timer using `clock()` or `time()`

```c
// gpio.h example
#define LED_STATUS_PIN   0
#define LED_ERROR_PIN    1
#define LED_DATA_PIN     2

void gpio_init(void);
void gpio_set_pin(uint32_t pin);
void gpio_clear_pin(uint32_t pin);
void gpio_toggle_pin(uint32_t pin);
uint32_t gpio_read_pin(uint32_t pin);
void gpio_print_register(void);  // Print all 32 bits in binary
```

```c
// uart.h example
void uart_init(void);
void uart_send_string(const char *str);
void uart_printf(const char *fmt, ...);  // Use stdarg.h for variadic
```

### ✅ Day 23 Checklist
- [ ] gpio.c — bit manipulation register working
- [ ] uart.c — formatted output with timestamps
- [ ] timer.c — periodic trigger mechanism
- [ ] All modules compile independently

---

## DAY 24 — Wednesday, Jun 25

### 🔶 Morning Block (5:10 - 6:30 AM) — CAPSTONE: STATE MACHINE + INTEGRATION

#### 💻 CODE (1h 20m)

Implement `main.c` with the full state machine:

```c
typedef enum {
    SYS_INIT,
    SYS_CALIBRATE,
    SYS_RUNNING,
    SYS_ERROR,
    SYS_SHUTDOWN
} SystemState;

typedef SystemState (*StateHandler)(void);

SystemState handle_init(void) {
    uart_printf("System initializing...\n");
    gpio_init();
    sensor_init();
    ringbuf_init(&sensor_buffer);
    return SYS_CALIBRATE;
}

SystemState handle_calibrate(void) {
    // Read 10 samples, calculate baseline
    // ...
    return SYS_RUNNING;
}

SystemState handle_running(void) {
    int value = sensor_read();
    ringbuf_write(&sensor_buffer, value);
    
    if (value > SENSOR_MAX || value < SENSOR_MIN) {
        gpio_set_pin(LED_ERROR_PIN);
        return SYS_ERROR;
    }
    
    gpio_toggle_pin(LED_DATA_PIN);
    logger_write(value);
    return SYS_RUNNING;
}

// ... implement handle_error, handle_shutdown
```

Implement `logger.c` — writes to `sensor_log.csv`:
```
timestamp,reading,status
1719300000,2048,OK
1719300001,2100,OK
1719300002,4500,ERROR
```

### 🇩🇪 German (if Wednesday is German morning)
- Nicos Weg Lesson 41-42 (starting final A1 section!)

### ✅ Day 24 Checklist
- [ ] State machine dispatching through function pointer array
- [ ] All 5 states implemented and transitions working
- [ ] Logger writing CSV file with real data
- [ ] Error detection triggering state transition
- [ ] The whole system runs in a loop for 30+ "seconds"

---

## DAY 25 — Thursday, Jun 26

### 🔶 Morning Block (5:10 - 6:30 AM) — CAPSTONE: POLISH + DOCUMENTATION

#### 💻 CODE (1h 20m)

- Add command-line arguments: `./simulator --duration 60 --sample-rate 1`
- Add statistics: min, max, average of sensor readings
- Add graceful shutdown with signal handling (Ctrl+C → SYS_SHUTDOWN)
- Write comprehensive `README.md`:
  - Project description
  - How to build (`make`)
  - How to run
  - Architecture diagram (draw in ASCII art)
  - What each module does
  - What you learned
  - How this maps to real STM32 (the simulation → reality table)

**Simulation → Reality mapping table (put in README):**

| Simulator (PC) | Real STM32 (July+) |
|:---|:---|
| `printf()` | `HAL_UART_Transmit()` |
| `rand() % 4096` | `HAL_ADC_GetValue()` |
| `uint32_t gpio_reg` | `GPIOA->ODR` (real register at 0x40020014) |
| `time()` | `HAL_TIM_Base_Start_IT()` |
| `fopen("log.csv")` | Flash memory or SD card |
| `ringbuf_write()` | Same code! Works on both PC and STM32 |

### ✅ Day 25 Checklist
- [ ] Command-line arguments working
- [ ] Statistics calculated (min/max/avg)
- [ ] README with architecture diagram and simulation→reality table
- [ ] Code compiles with `-Wall -Wextra -Werror` — zero warnings

---

## DAY 26 — Friday, Jun 27

### 🔶 Morning Block (5:10 - 6:30 AM) — PHASE 1 COMPREHENSIVE TEST

**Time yourself. No AI. No books. No references. Just you and gcc.**

Test 1 (15 min): From a blank file, implement a circular buffer.
```bash
touch test_ringbuf.c
# Implement: init, write, read, is_full, is_empty
# Timer starts NOW
```

Test 2 (20 min): From a blank file, implement a singly linked list.
```bash
touch test_linked_list.c
# Implement: create_node, insert_front, insert_back, delete, reverse, free_list, print
```

Test 3 (15 min): From a blank file, write a Makefile for a 4-file project.
```bash
touch Makefile
# Write proper Makefile with CC, CFLAGS, pattern rules, clean, .PHONY
```

Test 4 (15 min): Write a state machine with function pointer dispatch table.
```bash
touch test_state_machine.c
# 3 states, transitions, handler function array
```

Test 5 (15 min): Debug this program using only GDB:
```c
// Someone gives you this buggy code. Find ALL bugs.
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char *create_greeting(const char *name) {
    char buffer[50];
    sprintf(buffer, "Hello, %s!", name);
    return buffer;  // BUG: returning local array
}

int main(void) {
    char *msg = create_greeting("Khashyap");
    printf("%s\n", msg);
    
    int *arr = malloc(3 * sizeof(int));
    arr[0] = 10; arr[1] = 20; arr[2] = 30;
    
    for (int i = 0; i <= 3; i++) {  // BUG: off-by-one
        printf("arr[%d] = %d\n", i, arr[i]);
    }
    
    free(arr);
    free(arr);  // BUG: double free
    
    return 0;
}
```

**Score yourself:**
- Test 1 in < 15 min: ✅
- Test 2 in < 20 min: ✅
- Test 3 in < 15 min: ✅
- Test 4 in < 15 min: ✅
- Test 5 all 3 bugs found: ✅

**If you failed any test → spend the weekend re-practicing that topic.**
**If you passed all 5 → you are READY for STM32.**

### ✅ Day 26 Checklist
- [ ] All 5 tests attempted
- [ ] Scored myself honestly
- [ ] Identified weak areas for weekend catch-up

---

## DAY 27-28 — Saturday-Sunday, Jun 28-29 (FINAL WEEKEND)

### Saturday (6:30 AM - 12:45 PM) — CAPSTONE FINALIZATION

**Session 1 (6:30-9:15)**: Fix any bugs in your capstone. Run Valgrind. Zero leaks. Zero warnings.

**Session 2 (9:30-12:45)**: Git push the complete capstone project:
```bash
cd /mnt/f/Documents/DEVELOP/C-Practice
git add -A
git commit -m "Phase 1 Capstone: Embedded System Simulator - complete C foundation project"
git push
```

Review your ENTIRE C-Practice repo. You should have:
```
C-Practice/
├── week1/     # Hello world, variables, loops
├── week2/     # Functions, arrays, strings
├── week3/     # Pointers (the critical week)
├── week4/     # Structs, bitwise
├── week5/     # File I/O, preprocessor, volatile
├── week6/     # Makefiles, GDB, multi-file
├── week7/     # Linked lists, queues, circular buffer
├── week8/     # State machines, memory layout, bit fields
└── week9/     # CAPSTONE: Embedded System Simulator
```

**That's 9 weeks, 50+ programs, 1 capstone. You built this WITHOUT AI.** 💪

### Saturday Afternoon — German (2:00-5:00 PM)
- Nicos Weg Lessons 45-48
- Mega Anki review (150+ cards)
- **You're almost done with A1!**

### Sunday (7:30 AM - 12:30 PM) — STM32 PREP

**7:30-9:00**: Read **"Mastering STM32"** by Carmine Noviello — Chapter 1 (Introduction)
- Skim the first 30 pages
- Understand what STM32CubeIDE is, what HAL is, what CMSIS is

**9:15-10:45**: Install **STM32CubeIDE** on Windows
- Download from st.com
- Create your first empty project for STM32F411CEU6
- Don't code anything — just see the IDE, see the generated files

**11:00-12:30**: Watch **FastBit MCU1 course** — Section 1 (Introduction)
- Watch at 1.5× speed
- Get the big picture of what July-September will look like

### Sunday Afternoon — German (2:00-4:00 PM)
- Nicos Weg Lessons 49-50 → **A1 COMPLETE!** 🎉
- Review all vocabulary
- Write a paragraph about yourself in German (past + present tense)

### 📋 Weekly Review (4:00-4:30 PM) — MONTH REVIEW
- How many total programs written in June?
- Phase 1 test results review
- Capstone project quality check
- Set July goals

---

## DAY 29 — Monday, Jun 30 — LAST DAY OF PHASE 1

### 🔶 Morning Block (5:10 - 6:30 AM) — PHASE 1 EXIT INTERVIEW

**Pretend you're in a job interview. Answer these OUT LOUD (not in your head):**

1. "Explain the difference between stack and heap memory"
2. "What is a pointer? Draw a diagram showing pointer to pointer"
3. "What does `volatile` mean and when must you use it?"
4. "What is a circular buffer and where is it used in embedded?"
5. "Explain the C compilation pipeline — all 4 stages"
6. "What is a state machine? Draw one for a washing machine"
7. "What is struct padding? How do you prevent it?"
8. "How are hardware registers accessed in C?"
9. "What is a function pointer? Give a real use case"
10. "What is the difference between `const int *p` and `int *const p`?"

**If you can answer all 10 confidently → Phase 1 is COMPLETE.**
**If you struggle on any → mark it and fix it in Week 1 of July (evenings).**

### 🎧 Commute — Final German A1 review
- Listen to Nicos Weg A1 highlights
- Practice: introduce yourself, daily routine, family, food, past tense

---

## 📋 WEEK 4 CHECKPOINT — END OF PHASE 1

- [ ] ✅ Capstone project complete and on GitHub with README
- [ ] ✅ Phase 1 test: passed all 5 timed tests
- [ ] ✅ Phase 1 exit interview: answered 10/10 questions confidently
- [ ] ✅ Zero warnings, zero memory leaks in all programs
- [ ] ✅ 50+ programs in C-Practice repo, properly organized
- [ ] ✅ STM32CubeIDE installed, first empty project created
- [ ] ✅ Nicos Weg A1 COMPLETE (50 lessons), 150+ Anki cards
- [ ] ✅ **READY FOR PHASE 2: STM32 MICROCONTROLLER PROGRAMMING** 🚀

---

## 🎯 PHASE 1 COMPLETE — WHAT YOU'VE BUILT

```
MAY-JUNE 2026: 9 WEEKS OF PURE C PROGRAMMING

Week 1:  Setup + basics → "I can write Hello World"
Week 2:  Functions + arrays → "I can solve problems"
Week 3:  POINTERS → "I understand how memory works"
Week 4:  Structs + bitwise → "I can manipulate hardware registers"
Week 5:  File I/O + special → "I understand the full C language"
Week 6:  Makefiles + GDB → "I can build and debug real projects"
Week 7:  Data structures → "I can implement linked lists and queues"
Week 8:  State machines → "I can design embedded firmware patterns"
Week 9:  CAPSTONE → "I can build a complete system in C"

You wrote 50+ programs WITHOUT AI.
You debugged them WITH GDB, not printf.
You drew memory diagrams on PAPER.
You can explain EVERYTHING on a whiteboard.

THIS is your foundation. THIS is what makes you a Type 3 engineer.
AI can generate code. YOU understand why it works.

JULY 1st → STM32 begins. The real hardware journey starts. 🔧
```
