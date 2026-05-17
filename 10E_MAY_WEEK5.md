# 📅 WEEK 5 — May 26-31 (Tue-Sun): SPECIAL TOPICS + MONTH REVIEW

> **Topics**: enum, volatile, const, static, extern, file I/O, preprocessor, Makefile, month test
> **K.N. King Chapters**: Ch 22 (Input/Output), Ch 14 revisit (Preprocessor), review all chapters
> **K&R Bed Reading**: Chapter 4 (finish — Preprocessor), Chapter 7 (Input/Output)
> **FastBit Udemy**: Remaining sections + review
> **Programs to write**: 6-8
> **German**: Nicos Weg Lessons 21-25, review all vocabulary, first attempt at writing a paragraph
> **Goal**: Finish May with solid C fundamentals ready for STM32 in July
> **📚 Full resource details**: See `10_RESOURCES.md`

---

## DAY 26 — Tuesday, May 26

### 🔶 Morning (5:10-6:30 AM) — Enums + State Machines

---

#### 📺 WATCH FIRST (20 min) — 5:10 to 5:30 AM

1. **Neso Academy: "Enumeration in C"** (~8 min)
   - Focus on: `enum` gives names to numbers. Much cleaner than `#define STATE_IDLE 0`
2. **Jacob Sorber: "State Machines in C"** (~15 min)
   - Focus on: The `switch(current_state)` pattern inside a `while(1)` loop. This is the heart of ALL embedded firmware.

> **Deeper understanding**: Search YouTube: "State Machine Design Pattern in C" — any video under 15 min that shows a practical example

---

#### 📖 READ (5 min)

- **K&R section on enumerations** (pp. 39-40). Short section — only 2 pages.

---

#### 💻 CODE (45 min) — 5:30 to 6:15 AM

**Program 1 — `enum_states.c`:**
```c
typedef enum { STATE_IDLE, STATE_RUNNING, STATE_ERROR, STATE_DONE } State;
```
- These become 0, 1, 2, 3 automatically
- Write a state machine using `switch(current_state)` in a `while(1)` loop
- Simulate: **Traffic light controller** — RED → GREEN → YELLOW → RED
- Each state prints what's happening, waits (use `sleep(1)` from `<unistd.h>` on Linux), transitions to next state

**Why state machines are EVERYTHING in embedded**:
- Washing machine? State machine (fill → wash → rinse → spin → done)
- UART driver? State machine (idle → receiving → processing → sending)
- Your STM32 LED blink? State machine (on → wait → off → wait)
- FreeRTOS task states? State machine (ready → running → blocked → suspended)

---

#### 🧪 TEST YOURSELF

- Modify your traffic light to handle a "pedestrian button press" (new state transition)
- **Exercism**: `resistor-color-duo` → https://exercism.org/tracks/c/exercises/resistor-color-duo (uses enums)

---

### 🎧 Commute: Nicos Weg Lesson 21 | 📱 Lunch: Anki | 📖 Bed: K&R Chapter 4 preprocessor section (pp. 86-92)

### ✅ Day 26: `enum_states.c` — traffic light state machine working.

---

## DAY 27 — Wednesday, May 27

### 🔶 Morning (5:10-6:30 AM) — 🇩🇪 German + volatile, const, static

---

#### 📺 GERMAN (15 min) — 5:10 to 5:25 AM

- **DW Nicos Weg app**: Lesson 22
- **Learn German with Anja** (YouTube): Search "German Accusative Case for Beginners" (~12 min)
  - Key: der → den (masculine accusative only changes!), die stays die, das stays das
  - Practice: "Ich habe **den** Computer." "Ich trinke **den** Kaffee."

---

#### 📺 WATCH (20 min) — 5:25 to 5:45 AM

1. **Jacob Sorber: "The volatile keyword in C"** (~10 min)
   - Focus on: `volatile` tells the compiler "this variable can change WITHOUT your code changing it" (hardware registers, ISR variables). Compiler must NOT optimize it away.
2. **Jacob Sorber: "const in C — what does it really mean?"** (~8 min)
   - Focus on: `const int *p` (pointer to const int — can't change value) vs `int * const p` (const pointer — can't change where it points)
