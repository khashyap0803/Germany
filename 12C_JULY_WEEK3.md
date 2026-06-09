# JULY WEEK 3 (Jul 14–20) — Phase 1 Week 6: MAKEFILES + GDB + MULTI-FILE PROJECTS

> **Topics**: Makefiles (variables, rules, pattern rules, automatic variables, .PHONY), GDB (breakpoints, step/next, examine memory, watch), multi-file project architecture
> **K.N. King Reading**: Chapter 15 (Writing Large Programs) — header files, compilation, linking
> **K&R Bed Reading**: Chapter 4 (Functions and Program Structure) — compilation units, scope
> **YouTube**: Jacob Sorber "Makefiles" series + "GDB Tutorial" (~3 videos)
> **AI Policy**: BANNED for code — AI may only explain concepts
> **Dates**: Tuesday July 14 → Monday July 20, 2026

---

## WEEKDAY READING SCHEDULE (Jul 14–18)

### Tuesday July 14 — Pre-Gym (5:00–5:25 AM)
**Read**: K.N. King Chapter 15 (Writing Large Programs — pages 1–20)
- Why split into multiple files? Maintainability, reuse, separate compilation
- `.h` files: declarations only (function prototypes, typedefs, macros, struct definitions)
- `.c` files: definitions (actual function bodies, global variable definitions)
- Include guards: `#ifndef FILE_H` — prevents double-inclusion when multiple .c files include the same .h
- The rule: `extern` declarations in .h, actual definitions in .c

**Bed Reading (9:30–10:00 PM)**: K&R Chapter 4 pages 67–83

### Wednesday July 15 — Pre-Gym (5:00–5:25 AM)
**Read**: K.N. King Chapter 15 (pages 20–end)
- Compilation process: `.c` → (preprocessor) → `.i` → (compiler) → `.s` → (assembler) → `.o` → (linker) → executable
- Object files `.o`: what they contain, why they exist
- Linker: resolves external references across `.o` files
- `static` at file scope: limits visibility to current translation unit (like "private" in C)
- Building without a Makefile: `gcc file1.c file2.c file3.c -o program` — why this becomes painful for large projects

**Bed Reading**: K&R Chapter 4 pages 83–88 (Scope Rules, Initialization)

### Thursday July 16 — Pre-Gym (5:00–5:25 AM)
**Read**: GNU Make manual concepts (search: "GNU Make tutorial" — read the first 3 sections online)
- A Makefile is a recipe: `target: dependencies`, then TAB + command
- Variables: `CC = gcc`, `CFLAGS = -Wall -Wextra -g -std=c99`
- Pattern rules: `%.o: %.c` — builds any .o from the corresponding .c
- Automatic variables: `$@` (target name), `$<` (first dependency), `$^` (all dependencies)
- `.PHONY` targets: `clean` is not a file — declare it phony to prevent confusion
- `make` vs `make clean` vs `make all` — what each does

**Bed Reading**: K&R Chapter 4 — re-read compilation units section

### Friday July 17 — Pre-Gym (5:00–5:25 AM)
**Read**: GDB quick reference (search: "GDB cheat sheet" — print or save on phone)
- `gcc -g`: include debug symbols (MUST have this for GDB to show line numbers)
- `gdb ./program`: start GDB
- `break main` or `break filename.c:42`: set breakpoint
- `run [args]`: start program
- `next` (n): execute one line, don't enter functions
- `step` (s): execute one line, enter functions
- `continue` (c): run until next breakpoint
- `print x` (p x): print value of variable x
- `x/4xw 0x...`: examine memory at address (4 words in hex format)
- `backtrace` (bt): show call stack
- `watch x`: break when variable x changes value
- `quit`: exit GDB

**Bed Reading**: K&R Chapter 4 pages 88–102

### Monday July 20 — Pre-Gym (5:00–5:25 AM)
**Read**: Review K.N. King Ch 15 — linker errors section
- "undefined reference" = definition missing (forgot to link the .o or .c)
- "multiple definition" = defined in two places (forgot include guard or defined in .h instead of .c)
- Review the difference: DECLARATION (prototype, no memory) vs DEFINITION (body, allocates memory)

**Bed Reading**: K&R Chapter 4 — re-read header files section

---

## SATURDAY JULY 18 — MAKEFILES + MULTI-FILE PROJECT (7:30 AM–6:30 PM)

### Warmup (7:30–8:00 AM): Jacob Sorber YouTube Videos
Watch these in order (search on YouTube):
- "Makefiles: 95% of what you need to know" by Jacob Sorber (~10 min)
- "Introduction to GDB" — any short tutorial (~12 min)

### BLOCK 1 (8:00–9:30 AM): Write a Complete Makefile from Scratch
Create a 5-file project and write its Makefile manually. NO CMake. NO IDE-generated Makefile.

```
week6/calculator/
├── Makefile
├── main.c
├── math_ops.h + math_ops.c     — add, sub, mul, div_safe, power, factorial
├── string_utils.h + string_utils.c — parse_number, is_valid_input
└── io_utils.h + io_utils.c     — print_menu, read_choice, print_result
```

