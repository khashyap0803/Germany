# 📅 WEEK 1 — Jun 1-7 (Mon-Sun): MAKEFILES + GDB + MULTI-FILE PROJECTS

> **Topics**: Compilation pipeline, gcc flags, Makefiles, multi-file C projects, header files, include guards, GDB debugging
> **K.N. King Chapters**: Ch 15 (Writing Large Programs), Ch 14 revisit (Preprocessor deep)
> **K&R Bed Reading**: Chapter 4 (Functions & Program Structure) — finish it
> **FastBit Udemy**: Sections on compilation, preprocessor, multi-file projects
> **Programs to write**: 6-8
> **German**: Nicos Weg Lessons 26-30, past tense intro (Perfekt with haben/sein)
> **📚 Full resource details**: See `10_RESOURCES.md`

---

## 📺 PRE-WEEK HOMEWORK (Watch on May 31st evening)

1. **Jacob Sorber: "How do Makefiles work?"** (~12 min)
   - Search YouTube: `Jacob Sorber Makefile`
   - Gives you the big picture before diving in Monday

2. **Skim K.N. King Ch 15** — Table of Contents and first 3 pages. See what "large programs" means.

---

## DAY 1 — Monday, Jun 1

### 🔶 Morning Block (5:10 - 6:30 AM) — COMPILATION PIPELINE

---

#### 📺 WATCH FIRST (15 min) — 5:10 to 5:25 AM

**FastBit Udemy**: Section on compilation process (or remaining sections not covered in May)

**Supplement**: Neso Academy: "Compilation Process in C" (~8 min)

---

#### 💻 CODE (45 min) — 5:25 to 6:10 AM

**Exercise 1 — See the pipeline (5:25-5:40):**
```bash
cd /mnt/f/Documents/DEVELOP/C-Practice
mkdir week6 && cd week6
```

Create `pipeline_demo.c`:
```c
#include <stdio.h>
#define MAX_SIZE 100

int main(void) {
    int arr[MAX_SIZE];
    printf("Array size: %d\n", MAX_SIZE);
    printf("sizeof(int): %zu\n", sizeof(int));
    return 0;
}
```

Now run EACH stage separately:
```bash
# Stage 1: Preprocessing — see #include expanded, #define replaced
gcc -E pipeline_demo.c -o pipeline_demo.i
wc -l pipeline_demo.i    # Thousands of lines! stdio.h is huge.
head -50 pipeline_demo.i  # See the expanded output

# Stage 2: Compilation — C to Assembly
gcc -S pipeline_demo.c -o pipeline_demo.s
cat pipeline_demo.s       # Read the assembly. Find your printf call.

# Stage 3: Assembly — Assembly to Object file
gcc -c pipeline_demo.c -o pipeline_demo.o
file pipeline_demo.o       # "ELF 64-bit LSB relocatable"

# Stage 4: Linking — Object file to Executable
gcc pipeline_demo.o -o pipeline_demo
./pipeline_demo
```

**What to understand**: C source → preprocessed → assembly → object → executable. On STM32, the linker script controls WHERE each section goes in flash/RAM.

**Exercise 2 — GCC warning flags (5:40-5:55):**

Create `warnings_demo.c` with intentional issues:
```c
#include <stdio.h>

int main() {       // Note: no 'void' — this is a warning
    int x;         // Uninitialized
    printf("%d\n", x);  // Using uninitialized variable
    
    int y = 3.14;  // Implicit truncation
    printf("%d\n", y);
    
    return 0;
}
```

Compile with different flag levels:
```bash
gcc warnings_demo.c -o warnings_demo              # No warnings shown!
gcc -Wall warnings_demo.c -o warnings_demo         # Some warnings
gcc -Wall -Wextra warnings_demo.c -o warnings_demo # More warnings
gcc -Wall -Wextra -Werror warnings_demo.c          # Warnings = errors!
gcc -Wall -Wextra -Werror -pedantic -std=c99 warnings_demo.c  # STRICTEST
```

**Rule for June**: Always compile with `-Wall -Wextra -g` minimum. From now on, ZERO warnings allowed.

