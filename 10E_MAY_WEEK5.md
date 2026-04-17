# 📅 WEEK 5 — May 26-31 (Tue-Sun): SPECIAL TOPICS + MONTH REVIEW

> **Topics**: enum, volatile, const, static, extern, file I/O, preprocessor, Makefile, month test
> **K&R Chapters**: Chapter 4 (finish — Preprocessor), Chapter 7 (Input/Output) start
> **Programs to write**: 6-8
> **German**: Nicos Weg Lessons 21-25, review all vocabulary, first attempt at writing a paragraph
> **Goal**: Finish May with solid C fundamentals ready for STM32 in July

---

## DAY 26 — Tuesday, May 26

### 🔶 Morning (5:10-6:30 AM) — Enums + State Machines

**What to learn**: `enum` gives names to numbers. State machines are THE design pattern for embedded firmware — every embedded device is a state machine.

**How to learn**:
1. **(5:10-5:20)** Read **K&R section on enumerations** (pp. 39-40). Short section.
2. **(5:20-5:50)** Write `enum_states.c`:
   - Define: `typedef enum { STATE_IDLE, STATE_RUNNING, STATE_ERROR, STATE_DONE } State;`
   - These become 0, 1, 2, 3 automatically
   - Write a state machine using `switch(current_state)` in a `while(1)` loop
   - Simulate: Traffic light controller — RED → GREEN → YELLOW → RED
   - Each state prints what's happening, waits (use `sleep(1)` on Linux), transitions to next state
   - **Why state machines are EVERYTHING in embedded**:
     - Washing machine? State machine (fill → wash → rinse → spin → done)
     - UART driver? State machine (idle → receiving → processing → sending)
     - Your STM32 LED blink? State machine (on → wait → off → wait)
     - FreeRTOS task states? State machine (ready → running → blocked → suspended)

3. **(5:50-6:20)** Write `state_machine_menu.c`:
   - A vending machine simulator with states: IDLE → COIN_INSERTED → ITEM_SELECTED → DISPENSING → CHANGE → IDLE
   - Use enums for states AND for items
   - This is EXACTLY the kind of code you'll write on STM32 for real products

4. **(6:20-6:30)** Review: Can you explain what a state machine is without looking? Draw the traffic light state diagram on paper (circles and arrows).

### 🎧 Commute: Nicos Weg Lesson 21 | 📱 Lunch: Anki | 📖 Bed: K&R Chapter 4 (pp. 85-90, Preprocessor intro)

### ✅ Day 26: `enum_states.c` + `state_machine_menu.c`. State machine concept mastered.

---

## DAY 27 — Wednesday, May 27

### 🔶 Morning (5:10-6:30 AM) — volatile, const, static, extern — Storage Classes

**What to learn**: These 4 keywords control HOW and WHERE variables are stored and accessed. They're used in EVERY embedded C file.

**How to learn**:
1. **(5:10-5:15)** Jacob Sorber videos (watch these short ones): "The static keyword" (~5 min), "volatile in C" (~6 min), "extern in C" (~4 min)

2. **(5:15-5:45)** Write `storage_classes.c` — demonstrate each one:

   **`const`**:
   - `const int MAX_TEMP = 150;` — value CANNOT be changed after initialization
   - Try to modify it: compiler error!
   - **Embedded use**: Configuration values, calibration constants, lookup tables stored in FLASH

   **`static`** (3 different meanings!):
   - Static local variable: retains value between function calls (like a mini-global)
   - Static global variable: visible only in this `.c` file (file scope)
   - Static function: callable only within this `.c` file (information hiding)
   - **Embedded use**: Static variables = persistent counters in interrupt handlers. Static functions = internal module functions hidden from other modules.

   **`volatile`**:
   - `volatile int sensor_value;` — tells compiler "this value can change at ANY time without the code changing it"
   - WITHOUT volatile, compiler might optimize away your loop: `while (flag == 0) {}` → compiler sees flag never changes → removes the loop!
   - **Embedded use**: EVERY hardware register access, EVERY shared variable in interrupts. If you forget `volatile` on an ISR flag, your code WILL break at -O2 optimization. This is the #1 embedded C bug that students miss.
   - **Ask Google AI**: "Give me a real example of a bug caused by missing `volatile` in embedded C. Show the assembly difference."

   **`extern`**:
   - `extern int count;` — "this variable EXISTS in another file, don't allocate memory, just reference it"
   - Used in header files to share global variables across `.c` files
   - **Embedded use**: Sharing configuration between modules