**Makefile** requirements — write this from scratch:
```makefile
CC      = gcc
CFLAGS  = -Wall -Wextra -g -std=c99
TARGET  = calculator
SRCS    = main.c math_ops.c string_utils.c io_utils.c
OBJS    = $(SRCS:.c=.o)

.PHONY: all clean

all: $(TARGET)

$(TARGET): $(OBJS)
	$(CC) $(CFLAGS) -o $@ $^

%.o: %.c
	$(CC) $(CFLAGS) -c -o $@ $<

clean:
	rm -f $(OBJS) $(TARGET)
```

Every `.h` file needs a proper include guard. Every `.c` file includes only what it needs.

Rules for this project:
- `math_ops.c` should NOT include `io_utils.h` (no I/O in math module)
- `io_utils.c` should NOT include `math_ops.h` (no math in I/O module)
- Only `main.c` knows about all modules

Run: `make` → compiles all 4 .c files → links into `calculator`
Run: `make clean` → removes all .o files and binary
Edit `math_ops.c` → run `make` → only `math_ops.o` and `calculator` recompile (the others don't)

### BREAK (9:30–9:45)

### BLOCK 2 (9:45–11:15 AM): GDB Debugging Session
Debug TWO programs using GDB. NO printf debugging allowed in this block.

**Program 1 — Segfault hunt** (`week6/buggy1.c`):
Write this program with the intentional bugs, then find them using GDB:
```c
#include <stdio.h>
#include <string.h>

void copy_string(char *dest, const char *src) {
    for (int i = 0; i <= strlen(src); i++) {  // BUG: <= should be <
        dest[i] = src[i];
    }
}

int sum_array(int *arr, int n) {
    int sum = 0;
    for (int i = 0; i <= n; i++) {  // BUG: off-by-one reads past array end
        sum += arr[i];
    }
    return sum;
}

int main(void) {
    char buf[5];
    copy_string(buf, "hello");   // writes 6 bytes into 5-byte buffer
    printf("buf = %s\n", buf);
    int nums[] = {1, 2, 3, 4, 5};
    printf("sum = %d\n", sum_array(nums, 5));  // reads nums[5] (out of bounds)
    return 0;
}
```

GDB session to run:
```bash
gcc -Wall -Wextra -g -std=c99 buggy1.c -o buggy1
gdb ./buggy1
(gdb) break main
(gdb) run
(gdb) step           # step into copy_string
(gdb) print i
(gdb) print strlen(src)
(gdb) backtrace      # see call stack when crash happens
```

Document in comments: what GDB showed you, how you found each bug.

**Program 2 — Infinite loop bug hunt** (`week6/buggy2.c`):
```c
#include <stdio.h>

int binary_search(int *arr, int n, int target) {
    int left = 0, right = n;  // BUG: should be n-1
    while (left <= right) {
        int mid = left + (right - left) / 2;
        if (arr[mid] == target) return mid;
        if (arr[mid] < target) left = mid;   // BUG: should be mid+1
        else right = mid;                     // BUG: should be mid-1
    }
    return -1;
}

int main(void) {
    int sorted[] = {2, 5, 8, 12, 16, 23, 38, 56, 72, 91};
    int idx = binary_search(sorted, 10, 23);
    printf("Found 23 at index: %d (expected 5)\n", idx);
    return 0;
}
```

Use GDB watch points to find why it loops forever:
```bash
gdb ./buggy2
(gdb) break binary_search
(gdb) run
(gdb) watch left
(gdb) watch right
(gdb) continue    # watch left/right changing — spot the infinite loop
```

### BREAK (11:15–11:30)

### BLOCK 3 (11:30 AM–12:30 PM): Advanced Makefile — Build Directory
Write a Makefile that puts `.o` files in a `build/` subdirectory:
```makefile
CC       = gcc
CFLAGS   = -Wall -Wextra -g -std=c99
BUILD    = build
SRCS     = $(wildcard *.c)
OBJS     = $(SRCS:%.c=$(BUILD)/%.o)
TARGET   = $(BUILD)/program

.PHONY: all clean debug release

all: $(TARGET)

$(TARGET): $(OBJS) | $(BUILD)
	$(CC) $(CFLAGS) -o $@ $^

$(BUILD)/%.o: %.c | $(BUILD)
	$(CC) $(CFLAGS) -c -o $@ $<

$(BUILD):
	mkdir -p $@

clean:
	rm -rf $(BUILD)

debug: CFLAGS += -DDEBUG -O0
debug: $(TARGET)

release: CFLAGS += -DNDEBUG -O2
release: $(TARGET)
```

### LUNCH (12:30–1:30 PM)

### GERMAN BLOCK 1 (1:30–4:30 PM)
- Nicos Weg Lessons 36–37
- Simple past tense: -te ending for regular verbs
- Write 10 sentences: "Ich lernte gestern C. Ich arbeitete den ganzen Tag."
- Anki: add 15 new cards

### GERMAN BLOCK 2 (5:00–6:30 PM)
- Nicos Weg Lessons 38–39
- AnkiDroid: review ALL pending cards
- Write from memory: describe your week in German using past tense

---

## SUNDAY JULY 19 — GDB MEMORY + INTEGRATION PROJECT + GIT (7:30 AM–4:00 PM)

### BLOCK 1 (7:30–9:00 AM): GDB Memory Examination
```
week6/
└── gdb_memory.c    — Program to inspect memory layout with GDB
```

Write a program with stack + heap allocations, then examine memory in GDB:
```c
#include <stdio.h>
#include <stdlib.h>

int main(void) {
    int stack_arr[5] = {0xAA, 0xBB, 0xCC, 0xDD, 0xEE};
    char stack_str[20] = "Hello, GDB!";
    int *heap_arr = malloc(5 * sizeof(int));
    for (int i = 0; i < 5; i++) heap_arr[i] = i * 100;

    printf("stack_arr at: %p\n", (void *)stack_arr);
    printf("heap_arr at:  %p\n", (void *)heap_arr);
    // SET BREAKPOINT HERE IN GDB

    free(heap_arr);
    return 0;
}
```

GDB commands to practice:
```
x/5dw stack_arr   — examine 5 decimal words at stack_arr
x/20cb stack_str  — examine 20 chars at stack_str
x/5dw heap_arr    — examine heap memory
info locals       — show all local variables
p sizeof(int)     — print expression
```

Note the address range differences: stack addresses are much higher than heap addresses.

### BLOCK 2 (9:15–10:30 AM): Integration Project
Combine Weeks 4, 5, 6 into one properly organized project:
```
week6/embedded_project/
├── Makefile
├── config.h          — board configuration (from Week 5)
├── bit_macros.h      — bit manipulation macros (from Week 4)
├── gpio_sim.h/.c     — GPIO module (from Week 4)
├── logger.h/.c       — Logger module (from Week 5)
├── timer_sim.h/.c    — NEW: timer simulation
└── main.c
```

**timer_sim.h** (new — write from scratch):
```c
#ifndef TIMER_SIM_H
#define TIMER_SIM_H
#include <time.h>

typedef struct { clock_t start; unsigned long ticks; } Timer;

void          timer_init(Timer *t);
void          timer_tick(Timer *t);
unsigned long timer_get_ticks(const Timer *t);
double        timer_elapsed_ms(const Timer *t);

#endif
```

The full project must: compile with `make`, run clean under Valgrind, write log to file.

### GIT PUSH (10:30–11:00 AM)
```bash
cd ~/C-Practice
git add week6/
git commit -m "Week 6: Makefiles, GDB debugging (found 5 bugs), multi-file project with timer/GPIO/logger"
git push origin main
```

Write `week6/README.md` — list files, GDB commands used, bugs found.

### REST + LUNCH (11:00 AM–12:00 PM)

### GERMAN (12:00–2:00 PM)
- Nicos Weg Lesson 40 (milestone — two-thirds of A1 complete)
- Anki mega review (aim for 90+ words total)
- Write German from memory: what you built this week

### EXTENDED CODING (2:00–4:00 PM): From Memory Challenge
Without looking at previous code:
1. Write a Makefile for a 3-file project from scratch (10 min max)
2. Find a bug using only GDB, no printf (15 min max)
3. Write `bit_macros.h` with all 4 macros from memory (5 min max)

---

## WEEK 6 CHECKPOINT (Monday July 20, 4:00 PM)

Update PROGRESS.md now. Be honest.

| Checkpoint Item | Done? |
|:---|:---|
| Can write a complete Makefile for a 3-file project from memory | |
| Pattern rule %.o: %.c with $@, $<, $^ | |
| make clean removes .o files and binary | |
| GDB: set breakpoint, step through code, print variables | |
| GDB: found a bug using only GDB (no printf debugging) | |
| GDB: x/ command to examine raw memory | |
| Multi-file project: clean .h/.c separation, include guards | |
| "Undefined reference" error: know what causes it | |
| static at file scope: "private" to module | |
| GitHub: week6 pushed with README | |
| Nicos Weg: Lessons 36–40 done | |
| Anki: 90+ German words total | |

**Self-rating (Makefiles + GDB 1–10)**: ___ (minimum 6 before Week 7)

---

## WEEKDAY THEORY FOCUS (Week 6)

| Day | Read Before Gym | Bed Read |
|:---|:---|:---|
| Tue Jul 14 | K.N. King Ch 15 pp. 1–20 | K&R Ch 4 pp. 67–83 |
| Wed Jul 15 | K.N. King Ch 15 pp. 20–end | K&R Ch 4 pp. 83–88 |
| Thu Jul 16 | GNU Make tutorial (online, first 3 sections) | K&R Ch 4 pp. 88–102 |
| Fri Jul 17 | GDB cheat sheet — memorize commands | K&R Ch 4 — re-read |
| Mon Jul 20 | K.N. King Ch 15 — linker errors section | K&R Ch 4 — header files |

> A bug you find with GDB in 5 minutes would take 30 minutes to find with printf.
> Learn GDB this week. Use it every week after this for the rest of Phase 1.