3. **Neso Academy: "Storage Classes in C — static, extern"** (~12 min)
   - Focus on: `static` in 3 contexts, `extern` for cross-file variables

---

#### 📖 READ

- **Beej's Guide** → "The C Preprocessor" → https://beej.us/guide/bgc/html/split/the-c-preprocessor.html (more beginner-friendly than K&R for this topic)

---

#### 💻 CODE (35 min) — 5:45 to 6:20 AM

**Program 2 — `volatile_const.c`:**
```c
volatile int sensor_value = 0;  // Might change from hardware/ISR
const int MAX_SENSORS = 10;     // Read-only constant

// const pointer vs pointer to const:
int x = 5, y = 10;
const int *p1 = &x;    // Can change where p1 points, but NOT *p1
int * const p2 = &x;   // Can change *p2, but NOT where p2 points
const int * const p3 = &x;  // Can change NOTHING
```
- Demonstrate what happens when you try to modify a `const` — compiler error!
- Simulate `volatile`: In embedded, `volatile` is used for:
  - Hardware registers that change by themselves (ADC result, timer counter)
  - Variables modified inside an ISR (interrupt service routine)

**Why these matter for embedded interviews**:
> "What is volatile and when do you use it?" — The #1 most-asked embedded C interview question. If you can't answer it, you fail the interview.

---

#### 🧪 TEST YOURSELF

- **Ask Google AI**: "Give me 5 interview questions about volatile, const, and static in C. Quiz me and I'll answer."
- Write the answers in a file: `keyword_interview_answers.c`

---

### 📖 Bed: K&R pp. 86-92 (preprocessor: #define, #include, conditional compilation)

### ✅ Day 27: `volatile_const.c` + `keyword_interview_answers.c`. German accusative case started.

---

## DAY 28 — Thursday, May 28

### 🔶 Morning (5:10-6:30 AM) — File I/O

---

#### 📺 WATCH FIRST (20 min) — 5:10 to 5:30 AM

1. **Neso Academy: "File Handling in C (Part 1)"** (~10 min)
   - Focus on: `fopen()`, `fclose()`, file modes ("r", "w", "a")
2. **Neso Academy: "File Handling in C (Part 2)"** (~10 min)
   - Focus on: `fprintf()`, `fscanf()`, `fgets()`, `fread()`, `fwrite()`
3. **Neso Academy: "File Handling in C (Part 3)"** (~8 min) — if time permits
   - Focus on: `fseek()`, `ftell()`, binary vs text mode

---

#### 📖 READ

- **K&R Chapter 7** (Input and Output) — pp. 151-168
- Or: **Beej's Guide** → "File I/O" → https://beej.us/guide/bgc/html/split/file-input-output.html

---

#### 💻 CODE (40 min) — 5:30 to 6:10 AM

**Program 3 — `file_io.c`:**
- Open a file for writing: `FILE *fp = fopen("data.txt", "w");`
- **ALWAYS check if fopen returned NULL** (file might not exist or no permission)
- Write 10 sensor readings using `fprintf(fp, "%d, %.2f\n", id, value);` — CSV format
- Close the file: `fclose(fp);`
- Re-open for reading: `fp = fopen("data.txt", "r");`
- Read back with `fscanf()` and print to console
- Calculate min, max, average from the file data

**Program 4 — `logger.c`:**
- A simple data logger:
  - Ask user for sensor readings (temperature values)
  - Append each reading to a file with timestamp: `fprintf(fp, "%d, %.1f\n", count, temp);`
  - File mode "a" (append) — doesn't overwrite existing data
  - At the end, read the file and print statistics

---

#### 🧪 TEST YOURSELF

- **HackerRank**: search for "File" challenges in C domain
- **Exercism**: `phone-number` → https://exercism.org/tracks/c/exercises/phone-number

---

### 🎧 Commute: Nicos Weg Lesson 23 | 📖 Bed: K&R chapter 7 continued

### ✅ Day 28: `file_io.c` + `logger.c`. Can read/write CSV files.

---

## DAY 29 — Friday, May 29

### 🔶 Morning (5:10-6:30 AM) — 🇩🇪 German + Preprocessor

---

#### 📺 GERMAN (15 min) — 5:10 to 5:25 AM

