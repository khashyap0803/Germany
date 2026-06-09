# JULY WEEK 2 (Jul 7–13) — Phase 1 Week 5: SPECIAL C TOPICS

> **Topics**: volatile, const, extern, static, enum, typedef, preprocessor (#define, #ifdef, macros), file I/O (fopen/fclose/fread/fwrite/fgets/fprintf)
> **K.N. King Reading**: Ch 14 (Preprocessor), Ch 20 (Low-Level — volatile/const), Ch 22 (Input/Output)
> **K&R Bed Reading**: Chapter 7 (Input and Output)
> **FastBit Embedded C**: Watch the volatile + const + extern sections on Saturday warmup
> **AI Policy**: BANNED for code — AI may only explain concepts
> **Dates**: Tuesday July 7 → Monday July 13, 2026

---

## WEEKDAY READING SCHEDULE (Jul 7–11)

### Tuesday July 7 — Pre-Gym (5:00–5:25 AM)
**Read**: K.N. King Chapter 14 (Preprocessor — pages 1–20)
- `#define` for constants: `#define PI 3.14159265` — NOT a variable, replaced by text
- `#define` for macros with arguments: `#define SQUARE(x) ((x)*(x))` — parentheses critical
- Why `SQUARE(x+1)` expands to `((x+1)*(x+1))` but `SQUARE(x+1)` without parens would break
- `#include` system headers `<file.h>` vs user headers `"file.h"` — what the difference means
- Include guards: `#ifndef MYHEADER_H` — prevents double-inclusion

**Bed Reading (9:30–10:00 PM)**: K&R Chapter 7 pages 151–165 (Standard Input/Output)

### Wednesday July 8 — Pre-Gym (5:00–5:25 AM)
**Read**: K.N. King Chapter 14 (Preprocessor — pages 20–end)
- Conditional compilation: `#ifdef DEBUG`, `#ifndef NDEBUG`, `#if`, `#else`, `#endif`
- `#ifdef` for platform-specific code: different paths for Windows vs Linux
- `#pragma once` — modern alternative to include guards (NOT in K&R-style C, but widely used)
- Predefined macros: `__FILE__`, `__LINE__`, `__DATE__`, `__TIME__` — useful for debugging
- `#error` directive: compile-time assertion

**Bed Reading**: K&R Chapter 7 pages 165–180

### Thursday July 9 — Pre-Gym (5:00–5:25 AM)
**Read**: K.N. King Chapter 20 (Low-Level — volatile and const sections)
- `volatile`: tells compiler "this variable can change without your knowledge" — do NOT optimize it away
  - Example: `volatile uint32_t *STATUS_REG = (uint32_t *)0x40020010;`
  - Without volatile: compiler may cache the value in a register — misses hardware changes
  - With volatile: compiler re-reads from memory every time (critical for hardware registers + ISR variables)
- `const`: tells compiler "do not allow modification"
  - `const int *p` — pointer to const int (can't change `*p`)
  - `int *const p` — const pointer to int (can't change `p` itself, but can change `*p`)
  - `const int *const p` — both pointer and value are const
- `extern`: declares a variable/function defined in another file
  - `extern int g_counter;` in a .h file tells the compiler "this exists somewhere else"
  - `int g_counter = 0;` in one .c file is the actual definition

**Bed Reading**: K&R Chapter 7 pages 180–195

### Friday July 10 — Pre-Gym (5:00–5:25 AM)
**Read**: K.N. King Chapter 22 (Input/Output — pages 1–25)
- `fopen(filename, mode)`: modes "r", "w", "a", "rb", "wb" — what each does
- ALWAYS check: `if (fp == NULL) { perror("fopen"); exit(1); }`
- `fclose(fp)`: MUST be called or data may not be flushed to disk
- `fprintf(fp, ...)`: same as printf but writes to file
- `fscanf(fp, ...)`: same as scanf but reads from file
- `fgets(buf, n, fp)`: safe line reading — reads up to n-1 chars, adds '\0'
- `feof(fp)` vs `ferror(fp)`: checking end-of-file vs errors

**Bed Reading**: K&R Chapter 7 pages 195–210 (File Access, Error Handling)

### Monday July 13 — Pre-Gym (5:00–5:25 AM)
**Read**: K.N. King Chapter 22 (Input/Output — pages 25–end)
- Binary vs text mode: `"rb"` vs `"r"` — on Windows these differ (line endings!)
- `fread(buf, size, count, fp)` and `fwrite(buf, size, count, fp)` — binary I/O
- `fseek(fp, offset, SEEK_SET/SEEK_CUR/SEEK_END)` and `ftell(fp)`: file position
- `rewind(fp)`: reset to beginning of file
- Buffering: why data isn't written immediately, how to force flush with `fflush(fp)`

**Bed Reading**: K&R Chapter 7 — re-read the sections you found hard

---

## SATURDAY JULY 11 — SPECIAL TOPICS CODING (7:30 AM–6:30 PM)

### Warmup (7:30–8:00 AM): FastBit Embedded C Videos
Watch specific sections at 1.5× (search in the Udemy course):
- Section on `volatile` and why it matters in embedded (~10 min)
- Section on `const` with pointers in embedded (~8 min)

### BLOCK 1 (8:00–9:30 AM): Preprocessor + Conditional Compilation
Write ALL from scratch. NO AI code.

```
week5/
├── macros_demo.c       — Function-like macros, debug macros, stringify
├── config.h            — Conditional compilation for debug/release builds
└── platform.c          — Platform-specific code using #ifdef
```

**macros_demo.c** requirements:
```c
// Utility macros:
#define MIN(a, b)          ((a) < (b) ? (a) : (b))
#define MAX(a, b)          ((a) > (b) ? (a) : (b))
#define CLAMP(x, lo, hi)   ((x) < (lo) ? (lo) : (x) > (hi) ? (hi) : (x))
#define ABS(x)             ((x) < 0 ? -(x) : (x))
#define ARRAY_SIZE(arr)    (sizeof(arr) / sizeof((arr)[0]))

// Debug macro (prints file + line + message only in debug mode):
#ifdef DEBUG
#define DBG(fmt, ...) fprintf(stderr, "[%s:%d] " fmt "\n", __FILE__, __LINE__, ##__VA_ARGS__)
#else
#define DBG(fmt, ...) /* nothing — compiled out in release */
#endif

// Test all macros with various values
// Compile twice: once with -DDEBUG (debug mode) and once without
```

**config.h** requirements:
```c
// Hardware configuration that changes between boards
#ifndef CONFIG_H
#define CONFIG_H

#define BOARD_BLACK_PILL   1
#define BOARD_NUCLEO       2

// Set your current board:
#define CURRENT_BOARD      BOARD_BLACK_PILL

// Conditional pin assignments:
#if (CURRENT_BOARD == BOARD_BLACK_PILL)
    #define LED_PIN    13   // PC13 on Black Pill
    #define UART_TX    2    // PA2 (USART2)
    #define CPU_FREQ   84000000UL
#elif (CURRENT_BOARD == BOARD_NUCLEO)
    #define LED_PIN    5    // PA5 on Nucleo
    #define UART_TX    2    // PA2 (USART2)
    #define CPU_FREQ   80000000UL
#else
    #error "Unknown board selected"
#endif

#endif
```

Write a `config_test.c` that `#include "config.h"` and prints the LED_PIN and CPU_FREQ values. Verify it changes when you change CURRENT_BOARD.

### BREAK (9:30–9:45)

### BLOCK 2 (9:45–11:15 AM): volatile + const + extern in Practice
```
week5/
├── volatile_demo.c     — Simulate ISR variable, show why volatile matters
├── const_demo.c        — All 4 const-pointer combinations + const structs
└── extern_demo/        — Multi-file extern variable example
    ├── counter.h        — extern declaration
    ├── counter.c        — actual definition
    └── extern_main.c   — uses the counter
```

**volatile_demo.c** — simulate an interrupt-driven flag:
```c
#include <stdio.h>
#include <signal.h>   // for signal() to simulate an interrupt

volatile int timer_fired = 0;   // volatile because set by "interrupt" (signal handler)

void timer_isr(int sig) {
    timer_fired = 1;            // simulated interrupt: sets flag
    (void)sig;
}

int main(void) {
    signal(SIGALRM, timer_isr); // register signal handler (simulates NVIC in STM32)

    // Simulate a periodic timer firing
    for (int i = 0; i < 5; i++) {
        timer_fired = 0;
        raise(SIGALRM);         // fire the "interrupt"

        if (timer_fired) {
            printf("Timer fired! Processing...\n");
        }
    }
    return 0;
}
```

In comments: explain WHY timer_fired must be volatile. What would happen if it were not volatile? (Compiler might optimize the `if (timer_fired)` check away since it "knows" no code between the check and the assignment modifies it.)

**extern_demo/** — three-file project:
```c
// counter.h
#ifndef COUNTER_H
#define COUNTER_H
extern int g_event_count;  // declaration — tells compiler "this exists somewhere"
void increment_counter(void);
void reset_counter(void);
int  get_count(void);
#endif

// counter.c
#include "counter.h"
int g_event_count = 0;     // definition — actual memory allocation
void increment_counter(void) { g_event_count++; }
void reset_counter(void)     { g_event_count = 0; }
int  get_count(void)         { return g_event_count; }

// extern_main.c — uses counter module
#include <stdio.h>
#include "counter.h"
int main(void) {
    increment_counter();
    increment_counter();
    increment_counter();
    printf("Count: %d\n", get_count());  // Expected: 3
    reset_counter();
    printf("After reset: %d\n", get_count());  // Expected: 0
    return 0;
}
```
Compile: `gcc -Wall -Wextra -g -std=c99 counter.c extern_main.c -o extern_demo`

### BREAK (11:15–11:30)

### BLOCK 3 (11:30 AM–12:30 PM): File I/O Programs
```
week5/
├── file_write.c        — Write data to a text file (names + scores)
├── file_read.c         — Read and process the file written above
└── binary_io.c         — fwrite/fread struct array to binary file
```

**file_write.c** requirements:
- Create `scores.txt` with `fprintf`
- Write format: `name,score\n` for 5 students (hard-coded)
- Print confirmation: "Written 5 records to scores.txt"
- ALWAYS check fopen return. ALWAYS call fclose.

**file_read.c** requirements:
- Open `scores.txt` with `"r"` mode
- Read line by line with `fgets`
- Parse each line: split on comma, extract name and score (use `sscanf`)
- Calculate and print: average score, highest score + student name
- Handle missing file gracefully (if fopen returns NULL, print error + exit)

**binary_io.c** requirements:
```c
typedef struct { char name[20]; int score; } Record;

// Write 5 Record structs to binary file "scores.bin" using fwrite
// Read them back using fread into a new array
// Verify: print both arrays, they should be identical
// Also: use fseek + ftell to get file size (should be 5 * sizeof(Record))
```

### LUNCH (12:30–1:30 PM)

### GERMAN BLOCK 1 (1:30–4:30 PM)
- Nicos Weg Lessons 30–31 (reaching Lesson 30 milestone!)
- Learn modal verbs: können (can), müssen (must), wollen (want to)
- Write 10 sentences: "Ich kann Deutsch lernen. Ich muss arbeiten. Ich will nach Deutschland gehen."
- Anki: add 15 new cards

### GERMAN BLOCK 2 (5:00–6:30 PM)
- Nicos Weg Lessons 32–33
- AnkiDroid: review ALL pending cards
- Write from memory: introduce yourself AND explain what you're studying and why (in German)

---

## SUNDAY JULY 12 — FILE I/O DEEP + ENUM + GIT (7:30 AM–4:00 PM)

### BLOCK 1 (7:30–9:00 AM): Enum + Static
Watch: Neso Academy "Enumeration in C" (~8 min) first.

```
week5/
├── enum_demo.c         — Days of week, traffic light, error codes
└── static_demo.c       — static local variable (persists between calls), static function
```

**enum_demo.c** requirements:
```c
typedef enum { MON=1, TUE, WED, THU, FRI, SAT, SUN } Weekday;
typedef enum { RED, YELLOW, GREEN } TrafficLight;
typedef enum { ERR_NONE=0, ERR_OVERFLOW=-1, ERR_NULL=-2, ERR_RANGE=-3 } ErrorCode;

// Functions to implement:
const char *weekday_name(Weekday d);     // returns "Monday", "Tuesday", etc.
const char *light_name(TrafficLight t);  // returns "RED", "YELLOW", "GREEN"
const char *error_msg(ErrorCode e);      // returns human-readable error message

// Demonstrate: switch/case with enum, compare enum to int,
// print the numeric value of each enum member
```

**static_demo.c** requirements:
```c
// Static local variable — persists between function calls
int call_counter(void) {
    static int count = 0;  // initialized only once, persists
    count++;
    return count;
}

// Static function — visible only in this .c file (like "private")
static void helper_function(void) {
    printf("I'm a private helper\n");
}

// Test: call call_counter() 5 times, print result each time (should be 1,2,3,4,5)
// Show: static local is NOT reset between calls (unlike normal local)
```

### BLOCK 2 (9:15–10:30 AM): Log File System
```
week5/
├── logger.h        — Logger interface: log_init, log_write, log_close, log_levels
└── logger.c        — Implementation using file I/O
```

**logger.h**:
```c
#ifndef LOGGER_H
#define LOGGER_H

typedef enum { LOG_DEBUG, LOG_INFO, LOG_WARNING, LOG_ERROR } LogLevel;

int  log_init(const char *filename);
void log_write(LogLevel level, const char *message);
void log_close(void);

#endif
```

**logger.c** requirements:
- Use a `static FILE *log_fp = NULL;` (module-private file pointer)
- `log_init` opens the file; returns -1 on failure
- `log_write` appends: `[TIMESTAMP][LEVEL] message\n` — use `time()` for timestamp
- `log_close` closes the file
- Test from `logger_main.c` — write 10 log entries at different levels

### GIT PUSH (10:30–11:00 AM)
```bash
cd ~/C-Practice
git add week5/
git commit -m "Week 5: volatile, const, extern, preprocessor macros, file I/O, enum, logger module"
git push origin main
```

Write `week5/README.md` — list every file + one-line description.

### REST + LUNCH (11:00 AM–12:00 PM)

### GERMAN (12:00–2:00 PM)
- Nicos Weg Lessons 34–35
- Anki mega review (aim for 80+ words total)
- Write German from memory: what you learned this week and your study plan

### EXTENDED CODING (2:00–4:00 PM): Config + Logger Integration
Build a `mini_embedded_sim.c` that combines Week 4 and Week 5 skills:
- `#include "config.h"` — uses board config defines
- `#include "logger.h"` — uses your logger module
- `#include "gpio_sim.h"` — uses Week 4 GPIO simulator
- Simulate: configure GPIO, toggle LED 10 times with 500ms delay, log each state change to file
- At the end: print "Simulation complete. See sim_log.txt for details."

Compile: `gcc -Wall -Wextra -g -std=c99 gpio_sim.c logger.c mini_embedded_sim.c -o sim`
Run, then: `cat sim_log.txt` — verify log has 10+ entries.

---

## WEEK 5 CHECKPOINT (Monday July 13, 4:00 PM)

Update PROGRESS.md now. Be honest.

| Checkpoint Item | Done? |
|:---|:---|
| volatile: can explain why it's needed for hardware registers and ISR flags | |
| const: know all 4 pointer-const combinations and when to use each | |
| extern: multi-file project with extern variable compiles and runs | |
| Preprocessor macros: MIN, MAX, CLAMP, DEBUG macro written correctly | |
| Conditional compilation: same code behaves differently with -DDEBUG | |
| File I/O: can write and read text files (fopen, fprintf, fgets, fclose) | |
| Binary file I/O: fwrite/fread struct array to binary file | |
| Logger module: log_init, log_write, log_close — Valgrind clean | |
| enum used correctly in switch/case | |
| static local variable: persists between calls | |
| GitHub: week5 pushed with README | |
| Nicos Weg: Lessons 30–35 done | |
| Anki: 80+ German words total | |

**Self-rating (special C topics 1–10)**: ___ (minimum 6 before Week 6)

---

## WEEKDAY THEORY FOCUS (Week 5)

| Day | Read Before Gym | Bed Read |
|:---|:---|:---|
| Tue Jul 7 | K.N. King Ch 14 pp. 1–20 | K&R Ch 7 pp. 151–165 |
| Wed Jul 8 | K.N. King Ch 14 pp. 20–end | K&R Ch 7 pp. 165–180 |
| Thu Jul 9 | K.N. King Ch 20 (volatile/const) | K&R Ch 7 pp. 180–195 |
| Fri Jul 10 | K.N. King Ch 22 pp. 1–25 | K&R Ch 7 pp. 195–210 |
| Mon Jul 13 | K.N. King Ch 22 pp. 25–end | K&R Ch 7 — re-read hard parts |

> volatile is the most important keyword in embedded C. If you don't understand it yet after reading, ask AI to explain ONLY the concept (no code). Then write the volatile_demo.c yourself.