3. **(5:45-6:20)** Write a multi-file example:
   - `config.h` — declare `extern const int MAX_SENSORS;`
   - `config.c` — define `const int MAX_SENSORS = 8;`
   - `main.c` — `#include "config.h"` and use `MAX_SENSORS`
   - Compile: `gcc main.c config.c -o main -Wall`

4. **(6:20-6:30)** Quick quiz yourself: What's the difference between `const int *p` and `int * const p` and `static int x` and `volatile int y`?

### 🎧 Commute: Nicos Weg Lesson 22 | 📱 Lunch: Anki | 📖 Bed: K&R Chapter 4 pp. 90-93

### ✅ Day 27: `storage_classes.c` + multi-file extern example. ALL 4 keywords understood.

---

## DAY 28 — Thursday, May 28

### 🔶 Morning (5:10-6:30 AM) — File I/O

**What to learn**: Reading from and writing to files. In embedded, you might not have files — but you WILL have data logging, configuration parsing, and firmware update buffers that work the same way.

**How to learn**:
1. **(5:10-5:20)** Read **K&R Chapter 7** pages 151-160 (Standard I/O)

2. **(5:20-5:50)** Write `file_io.c`:
   - Write to file: `FILE *fp = fopen("log.txt", "w"); fprintf(fp, "Sensor: %d\n", value); fclose(fp);`
   - Read from file: `FILE *fp = fopen("log.txt", "r"); fscanf(fp, ...); fclose(fp);`
   - Read line by line: `fgets(line, sizeof(line), fp)`
   - Append mode: `fopen("log.txt", "a")` — add without overwriting
   - **ALWAYS check**: `if (fp == NULL) { perror("Error"); return 1; }`
   - **Embedded connection**: Data logging to SD card, reading config files, storing calibration data

3. **(5:50-6:20)** Write `csv_parser.c`:
   - Read a simple CSV file (name,cgpa,branch)
   - Parse each line using `strtok()` or manual comma splitting
   - Store in array of structs
   - **Why this matters**: Parsing structured data is what embedded devices do with sensor packets, GPS NMEA sentences, AT commands from modems

4. **(6:20-6:30)** Write `binary_file.c`:
   - Write struct to file in binary mode: `fwrite(&student, sizeof(Student), 1, fp);`
   - Read it back: `fread(&student, sizeof(Student), 1, fp);`
   - **Embedded use**: EEPROM emulation, firmware image reading, raw sensor data storage

### 🎧 Commute: Nicos Weg Lesson 23 | 📱 Lunch: Anki | 📖 Bed: K&R Chapter 7 finish

### ✅ Day 28: `file_io.c` + `csv_parser.c` + `binary_file.c`. fopen/fclose/fprintf/fscanf/fwrite/fread all used.

---

## DAY 29 — Friday, May 29

### 🔶 Morning (5:10-6:30 AM) — Preprocessor + Makefile

**What to learn**: `#define`, `#ifdef`, `#ifndef`, `#include` guards, conditional compilation. Plus: how to write a Makefile so you don't type long `gcc` commands every time.

**How to learn**:
1. **(5:10-5:20)** Read **K&R pages 88-93** (Macro substitution, Conditional inclusion)

2. **(5:20-5:45)** Write `preprocessor.c`:
   - Simple macros: `#define PI 3.14159`, `#define MAX(a,b) ((a) > (b) ? (a) : (b))`
   - **WARNING**: Macro pitfall: `MAX(i++, j++)` — i or j gets incremented twice! This is a classic C bug.
   - Conditional compilation:
     ```
     #define DEBUG 1
     #ifdef DEBUG
         printf("Debug: x = %d\n", x);
     #endif
     ```
   - **Embedded use**: Same code compiled for different boards: `#ifdef STM32F411` vs `#ifdef STM32F103`. Debug prints compiled out in release builds.

3. **(5:45-6:15)** Write your first `Makefile`:
   - For your week5 multi-file project
   - Rules: `all`, `clean`, variable for compiler and flags
   - Target/dependency/recipe structure
   - Watch **Jacob Sorber: "Makefiles"** (~8 min) if stuck
   - **This is mandatory knowledge**: Every professional embedded project uses Make or CMake. No more typing `gcc main.c utils.c math.c -o main -Wall -g` by hand.

