# 📅 WEEK 1 — May 1-4 (Fri-Mon): SETUP + C BASICS

> **Topics**: Development environment, variables, data types, printf/scanf, operators, conditions, loops
> **K.N. King Chapters**: Ch 1-5 (Introducing C, C Fundamentals, Formatted I/O, Expressions, Selection Statements)
> **K&R Bed Reading**: Chapter 1 (Tutorial Introduction), Chapter 2 (Types, Operators, Expressions)
> **FastBit Udemy**: Sections 1-4 (Introduction, Hello World, Data types, Variables)
> **Programs to write**: 12-15
> **German**: Nicos Weg Lessons 1-6, learn 20 words
> **📚 Full resource details**: See `10_RESOURCES.md`

---

## 📺 PRE-WEEK HOMEWORK (Watch before May 1st)

> **Do this on the weekend of April 26-27.** It gives you a mental map of everything you'll learn in May.

1. **Bro Code — "C Programming Full Course"** (~4 hours, single video)
   - Search YouTube: `Bro Code C Programming Full Course`
   - Watch at 1.5× speed over a weekend afternoon
   - Don't take notes — just absorb the big picture
   - You'll recognize every topic when you encounter it in May

2. **Open K.N. King PDF** — skim the Table of Contents to see what chapters you'll cover
   - File: `f:\Documents\DEVELOP\Books\C Programming - A Modern Approach - 2nd_Ed(C89, c99) - King by .pdf`
   - Bookmark Chapters 1-5 in Adobe Acrobat Reader Pro — these are your Week 1 reading

---

## DAY 1 — Friday, May 1 ⭐ THE BEGINNING

### 🔶 Morning Block (5:10 - 6:30 AM) — FIRST EVER C CODING SESSION

---

#### 📺 WATCH FIRST (15 min) — 5:10 to 5:25 AM

Watch these videos (choose one track):

**Option A — FastBit Udemy (PRIMARY):**
- Open FastBit "Embedded C Programming" course → Section 1: Introduction
- Watch at 1.5× speed

**Option B — Neso Academy (FREE supplement):**
1. **Neso Academy: "Introduction to C Programming"** (~8 min)
2. **Neso Academy: "First C Program"** (~7 min)

> **Rule**: FastBit is your primary video. Use Neso for quick 7-min explanations of specific concepts when you need a second perspective.

---

#### 💻 CODE (45 min) — 5:25 to 6:10 AM

**Setup (5:25-5:35):** Open WSL terminal. Create your workspace:
```bash
wsl
cd /mnt/f/Documents/DEVELOP
mkdir C-Practice && cd C-Practice
mkdir week1 && cd week1
```

**Program 1 — `hello.c` (5:35-5:45):**
- Open `nano hello.c` (or VS Code if you prefer: `code .` → new file)
- Type a Hello World program yourself — include your name, the date, your goal
- Compile: `gcc hello.c -o hello -Wall`
- If errors: READ the error message carefully. Google it. Fix it yourself.
- Run: `./hello`
- **What to understand**: What does `#include <stdio.h>` actually do? What is `int main(void)` returning and to whom? What does `\n` do?
- **Ask Google AI** (explanation only): "Explain what happens step by step when I run `gcc hello.c -o hello` — what is preprocessing, compilation, assembly, and linking?"

**Program 2 — `variables.c` (5:45-5:55):**
- Declare variables of every type: `int`, `float`, `double`, `char`, `long`, `short`, `unsigned`
- Print each with correct format specifier (`%d`, `%f`, `%lf`, `%c`, `%ld`, `%u`)
- Use `sizeof()` to print the size of each type
- **What to understand**: Why is `int` 4 bytes? Why does `char` store numbers (ASCII)?
- **Ask Google AI**: "Why is `sizeof(int)` different on different machines? What does it mean for embedded systems?"

**Program 3 — `input.c` (5:55-6:05):**
- Use `scanf()` to read two numbers from user
- Print their sum, difference, product, quotient
- **What to understand**: Why does `scanf` need `&` before variable name? (Preview of pointers!)
- **Trap to discover**: What happens when you divide two integers? `17 / 5` = ? (answer: 3, not 3.4!)

**Program 4 — `datatypes.c` (6:05-6:15):**
- Print `sizeof()` for ALL types in a neat table format using `printf` alignment
- This program is your **reference sheet** — you'll come back to it throughout May

---

#### 📖 READ (if time remains) — 6:15 to 6:30 AM

