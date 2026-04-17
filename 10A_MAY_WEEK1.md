# 📅 WEEK 1 — May 1-4 (Fri-Mon): SETUP + C BASICS

> **Topics**: Development environment, variables, data types, printf/scanf, operators, conditions, loops
> **K&R Chapters**: Chapter 1 (Tutorial Introduction), Chapter 2 (Types, Operators, Expressions)
> **Programs to write**: 12-15
> **German**: Nicos Weg Lessons 1-5, learn 20 words

---

## DAY 1 — Friday, May 1 ⭐ THE BEGINNING

### 🔶 Morning Block (5:10 - 6:30 AM) — FIRST EVER C CODING SESSION

**What to learn**: How C programs are structured, what `#include` means, what `main()` does, how `printf` formats output, what data types exist.

**How to learn**:
1. **(5:10-5:20)** Open WSL terminal. Navigate to your workspace:
   ```
   wsl → cd /mnt/f/Documents/DEVELOP → mkdir C-Practice → cd C-Practice → mkdir week1 → cd week1
   ```

2. **(5:20-5:40)** Write your first program `hello.c`:
   - Open `nano hello.c`
   - Type a Hello World program yourself — include your name, the date, your goal
   - Compile: `gcc hello.c -o hello -Wall`
   - If errors: READ the error message carefully. Google it. Fix it yourself.
   - Run: `./hello`
   - **What to understand**: What does `#include <stdio.h>` actually do? What is `int main(void)` returning and to whom? What does `\n` do?
   - **Ask Google AI**: "Explain what happens step by step when I run `gcc hello.c -o hello` — what is preprocessing, compilation, assembly, and linking?"

3. **(5:40-6:00)** Write `variables.c`:
   - Declare variables of every type: `int`, `float`, `double`, `char`, `long`, `short`, `unsigned`
   - Print each with correct format specifier (`%d`, `%f`, `%lf`, `%c`, `%ld`, `%u`)
   - Use `sizeof()` to print the size of each type
   - **What to understand**: Why is `int` 4 bytes? Why does `char` store numbers (ASCII)?
   - **Ask Google AI**: "Why is `sizeof(int)` different on different machines? What does it mean for embedded systems?"

4. **(6:00-6:20)** Write `input.c`:
   - Use `scanf()` to read two numbers from user
   - Print their sum, difference, product, quotient
   - **What to understand**: Why does `scanf` need `&` before variable name? (Preview of pointers!)
   - **Trap to discover**: What happens when you divide two integers? `17 / 5` = ? (answer: 3, not 3.4!)

5. **(6:20-6:30)** Write `datatypes.c`:
   - Print `sizeof()` for ALL types in a table format
   - **This program is your reference sheet** — you'll come back to it throughout May

### 🎧 Commute IN (7:00-8:30 AM)
- Open **DW Nicos Weg** app → Start **Lesson 1: "Hallo!"**
- Watch the video. Listen to pronunciation carefully.
- Repeat every German phrase out loud (quietly)
- If short, continue to **Lesson 2: "Ich heiße..."**

### 📱 Lunch (12:30-12:45 PM)
- Open **AnkiDroid** → Download the **"German A1 Vocabulary"** deck from shared decks
- Study first 5 cards. This takes 3-4 minutes. Do it EVERY day from now on.

### 🎧 Commute BACK (7:30-9:00 PM)
- Continue Nicos Weg Lessons 2-3 (or re-listen to Lesson 1 if you forgot)
- Practice in your head: *"Ich heiße Khashyap. Ich komme aus Indien. Ich bin Ingenieur."*

### 📖 Bed (9:30-10:00 PM)
- Read **K&R Chapter 1**, pages 1-15 ("A Tutorial Introduction")
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

---

## DAY 2 — Saturday, May 2 🟩 FIRST BIG STUDY DAY

### 💻 Warmup (6:30-7:30 AM) — Operators + Type Casting

**What to learn**: All arithmetic operators, the integer division trap, pre/post increment, type casting, ASCII values.

**How to learn**:
1. **(6:30-6:50)** Read **K&R pages 16-25** (section on expressions and operators). OR watch **Jacob Sorber: "C Operators You Need to Know"** on YouTube (~8 min).

2. **(6:50-7:10)** Write `operators.c`:
   - Test ALL operators: `+`, `-`, `*`, `/`, `%`
   - Discover: `17 / 5` = `3` (integer division!). Then fix it with `(float)17 / 5`
   - Test `++a` vs `a++` — print them to see the difference
   - **What to understand**: Why does C truncate integer division? (Because embedded systems need fast integer math)