4. **(6:15-6:30)** Add include guards to ALL your `.h` files from this month:
   ```
   #ifndef MATH_UTILS_H
   #define MATH_UTILS_H
   // declarations here
   #endif
   ```

### 🎧 Commute: Nicos Weg Lesson 24 | 📱 Lunch: Anki | 📖 Bed: Review K&R chapters 1-7 (skim)

### ✅ Day 29: `preprocessor.c` + first `Makefile`. Conditional compilation understood.

---

## DAY 30 — Saturday, May 30 🟩 REVIEW + GIT PUSH DAY

### 💻 Full Morning (6:30 AM - 12:30 PM) — Re-type + Polish + Push

**Session 1 (6:30-8:00)**: Re-type your 5 hardest programs from memory:
1. Bubble sort (swap + nested loops)
2. Your own strlen (pointer traversal to `\0`)
3. Pointer swap function (pass by reference)
4. Malloc + array + free (dynamic memory)
5. Bit manipulation macros (SET, CLEAR, TOGGLE, CHECK)

**Time yourself.** Each should take under 10 minutes. If any takes longer than 15 min, that topic needs more practice in June.

**Session 2 (8:15-9:45)**: Polish register simulator + student records — add comments, clean up code, write README for each.

**Session 3 (10:00-12:00)**: Git push ALL remaining weeks:
- `git add . → git commit -m "Weeks 4-5: structs, bitwise, file I/O" → git push`
- Update main README with full month progress
- **Milestone**: Your GitHub now shows 30 days of green!

### 🇩🇪 German (2:00-5:00 PM)
- Nicos Weg Lesson 24-25
- Google AI: Practice describing your week in German
- Anki: mega review all 100+ cards

### ✅ Day 30: 5 programs from memory. All code pushed. GitHub portfolio updated.

---

## DAY 31 — Sunday, May 31 🟨 THE MONTH TEST

### 💻 Morning (7:30 AM - 12:30 PM) — FINAL TEST + PORTFOLIO UPDATE

**THE TEST**: Write ONE complete program that uses EVERYTHING you learned this month. No references. No AI. No internet. Just you, `nano`, and `gcc`.

**Program**: `month_test.c` — An embedded sensor data system simulator:

Requirements (write ALL from scratch):
1. **Structs**: `SensorReading` with timestamp, temperature, humidity, status flags
2. **Array of structs**: Store 10 readings
3. **Pointers**: Pass arrays by pointer to functions
4. **Dynamic memory**: Allocate reading array with malloc, free at end
5. **Bitwise**: Use flags field to store: `FLAG_VALID`, `FLAG_ALARM`, `FLAG_CALIBRATED`
6. **Functions**: `add_reading()`, `find_max_temp()`, `count_alarms()`, `print_all()`
7. **File I/O**: Save readings to `sensor_log.csv`, then read them back
8. **Enum**: State machine for sensor states: INIT → READING → PROCESSING → LOGGING → IDLE
9. **Preprocessor**: `#define MAX_READINGS 10`, `#ifdef DEBUG`
10. **Multi-file**: Split into `sensor.h`, `sensor.c`, `main.c`, and a `Makefile`

**Grading yourself**:
- Can compile with `make` → ✅
- All 10 features present → ✅
- Valgrind shows zero leaks → ✅
- Code is clean and commented → ✅

### 🇩🇪 German (2:00-5:00) — END OF MONTH CELEBRATION + REVIEW
- Nicos Weg Lesson 25 (if not done)
- **Write a paragraph in German** (5-7 sentences):
  ```
  Ich heiße Khashyap. Ich bin dreiundzwanzig Jahre alt.
  Ich komme aus Indien. Ich bin Ingenieur.
  Ich lerne Deutsch und C-Programmierung.
  Ich möchte nach Deutschland gehen.
  Ich stehe jeden Tag um fünf Uhr auf.
  ```
- Have Google AI correct your paragraph, explain errors
- Anki: FINAL mega review — how many of 100+ cards do you know?

### 💻 Git Push + Portfolio (after German)
- Push `month_test.c` to GitHub
- Update README with COMPLETE month 1 summary
- Take screenshot of your GitHub contribution graph — it should show 30+ days of green!
- **This is the start of your portfolio.** By the time German universities see this (2028), you'll have 24 months of green squares and 15+ professional projects.