**Exercise 3 — Optimization flags (5:55-6:10):**

Create `optimize_demo.c`:
```c
#include <stdio.h>

int main(void) {
    volatile int sum = 0;  // volatile prevents optimization
    for (int i = 0; i < 1000000; i++) {
        sum += i;
    }
    printf("Sum: %d\n", sum);
    return 0;
}
```

```bash
gcc -O0 optimize_demo.c -o opt0 && time ./opt0   # No optimization
gcc -O2 optimize_demo.c -o opt2 && time ./opt2   # Fast optimization
gcc -Os optimize_demo.c -o opts && time ./opts   # Size optimization (embedded!)

ls -la opt0 opt2 opts  # Compare binary sizes
```

**What to understand**: `-Os` is what STM32 projects use — smallest binary to fit in flash memory.

---

#### 📖 READ (6:10 - 6:30 AM)

- Open **K.N. King Chapter 15**: "Writing Large Programs" — read sections 15.1-15.2 (Source files, Header files)
- Key concepts: `#include "file.h"` vs `#include <file.h>`, include guards, extern declarations

---

#### 🧪 TEST YOURSELF

- Can you explain what happens at each compilation stage?
- Why does `-Wall` catch bugs that default gcc doesn't?
- What's the difference between `-O2` and `-Os`? Which one for embedded?

---

### 🎧 Commute IN (7:00-8:30 AM) — German
- **Nicos Weg Lesson 26**: New topic. Listen carefully, repeat phrases.
- Review Anki cards from May (cumulative review)

### 📱 Lunch (12:30-12:45 PM) — German Anki
- 5 new cards + review old ones. You should have 100+ cards by now.

### 🎧 Commute BACK — German
- Re-listen Nicos Weg lessons 25-26 for reinforcement
- Practice in your head: past tense sentences

### 📖 Bed (9:30-10:00 PM) — K&R Reading
- **K&R Chapter 4** — "Functions and Program Structure" (pp. 65-91)
- Focus on: external variables, scope rules, header files, static

### ✅ Day 1 Checklist
- [ ] Ran all 4 compilation stages separately (preprocess, compile, assemble, link)
- [ ] Compiled with `-Wall -Wextra -Werror` — understand what each flag does
- [ ] Compared `-O0` vs `-O2` vs `-Os` binary sizes
- [ ] Read K.N. King Ch 15, sections 15.1-15.2
- [ ] Nicos Weg Lesson 26 completed

---

## DAY 2 — Tuesday, Jun 2

### 🔶 Morning Block (5:10 - 6:30 AM) — MULTI-FILE PROJECT BASICS

#### 💻 CODE (1h 20m)

**Build your first multi-file project:**

Create the following file structure:
```
week6/calculator/
├── main.c
├── math_ops.c
├── math_ops.h
├── string_ops.c
├── string_ops.h
└── utils.h
```

**`utils.h`** — common definitions:
```c
#ifndef UTILS_H
#define UTILS_H

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_INPUT 256
#define VERSION "1.0"

#endif
```

**`math_ops.h`** — function declarations:
```c
#ifndef MATH_OPS_H
#define MATH_OPS_H

int add(int a, int b);
int subtract(int a, int b);
int multiply(int a, int b);
double divide(int a, int b);
int factorial(int n);
int fibonacci(int n);
int is_prime(int n);

#endif
```

**`math_ops.c`** — implement ALL functions yourself. Do NOT copy from May. Write from memory.

**`string_ops.h`**:
```c
#ifndef STRING_OPS_H
#define STRING_OPS_H

int my_strlen(const char *s);
void my_strcpy(char *dest, const char *src);
void my_strrev(char *s);
int is_palindrome(const char *s);

#endif
```

**`string_ops.c`** — implement ALL functions from scratch.

**`main.c`** — menu-driven program that lets user choose math or string operations.

Compile manually first:
```bash
gcc -Wall -Wextra -g -c main.c
gcc -Wall -Wextra -g -c math_ops.c
gcc -Wall -Wextra -g -c string_ops.c
gcc main.o math_ops.o string_ops.o -o calculator
./calculator
```