- Open: **K.N. King Chapter 2** — "C Fundamentals" → read sections 2.1-2.4 (program structure, comments, variables)
- Highlight key points in Adobe Acrobat Reader Pro
- **Bed reading tonight**: Open K&R Chapter 1 (pp. 9-35) for the concise "expert" take on the same topics

---

#### 🧪 TEST YOURSELF (do during lunch or after dinner)

- Go to **learn-c.org** → "Hello, World!" lesson → https://www.learn-c.org/en/Hello%2C_World%21
- Go to **learn-c.org** → "Variables and Types" lesson → https://www.learn-c.org/en/Variables_and_Types
- Try **HackerRank**: "Hello World in C" → https://www.hackerrank.com/challenges/hello-world-c
- Try **HackerRank**: "Playing With Characters" → https://www.hackerrank.com/challenges/playing-with-characters

---

### 🎧 Commute IN (7:00-8:30 AM) — German
- Open **DW Nicos Weg** app → Start **Lesson 1: "Hallo!"**
- Watch the video. Listen to pronunciation carefully.
- Repeat every German phrase out loud (quietly)
- If short, continue to **Lesson 2: "Ich heiße..."**

### 📱 Lunch (12:30-12:45 PM) — German
- Open **AnkiDroid** → Download the **"German A1 Vocabulary"** deck from shared decks
- Study first 5 cards. This takes 3-4 minutes. Do it EVERY day from now on.

### 🎧 Commute BACK (7:30-9:00 PM) — German
- Continue Nicos Weg Lessons 2-3 (or re-listen to Lesson 1 if you forgot)
- Practice in your head: *"Ich heiße Khashyap. Ich komme aus Indien. Ich bin Ingenieur."*

### 📖 Bed (9:30-10:00 PM) — K&R Reading
- Read **K&R Chapter 1**, pages 1-15 ("A Tutorial Introduction")
- This is why you printed it. Read on paper, not screen.
- Don't code — just READ and absorb. Underline things you don't understand.

### ✅ Day 1 Checklist
- [ ] WSL opened, `C-Practice/week1/` created
- [ ] `hello.c` compiled and ran
- [ ] `variables.c` — all types printed with sizeof
- [ ] `input.c` — scanf + arithmetic working
- [ ] `datatypes.c` — reference table printed
- [ ] Nicos Weg Lesson 1-2 watched
- [ ] AnkiDroid A1 deck downloaded, 5 cards studied
- [ ] K&R pages 1-15 read
- [ ] At least 1 HackerRank/learn-c.org exercise done

---

## DAY 2 — Saturday, May 2 🟩 FIRST BIG STUDY DAY

### 💻 Warmup (6:30-7:30 AM) — Operators + Type Casting

---

#### 📺 WATCH FIRST (20 min) — 6:30 to 6:50 AM

1. **Neso Academy: "Arithmetic Operators in C"** (~10 min)
   - Focus on: Integer division trap (`17/5 = 3`), modulo operator `%`

2. **Neso Academy: "Increment and Decrement Operators"** (~8 min)
   - Focus on: `++a` (pre) vs `a++` (post) — print both to see the difference

> **Alternative**: **Jacob Sorber: "C Operators You Need to Know"** (~8 min) — more practical, terminal-based

---

#### 📖 READ (10 min) — 6:50 to 7:00 AM

- **K&R pages 16-25** (section 2.1-2.7: Types, Operators, Expressions)
- Pay attention to: type conversion rules, operator precedence table

---

#### 💻 CODE (30 min) — 7:00 to 7:30 AM

**Program 5 — `operators.c`:**
- Test ALL operators: `+`, `-`, `*`, `/`, `%`
- Discover: `17 / 5` = `3` (integer division!). Then fix it with `(float)17 / 5`
- Test `++a` vs `a++` — print them to see the difference
- **Why this matters for embedded**: C truncates integer division because embedded systems need fast integer math without floating point hardware.

**Program 6 — `ascii.c`:**
- Print ASCII values of `'A'` to `'Z'` using a loop
- Discover: `'A' + 32 = 'a'` (lowercase!)
- Print `'0'` to `'9'` — discover they have ASCII values 48-57
- **Why this matters for embedded**: UART sends bytes (numbers), not letters. Understanding ASCII = understanding serial communication.

**Program 7 — `type_casting.c`:**
- CGPA calculation: `450 / 600` = `0` (WRONG!) vs `(float)450 / 600` = `0.75` (RIGHT!)
- Bavarian formula: write it in C: `grade = ((10 - 7.5) / (10 - 4.0)) * 3 + 1`
- Print: "Your German grade: 2.25"

---