### ✅ Day 31: Month test PASSED. 30+ programs on GitHub. 100+ German words. Month 1 COMPLETE.

---

## 📊 MAY 2026 — FINAL SCORECARD

| Metric | Target | Result | Notes |
|:---|:---|:---|:---|
| C programs written | 30+ | [ ] | Count them in your C-Practice folder |
| GitHub commits | 15+ | [ ] | Check contribution graph |
| K&R chapters read | 1-7 | [ ] | Should be comfortable with chapters 1-6 |
| Programs from memory | 10+ | [ ] | Bubble sort, strlen, swap, malloc, bit macros, etc. |
| GDB debugging sessions | 5+ | [ ] | Should know: break, run, next, print, quit |
| Valgrind runs | 3+ | [ ] | Should know how to detect leaks |
| Nicos Weg lessons | 20-25 | [ ] | Almost finished A1 content |
| German words in Anki | 100+ | [ ] | Check Anki stats |
| German sentences written | 15+ | [ ] | Count in your notebook |
| 5 AM wake-ups | ≥ 25/31 | [ ] | Be honest with yourself |

---

## 🔭 WHAT'S NEXT — JUNE 2026 PREVIEW

| Topic | Description |
|:---|:---|
| **Linked Lists complete** | Insert, delete, reverse, doubly linked, circular |
| **Makefiles deep** | Variables, pattern rules, automatic variables |
| **GDB mastery** | Watchpoints, conditional breakpoints, core dumps |
| **K&R finish** | Chapters 7-8, Appendix A (grammar reference) |
| **Start using CLion** | JetBrains IDE for multi-file C projects |
| **Educative course start** | "Grokking the Behavioral Interview" (5h) — prep for Unistring exit conversations |
| **German A1 continue** | Nicos Weg A1 finish, start Duolingo for grammar drills |

> **June is when baby C becomes real C.** Dynamic data structures, proper build systems, proper debugging. The bridge to STM32 in July.

---

## 🗂️ YOUR FOLDER AFTER MAY 31

```
C-Practice/
├── README.md            ← Updated weekly
├── .gitignore
├── week1/
│   ├── hello.c, variables.c, input.c, datatypes.c
│   ├── operators.c, ascii.c, type_casting.c
│   ├── conditions.c, switch_demo.c
│   ├── loops.c, patterns.c, number_games.c
│   ├── functions.c, calculator.c
│   └── (10-15 files)
├── week2/
│   ├── arrays.c, array_operations.c
│   ├── bubble_sort.c, selection_sort.c, search.c
│   ├── strings_basic.c, my_strlen.c, my_reverse.c, my_strcmp.c, my_strcpy.c
│   ├── string_library.c, safe_input.c
│   ├── matrix.c, string_array.c
│   ├── scope.c, math_utils.h, math_utils.c
│   └── student_records.c (10-12 files)
├── week3/
│   ├── pointer_basics.c, pointer_sizes.c, pointer_arithmetic.c
│   ├── pointer_vs_array.c, swap.c, pass_by_ref.c
│   ├── array_functions.c, const_pointers.c, string_pointers.c
│   ├── malloc_demo.c, dynamic_string.c
│   ├── double_pointer.c, dynamic_2d.c, function_pointers.c
│   └── phonebook.c (10-12 files)
├── week4/
│   ├── struct_basics.c, struct_functions.c
│   ├── student_system.c, university_db.c, sizeof_struct.c
│   ├── dynamic_structs.c, linked_list_intro.c
│   ├── bitwise_basics.c, bit_macros.c, bit_patterns.c
│   ├── flags.c, rgb_color.c
│   └── register_simulator.c  ⭐ (10-12 files)
├── week5/
│   ├── enum_states.c, state_machine_menu.c
│   ├── storage_classes.c, config.h, config.c
│   ├── file_io.c, csv_parser.c, binary_file.c
│   ├── preprocessor.c
│   ├── Makefile                ⭐
│   ├── sensor.h, sensor.c     ⭐
│   └── month_test.c           ⭐ (8-10 files)
└── (TOTAL: 50-60 files, all hand-written, zero AI code)
```

---

> **You started with `printf("Hello World")`. You ended with a multi-file, Makefile-built, Valgrind-tested sensor system simulator with structs, pointers, bitwise, file I/O, and state machines.**
>
> **In 31 days, you went from zero to C fundamentals. The hard part is over. Now comes the fun part: STM32.**