**What to understand**: Each `.c` file compiles independently into a `.o` file. The linker combines them. Header files tell each `.c` file what functions exist elsewhere.

### 📖 READ (remaining time)
- **K.N. King Ch 15** — sections 15.3-15.4 (Splitting a program, Building a multi-file program)

### ✅ Day 2 Checklist
- [ ] Created multi-file project with 3 .c files and 3 .h files
- [ ] All include guards working (`#ifndef`)
- [ ] Compiled each file separately with `gcc -c`
- [ ] Linked manually and program runs
- [ ] Can explain: why separate compilation? Why header files?

---

## DAY 3 — Wednesday, Jun 3

### 🔶 Morning Block (5:10 - 6:30 AM) — MAKEFILES FROM SCRATCH

#### 💻 CODE (1h 20m)

**Write a Makefile for yesterday's calculator project:**

Create `Makefile` (note: MUST use TABS, not spaces for indentation):
```makefile
CC = gcc
CFLAGS = -Wall -Wextra -g -std=c99

# Target: all object files linked together
calculator: main.o math_ops.o string_ops.o
	$(CC) $(CFLAGS) main.o math_ops.o string_ops.o -o calculator

# Each .c file compiles to .o
main.o: main.c math_ops.h string_ops.h utils.h
	$(CC) $(CFLAGS) -c main.c

math_ops.o: math_ops.c math_ops.h
	$(CC) $(CFLAGS) -c math_ops.c

string_ops.o: string_ops.c string_ops.h
	$(CC) $(CFLAGS) -c string_ops.c

# Clean up
clean:
	rm -f *.o calculator

# Phony targets
.PHONY: clean
```

Test it:
```bash
make              # Builds everything
./calculator      # Run
make clean        # Removes .o and executable
make              # Rebuilds

# Now modify ONLY math_ops.c and run make again
# Notice: only math_ops.c recompiles! Not everything. THIS is why Makefiles exist.
```

**Exercise 2 — Pattern rules:**

Upgrade your Makefile with automatic pattern rules:
```makefile
CC = gcc
CFLAGS = -Wall -Wextra -g -std=c99
SRCS = main.c math_ops.c string_ops.c
OBJS = $(SRCS:.c=.o)
TARGET = calculator

$(TARGET): $(OBJS)
	$(CC) $(CFLAGS) $(OBJS) -o $(TARGET)

%.o: %.c
	$(CC) $(CFLAGS) -c $< -o $@

clean:
	rm -f $(OBJS) $(TARGET)

.PHONY: clean
```

**What to understand**: `$<` = first prerequisite (the .c file), `$@` = target (the .o file). This pattern scales to 50+ files.

### 🇩🇪 German Morning (if Wed is German day)
- If following the alternating schedule from May, do Nicos Weg Lesson 27 in the morning instead
- Move Makefile practice to the evening slot

### ✅ Day 3 Checklist
- [ ] Wrote a Makefile from scratch (not copied!)
- [ ] `make` builds correctly, `make clean` cleans up
- [ ] Modified one .c file → only that file recompiled (incremental build)
- [ ] Upgraded to pattern rules with `%.o: %.c`
- [ ] Can explain: `$<`, `$@`, `.PHONY`, tab vs space rule

---

## DAY 4 — Thursday, Jun 4

### 🔶 Morning Block (5:10 - 6:30 AM) — GDB DEBUGGING (Part 1)

#### 💻 CODE (1h 20m)

**Exercise 1 — GDB basics with your calculator:**
```bash
# Compile with debug info
make clean && make  # Your Makefile already has -g flag

# Start GDB
gdb ./calculator
```

GDB session:
```
(gdb) break main            # Breakpoint at start
(gdb) run                   # Start execution
(gdb) next                  # Step over (don't enter functions)
(gdb) step                  # Step into function
(gdb) print variable_name   # Print any variable
(gdb) print *pointer        # Print what pointer points to
(gdb) print &variable       # Print address
(gdb) backtrace             # Show call stack
(gdb) continue              # Run until next breakpoint
(gdb) quit                  # Exit
```

