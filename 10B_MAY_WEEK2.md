# 📅 WEEK 2 — May 5-11 (Tue-Mon): FUNCTIONS DEEP + ARRAYS + STRINGS

> **Topics**: Multi-file programs, arrays (1D, 2D), sorting algorithms, string manipulation, C standard library
> **K.N. King Chapters**: Ch 6-10 (Loops, Basic Types, Arrays, Functions, Program Organization)
> **K&R Bed Reading**: Chapter 2 (finish), Chapter 3 (Control Flow), Chapter 4 (Functions) start
> **FastBit Udemy**: Sections 5-8 (Operators, Decision making, Bitwise, Loops)
> **Programs to write**: 8-10 (1-2 per weekday, 3-5 on Saturday)
> **German**: Nicos Weg Lessons 6-10, 15 more words, numbers 1-100
> **📚 Full resource details**: See `10_RESOURCES.md`
>
> ⚠️ **WEDDING DISRUPTION**: Sister's wedding (May 1-13) may still be affecting schedule.
> If behind, **prioritize**: arrays → sorting → strings. Functions will carry from Week 1.

---

## DAY 5 — Tuesday, May 5

### 🔶 Morning (5:10-6:30 AM) — Arrays Deep Dive

---

#### 📺 WATCH FIRST (15 min) — 5:10 to 5:25 AM

1. **Neso Academy: "1D Arrays in C"** (~10 min)
   - Focus on: How arrays are stored in contiguous memory, index starts at 0
2. **Neso Academy: "Accessing Array Elements"** (~6 min)
   - Focus on: What happens when you access `arr[5]` in a 5-element array (undefined behavior!)

> **Alternative**: **Jacob Sorber: "Arrays in C"** (~7 min) — explains memory layout with terminal demos

---

#### 📖 READ (5 min)

- **K&R pp. 22-28** (arrays section in Chapter 1)
- Or: **Beej's Guide** → Chapter 6: "Arrays" → https://beej.us/guide/bgc/html/split/arrays.html

---

#### 💻 CODE (45 min) — 5:25 to 6:10 AM

