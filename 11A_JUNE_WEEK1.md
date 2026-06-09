# JUNE WEEK 1 (Jun 9–15) — Phase 1 Week 1: SETUP + C BASICS

> **Topics**: Environment setup, WSL2 + gcc, variables, data types, operators, conditions, loops, functions, arrays
> **K.N. King Reading**: Ch 1–7 (pre-gym + bed — read these all week)
> **K&R Bed Reading**: Chapter 1 (A Tutorial Introduction) — pages 1–52
> **AI Policy**: BANNED for code — AI may only explain concepts
> **Dates**: Tuesday June 9 → Sunday June 15, 2026

---

## PRE-WEEK SETUP (June 9 — First Day)

Before doing anything else on June 9:
- [ ] WSL2 installed and working (test: `wsl --version` in PowerShell)
- [ ] gcc installed: `sudo apt install build-essential gdb valgrind make`
- [ ] Test: `echo '#include <stdio.h>\nint main(){printf("hello\\n");}' | gcc -x c - -o test && ./test`
- [ ] GitHub account active, SSH key configured
- [ ] Create repo: "C-Practice" (public, no README — you'll write it)
- [ ] AnkiDroid installed on phone + German A1 deck downloaded
- [ ] DW Nicos Weg app installed, first lesson downloaded for offline

---

## WEEKDAY READING SCHEDULE (Jun 9–13)

### Tuesday June 9 — Pre-Gym (5:00–5:25 AM)
**Read**: K.N. King Chapter 1 (Introducing C)
- What is C? History, standards (C89, C99, C11)
- First program structure: `#include`, `main()`, `return`
- How to compile: gcc flags overview

**Bed Reading (9:30–10:00 PM)**: K&R Chapter 1 pages 1–15

### Wednesday June 10 — Pre-Gym (5:00–5:25 AM)
**Read**: K.N. King Chapter 2 (C Fundamentals)
- Variable declarations, naming rules
- Assignment, printf format specifiers (%d, %f, %c, %s, %x)
- Comments, whitespace, C program structure

**Bed Reading**: K&R Chapter 1 pages 16–30

### Thursday June 11 — Pre-Gym (5:00–5:25 AM)
**Read**: K.N. King Chapter 3 (Formatted Input/Output)
- printf format strings deep
- scanf: reading integers, floats, strings
- Why gets() is BANNED, use fgets() instead

**Bed Reading**: K&R Chapter 1 pages 30–52

### Friday June 12 — Pre-Gym (5:00–5:25 AM)
**Read**: K.N. King Chapters 4–5 (Expressions, Selection)
- Arithmetic operators, precedence
- if/else, switch/case, ternary operator ?:
- Logical operators: &&, ||, !

**Bed Reading**: K.N. King Chapter 6 (Loops) — preview for Saturday

### Monday June 15 — Pre-Gym (5:00–5:25 AM)
**Read**: K.N. King Chapter 7 (Basic Types — int, float, double, char, unsigned)
**Bed Reading**: K&R Chapter 2 (Types, Operators, Expressions)

---

## SATURDAY JUNE 13 — FIRST CODING DAY (7:30 AM–6:30 PM)

### Warmup (7:30–8:00 AM): Watch FastBit Embedded C Section 1
- Introduction to the course (15 min at 1.5×)
- What is embedded C, why it matters

### BLOCK 1 (8:00–9:30 AM): C Basics Programs
Write ALL programs from scratch. NO copy-paste. NO AI code.

```
week1/
├── hello.c          — Hello World + your name, date, and goal in comments
├── variables.c      — All 6 types: int, float, double, char, long, unsigned. Print with sizeof()
├── input.c          — scanf two numbers, print sum/difference/product/quotient
├── ascii.c          — Print ASCII values of 'A'-'Z', 'a'-'z', '0'-'9'
└── type_cast.c      — Calculate your CGPA in German grade: ((10-7.5)/(10-4))*3+1
```

Compile each: `gcc -Wall -Wextra -g -std=c99 hello.c -o hello`
ZERO warnings allowed. Fix every warning before moving on.

### BREAK (9:30–9:45)

### BLOCK 2 (9:45–11:15 AM): Operators + Conditions
```
├── operators.c      — All operators: arithmetic, assignment, increment, comparison, logical
├── conditions.c     — if/else chains, logical operators, ternary operator ?:
├── switch_demo.c    — Switch/case for month names. Deliberately leave out one break to see fall-through
└── type_limits.c    — Print INT_MAX, INT_MIN, FLT_MAX, DBL_MAX using <limits.h> and <float.h>
```

### BREAK (11:15–11:30)

### BLOCK 3 (11:30 AM–12:30 PM): Loops
```
├── loops.c          — Same task (print 1-100, skip multiples of 3) using: for, while, do-while
├── patterns.c       — Nested loops: right-triangle star pattern, number pyramid
└── number_games.c   — Check prime, factorial (iterative), count digits, reverse a number
```

### LUNCH (12:30–1:30 PM)

### GERMAN BLOCK 1 (1:30–4:30 PM)
- Nicos Weg Lessons 3–5 (DW online or app)
- Learn German with Anja: "German Greetings" video (YouTube)
- Write 10 sentences introducing yourself in German
- Anki: add 10 new cards from today's lessons
- ChatGPT: "I'm a German A1 learner. Ask me simple yes/no questions in German."

### GERMAN BLOCK 2 (5:00–6:30 PM)
- Nicos Weg Lessons 6–7
- AnkiDroid: review all cards pending
- Write from memory: your self-introduction (without looking at notes)

---

## SUNDAY JUNE 14 — FUNCTIONS + ARRAYS + GIT (7:30 AM–4:00 PM)

### BLOCK 1 (7:30–9:00 AM): Functions
Watch: Neso Academy "Functions in C" (~10 min) + "Call by Value" (~8 min)

```
├── functions.c      — 5+ functions: add(), factorial(), is_prime(), max_of_three(), print_line()
└── calculator.c     — Menu-driven, do-while loop, switch/case, divide by zero protection
```

### BLOCK 2 (9:15–10:30 AM): Arrays
Watch: Neso Academy "1D Arrays" (~10 min)

```
├── arrays.c         — 5 exam marks, sum/avg/max/min, reverse order
└── array_ops.c      — Read N from user, count positive/negative/zero, find 2nd largest
```

### GIT PUSH (10:30–11:00 AM)
```bash
cd ~/C-Practice
git init
echo "*.o\n*.out\na.out" > .gitignore
git add .
git commit -m "Week 1: C basics — variables, operators, loops, functions, arrays"
git push origin main
```

Write week1/README.md: list all programs + one sentence about what each does.

### REST + LUNCH (11:00 AM–12:00 PM)

### GERMAN (12:00–2:00 PM)
- Nicos Weg Lessons 8–9
- Anki: mega review (clear all pending cards)
- Write 10 German words from memory without looking

### EXTENDED CODING (2:00–4:00 PM): Bubble Sort
```
├── bubble_sort.c    — Sort array ascending, then descending. Print each pass.
└── selection_sort.c — Implement selection sort, compare with bubble sort
```

**IMPORTANT**: Can you write bubble_sort from MEMORY after implementing it? Try. If not, implement again from scratch without looking.

---

## WEEK 1 CHECKPOINT (Sunday June 15, 4:00 PM)

Update PROGRESS.md now. Be honest.

| Checkpoint Item | Done? |
|:---|:---|
| WSL2 + gcc working | |
| 12+ programs written and compiling with 0 warnings | |
| Can write bubble_sort from memory | |
| Understand printf + scanf | |
| Understand all loop types | |
| Calculator program working | |
| GitHub: first commit pushed | |
| Nicos Weg: lessons 1–9 done | |
| Anki: 20+ German words | |
| K.N. King Ch 1–7 read | |

**Self-rating (C basics 1–10)**: ___ (minimum 6 before Week 2)

---

## WEEKDAY THEORY FOCUS (Week 1)

| Day | Read Before Gym | Bed Read |
|:---|:---|:---|
| Tue Jun 9 | K.N. King Ch 1 | K&R pp. 1–15 |
| Wed Jun 10 | K.N. King Ch 2 | K&R pp. 16–30 |
| Thu Jun 11 | K.N. King Ch 3 | K&R pp. 30–52 |
| Fri Jun 12 | K.N. King Ch 4–5 | K.N. King Ch 6 preview |
| Mon Jun 15 | K.N. King Ch 7 | K&R Ch 2 |

> The coding block this week is Saturday + Sunday. Monday is reading-only.
> By Saturday, you will have read 7 chapters before writing a single line of code. Your coding sessions will be faster because you'll already understand the theory.