3. **(7:10-7:30)** Write `ascii.c`:
   - Print ASCII values of `'A'` to `'Z'` using a loop
   - Discover: `'A' + 32 = 'a'` (lowercase!)
   - Print `'0'` to `'9'` — discover they have ASCII values 48-57
   - **Why this matters for embedded**: UART sends bytes (numbers), not letters. Understanding ASCII = understanding serial communication.

4. **(7:30-7:45)** Write `type_casting.c`:
   - CGPA calculation: `450 / 600` = `0` (WRONG!) vs `(float)450 / 600` = `0.75` (RIGHT!)
   - Bavarian formula: write it in C: `grade = ((10 - 7.5) / (10 - 4.0)) * 3 + 1`
   - Print: "Your German grade: 2.25"

### 💻 Deep Session 1 (7:45-9:15 AM) — Conditions
Continue into if/else, switch/case, logical operators. Write `conditions.c` and `switch_demo.c`.
See Day 3 below for details (originally covered there, now moved forward since Day 2 is a full Saturday).

### 💻 Deep Session 2 (9:30-11:00 AM) — Loops
for, while, do-while, nested loops. Write `loops.c` and `patterns.c`.

### 💻 Deep Session 3 (11:15 AM-12:45 PM) — More Loop Practice
Write `number_games.c` — prime check, factorial, reverse number, digit count.

### 🇩🇪 German (2:00-5:00 PM) — Saturday Template
- Nicos Weg Lessons 3-5
- Google AI speaking practice: Greetings, numbers 1-20
- Anki: add 10 new cards

### ✅ Day 2: `operators.c` + `ascii.c` + `type_casting.c` + `conditions.c` + `switch_demo.c` + `loops.c` + `patterns.c` + `number_games.c`. BIG day! 6-8 programs.

---

## DAY 3 — Sunday, May 3 🟨 FUNCTIONS + REVIEW + GIT

### 💻 C Practice (7:30-9:00 AM) — Functions

**What to learn**: Function declaration vs definition, parameters, return values, scope.

**How to learn**:
1. Read **K&R pages 35-50** (functions) OR watch **Jacob Sorber: "Functions in C"** (~8 min)
2. Write `functions.c`: 5+ functions from scratch (add, factorial, is_prime, max_of_three, print_line)

### 💻 Mini-Project (9:15-10:45 AM) — Calculator

Write `calculator.c` — combines everything from Days 1-2:
- Use a `do-while` loop for main menu
- Use `switch/case` for operator selection
- Use functions for each operation
- Handle division by zero
- This is your first "portfolio-worthy" program.

### 💻 Git Push (11:00 AM-12:30 PM)

**What to learn**: Git basics — init, add, commit, push, .gitignore, README.md

**How to learn**:
1. Watch **Jacob Sorber: "Git for Beginners"** (~10 min)
2. In WSL: `git init` → create `.gitignore` → write `README.md` → `git add .` → `git commit` → `git push`
3. Create the repo on GitHub first: github.com → New → "C-Practice"

### 🇩🇪 German Review (2:00-3:00 PM)
- Write 10 German sentences from MEMORY in notebook
- Use dict.cc to check correctness

### 🇩🇪 Anki Mega Review (3:00-4:00 PM)
- Clear ALL pending cards. Target: 20+ cards mastered.

### 📋 Weekly Review (4:00-4:30 PM)
- Open Notion → Create "May 2026" page
- Log: hours studied, programs written, German words learned, what was hardest

### ✅ Day 3: `functions.c` + `calculator.c` + Git setup + first push. German 10 sentences. Anki 20+ cards.

---

## DAY 4 — Monday, May 4 🟦 WEEKDAY

### 🔶 Morning Block (5:10-6:30 AM) — Arrays Introduction

**What to learn**: What arrays are, how they're stored in memory, indexing, iterating.
**How to learn**:
1. Watch **Jacob Sorber: "Arrays in C"** (~7 min)
2. Write `arrays.c`:
   - Declare 5 exam marks, print all, find sum/average, find max/min, print reversed
   - **What to understand**: Index starts at 0. `marks[5]` with 5 elements → valid indices 0-4. `marks[5]` is a BUG (buffer overflow).
3. If time remains, start `array_operations.c` (count positives/negatives, find second largest)

### 🎧 Commute + Evening: Nicos Weg Lesson 6 | Anki | K&R pages 36-50

### ✅ Day 4: `arrays.c` (morning only). Continue array practice tomorrow.

---

## 📊 WEEK 1 SUMMARY

| Metric | Target | Done? |
|:---|:---|:---|
| Programs written | 10+ | [ ] |
| K&R pages read | 1-50 | [ ] |
| Nicos Weg lessons | 1-5 | [ ] |
| German words in Anki | 20+ | [ ] |
| Git commits | 1+ | [ ] |
| Mornings woke at 5 AM | 4/4 | [ ] |