### 💻 Deep Session 1 (7:45-9:15 AM) — Conditions

---

#### 📺 WATCH FIRST (15 min) — 7:45 to 8:00 AM

1. **Neso Academy: "If Statement in C"** (~8 min)
2. **Neso Academy: "If-Else Statement in C"** (~6 min)

---

#### 📖 READ — K&R pages 26-30 (if-else, switch)

---

#### 💻 CODE (60 min) — 8:00 to 9:00 AM

**Program 8 — `conditions.c`:**
- `if/else` chain: Check if a number is positive, negative, or zero
- Logical operators (`&&`, `||`, `!`): Check if a number is in a range (e.g., 18-65)
- Ternary operator: `result = (a > b) ? a : b;`
- **Embedded insight**: Short-circuit evaluation in `if (a && b)` — if `a` is false, `b` is NEVER checked. This prevents null pointer crashes in firmware.

**Program 9 — `switch_demo.c`:**
- Switch/case for month names (input month number, print name)
- DELIBERATELY forget `break` once — observe the "fall-through" behavior
- **Embedded insight**: Switch-case is the heart of state machines. Every embedded device firmware uses this.

---

#### 🧪 TEST YOURSELF — 9:00-9:15 AM

- **HackerRank**: "Conditional Statements in C" → https://www.hackerrank.com/challenges/conditional-statements-in-c
- **learn-c.org**: "Conditions" → https://www.learn-c.org/en/Conditions

---

### 💻 Deep Session 2 (9:30-11:00 AM) — Loops

---

#### 📺 WATCH FIRST (20 min) — 9:30 to 9:50 AM

1. **Neso Academy: "While Loop in C"** (~9 min)
2. **Neso Academy: "For Loop in C"** (~10 min)
3. **Neso Academy: "Do-While Loop in C"** (~7 min) — skim if short on time

---

#### 📖 READ — K&R pages 30-35 (Chapter 1 loops section)

---

#### 💻 CODE (55 min) — 9:50 to 10:45 AM

**Program 10 — `loops.c`:**
- Print numbers 1-100 using `for`, `while`, and `do-while`
- Use `break` to stop at 50, use `continue` to skip even numbers

**Program 11 — `patterns.c`:**
- Print these patterns using nested loops:
  ```
  *        1           *
  **       12         ***
  ***      123       *****
  ****     1234     *******
  ```
- **Why patterns matter**: Nested loops = nested array iteration = matrix operations = image processing on embedded systems

---

#### 🧪 TEST YOURSELF — 10:45-11:00 AM

- **HackerRank**: "For Loop in C" → https://www.hackerrank.com/challenges/for-loop-in-c
- **learn-c.org**: "Loops" → https://www.learn-c.org/en/For_loops

---

### 💻 Deep Session 3 (11:15 AM-12:45 PM) — More Loop Practice

---

#### 📺 WATCH (10 min) — 11:15 to 11:25 AM

- **Neso Academy: "Nested Loops in C"** (~8 min)
- **Neso Academy: "Break and Continue in C"** (~6 min) — skim if already clear

---

#### 💻 CODE (70 min) — 11:25 AM to 12:35 PM

**Program 12 — `number_games.c`:**
- Check if a number is prime (use trial division with a loop)
- Calculate factorial of N (loop version, NOT recursion yet)
- Reverse a number (extract digits with `% 10` and `/ 10`)
- Count digits in a number
- **Embedded insight**: These algorithms (especially digit extraction) are used in embedded displays (7-segment LED, LCD number display)

---

#### 🧪 TEST YOURSELF — 12:35-12:45 PM

- **HackerRank**: "Sum of Digits of a Five Digit Number" → https://www.hackerrank.com/challenges/sum-of-digits-of-a-five-digit-number
- **Exercism**: `hello-world` exercise → https://exercism.org/tracks/c/exercises/hello-world

---

### 🇩🇪 German (2:00-5:00 PM) — Saturday Template

#### 📺 German Resources for Today

- **DW Nicos Weg** (app): Lessons 3-5 (2:00-3:30 PM)
- **Learn German with Anja** (YouTube): Search "German Greetings for Beginners" (~10 min) (3:30-3:45 PM)
- **Google AI Pro** voice mode (3:45-5:00 PM):
  - Say: "Speak to me in simple German A1 level. Teach me how to greet people, introduce myself, and say where I come from. Correct my pronunciation."
- **AnkiDroid**: Add 10 new cards from today's Nicos Weg lessons

---

