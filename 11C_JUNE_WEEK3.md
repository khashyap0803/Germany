# JUNE WEEK 3 (Jun 23–29) — Phase 1 Week 3: POINTERS

> **Topics**: Address-of & dereference, pointer arithmetic, arrays-as-pointers, swap by pointer, double pointers, dynamic memory, malloc/free, Valgrind, function pointers
> **K.N. King Reading**: Ch 11–12 (Pointers, Dynamic Storage Allocation) — read all week
> **K&R Bed Reading**: Chapter 5 (Pointers and Arrays) — the most important chapter in K&R
> **mycodeschool Playlist**: "Pointers in C/C++" — 15 videos — watch on Saturday morning (1.5×)
> **AI Policy**: BANNED for code — AI may only explain concepts
> **Dates**: Tuesday June 23 → Monday June 29, 2026
> **WARNING**: This is the hardest week of Phase 1. Set aside more time if needed. Do NOT rush this.

---

## WEEKDAY READING SCHEDULE (Jun 23–27)

### Tuesday June 23 — Pre-Gym (5:00–5:25 AM)
**Read**: K.N. King Chapter 11 (Pointers — pages 1–20)
- What is a pointer: a variable that holds a memory address
- Address-of operator `&`: gives you the address of a variable
- Dereference operator `*`: gives you the value at that address
- Pointer declarations: `int *p;` — p is "pointer to int"
- NULL pointer: what it means, why you must check before dereferencing

**Bed Reading (9:30–10:00 PM)**: K&R Chapter 5 pages 93–110 (Pointers and Addresses, Pointers and Function Arguments)

### Wednesday June 24 — Pre-Gym (5:00–5:25 AM)
**Read**: K.N. King Chapter 11 (Pointers — pages 20–40)
- Pointer arithmetic: p+1 advances by `sizeof(*p)` bytes (NOT by 1 byte)
- Comparing pointers: only meaningful when pointing into the same array
- Pointers and arrays: array name is a constant pointer to element 0
- `arr[i]` and `*(arr + i)` are IDENTICAL — understand why

**Bed Reading**: K&R Chapter 5 pages 110–125 (Pointers and Arrays, Address Arithmetic)

### Thursday June 25 — Pre-Gym (5:00–5:25 AM)
**Read**: K.N. King Chapter 11 (Pointers — pages 40–end)
- Passing arrays to functions: array decays to pointer → function can modify original
- Why `swap(a, b)` doesn't work — call by VALUE makes a copy
- Why `swap(&a, &b)` works — function receives addresses, modifies originals
- Pointers to pointers: `int **pp` — pointer to a pointer to int

**Bed Reading**: K&R Chapter 5 pages 125–140 (Character Pointers, Pointer Arrays)

### Friday June 26 — Pre-Gym (5:00–5:25 AM)
**Read**: K.N. King Chapter 12 (Dynamic Storage Allocation)
- Heap vs stack: what lives where, who manages what
- `malloc(n)`: allocates n bytes, returns `void *` or NULL on failure
- ALWAYS check malloc return for NULL before using
- `free(ptr)`: returns memory to heap — MUST be called on every malloc
- `calloc(n, size)`: malloc + zeroes memory
- Memory leaks: allocated but never freed — program slowly consumes RAM

**Bed Reading**: K&R Chapter 5 pages 140–167 (Multi-dimensional arrays, Command-line args, Pointers to Functions)

### Monday June 29 — Pre-Gym (5:00–5:25 AM)
**Read**: K.N. King Chapter 12 (Dynamic Storage Allocation — review)
- `realloc(ptr, newsize)`: resize existing allocation — may move to different address
- Dangling pointer: pointer to freed memory — undefined behavior if used
- Double-free: freeing the same pointer twice — crash or heap corruption
- Rules: always free what you malloc, always NULL after free, always check malloc

**Bed Reading**: K&R Chapter 5 — re-read any section that wasn't clear the first time

---

## SATURDAY JUNE 27 — POINTERS DEEP CODING (7:30 AM–6:30 PM)