- **DW Nicos Weg app**: Lesson 24
- Practice accusative: write 10 sentences using "Ich habe..." "Ich sehe..." "Ich brauche..."

---

#### 📺 WATCH (15 min) — 5:25 to 5:40 AM

- **Jacob Sorber: "The C Preprocessor — #define, #ifdef, #include"** (~12 min)
  - Focus on: `#define` macros, `#include` guards, conditional compilation `#ifdef`/`#ifndef`
- **Neso Academy: "Macros in C"** (~8 min)
  - Focus on: Function-like macros (`#define MAX(a,b)`) — advantages (no function call overhead) and pitfalls (double evaluation)

---

#### 📖 READ — K&R pp. 86-92 (Preprocessor section in Chapter 4)

---

#### 💻 CODE (40 min) — 5:40 to 6:20 AM

**Program 5 — `preprocessor.c`:**
```c
#define PI 3.14159
#define MAX(a, b) ((a) > (b) ? (a) : (b))
#define ARRAY_SIZE(arr) (sizeof(arr) / sizeof(arr[0]))

#ifdef DEBUG
    #define LOG(msg) printf("[DEBUG] %s\n", msg)
#else
    #define LOG(msg)  // Does nothing in release
#endif
```
- Compile with: `gcc preprocessor.c -o prog -DDEBUG` → debug prints appear
- Compile without: `gcc preprocessor.c -o prog` → debug prints disappear
- **This is EXACTLY how embedded firmware switches between debug and release builds.**
- Demonstrate the `MAX(a++, b++)` pitfall — double evaluation!

**Program 6 — `include_guard.c`:**
- Create a header file with proper include guards:
```c
// my_header.h
#ifndef MY_HEADER_H
#define MY_HEADER_H

// declarations here
void my_function(void);

#endif // MY_HEADER_H
```
- Include it twice in main.c — show that without guards, you get "redefinition" errors
- **Every single `.h` file in STM32 projects uses include guards.**

---

#### 🧪 TEST YOURSELF

- Compile with `-E` flag: `gcc -E preprocessor.c` — see what the preprocessor produces (expanded macros, included headers). This is eye-opening!

---

### 📖 Bed: Start thinking about what you'll review this weekend for the month test

### ✅ Day 29: `preprocessor.c` + `include_guard.c`. Understand conditional compilation.

---

## DAY 30 — Saturday, May 30 🟩 DATA LOGGER SIMULATOR + MAKEFILE

### 💻 Warmup (6:30-7:30 AM) — Makefile Deep

---

#### 📺 WATCH FIRST (15 min) — 6:30 to 6:45 AM

- **Jacob Sorber: "How to Write a Makefile"** (~12 min)
  - Focus on: targets, prerequisites, recipes, variables, pattern rules
- Or: **CodeVault: "Makefiles in C"** (~15 min) — more practical example

---

#### 📖 READ

- **Beej's Guide to C** → Appendix on Makefiles (if available)
- Or: **Programiz**: "C Makefile Tutorial" (Google it — clean tutorial)

---

#### 💻 CODE (45 min) — 6:45 to 7:30 AM

Write a **proper Makefile** for your multi-file project from Week 2:
```makefile
CC = gcc
CFLAGS = -Wall -Wextra -g
SOURCES = main.c math_utils.c
HEADERS = math_utils.h
TARGET = main

$(TARGET): $(SOURCES) $(HEADERS)
	$(CC) $(CFLAGS) $(SOURCES) -o $(TARGET)

clean:
	rm -f $(TARGET) *.o

.PHONY: clean
```
- Understand each line. What is `$(CC)`? What is `.PHONY`?
- Add a `debug` target that compiles with `-DDEBUG`
- **Makefile is how ALL professional embedded projects are built.** Even when you use STM32CubeIDE, there's a Makefile underneath.

---

### 💻 Deep Session 1 (7:45-9:15 AM) — Data Logger Simulator Project 🏆

---

#### 💻 CODE (90 min)

**Program 7 — `data_logger_simulator/`** (multi-file project):

This combines EVERYTHING from May into one program:

