# 📅 WEEK 2 — May 5-11 (Tue-Mon): FUNCTIONS DEEP + ARRAYS + STRINGS

> **Topics**: Multi-file programs, arrays (1D, 2D), sorting algorithms, string manipulation, C standard library
> **K&R Chapters**: Chapter 2 (finish), Chapter 3 (Control Flow), Chapter 4 (Functions and Program Structure) start
> **Programs to write**: 10-12
> **German**: Nicos Weg Lessons 6-10, 15 more words, numbers 1-100

---

## DAY 5 — Tuesday, May 5

### 🔶 Morning (5:10-6:30 AM) — Arrays Introduction

**What to learn**: What arrays are, how they're stored in memory, indexing, iterating, basic operations.

**How to learn**:
1. **(5:10-5:20)** Watch **Jacob Sorber: "Arrays in C"** (~7 min). Pay attention to how he explains memory layout.
2. **(5:20-5:50)** Write `arrays.c` in `week2/` folder:
   - Declare an array of 5 exam marks
   - Print all elements using a for loop
   - Calculate sum and average
   - Find maximum and minimum
   - Print in reverse order
   - **What to understand**: Array indexing starts at 0, NOT 1. `marks[5]` with 5 elements → valid indices are 0,1,2,3,4. `marks[5]` is a BUG (buffer overflow — the #1 embedded software vulnerability).
   - **Ask Google AI**: "What is a buffer overflow in C? Why is it the most dangerous bug in embedded systems? Give me a simple example."

3. **(5:50-6:20)** Write `array_operations.c`:
   - Read N numbers from user into an array (where N is also input)
   - Count how many are positive, negative, zero
   - Find second largest element
   - Check if array is sorted
   - **Key C concept**: `int arr[n];` — this is a Variable Length Array (VLA). Some compilers don't support it. K&R doesn't cover VLAs. Use `#define MAX 100` instead for safety.

4. **(6:20-6:30)** Quick review: Can you explain to yourself what an array is, how it's stored, and why index starts at 0? If not, re-read K&R.

### 🎧 Commute: Nicos Weg Lesson 6 (numbers: eins, zwei, drei...) | 📱 Lunch: Anki | 📖 Bed: K&R Ch2 (pp. 36-50, Types and Operators)

### ✅ Day 5: `arrays.c` + `array_operations.c`. Understand buffer overflow concept.

---

## DAY 6 — Wednesday, May 6

### 🔶 Morning (5:10-6:30 AM) — Sorting: Bubble Sort

**What to learn**: How to sort an array. Why sorting matters. How to think about algorithms.

**How to learn**:
1. **(5:10-5:20)** DO NOT watch a tutorial yet. Try this FIRST:
   - Think about how YOU would sort 5 playing cards in your hand
   - Write down the steps in English on paper
   - Now try to translate that to C code

2. **(5:20-5:50)** Write `bubble_sort.c`:
   - The algorithm: compare adjacent elements, swap if out of order, repeat
   - Pass an array to a function `void bubble_sort(int arr[], int n)`
   - Print array before and after sorting
   - **What to understand**:
     - Why does `void bubble_sort(int arr[], int n)` work? Because arrays in C are automatically passed by reference (actually, by pointer — you'll understand this in Week 3)
     - What is the time complexity? O(n²) — slow. But simple. Good for small embedded datasets.

3. **(5:50-6:20)** If stuck, THEN watch **Jacob Sorber: "Bubble Sort"** or read **Beej's Guide** section on sorting
   - After watching: CLOSE the video. Write it again from memory. If you can't, you didn't understand it.

4. **(6:20-6:30)** Test with edge cases: already sorted array, reverse sorted, all same numbers, single element, empty array.

### 🎧 Commute: Nicos Weg Lesson 7 | 📱 Lunch: Anki (add "der Morgen", "der Abend", "die Nacht") | 📖 Bed: K&R Ch3 (Control Flow, pp. 55-65)

### ✅ Day 6: `bubble_sort.c` with edge cases tested.

---

## DAY 7 — Thursday, May 7

### 🔶 Morning (5:10-6:30 AM) — Strings (char arrays)

**What to learn**: Strings in C are NOT a special type — they're just `char` arrays ending with `\0`. This is unique to C and CRITICAL for embedded.

**How to learn**:
1. **(5:10-5:20)** Read **K&R section 1.9** (Character Arrays, pp. 28-32). This is one of the most important sections in the entire book. Read it slowly.

2. **(5:20-5:45)** Write `strings_basic.c`:
   - Declare: `char name[] = "Khashyap";` — understand that this is actually `{'K','h','a','s','h','y','a','p','\0'}` (9 bytes, not 8!)
   - Print character by character with a loop: `while (name[i] != '\0')`
   - Print using `%s`: `printf("%s\n", name);`
   - **What to understand**: The null terminator `\0`. Without it, `printf` keeps reading memory forever until it finds a random `\0`. This causes GARBAGE OUTPUT — the classic embedded C bug.

3. **(5:45-6:15)** Write `my_strlen.c`:
   - Write YOUR OWN `strlen` function — DO NOT use `#include <string.h>`
   - Logic: count characters until you hit `\0`
   - Compare your result with `strlen()` from `<string.h>` to verify
   - **Why this matters**: In embedded, you often DON'T have the standard library. You write everything yourself.

4. **(6:15-6:30)** Write `my_reverse.c`:
   - Write YOUR OWN string reverse function
   - Use two-pointer approach: swap first and last, move inward
   - **Drawing exercise**: Draw the string on paper. Draw arrows showing swaps. This builds the pointer intuition for Week 3.

### 🎧 German commute: Nicos Weg Lesson 8 + review lessons 1-7 | 📱 Lunch: Anki | 📖 Bed: K&R pp. 32-40

### ✅ Day 7: `strings_basic.c` + `my_strlen.c` + `my_reverse.c`. Understand the null terminator.

---

## DAY 8 — Friday, May 8

### 🔶 Morning (5:10-6:30 AM) — More String Functions + String Library

**What to learn**: Writing your own string functions, then learning the standard library equivalents.

**How to learn**:
1. **(5:10-5:35)** Write `my_strcmp.c`:
   - YOUR OWN string comparison function
   - Compare two strings character by character
   - Return 0 if equal, negative if first is "less", positive if first is "greater"
   - Use this to build a password checker: `if (my_strcmp(input, "germany2028") == 0)`

2. **(5:35-6:00)** Write `my_strcpy.c`:
   - YOUR OWN string copy function
   - Copy source string into destination character by character including `\0`
   - **DANGEROUS BUG TO DISCOVER**: What if destination is too small? Buffer overflow! This is the bug that caused the Morris Worm (1988).

3. **(6:00-6:20)** Write `string_library.c`:
   - Now #include `<string.h>` and use: `strlen()`, `strcmp()`, `strcpy()`, `strcat()`, `strncpy()` (safe version)
   - Compare YOUR functions' output with library functions
   - **Lesson**: In production embedded code, use `strncpy` (with length limit), NEVER `strcpy` (no length check).

4. **(6:20-6:30)** Write `safe_input.c`:
   - Learn `fgets()` (safe) vs `gets()` (BANNED since C11 — buffer overflow)
   - Read a full line including spaces: `fgets(buffer, sizeof(buffer), stdin);`

### 🎧 Commute: Nicos Weg Lesson 9 | 📱 Lunch: Anki | 📖 Bed: K&R Chapter 4 start (pp. 67-75, Functions)

### ✅ Day 8: `my_strcmp.c` + `my_strcpy.c` + `string_library.c` + `safe_input.c`. Understand buffer overflow.

---

## DAY 9 — Saturday, May 9 🟩 BIG DAY

### 💻 Warmup (6:30-7:30 AM) — 2D Arrays + Multi-dimensional Data

**What to learn**: Matrices (2D arrays), how they're stored in memory (row-major), nested loops for traversal.

**How to learn**:
1. **(6:30-6:35)** Read **K&R section on multi-dimensional arrays** (pp. 112-115)

2. **(6:35-7:05)** Write `matrix.c`:
   - Declare a 3×3 matrix, initialize with values
   - Print in matrix format (with aligned columns using `%3d`)
   - Calculate diagonal sum
   - Print transpose
   - **What to understand**: `int m[3][3]` — in memory this is 9 consecutive integers. `m[i][j]` = element at position `(i * 3 + j)`. This flat storage is how images/sensors data works in embedded.

3. **(7:10-7:30)** Write `matrix_multiply.c`:
   - Multiply two 3×3 matrices
   - Three nested loops: row of A × column of B
   - This is hard. If stuck after 15 min trying, watch a 5-min explanation, then CLOSE it and write from understanding.

4. **(7:30-7:45)** Write `string_array.c`:
   - Declare an array of strings: `char names[][20] = {"Bosch", "Continental", "Infineon", "Qualcomm"};`
   - Print all names. Sort them alphabetically using bubble sort + `strcmp()`.

> **Note**: This is Saturday — continue into Deep Sessions (7:45 AM onward) for more array and string exercises. Follow the Saturday template from the overview. German 2:00-5:00 PM.

### 📖 Evening: K&R pp. 75-85

### ✅ Day 9: `matrix.c` + `matrix_multiply.c` + `string_array.c`.

---

## DAY 10 — Sunday, May 10 🟨 REVIEW

### 💻 Warmup (7:30-8:30 AM) — Function Mastery

**What to learn**: Scope rules, static variables, multi-file programs, header files.

**How to learn**:
1. Watch **Jacob Sorber: "Scope in C"** (~6 min) and **"Static keyword"** (~5 min)
2. Write `scope.c`:
   - Global vs local variables
   - `static` variable inside a function — what happens across multiple calls?
   - **Ask Google AI**: "What does `static` mean in 3 different contexts in C: static variable in function, static global variable, static function?"

### 💻 Deep Session 1 (8:45-10:15) — Multi-file Programs

**What to learn**: How professional C projects are organized — separate `.c` files for each module, `.h` files for interfaces.

**How to learn**:
1. Read **K&R Chapter 4, section on external variables and scope** (pp. 80-85)
2. Create a multi-file program:
   - `math_utils.h` — function prototypes (declarations)
   - `math_utils.c` — function implementations
   - `main.c` — calls the functions
   - Compile: `gcc main.c math_utils.c -o main -Wall`
   - **What to understand**: Why `.h` files exist (to share function prototypes). What `#include` guards are: `#ifndef MATH_UTILS_H` / `#define MATH_UTILS_H` / `#endif`
   - **THIS IS HOW ALL PROFESSIONAL EMBEDDED CODE IS STRUCTURED.** Every STM32 project has dozens of `.c` and `.h` file pairs.

### 💻 Deep Session 2 (10:30-12:00) — Deeper Array Exercises

Write `search.c`:
- Linear search: scan every element. O(n). Simple but slow.
- Binary search: only works on sorted array. O(log n). Fast.
- **Think about this**: If your STM32 has a lookup table of 1000 sensor calibration values, binary search finds the right one in ~10 comparisons instead of ~500. That's the difference between hitting a real-time deadline or missing it.

### 💻 Deep Session 3 (12:15-12:45) — Selection Sort

Write `selection_sort.c`:
- Different algorithm from bubble sort
- Find minimum → swap with first → repeat for remaining
- Compare with bubble sort — which is faster in practice?
- **Tracker Roadmap Reference**: This maps to Week 05 "C programming foundations & syntax fluency" from your Embedded_Systems_Tracker.

### 🇩🇪 German (2:00-3:30) — Sunday German template

- Nicos Weg Lessons 9-10 (re-watch if needed)
- Write 15 sentences in notebook
- Google AI: Practice numbers 1-20 in German, then self-introduction
- Anki: mega review

### 💻 Mini-Project (3:30-5:00) — Student Records System

Write `student_records.c`:
- Store 5 students using parallel arrays: `char names[][50]`, `float cgpa[]`, `char branch[][20]`
- Menu: Add student, Display all, Search by name, Sort by CGPA, Find topper
- Uses everything from Weeks 1-2. Preview for structs in Week 4.

### 💻 Git Push (5:00-5:30) — Push `week2/`
- `git add . → git commit → git push`
- Update README with Week 2 progress

### 📋 Weekly Review (5:30-6:00)
- Notion: Log hours, programs written, what was hardest

### ✅ Day 10: `scope.c` + multi-file project + `search.c` + `selection_sort.c` + `student_records.c`. Git push. German review.

---

## DAY 11 — Monday, May 11 🟦 WEEKDAY

### 🔶 Morning (5:10-6:30 AM) — RE-TYPE FROM MEMORY

Pick 2 programs from this week. Close all references. Type from MEMORY:
- `bubble_sort.c` — can you write it without looking?
- `my_strlen.c` — can you write it without looking?

If stuck, review solution, close it, wait 5 minutes, try again.

> **Note**: Student records project and Git push are on Day 10 (Sunday). Weekday mornings are coding-only.

### 🎧 Commute: Review Nicos Weg 6-10 | 📱 Lunch: Anki | 📖 Bed: K&R Chapter 4 start

### ✅ Day 11: 2 programs from memory. Identify weak spots for Week 3.

---

## 📊 WEEK 2 SUMMARY

| Metric | Target | Done? |
|:---|:---|:---|
| Programs written | 10+ (cumulative 20+) | [ ] |
| Can write from memory | `bubble_sort`, `my_strlen`, `binary_search` | [ ] |
| K&R pages read | 35-85 | [ ] |
| Multi-file compilation | Understand `.h` + `.c` separation | [ ] |
| Nicos Weg lessons | 6-10 (cumulative: 10) | [ ] |
| German words in Anki | 35+ (cumulative) | [ ] |
| Git commits | 2+ (cumulative) | [ ] |