### Warmup (7:30–9:00 AM): mycodeschool Pointers Playlist
Watch videos 1–8 at 1.5× speed. Take notes on paper — draw every diagram they draw.

```
Video 1:  Introduction to pointers               (~12 min)
Video 2:  Pointer types, pointer arithmetic       (~14 min)
Video 3:  Pointers and arrays                     (~12 min)
Video 4:  Pointer to pointer (double pointer)     (~10 min)
Video 5:  Passing pointers to functions           (~12 min)
Video 6:  Pointers and arrays in functions        (~10 min)
Video 7:  Pointers and dynamic memory (stack vs heap) (~15 min)
Video 8:  Dynamic memory allocation (malloc)      (~12 min)
```

After watching: DRAW from memory on paper:
- Memory diagram: stack (local vars, function frames) vs heap (malloc'd data)
- What `int *p = &x` looks like in memory (box for x, box for p, arrow between them)
- What `p++` does to a pointer vs what `(*p)++` does

### BLOCK 1 (9:00–10:30 AM): Pointer Fundamentals
Write ALL programs from scratch. NO copy-paste. NO AI code.

```
week3/
├── pointer_basics.c    — &, *, NULL check, sizeof pointer
├── pointer_arith.c     — pointer arithmetic with arrays
└── swap.c              — swap_wrong (by value) vs swap_correct (by pointer)
```

**pointer_basics.c** requirements:
```c
// Declare int x = 42
// Declare int *p = &x
// Print: address of x, value of x, value of p (same as address), value at *p (same as x)
// Change x through pointer: *p = 100 — print x again (shows 100)
// Show pointer size: sizeof(p) — always 8 on 64-bit, 4 on 32-bit
// Show: p is NOT the same as *p (address vs value)
// Try: int *null_p = NULL — print it (shows 0), but DON'T dereference it (that's undefined behavior)
```

**pointer_arith.c** requirements:
```c
int arr[] = {10, 20, 30, 40, 50};
int *p = arr;  // p points to arr[0]

// Print all 5 elements FOUR ways:
// 1. arr[i]         — array indexing
// 2. *(arr + i)     — pointer arithmetic with array name
// 3. p[i]           — pointer used like an array
// 4. *(p + i)       — pointer arithmetic with p

// Advance p through the array manually:
// p = arr; print *p; p++; print *p; etc.

// Show pointer subtraction: int *end = arr + 5; printf("distance = %ld\n", end - arr);
```

**swap.c** requirements:
```c
// Version 1: swap_wrong(int a, int b) — swaps the copies, original unchanged
// Version 2: swap_correct(int *a, int *b) — swaps originals through pointers

// Test:
// int x = 5, y = 10;
// swap_wrong(x, y);  print x and y — they are NOT swapped
// swap_correct(&x, &y); print x and y — they ARE swapped
// Draw this on paper: show the two function call stacks
```

### BREAK (10:30–10:45)

### BLOCK 2 (10:45 AM–12:15 PM): Strings as Char Pointers + Double Pointers
```
week3/
├── string_pointers.c   — String traversal with char pointers, pointer-based strlen
└── double_ptr.c        — Pointer to pointer: modify pointer from inside function
```

**string_pointers.c** requirements:
```c
// Part 1: traverse a string with a pointer (not array indexing)
// Write ptr_strlen(const char *s) using pointer traversal:
//   while (*s != '\0') { s++; count++; }
// Write ptr_toupper(char *s) using pointer traversal — modify in place
// Write ptr_count_char(const char *s, char c) — count occurrences

// Part 2: pointer vs array notation
// char arr[] = "hello";   // arr is array — CAN modify arr[0]
// char *ptr = "hello";    // ptr is pointer to string literal — do NOT modify
// Show sizeof difference: sizeof(arr) vs sizeof(ptr)
// Explain in comments: why modifying ptr[0] is undefined behavior
```

**double_ptr.c** requirements:
```c
// Why double pointer? When you need to change a pointer inside a function.

// Function that allocates memory and returns through double pointer:
void allocate_array(int **arr, int size) {
    *arr = malloc(size * sizeof(int));
    // caller's pointer now points to new malloc'd memory
}

// Function that resets a pointer to NULL (for cleanup):
void free_and_null(int **arr) {
    free(*arr);
    *arr = NULL;   // prevents dangling pointer
}

// Demonstrate:
// int *p = NULL;
// allocate_array(&p, 5);   // p is now valid
// fill and print the array
// free_and_null(&p);        // p is now NULL
// printf("p is %s\n", p == NULL ? "NULL" : "not NULL");
```

### LUNCH (12:15–1:15 PM)

### GERMAN BLOCK 1 (1:15–4:15 PM)
- Nicos Weg Lessons 17–19 (DW online or app)
- Review all vocabulary from Weeks 1–2 German sessions
- Write 10 sentences using accusative case: "Ich habe einen Computer. Ich trinke einen Kaffee."
- Anki: add 15 new cards from today's lessons

### GERMAN BLOCK 2 (4:45–6:15 PM)
- Nicos Weg Lesson 20 (milestone — 1/3 of A1 complete)
- AnkiDroid: review ALL pending cards
- Write from memory: your full introduction + daily schedule in German

---

## SUNDAY JUNE 28 — DYNAMIC MEMORY + FUNCTION POINTERS + GIT (7:30 AM–4:00 PM)

### BLOCK 1 (7:30–9:00 AM): Watch Remaining mycodeschool Videos
Watch videos 9–15 at 1.5× speed.

```
Video 9:  Memory leak and dangling pointer        (~12 min)
Video 10: Pointers and 2D arrays                 (~12 min)
Video 11: Pointers to functions                  (~10 min)
Video 12: Function pointers and callbacks         (~12 min)
Video 13: void pointers and generic programming  (~10 min)
Video 14: Const pointers                         (~8 min)
Video 15: Summary + practice                     (~10 min)
```

After watching: DRAW on paper:
- The difference between `int *p`, `int * const p`, `const int *p`, `const int * const p`
- What a dangling pointer looks like (pointer → freed memory)

### BLOCK 2 (9:15–10:45 AM): Dynamic Memory Programs
```
week3/
├── dynamic_array.c     — malloc/realloc to grow array dynamically
├── my_malloc_strings.c — malloc'd strings, free every one, Valgrind clean
└── valgrind_demo.c     — TWO versions: one with leak, one fixed. Run both under Valgrind.
```

**dynamic_array.c** requirements:
```c
// Build a growable integer array:
// Start with malloc(5 * sizeof(int))
// Fill first 5 elements
// Grow with realloc to 10 elements
// Fill elements 5–9
// Print all 10
// Free — no leaks
// Run with: valgrind --leak-check=full ./dynamic_array
// Expected: 0 bytes in 0 blocks lost
```

**valgrind_demo.c** requirements:
```c
// Version 1 — INTENTIONAL memory leak (keep for demonstration):
//   malloc 100 ints, fill them, print them, but DO NOT free
//   Valgrind will report: definitely lost: 400 bytes in 1 blocks
//   Compile as: gcc -g valgrind_demo_leak.c -o demo_leak

// Version 2 — Fixed version (same program with free added):
//   Same as version 1 but with free() before return
//   Valgrind will report: 0 bytes in 0 blocks lost
//   Compile as: gcc -g valgrind_demo_fixed.c -o demo_fixed

// Compare Valgrind output side by side — understand what "definitely lost" means
```

Rules:
- Every `malloc` or `calloc` call needs a matching `free`
- After `free(p)`, set `p = NULL` immediately
- Before using any malloc'd pointer: check `if (ptr == NULL) { /* handle error */ }`

### GIT PUSH (10:45–11:15 AM)
```bash
cd ~/C-Practice
git add week3/
git commit -m "Week 3: pointers — arithmetic, swap, dynamic memory, function pointers. Valgrind clean."
git push origin main
```

Write `week3/README.md`:
- List every file in week3/
- One sentence per file: what concept it demonstrates
- Add a section "Key insight this week": in your own words, explain what a pointer is and why C uses them

### REST + LUNCH (11:15 AM–12:00 PM)

### GERMAN (12:00–2:00 PM)
- Nicos Weg Lessons 21–22
- Anki mega review (clear all pending cards — aim for 50+ words total)
- Write German from memory: introduce yourself AND describe what you are studying and why

### EXTENDED CODING (2:00–4:00 PM): Pointer-Based Functions Rewrite
Take your Week 1 and Week 2 programs and rewrite them to use pointers:

```
week3/
├── ptr_bubble_sort.c   — bubble_sort(int *arr, int n) — modifies original array via pointer
├── ptr_my_strlen.c     — my_strlen using pointer traversal (while *s++ != '\0')
└── ptr_functions.c     — max_in_array, sum_array, find_element — all use pointer parameters
```

**ptr_bubble_sort.c** — from memory, no reference:
- Write `void bubble_sort(int *arr, int n)` — sorts in place via pointer
- Write `void print_array(const int *arr, int n)` — const pointer: cannot modify elements
- Test with an array of 10 numbers — sort ascending, print each pass

**ptr_my_strlen.c** — two implementations:
```c
// Version 1: index-based (what you wrote in Week 2)
int my_strlen_index(const char *s) {
    int count = 0;
    while (s[count] != '\0') count++;
    return count;
}

// Version 2: pointer-based (new — more idiomatic C)
int my_strlen_ptr(const char *s) {
    const char *start = s;
    while (*s) s++;         // advance until null terminator
    return (int)(s - start); // pointer subtraction = length
}
```

Both must return IDENTICAL results for the same input. Verify with 10 test strings.

**IMPORTANT end-of-week challenge**: From a blank file, write BOTH of these from memory with no references:
1. `swap(int *a, int *b)` — correct pointer-based swap
2. `my_strlen(const char *s)` — pointer traversal version

If you can do both in under 5 minutes total → you understand pointers. If not → re-read K.N. King Ch 11 and try again.

---

## WEEK 3 CHECKPOINT (Monday June 29, 4:00 PM)

Update PROGRESS.md now. Be honest.

| Checkpoint Item | Done? |
|:---|:---|
| Can explain: what is a pointer, what is & and * | |
| swap(int *a, int *b) written from memory — works correctly | |
| Understand why swap(a, b) by value does NOT swap | |
| Pointer arithmetic: p+1 advances by sizeof(*p) | |
| Know that arr[i] and *(arr+i) are identical | |
| malloc/free used in at least 3 programs | |
| Valgrind: all programs show 0 leaks | |
| my_strlen written with pointer traversal (while *s++ style) | |
| mycodeschool 15 videos watched, notes taken | |
| GitHub: week3 pushed with README | |
| Nicos Weg: lessons 17–22 done | |
| Anki: 50+ German words total | |
| K.N. King Ch 11–12 read | |
| K&R Ch 5 read | |

**Self-rating (pointers 1–10)**: ___ (minimum 6 before Week 4 — you WILL use pointers in structs)

> If your self-rating is below 6: spend the first weekday mornings of Week 4 re-reading K.N. King Ch 11.
> Do not proceed to structs without a working mental model of pointers.
> The rest of embedded C (malloc, linked lists, function callbacks, hardware register access) is ALL pointers.

---

## WEEKDAY THEORY FOCUS (Week 3)

| Day | Read Before Gym | Bed Read |
|:---|:---|:---|
| Tue Jun 23 | K.N. King Ch 11 pp. 1–20 | K&R Ch 5 pp. 93–110 |
| Wed Jun 24 | K.N. King Ch 11 pp. 20–40 | K&R Ch 5 pp. 110–125 |
| Thu Jun 25 | K.N. King Ch 11 pp. 40–end | K&R Ch 5 pp. 125–140 |
| Fri Jun 26 | K.N. King Ch 12 (Dynamic Memory) | K&R Ch 5 pp. 140–167 |
| Mon Jun 29 | K.N. King Ch 12 (review) | K&R Ch 5 — re-read hard parts |

> Pointers will feel confusing mid-week. That is normal. The confusion resolves when you CODE.
> Read carefully on weekdays. Draw diagrams in your notebook. Then code on the weekend.
> The mycodeschool videos + your own diagrams are more valuable than re-reading the same paragraph 5 times.