**Exercise 2 — Create a buggy program on purpose:**

Create `buggy.c`:
```c
#include <stdio.h>
#include <stdlib.h>

int main(void) {
    int *arr = malloc(5 * sizeof(int));
    
    // Bug 1: Using uninitialized memory
    printf("arr[0] = %d\n", arr[0]);
    
    // Bug 2: Off-by-one
    for (int i = 0; i <= 5; i++) {  // Should be < 5
        arr[i] = i * 10;
    }
    
    // Bug 3: Use after free
    free(arr);
    printf("After free: arr[0] = %d\n", arr[0]);
    
    // Bug 4: Double free
    free(arr);
    
    return 0;
}
```

Debug with GDB + Valgrind:
```bash
gcc -Wall -Wextra -g buggy.c -o buggy
gdb ./buggy          # Step through, watch the bugs happen
valgrind ./buggy     # Memory error detection (install: sudo apt install valgrind)
```

**What to understand**: GDB shows you WHERE the bug is. Valgrind shows you WHAT the memory error is. Together, they replace 90% of printf debugging.

### ✅ Day 4 Checklist
- [ ] Debugged calculator with GDB — set breakpoints, stepped through
- [ ] Found all 4 bugs in `buggy.c` using GDB
- [ ] Ran Valgrind and understood its output
- [ ] Can explain: breakpoint, backtrace, step vs next, watchpoint

---

## DAY 5 — Friday, Jun 5

### 🔶 Morning Block (5:10 - 6:30 AM) — GDB DEBUGGING (Part 2)

#### 💻 CODE (1h 20m)

**Exercise 1 — Watchpoints and conditional breakpoints:**

Create `watchpoint_demo.c`:
```c
#include <stdio.h>

int main(void) {
    int counter = 0;
    
    for (int i = 0; i < 100; i++) {
        counter += i;
        if (i == 50) {
            counter = -999;  // Mysterious corruption!
        }
    }
    
    printf("Final counter: %d\n", counter);
    return 0;
}
```

GDB session — find where counter gets corrupted:
```
(gdb) break main
(gdb) run
(gdb) watch counter           # Break whenever counter changes
(gdb) continue                # Runs until counter changes
(gdb) print counter           # What's the value now?
(gdb) continue                # Keep going...

# Alternative: conditional breakpoint
(gdb) break 8 if i == 49      # Break at line 8 when i is 49
(gdb) run
(gdb) next                    # Step to see corruption happen
```

**Exercise 2 — Debug a real segfault:**

Create `segfault.c`:
```c
#include <stdio.h>

void recursive_bomb(int n) {
    int big_array[10000];  // 40KB on stack each call
    big_array[0] = n;
    printf("Depth: %d, array[0]=%d\n", n, big_array[0]);
    recursive_bomb(n + 1);  // Never stops → stack overflow
}

int main(void) {
    recursive_bomb(1);
    return 0;
}
```

```bash
gcc -Wall -Wextra -g segfault.c -o segfault
./segfault             # Segfault!
gdb ./segfault
(gdb) run              # It crashes
(gdb) backtrace        # See the MASSIVE call stack — that's your stack overflow
(gdb) frame 0          # Look at the deepest frame
(gdb) print n          # How deep did it go?
```

**What to understand**: Stack overflow = recursion too deep + large local variables. On STM32, stack is only 1-4KB. This bug WILL happen in embedded.

### 🇩🇪 German (if Friday is mixed day)
- Nicos Weg Lesson 28-29

### ✅ Day 5 Checklist
- [ ] Used GDB watchpoints to find corruption
- [ ] Used conditional breakpoints (`break 8 if i == 49`)
- [ ] Debugged a stack overflow — understood backtrace output
- [ ] Can explain: watchpoint, conditional breakpoint, stack overflow

---

## DAY 6 — Saturday, Jun 6 (DEEP STUDY DAY)