**File structure:**
```
data_logger_simulator/
├── main.c              — Main loop with state machine menu
├── sensor.h / sensor.c — Sensor data generation (random values)
├── logger.h / logger.c — File I/O: write readings to CSV
├── stats.h / stats.c   — Statistics: min, max, avg from data
├── buffer.h / buffer.c — Circular buffer for recent readings
├── Makefile            — Build everything with `make`
└── README.md           — What it does, how to build, what you learned
```

**Features:**
1. Generate fake sensor data (random temperature 15.0-45.0°C)
2. Store in circular buffer (last 10 readings)
3. Log all readings to CSV file with timestamps
4. Display statistics (min, max, avg) from circular buffer
5. Menu-driven using enum state machine
6. Compile with Makefile

**What this proves you know:**
- ✅ Structs (sensor readings, ring buffer)
- ✅ Pointers (passing structs, circular buffer logic)
- ✅ Bitwise (not in this project, but you know it)
- ✅ File I/O (CSV logging)
- ✅ Enums (state machine)
- ✅ Multi-file organization (.c + .h pairs)
- ✅ Makefile
- ✅ Dynamic memory (if you `malloc` the buffer)

---

### 💻 Deep Session 2 (9:30-11:00 AM) — Continue Data Logger

Continue building. Focus on clean code:
- Add `const` to read-only parameters
- Use `uint32_t` instead of `unsigned int`
- Add comments explaining WHY, not WHAT
- Handle errors (null file pointer, malloc failure)

---

### 💻 Deep Session 3 (11:15 AM-12:45 PM) — GDB + Final Polish

- Compile with `-g`
- Run through GDB: set breakpoints, step through the state machine, inspect the circular buffer contents
- Fix any remaining bugs
- Push to GitHub: `git add .` → `git commit -m "May final project: data logger simulator"` → `git push`

---

### 🇩🇪 German (2:00-5:00 PM)

- **DW Nicos Weg**: Lessons 24-25 (2:00-3:30 PM)
- **Write a paragraph in German** (3:30-4:00 PM): 5-7 sentences about yourself, your job, your goals. Use dict.cc for words you don't know.
- **Google AI Pro** (4:00-5:00 PM): "Read my German paragraph and correct it. Explain each correction."
- **Anki**: Mega review — clear all pending cards

---

### ✅ Day 30: Data logger simulator COMPLETE. Multi-file project with Makefile. Git pushed. German paragraph written.

---

## DAY 31 — Sunday, May 31 🟨 MONTH TEST + REVIEW 🏆

### 💻 MONTH TEST (7:30-12:30 PM)

---

**This is your self-assessment. No videos. No books. No Google AI. Just you and gcc.**

#### Test 1: Write From Memory (7:30-9:00 AM)

Close ALL references. Open a blank file. Write these from memory:

1. **A program with a struct, typedef, and passing struct by pointer** — 15 min
2. **The 4 bitwise macros (SET, CLEAR, TOGGLE, CHECK)** — 5 min
3. **A linked list with insert, delete, and print** — 20 min
4. **A circular buffer with push and pop** — 15 min
5. **A swap function using pointers** — 5 min
6. **A bubble sort function** — 10 min

**Scoring**: If you can write 5/6 without looking → you're READY for Phase 2. 3-4/6 → review weak areas this week. Under 3 → repeat key exercises before moving on.

---

#### Test 2: HackerRank Challenge Session (9:15-10:45 AM)

Go to **HackerRank C domain** → attempt 5 challenges you haven't done:
- https://www.hackerrank.com/domains/c

Try challenges from these categories:
- "Structs and Enums"
- "Dynamic Array in C"
- "Printing Tokens"
- Any challenge rated "Medium"

---

#### Test 3: Interview Questions (11:00 AM-12:30 PM)

Open a file `may_review.c`. Write answers (in comments) to these questions:
1. What is a pointer? Draw a memory diagram.
2. What is the difference between stack and heap?
3. What does `volatile` mean and when do you use it?
4. What is a function pointer? Give an example use case.
5. Explain `const int *p` vs `int * const p`
6. What is a buffer overflow and how do you prevent it?
7. What is the compilation pipeline (preprocess → compile → assemble → link)?
8. What is a state machine? Why is it important in embedded?
9. What is typedef and why do we use stdint.h types in embedded?
10. Explain SET_BIT, CLEAR_BIT macros — how do they work?

---