### ✅ Day 2 Checklist
- [ ] `operators.c` + `ascii.c` + `type_casting.c` — operators mastered
- [ ] `conditions.c` + `switch_demo.c` — if/else and switch working
- [ ] `loops.c` + `patterns.c` — all 3 loop types demonstrated
- [ ] `number_games.c` — prime, factorial, reverse all working
- [ ] At least 3 HackerRank/learn-c.org exercises completed
- [ ] Nicos Weg Lessons 3-5 watched
- [ ] 10 new Anki cards added
- [ ] K&R pages 16-35 read or skimmed
- [ ] **BIG day! 6-8 programs written from scratch.**

---

## DAY 3 — Sunday, May 3 🟨 FUNCTIONS + REVIEW + GIT

### 💻 C Practice (7:30-9:00 AM) — Functions

---

#### 📺 WATCH FIRST (20 min) — 7:30 to 7:50 AM

1. **Neso Academy: "Functions in C"** (~10 min)
   - Focus on: function declaration, definition, calling, return values
2. **Neso Academy: "Call by Value in C"** (~8 min)
   - Focus on: Understanding that C functions get COPIES of arguments (this matters A LOT when you learn pointers in Week 3)

> **Deeper understanding**: **Jacob Sorber: "Functions in C explained"** (~12 min) — watch this if you have extra time

---

#### 📖 READ — K&R pages 35-50 (Chapter 1 functions, Chapter 4 start)
- Or: **Beej's Guide** → Chapter 4: Functions → https://beej.us/guide/bgc/html/split/functions.html

---

#### 💻 CODE (50 min) — 7:50 to 8:40 AM

**Program 13 — `functions.c`:**
Write 5+ functions from scratch (ALL returning values, ALL with parameters):
- `int add(int a, int b)` — returns sum
- `long factorial(int n)` — returns n!
- `int is_prime(int n)` — returns 1 if prime, 0 if not
- `int max_of_three(int a, int b, int c)` — returns the largest
- `void print_line(int length)` — prints a line of `=` characters

---

#### 🧪 TEST YOURSELF — 8:40-9:00 AM

- **learn-c.org**: "Functions" → https://www.learn-c.org/en/Functions
- **HackerRank**: "Functions in C" → https://www.hackerrank.com/challenges/functions-in-c

---

### 💻 Mini-Project (9:15-10:45 AM) — Calculator

#### 💻 CODE — Build `calculator.c`

