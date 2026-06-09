# JUNE WEEK 2 (Jun 16–22) — Phase 1 Week 2: FUNCTIONS DEEP + ARRAYS + STRINGS

> **Topics**: Multi-param functions, recursion, scope, 1D/2D arrays, strings from scratch, multi-file compilation, binary search
> **K.N. King Reading**: Ch 8–10 (pre-gym + bed — read these all week)
> **K&R Bed Reading**: Chapter 2 (Types, Operators, Expressions) + Chapter 3 (Control Flow)
> **AI Policy**: BANNED for code — AI may only explain concepts
> **Dates**: Tuesday June 16 → Monday June 22, 2026

---

## WEEKDAY READING SCHEDULE (Jun 16–20)

### Tuesday June 16 — Pre-Gym (5:00–5:25 AM)
**Read**: K.N. King Chapter 8 (Arrays)
- 1D array declaration, initialization, traversal
- Passing arrays to functions (arrays decay to pointers)
- Common mistakes: off-by-one, writing past the end

**Bed Reading (9:30–10:00 PM)**: K&R Chapter 2 pages 35–55

### Wednesday June 17 — Pre-Gym (5:00–5:25 AM)
**Read**: K.N. King Chapter 9 (Functions)
- Function prototypes and why they matter
- Call by value (C default) — everything is copied
- Variable scope: local vs global, why global is usually wrong
- Storage classes: auto, static, extern

**Bed Reading**: K&R Chapter 2 pages 55–70

### Thursday June 18 — Pre-Gym (5:00–5:25 AM)
**Read**: K.N. King Chapter 13 (Strings — first 15 pages)
- Strings as char arrays: null terminator `\0`
- String literals vs char arrays
- Why `str1 = str2` does NOT copy a string
- Library functions: strlen, strcpy, strcmp, strcat overview

**Bed Reading**: K&R Chapter 3 (Control Flow) pages 55–75

### Friday June 19 — Pre-Gym (5:00–5:25 AM)
**Read**: K.N. King Chapter 13 (Strings — remaining pages)
- scanf %s vs fgets — why scanf is dangerous for strings
- String traversal with pointers
- Null terminator edge cases

**Bed Reading**: K.N. King Chapter 10 (Program Organization) — preview for multi-file

### Monday June 22 — Pre-Gym (5:00–5:25 AM)
**Read**: K.N. King Chapter 10 (Program Organization)
- Header files (.h): declarations, include guards, #ifndef
- Separating .c files: what goes in .h vs .c
- extern keyword and global variables across files
- How the compiler + linker work together (conceptual)

**Bed Reading**: K&R Chapter 4 (Functions and Program Structure) pages 67–88

---

## SATURDAY JUNE 20 — STRINGS + MULTI-FILE (7:30 AM–6:30 PM)

### Warmup (7:30–8:00 AM): Watch Neso Academy Videos
- "Strings in C" — Introduction (~10 min at 1.5×)
- "String functions" — strlen, strcmp overview (~8 min at 1.5×)

### BLOCK 1 (8:00–9:30 AM): String Functions From Scratch
Write ALL functions from scratch. Do NOT use `<string.h>` functions. NO AI code.

```
week2/
├── my_strings.h     — Declarations for all your string functions
└── my_strings.c     — Implementations
```

Implement these 6 functions:
```c
int    my_strlen(const char *s);              // Count chars before '\0'
int    my_strcmp(const char *s1, const char *s2);  // Lexicographic compare
char  *my_strcpy(char *dest, const char *src); // Copy including '\0'
char  *my_strcat(char *dest, const char *src); // Append src to dest
char  *my_strrev(char *s);                    // Reverse string in place
int    my_strcount(const char *s, char c);    // Count occurrences of char c
```