**Program 1 — `arrays.c`** in `week2/` folder (continue from Day 4 if incomplete, or redo for mastery):
- Declare an array of 5 exam marks
- Print all elements using a for loop
- Calculate sum and average
- Find maximum and minimum
- Print in reverse order
- **What to understand**: Array indexing starts at 0, NOT 1. `marks[5]` with 5 elements → valid indices are 0,1,2,3,4. `marks[5]` is a BUG (buffer overflow — the #1 embedded software vulnerability).
- **Ask Google AI**: "What is a buffer overflow in C? Why is it the most dangerous bug in embedded systems? Give me a simple example."

**Program 2 — `array_operations.c`:**
- Read N numbers from user into an array (where N is also input)
- Count how many are positive, negative, zero
- Find second largest element
- Check if array is sorted
- **Key C concept**: `int arr[n];` — this is a Variable Length Array (VLA). Some compilers don't support it. K&R doesn't cover VLAs. Use `#define MAX 100` instead for safety.

---

#### 🧪 TEST YOURSELF (during lunch or evening)

- **learn-c.org**: "Arrays" → https://www.learn-c.org/en/Arrays
- **HackerRank**: "1D Arrays in C" → https://www.hackerrank.com/challenges/1d-arrays-in-c
- **HackerRank**: "Array Reversal" → https://www.hackerrank.com/challenges/reverse-array-c

---

### 🎧 Commute: Nicos Weg Lesson 6 (numbers: eins, zwei, drei...) | 📱 Lunch: Anki | 📖 Bed: K&R Ch2 (pp. 36-50, Types and Operators)

### ✅ Day 5: `arrays.c` + `array_operations.c`. Understand buffer overflow concept.

---

## DAY 6 — Wednesday, May 6

### 🔶 Morning (5:10-6:30 AM) — 🇩🇪 German + Sorting: Bubble Sort

---

#### 📺 GERMAN (20 min) — 5:10 to 5:30 AM

- **DW Nicos Weg app**: Lesson 7 (watch video, do exercises, repeat phrases)
- **Learn German with Anja** (YouTube): Search "German Numbers 1-100" (~12 min)
  - Write numbers 1-20 in your notebook: eins, zwei, drei, vier, fünf, sechs, sieben, acht, neun, zehn, elf, zwölf...

---

#### 📺 WATCH for Sorting (10 min) — 5:30 to 5:40 AM

- **Neso Academy: "Bubble Sort in C"** (~10 min)
  - Focus on: Adjacent element comparison, swapping, multiple passes
  - Pay attention to the optimization: if no swaps in a pass → array is sorted, stop early

> **IMPORTANT**: Before watching, try to figure it out yourself for 5 minutes. Think: "How would I sort 5 playing cards in my hand?" Write the steps in English on paper.

---

#### 💻 CODE (45 min) — 5:40 to 6:25 AM

**Program 3 — `bubble_sort.c`:**
- The algorithm: compare adjacent elements, swap if out of order, repeat
- Pass an array to a function `void bubble_sort(int arr[], int n)`
- Print array before and after sorting
- **What to understand**:
  - Why does `void bubble_sort(int arr[], int n)` work? Because arrays in C are automatically passed by reference (actually, by pointer — you'll understand this in Week 3)
  - What is the time complexity? O(n²) — slow. But simple. Good for small embedded datasets.

**After writing**: Close the video. Close all references. Try writing it again from memory. If you can't → you didn't understand it, re-watch.

**Test with edge cases**: already sorted array, reverse sorted, all same numbers, single element.

---

#### 🧪 TEST YOURSELF

- **Programiz**: "Bubble Sort Algorithm" → https://www.programiz.com/dsa/bubble-sort (check your understanding against their explanation)
- **Exercism**: `resistor-color` exercise → https://exercism.org/tracks/c/exercises/resistor-color

---

### 🎧 Commute: Nicos Weg Lesson 7 | 📱 Lunch: Anki (add "der Morgen", "der Abend", "die Nacht") | 📖 Bed: K&R Ch3 (Control Flow, pp. 55-65)

### ✅ Day 6: `bubble_sort.c` with edge cases tested. German numbers started.

---

## DAY 7 — Thursday, May 7

### 🔶 Morning (5:10-6:30 AM) — Strings (char arrays)

---

#### 📺 WATCH FIRST (15 min) — 5:10 to 5:25 AM

1. **Neso Academy: "Strings in C"** (~10 min)
   - Focus on: Strings are just char arrays with `\0` at the end. NOT a special type.
2. **Neso Academy: "String Input/Output (gets, puts, fgets)"** (~8 min)
   - Focus on: Why `gets()` is BANNED (buffer overflow). Use `fgets()` instead.

> **Deeper understanding**: Read **K&R section 1.9** (Character Arrays, pp. 28-32). This is one of the most important sections in the entire book. Read it SLOWLY.

---

#### 📖 READ (5 min)

- **Beej's Guide** → Chapter 4: "Strings" → https://beej.us/guide/bgc/html/split/strings.html

---

#### 💻 CODE (45 min) — 5:25 to 6:10 AM

**Program 4 — `strings_basic.c`:**
- Declare: `char name[] = "Khashyap";` — understand that this is actually `{'K','h','a','s','h','y','a','p','\0'}` (9 bytes, not 8!)
- Print character by character with a loop: `while (name[i] != '\0')`
- Print using `%s`: `printf("%s\n", name);`
- **What to understand**: The null terminator `\0`. Without it, `printf` keeps reading memory forever until it finds a random `\0`. This causes GARBAGE OUTPUT — the classic embedded C bug.

**Program 5 — `my_strlen.c`:**
- Write YOUR OWN `strlen` function — DO NOT use `#include <string.h>`
- Logic: count characters until you hit `\0`
- Compare your result with `strlen()` from `<string.h>` to verify
- **Why this matters**: In embedded, you often DON'T have the standard library. You write everything yourself.

**Program 6 — `my_reverse.c`:**
- Write YOUR OWN string reverse function
- Use two-pointer approach: swap first and last, move inward
- **Drawing exercise**: Draw the string on paper. Draw arrows showing swaps. This builds the pointer intuition for Week 3.

---

#### 🧪 TEST YOURSELF

- **learn-c.org**: "Strings" → https://www.learn-c.org/en/Strings
- **HackerRank**: "Printing Tokens" → https://www.hackerrank.com/challenges/printing-tokens-
- **Exercism**: `isogram` exercise → https://exercism.org/tracks/c/exercises/isogram

---

### 🎧 German commute: Nicos Weg Lesson 8 + review lessons 1-7 | 📱 Lunch: Anki | 📖 Bed: K&R pp. 32-40

### ✅ Day 7: `strings_basic.c` + `my_strlen.c` + `my_reverse.c`. Understand the null terminator.

---

## DAY 8 — Friday, May 8

### 🔶 Morning (5:10-6:30 AM) — 🇩🇪 German + More String Functions

---

#### 📺 GERMAN (20 min) — 5:10 to 5:30 AM

- **DW Nicos Weg app**: Lesson 9
- Review numbers 1-20 out loud. Can you count without hesitation?

---

#### 📺 WATCH for Strings (10 min) — 5:30 to 5:40 AM

- **Neso Academy: "String Functions in C (strlen, strcmp, strcpy, strcat)"** (~12 min)
  - Focus on: How each function works internally (you'll write your own versions)

---

#### 💻 CODE (45 min) — 5:40 to 6:25 AM

**Program 7 — `my_strcmp.c`:**
- YOUR OWN string comparison function
- Compare two strings character by character
- Return 0 if equal, negative if first is "less", positive if first is "greater"
- Use this to build a password checker: `if (my_strcmp(input, "germany2028") == 0)`

**Program 8 — `my_strcpy.c`:**
- YOUR OWN string copy function
- Copy source string into destination character by character including `\0`
- **DANGEROUS BUG TO DISCOVER**: What if destination is too small? Buffer overflow! This is the bug that caused the Morris Worm (1988).

**Program 9 — `string_library.c`:**
- Now `#include <string.h>` and use: `strlen()`, `strcmp()`, `strcpy()`, `strcat()`, `strncpy()` (safe version)
- Compare YOUR functions' output with library functions
- **Lesson**: In production embedded code, use `strncpy` (with length limit), NEVER `strcpy` (no length check).

---

#### 🧪 TEST YOURSELF

- **HackerRank**: "Digit Frequency" → https://www.hackerrank.com/challenges/frequency-of-each-digit-in-the-string
- **Exercism**: `hamming` exercise → https://exercism.org/tracks/c/exercises/hamming

---

### 🎧 Commute: Nicos Weg Lesson 9 | 📱 Lunch: Anki | 📖 Bed: K&R Chapter 4 start (pp. 67-75, Functions)

### ✅ Day 8: `my_strcmp.c` + `my_strcpy.c` + `string_library.c`. Understand buffer overflow.

---

## DAY 9 — Saturday, May 9 🟩 BIG DAY

### 💻 Warmup (6:30-7:30 AM) — 2D Arrays + Multi-dimensional Data

---

#### 📺 WATCH FIRST (15 min) — 6:30 to 6:45 AM

1. **Neso Academy: "2D Arrays in C"** (~10 min)
   - Focus on: Row-major storage, how `m[i][j]` maps to flat memory
2. **Neso Academy: "Passing 2D Arrays to Functions"** (~8 min)

---

#### 📖 READ — K&R section on multi-dimensional arrays (pp. 112-115)

---

#### 💻 CODE (45 min) — 6:45 to 7:30 AM

**Program 10 — `matrix.c`:**
- Declare a 3×3 matrix, initialize with values
- Print in matrix format (with aligned columns using `%3d`)
- Calculate diagonal sum
- Print transpose
- **What to understand**: `int m[3][3]` — in memory this is 9 consecutive integers. `m[i][j]` = element at position `(i * 3 + j)`. This flat storage is how images/sensors data works in embedded.

---

### 💻 Deep Session 1 (7:45-9:15 AM) — Multi-file Programs

---

#### 📺 WATCH FIRST (15 min) — 7:45 to 8:00 AM

- **Jacob Sorber: "Splitting your C code into multiple files"** (~10 min)
  - Focus on: Why `.h` files exist, what `#include` guards do, how compilation works with multiple files
- **Neso Academy: "Header Files in C"** (~8 min)

---

#### 📖 READ — K&R Chapter 4, section on external variables and scope (pp. 80-85)

---

#### 💻 CODE (60 min) — 8:00 to 9:00 AM

Create a **multi-file program**:
- `math_utils.h` — function prototypes (declarations) with include guards
- `math_utils.c` — function implementations (add, multiply, factorial, is_prime)
- `main.c` — calls the functions
- Compile: `gcc main.c math_utils.c -o main -Wall`
- **What to understand**: Why `.h` files exist (to share function prototypes). What `#include` guards are: `#ifndef MATH_UTILS_H` / `#define MATH_UTILS_H` / `#endif`
- **THIS IS HOW ALL PROFESSIONAL EMBEDDED CODE IS STRUCTURED.** Every STM32 project has dozens of `.c` and `.h` file pairs.

---

#### 🧪 TEST YOURSELF — 9:00-9:15 AM

- **learn-c.org**: "Functions" (review) → https://www.learn-c.org/en/Functions
- Compile your multi-file project with `gcc -Wall -Wextra` — fix ALL warnings

---

### 💻 Deep Session 2 (9:30-11:00 AM) — Search Algorithms

---

#### 📺 WATCH FIRST (15 min) — 9:30 to 9:45 AM

1. **Neso Academy: "Linear Search in C"** (~8 min)
2. **Neso Academy: "Binary Search in C"** (~12 min)
   - Focus on: Why binary search needs a SORTED array. How it halves the search space each time.

---

#### 💻 CODE (60 min) — 9:45 to 10:45 AM

**Program 11 — `search.c`:**
- Linear search: scan every element. O(n). Simple but slow.
- Binary search: only works on sorted array. O(log n). Fast.
- **Think about this**: If your STM32 has a lookup table of 1000 sensor calibration values, binary search finds the right one in ~10 comparisons instead of ~500. That's the difference between hitting a real-time deadline or missing it.

---

#### 🧪 TEST YOURSELF — 10:45-11:00 AM

- **HackerRank**: "Sherlock and Array" (search-related logic) → https://www.hackerrank.com/challenges/sherlock-and-array
- **Programiz**: "Binary Search" → https://www.programiz.com/dsa/binary-search (verify your implementation)

---

### 💻 Deep Session 3 (11:15 AM-12:45 PM) — Selection Sort + String Sorting

---

#### 📺 WATCH (8 min) — 11:15 to 11:25 AM

- **Neso Academy: "Selection Sort in C"** (~8 min)
  - Focus on: How it differs from bubble sort (find minimum first, then swap once)

---

#### 💻 CODE (70 min) — 11:25 AM to 12:35 PM

**Program 12 — `selection_sort.c`:**
- Find minimum → swap with first → repeat for remaining
- Compare with bubble sort — which is faster in practice?

**Program 13 — `string_array.c`:**
- Declare an array of strings: `char names[][20] = {"Bosch", "Continental", "Infineon", "Qualcomm"};`
- Print all names. Sort them alphabetically using bubble sort + `strcmp()`.

---

### 🇩🇪 German (2:00-5:00 PM)

#### 📺 German Resources for Today

- **DW Nicos Weg** (app): Lessons 9-10 (re-watch if needed) (2:00-3:00 PM)
- **Learn German with Anja** (YouTube): Search "German A1 Self Introduction" (~10 min) (3:00-3:15 PM)
- Write 15 sentences in German in notebook (3:15-3:45 PM)
- **Google AI Pro** voice mode (3:45-5:00 PM): Practice numbers, greetings, self-introduction

---

### 💻 Mini-Project (5:00-6:30 PM) — Student Records System

**Program 14 — `student_records.c`:**
- Store 5 students using parallel arrays: `char names[][50]`, `float cgpa[]`, `char branch[][20]`
- Menu: Add student, Display all, Search by name, Sort by CGPA, Find topper
- Uses everything from Weeks 1-2. Preview for structs in Week 4.

---

### 💻 Git Push (6:30-7:00 PM)
- `git add .` → `git commit -m "Week 2: functions, arrays, strings, sorting"` → `git push`
- Update README with Week 2 progress

---

### ✅ Day 9: `matrix.c` + multi-file project + `search.c` + `selection_sort.c` + `string_array.c` + `student_records.c`. Git push.

---

## DAY 10 — Sunday, May 10 🟨 REVIEW + SCOPE + RECURSION

### 💻 Practice (7:30-9:00 AM) — Scope + Static

---

#### 📺 WATCH FIRST (15 min) — 7:30 to 7:45 AM

1. **Jacob Sorber: "Scope in C — understanding variable lifetime"** (~6 min)
2. **Jacob Sorber: "The static keyword in C"** (~5 min)
   - Focus on: 3 different meanings of `static`: in function (persists), global (file-private), function (file-private)

> **Alternative**: **Neso Academy: "Storage Classes in C"** (~15 min) — covers auto, static, extern, register

---

#### 💻 CODE (45 min) — 7:45 to 8:30 AM

**Program 15 — `scope.c`:**
- Global vs local variables — demonstrate both
- `static` variable inside a function — what happens across multiple calls?
- **Ask Google AI**: "What does `static` mean in 3 different contexts in C: static variable in function, static global variable, static function?"

---

### 💻 Recursion (9:15-10:45 AM)

---

#### 📺 WATCH FIRST (15 min) — 9:15 to 9:30 AM

1. **Neso Academy: "Recursion in C (Part 1)"** (~12 min)
   - Focus on: Base case, recursive case, how the call stack grows
2. **Neso Academy: "Recursion in C (Part 2)"** (~10 min)
   - Focus on: Stack overflow risk if no base case

---

#### 💻 CODE (60 min) — 9:30 to 10:30 AM

**Program 16 — `recursion.c`:**
- Factorial (recursive)
- Fibonacci (recursive) — note: terribly slow for large N. Why? (overlapping subproblems)
- Power function: `int power(int base, int exp)` — recursive
- Reverse a string recursively

---

#### 🧪 TEST YOURSELF — 10:30-10:45 AM

- **HackerRank**: search for "Recursion" challenges in C domain
- **learn-c.org**: "Recursion" → https://www.learn-c.org/en/Recursion

---

### 💻 RE-TYPE FROM MEMORY (11:00-12:30 PM)

Close ALL references. Type from MEMORY:
- `bubble_sort.c` — can you write it without looking?
- `my_strlen.c` — can you write it without looking?
- `binary_search` function — can you write it without looking?

If stuck, review solution, close it, wait 5 minutes, try again.

### 🇩🇪 German (2:00-4:00 PM)
- Anki mega review — clear ALL pending cards
- Write 15 sentences from memory in notebook
- Use **dict.cc** to check correctness

### 📋 Weekly Review (4:00-4:30 PM)
- **PROGRESS.md**: Log hours, programs, what was hardest. Update the Week 2 row.
- Plan adjustments for Week 3 (Pointers — the hardest week)

---

### ✅ Day 10: `scope.c` + `recursion.c` + memory re-write test. German review. Weekly review.

---

## DAY 11 — Monday, May 11 🟦 WEEKDAY

### 🔶 Morning (5:10-6:30 AM) — Consolidation + Safe Input

---

#### 📺 WATCH (10 min) — 5:10 to 5:20 AM

- **Neso Academy: "fgets() vs gets() in C"** (~8 min)
  - Focus on: Why `gets()` was REMOVED from C11 (buffer overflow). Always use `fgets()`.

---

#### 💻 CODE (60 min) — 5:20 to 6:20 AM

**Program 17 — `safe_input.c`:**
- Learn `fgets()` (safe) vs `gets()` (BANNED since C11 — buffer overflow)
- Read a full line including spaces: `fgets(buffer, sizeof(buffer), stdin);`
- Remove the trailing newline that `fgets` adds

**Consolidation**: Pick 2 more programs from this week. Close all references. Rewrite from MEMORY.

---

#### 🧪 PREPARE FOR WEEK 3

- Go to **YouTube** → search **"mycodeschool Pointers in C"** → bookmark the playlist
  - URL: https://www.youtube.com/playlist?list=PL2_aWCzGMAwLZp6LMUKI3cc7pgGsasm2_
  - You will watch ALL 15 videos next week
- **This is THE most important playlist you will watch in May.**

---

### 🎧 Commute: Review Nicos Weg 6-10 | 📱 Lunch: Anki | 📖 Bed: K&R Chapter 5 preview (pp. 93-98, Pointers introduction)

### ✅ Day 11: `safe_input.c` + 2 programs from memory. Bookmark mycodeschool pointers playlist.

---

## 📊 WEEK 2 SUMMARY

| Metric | Target | Done? |
|:---|:---|:---|
| Programs written | 10+ (cumulative 20+) | [ ] |
| Can write from memory | `bubble_sort`, `my_strlen`, `binary_search` | [ ] |
| K&R pages read | 35-85 | [ ] |
| Neso Academy videos watched | 12-15 | [ ] |
| HackerRank/learn-c.org/Exercism exercises | 5+ | [ ] |
| Multi-file compilation | Understand `.h` + `.c` separation | [ ] |
| Nicos Weg lessons | 6-10 (cumulative: 10) | [ ] |
| German words in Anki | 35+ (cumulative) | [ ] |
| Git commits | 2+ (cumulative) | [ ] |
| mycodeschool pointers playlist bookmarked | ✅ | [ ] |