This is your first "portfolio-worthy" program. It combines everything from Days 1-2:
- Use a `do-while` loop for the main menu (keeps running until user quits)
- Use `switch/case` for operator selection (+, -, *, /, %)
- Use **separate functions** for each operation
- Handle division by zero gracefully (print error, don't crash)
- Handle invalid menu choices

> **No video needed** — you already know all the components. This is pure assembly. If stuck on HOW to structure it, ask Google AI: "How should I structure a menu-driven calculator in C? Give me the logic flow, NOT the code."

---

### 💻 Git Push (11:00 AM-12:30 PM)

---

#### 📺 WATCH FIRST (15 min) — 11:00 to 11:15 AM

- **Jacob Sorber: "Git for Beginners"** (search on YouTube, ~10 min)
  - Focus on: init, add, commit, push — that's all you need today
- OR: Read **GitHub Docs: "Set up Git"** → https://docs.github.com/en/get-started/getting-started-with-git/set-up-git

---

#### 💻 DO (75 min) — 11:15 AM to 12:30 PM

1. Create repo on GitHub: github.com → New → Name it **"C-Practice"** → Make it **Public** (portfolio!)
2. In WSL:
   ```bash
   cd /mnt/f/Documents/DEVELOP/C-Practice
   git init
   echo "*.o" > .gitignore
   echo "*.out" >> .gitignore
   ```
3. Write a proper `README.md`:
   ```markdown
   # C Practice — Embedded Systems Foundation
   Learning C programming from scratch for embedded systems (STM32/ESP32).
   Part of my 27-month roadmap to a German Masters in Embedded Systems.
   
   ## Week 1: Setup + C Basics
   - hello.c, variables.c, input.c, datatypes.c
   - operators.c, ascii.c, type_casting.c
   - conditions.c, switch_demo.c, loops.c, patterns.c
   - number_games.c, functions.c, calculator.c
   ```
4. `git add .` → `git commit -m "Week 1: C basics - variables, operators, loops, functions"` → `git remote add origin <URL>` → `git push -u origin main`

---

### 🇩🇪 German Review (2:00-3:00 PM)
- Write 10 German sentences from MEMORY in a notebook (or Notion)
- Use **dict.cc** to check correctness
- **Learn German with Anja** (YouTube): Search "German Numbers 1-100" — watch and repeat

### 🇩🇪 Anki Mega Review (3:00-4:00 PM)
- Clear ALL pending Anki cards. Target: 20+ cards mastered.

### 📋 Weekly Review (4:00-4:30 PM)
- Open **Notion** → Create "May 2026" page → "Week 1" sub-page
- Log: hours studied, programs written, German words learned, what was hardest, what to improve

---

### ✅ Day 3 Checklist
- [ ] `functions.c` — 5 functions written from scratch
- [ ] `calculator.c` — menu-driven, all operations working
- [ ] Git repo created, all code pushed to GitHub
- [ ] README.md written
- [ ] HackerRank/learn-c.org exercises done
- [ ] German: 10 sentences written from memory
- [ ] Anki: 20+ cards reviewed
- [ ] Weekly review in Notion completed

---

## DAY 4 — Monday, May 4 🟦 WEEKDAY

### 🔶 Morning Block (5:10-6:30 AM) — Arrays Introduction

---

#### 📺 WATCH FIRST (15 min) — 5:10 to 5:25 AM

1. **Neso Academy: "1D Arrays in C"** (~10 min)
   - Focus on: Declaration, initialization, indexing, memory layout
2. **Neso Academy: "Accessing Array Elements"** (~7 min)
   - Focus on: Index starts at 0, out-of-bounds is UNDEFINED BEHAVIOR

> **Deeper understanding**: **Jacob Sorber: "Arrays in C (the full story)"** (~12 min) — excellent explanation of how arrays live in memory

---

#### 📖 READ — K&R pages 22-28 (arrays in Chapter 1)
- Or: **Beej's Guide** → Chapter 6: Arrays → https://beej.us/guide/bgc/html/split/arrays.html

---

#### 💻 CODE (45 min) — 5:25 to 6:10 AM

**Program 14 — `arrays.c`:**
- Declare 5 exam marks in an array
- Print all elements using a for loop
- Calculate sum and average
- Find maximum and minimum
- Print in reverse order
- **What to understand**: Index starts at 0. `marks[5]` with 5 elements → valid indices 0-4. `marks[5]` is a BUG (buffer overflow — the #1 embedded software vulnerability).
- **Ask Google AI**: "What is a buffer overflow in C? Why is it the most dangerous bug in embedded systems? Give me a simple example."

If time remains, start **`array_operations.c`**:
- Read N numbers from user into an array (where N is also input)
- Count how many are positive, negative, zero
- Find second largest element

---

#### 🧪 TEST YOURSELF (during lunch break)

- **HackerRank**: "1D Arrays in C" → https://www.hackerrank.com/challenges/1d-arrays-in-c
- **learn-c.org**: "Arrays" → https://www.learn-c.org/en/Arrays

---

### 🎧 Commute IN: Nicos Weg Lesson 6
### 📱 Lunch Anki: 5 new cards + review
### 🎧 Commute BACK: Re-listen Nicos Weg Lessons 4-6
### 📖 Bed: K&R pages 36-50 (functions chapter)

---

### ✅ Day 4 Checklist
- [ ] `arrays.c` written (morning only)
- [ ] Neso Academy array videos watched
- [ ] HackerRank array challenge attempted
- [ ] German: Nicos Weg Lesson 6 + Anki 5 cards
- [ ] K&R pages 36-50 read before bed

---

## 📊 WEEK 1 SUMMARY

| Metric | Target | Done? |
|:---|:---|:---|
| Programs written | 10+ | [ ] |
| K&R pages read | 1-50 | [ ] |
| Neso Academy videos watched | 10-15 | [ ] |
| HackerRank/learn-c.org exercises | 5+ | [ ] |
| Nicos Weg lessons | 1-6 | [ ] |
| German words in Anki | 20+ | [ ] |
| Git commits | 1+ | [ ] |
| Mornings woke at 5 AM | 4/4 | [ ] |

---

## 📚 WEEK 1 RESOURCE CHECKLIST

Before starting Week 1, make sure you have:
- [ ] K&R Chapter 1-2 printed (or open the PDF)
- [ ] Neso Academy C Programming playlist bookmarked
- [ ] learn-c.org bookmarked
- [ ] HackerRank C domain bookmarked
- [ ] Beej's Guide bookmarked
- [ ] AnkiDroid installed with A1 German deck
- [ ] DW Nicos Weg app installed
- [ ] WSL2 + gcc working (`gcc --version` shows output)
- [ ] VS Code with C/C++ extension installed
- [ ] PomoDone timer ready (GitHub Student Pack)