### 🇩🇪 German Final Review (2:00-4:00 PM)

- Anki: can you get through ALL cards with ≥80% correct?
- Count: how many German words do you know? Target: 80+
- Read your German paragraph from yesterday — can you say it from memory?
- Nicos Weg: how many lessons completed? Target: 20-25

---

### 📋 MONTHLY REVIEW (4:00-5:00 PM)

Open **`PROGRESS.md`** → May Monthly Retrospective section:

| Metric | Target | Actual | Notes |
|:---|:---|:---|:---|
| C programs written from scratch | 30+ | ___ | |
| GitHub commits | 15+ | ___ | |
| Programs you can re-write from MEMORY | 10+ | ___ | |
| K&R chapters completed | Chapters 1-7 | ___ | |
| Neso Academy videos watched | 40+ | ___ | |
| mycodeschool pointers playlist | ALL 15 | ___ | |
| HackerRank challenges completed | 15+ | ___ | |
| Nicos Weg lessons completed | 20-25 | ___ | |
| German words in Anki | 80+ | ___ | |
| German sentences you can say | 15+ | ___ | |
| Days where you woke at 5 AM | ≥ 25 of 31 | ___ | |
| Total active study hours | ~90 hours | ___ | |
| Memory test score | 5/6 or better | ___ | |
| Data logger project on GitHub | ✅ | ___ | |

**Reflection questions:**
- What was the hardest topic this month?
- What would you do differently?
- Are you ready for STM32 in July? (Be honest)
- Rate your C confidence: 1-10

---

### ✅ Day 31: Month test COMPLETED. All metrics logged. June plan reviewed.

---

### 🛡️ AI SUPERVISOR READINESS CHECK (Answer honestly)

After completing May, you should be able to:
- [ ] **EXPLAIN** pointers, stack/heap, volatile on a whiteboard — no code, no AI, just you and a marker
- [ ] **SPOT BUGS** in code you've never seen before — because you've debugged 20+ of your own bugs manually
- [ ] **DEBUG** a segfault using `gdb` without asking AI for help
- [ ] **READ** a 32-bit register value in hex/binary and know which bits are set
- [ ] **DRAW** the memory layout of a struct with padding — on paper, from memory
- [ ] **WRITE** a state machine and a circular buffer from scratch — these are in EVERY embedded device ever made

> If you can do 5/6 of these: **you are already more capable than 90% of CSE graduates who learned with Copilot.** You understand the machine. They understand the prompt. When AI generates wrong code, they panic. You debug.

> **This is your edge. Protect it. Never stop learning the WHY.**

---

## 📚 WEEK 5 RESOURCE CHECKLIST

All resources used this week:
- [ ] Jacob Sorber: "State Machines in C" (Day 26)
- [ ] Neso Academy: "Enumeration in C" (Day 26)
- [ ] Jacob Sorber: "volatile in C" (Day 27)
- [ ] Jacob Sorber: "const in C" (Day 27)
- [ ] Neso Academy: "File Handling Parts 1-3" (Day 28)
- [ ] Jacob Sorber: "The C Preprocessor" (Day 29)
- [ ] Jacob Sorber: "How to Write a Makefile" (Day 30)
- [ ] K&R Chapters 4 (preprocessor) and 7 (I/O) (ongoing)
- [ ] Beej's Guide: Preprocessor and File I/O chapters (reference)
- [ ] HackerRank C domain (Day 31 test)

---

## 🎯 END OF MAY — WHAT'S NEXT?

**June 2026 (Phase 1 continued — Weeks 6-9):**
- Makefile mastery, GDB expertise
- Queue data structure, more state machine patterns
- Packed structs, bit fields deep, memory-mapped I/O concept
- **FINAL C PROJECT**: Polished GitHub repo with 15+ programs + READMEs
- German A1 completion (finish Nicos Weg A1)

> **Phase 1 now extends through Jul 15** to absorb the wedding disruption (May 1-13).
> Extra buffer weeks (Jul 1-15) can be used for catch-up or deeper capstone work.

**July 16 (Phase 2 — STM32):**
- Install STM32CubeIDE
- Start: GPIO → UART → Timers → Interrupts → ADC
- Your first blinking LED — but you'll understand EVERY BIT you set