Rules for each:
- `my_strlen`: loop until `*s == '\0'`, count iterations
- `my_strcmp`: return negative/zero/positive (match C standard exactly)
- `my_strcpy`: copy byte by byte including `'\0'`, return dest
- `my_strcat`: find end of dest first (don't call my_strlen), then copy
- `my_strrev`: use two-pointer technique (swap from ends, move inward)
- `my_strcount`: loop entire string, increment counter on match

Test file `week2/test_strings.c`:
```c
#include <stdio.h>
#include <string.h>   // for comparison only
#include "my_strings.h"

int main(void) {
    char s1[50] = "hello";
    char s2[50] = "world";

    printf("my_strlen(\"hello\") = %d (expected 5)\n", my_strlen(s1));
    printf("strlen(\"hello\")    = %lu\n", strlen(s1));

    printf("my_strcmp(\"hello\",\"hello\") = %d (expected 0)\n", my_strcmp(s1, s1));
    printf("my_strcmp(\"hello\",\"world\") = %d (expected <0)\n", my_strcmp(s1, s2));

    char buf[100] = "foo";
    my_strcat(buf, "bar");
    printf("my_strcat: \"%s\" (expected \"foobar\")\n", buf);

    char rev[50] = "abcde";
    my_strrev(rev);
    printf("my_strrev(\"abcde\") = \"%s\" (expected \"edcba\")\n", rev);

    printf("my_strcount(\"hello\", 'l') = %d (expected 2)\n", my_strcount(s1, 'l'));
    return 0;
}
```

Compile with: `gcc -Wall -Wextra -g -std=c99 my_strings.c test_strings.c -o test_strings`
ZERO warnings. Fix every warning before moving on.

### BREAK (9:30–9:45)

### BLOCK 2 (9:45–11:15 AM): 2D Arrays + String Arrays
```
week2/
├── arrays_2d.c      — 3×3 matrix: fill, print, transpose, row/col sums
├── word_list.c      — Array of strings: sort alphabetically, search by name
└── grade_book.c     — 5 students × 4 subjects: calculate avg per student + per subject
```

**arrays_2d.c** requirements:
- Hard-code a 3×3 matrix with your own values
- Print it formatted (right-aligned columns)
- Print the transpose (rows become columns)
- Print sum of each row and each column

**word_list.c** requirements:
- `char words[10][20]` — array of up to 10 words, each max 19 chars
- Read N words from user (fgets for each)
- Bubble sort the words using my_strcmp (DO NOT use strcmp from string.h)
- Linear search: ask user for a word, print "found at index X" or "not found"

**grade_book.c** requirements:
- 5 student names + 4 subject grades (hard-coded is fine)
- Print formatted table: names left-aligned, grades right-aligned
- Calculate and print: average for each student + average for each subject
- Print the student with the highest overall average

### BREAK (11:15–11:30)

### BLOCK 3 (11:30 AM–12:30 PM): Multi-File Calculator Project
Build a calculator where the logic lives in a separate file:

```
week2/
├── calc.h          — Declarations ONLY (no code): add, sub, mul, div_safe, power, is_prime
├── calc.c          — All implementations
└── calc_main.c     — main(): menu loop, reads user input, calls calc functions
```

**calc.h** must have:
- Include guard (`#ifndef CALC_H` / `#define CALC_H` / `#endif`)
- Function prototypes only — no implementations
- No global variables

**calc.c** rules:
- `div_safe(a, b)` returns 0 and prints error if b == 0, otherwise returns a/b
- `power(base, exp)` uses iteration (not recursion), handles exp == 0
- `is_prime(n)` returns 1 if prime, 0 if not — handle n <= 1 edge case

**calc_main.c** menu:
```
1. Add    2. Subtract    3. Multiply    4. Divide    5. Power    6. Is Prime    0. Quit
```
- Do-while loop until user enters 0
- Call the matching function from calc.c for each choice

Compile: `gcc -Wall -Wextra -g -std=c99 calc.c calc_main.c -o calculator`

### LUNCH (12:30–1:30 PM)

### GERMAN BLOCK 1 (1:30–4:30 PM)
- Nicos Weg Lessons 10–12 (DW online or app)
- Introduce yourself in German: Ich heiße ___. Ich komme aus Indien. Ich arbeite als Ingenieur.
- Learn numbers 1–20, days of the week, months
- Write 10 new sentences in German (full sentences, not just words)
- Anki: add 15 new cards from today's vocabulary

### GERMAN BLOCK 2 (5:00–6:30 PM)
- Nicos Weg Lessons 13–14
- AnkiDroid: review ALL pending cards
- Write from memory: introduce yourself + describe your daily routine

---

## SUNDAY JUNE 21 — RECURSION + SORTING + GIT (7:30 AM–4:00 PM)

### BLOCK 1 (7:30–9:00 AM): Recursion
Watch: Neso Academy "Recursion in C" (~12 min) + "Towers of Hanoi" (~10 min)

```
week2/
├── recursion.c     — factorial, fibonacci, power, sum_digits, count_digits
└── hanoi.c         — Towers of Hanoi: print each move, count total moves
```

**recursion.c** requirements — implement each two ways (iterative AND recursive):
```c
long factorial_iter(int n);
long factorial_rec(int n);

long fibonacci_iter(int n);
long fibonacci_rec(int n);     // WARNING: this gets slow for n > 35

int power_iter(int base, int exp);
int power_rec(int base, int exp);

int sum_digits_rec(int n);    // 123 → 1+2+3 = 6
int count_digits_rec(int n);  // 12345 → 5
```

Print both results for n = 0..10. Verify iterative == recursive every time.

**hanoi.c** requirements:
- Solve for 3 disks: print every move ("Move disk 1 from A to C")
- Count total moves = 2^n - 1. Verify your output has the right count.
- For 3 disks: should be exactly 7 moves total

### BLOCK 2 (9:15–10:30 AM): Binary Search + Sorting Review
```
week2/
└── searching.c     — linear_search, binary_search, test both on sorted array
```

**binary_search requirements**:
- Array MUST be sorted first (use bubble sort from Week 1 to sort it)
- Return the INDEX where target is found, or -1 if not found
- Print the number of comparisons made (to demonstrate O(log n) vs O(n))
- Test: array of 100 random numbers, search for 10 different targets
- Print: "linear search: N comparisons" vs "binary search: M comparisons" for same target

### GIT PUSH (10:30–11:00 AM)
```bash
cd ~/C-Practice
git add week2/
git commit -m "Week 2: functions, strings from scratch, 2D arrays, multi-file, recursion, binary search"
git push origin main
```

Write `week2/README.md`:
- List every file in week2/
- One sentence per file: what it does and the most important thing you learned from it

### REST + LUNCH (11:00 AM–12:00 PM)

### GERMAN (12:00–2:00 PM)
- Nicos Weg Lessons 15–16
- Anki mega review (clear all pending cards — aim for 35+ words total)
- Write German from memory: your full introduction + daily schedule sentence

### EXTENDED CODING (2:00–4:00 PM): Student Record System
```
week2/
├── student.h       — Student struct + function declarations
├── student.c       — All function implementations
└── student_main.c  — main(), menu, user interaction
```

**student.h** — define the struct and declare functions:
```c
#define MAX_STUDENTS 50
#define NAME_LEN     50

typedef struct {
    char name[NAME_LEN];
    int  roll;
    float marks[5];  // 5 subjects
    float average;
} Student;

void   calc_average(Student *s);
void   print_student(const Student *s);
void   sort_by_average(Student arr[], int n);    // Descending
int    find_by_roll(const Student arr[], int n, int roll);
void   print_top_three(const Student arr[], int n);
```

**student.c** — implement all functions. No AI.

**student_main.c** — menu-driven:
```
1. Add student    2. Print all    3. Find by roll    4. Top 3 students    0. Exit
```

- Hard-code 5 students with names, rolls, and marks to test with
- calc_average must be called before any print that shows average
- sort_by_average should sort DESCENDING (best average first)
- find_by_roll: if not found, print "Roll number not found"

**IMPORTANT**: Can you write `my_strlen` from memory at the end of the day without looking? Try. If not, write it from scratch until you can.

---

## WEEK 2 CHECKPOINT (Sunday June 22, 4:00 PM)

Update PROGRESS.md now. Be honest.

| Checkpoint Item | Done? |
|:---|:---|
| my_strlen, my_strcmp, my_strcpy written from scratch | |
| Multi-file calculator (calc.h + calc.c + main.c) compiling cleanly | |
| 2D arrays: matrix transpose + row/col sums working | |
| Word list sorted with my_strcmp | |
| Recursion: factorial + fibonacci both ways (iterative + recursive) | |
| Towers of Hanoi 3-disk printed correctly (7 moves) | |
| Binary search working + comparison count printed | |
| Student record system: sort by average, find by roll | |
| GitHub: week2 pushed with README | |
| Nicos Weg: lessons 10–16 done | |
| Anki: 35+ German words | |
| K.N. King Ch 8–10 read | |

**Self-rating (functions + strings 1–10)**: ___ (minimum 6 before Week 3 — pointers)

> Week 3 is POINTERS — the hardest week of Phase 1.
> If you rate yourself below 6 here, spend extra time this week before moving on.
> You cannot understand pointers without understanding how arrays and functions work.

---

## WEEKDAY THEORY FOCUS (Week 2)

| Day | Read Before Gym | Bed Read |
|:---|:---|:---|
| Tue Jun 16 | K.N. King Ch 8 (Arrays) | K&R pp. 35–55 |
| Wed Jun 17 | K.N. King Ch 9 (Functions) | K&R pp. 55–70 |
| Thu Jun 18 | K.N. King Ch 13 first half (Strings) | K&R Ch 3 pp. 55–75 |
| Fri Jun 19 | K.N. King Ch 13 second half | K.N. King Ch 10 preview |
| Mon Jun 22 | K.N. King Ch 10 (Program Organization) | K&R Ch 4 pp. 67–88 |

> The coding block this week is Saturday + Sunday. Monday is reading-only.
> By Saturday, you will have read about arrays, functions, and strings. Your implementations will be faster.
> After this week, pointers will click faster because you will have seen arrays decay to pointers in functions.