### 💻 C Deep Sessions (6:30 AM - 12:45 PM, ~6 hrs)

**Session 1 (6:30-7:30): Refactor May programs into multi-file project**

Take your best 5 programs from May and reorganize:
```
week6/may_refactored/
├── main.c
├── sorting.c / sorting.h       (bubble sort, selection sort)
├── searching.c / searching.h   (linear search, binary search)
├── strings.c / strings.h       (your custom string functions)
├── utils.c / utils.h           (helper functions)
└── Makefile
```

**Session 2 (7:45-9:15): Add GDB debugging practice**

Introduce 5 intentional bugs into your refactored project. Then fix each one using only GDB (NO printf, NO AI).

Bugs to plant:
1. Off-by-one in a loop
2. Wrong pointer arithmetic
3. Missing null terminator in string
4. Uninitialized variable
5. Memory leak (malloc without free)

**Session 3 (9:30-11:00): K.N. King Ch 15 exercises**

Do exercises from Chapter 15. Focus on:
- Exercise 15.1 (splitting a program)
- Exercise 15.2 (header file design)
- Write your own multi-file project from the exercises

**Session 4 (11:15-12:45): Interview prep — Build system questions**

Write answers (in a `.md` file, push to GitHub) for:
1. "Explain the C compilation pipeline (4 stages)"
2. "What is the difference between a header file and a source file?"
3. "What is an include guard and why is it needed?"
4. "What does `extern` do?"
5. "What is the difference between `static` in a function vs at file scope?"
6. "Explain what a Makefile does and why it's better than a build script"

### 🇩🇪 German (2:00-5:00 PM)
- Nicos Weg Lesson 29-30
- Practice past tense: "Ich habe gegessen. Ich bin gegangen."
- Google AI voice: "Quiz me on German A1 vocabulary and correct my pronunciation"

### ✅ Day 6 Checklist
- [ ] Refactored May programs into multi-file project with Makefile
- [ ] Found and fixed 5 planted bugs using only GDB
- [ ] K.N. King Ch 15 exercises completed
- [ ] 6 interview answers written in markdown
- [ ] German past tense practice

---

## DAY 7 — Sunday, Jun 7 (REVIEW + GIT)

### 💻 Morning (7:30 AM - 12:30 PM)

**7:30-9:00**: Solve 3 HackerRank C problems (medium difficulty)
**9:15-10:45**: Write a "Build System README" explaining your Makefile to someone who's never seen one
**11:00-12:30**: Git push ALL week 6 code. Clean up files. Write READMEs for each folder.

```bash
cd /mnt/f/Documents/DEVELOP/C-Practice
git add -A
git commit -m "Week 6: Makefiles, GDB, multi-file projects, compilation pipeline"
git push
```

### 🇩🇪 German (2:00-4:00 PM)
- Review all Nicos Weg A1 lessons so far (1-30)
- Anki mega review — aim for 120+ cards total
- Write 5 sentences in past tense

### 📋 Weekly Review (4:00-4:30 PM)
- How many programs written this week?
- Can you write a Makefile from memory?
- Can you use GDB without looking at a cheat sheet?
- What's your weakest area? Plan extra time next week.

### ✅ Day 7 Checklist
- [ ] 3 HackerRank problems solved
- [ ] Build System README written
- [ ] All code pushed to GitHub
- [ ] Nicos Weg A1 review (lessons 1-30)
- [ ] Weekly review completed

---

## 📋 WEEK 1 CHECKPOINT

- [ ] ✅ Understand full compilation pipeline (preprocess → compile → assemble → link)
- [ ] ✅ Can write Makefiles from scratch (with variables, pattern rules, clean target)
- [ ] ✅ Multi-file C project working (3+ .c files, proper .h files, include guards)
- [ ] ✅ Can debug with GDB: breakpoints, step, print, backtrace, watchpoints
- [ ] ✅ Valgrind installed and used for memory checking
- [ ] ✅ All code pushed to GitHub with READMEs
- [ ] ✅ Nicos Weg lessons 26-30 completed
- [ ] ✅ 120+ German words in Anki
