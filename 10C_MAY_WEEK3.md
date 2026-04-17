# 📅 WEEK 3 — May 12-18 (Tue-Mon): POINTERS ⚠️ MOST IMPORTANT WEEK

> **Topics**: Addresses, dereferencing, pointer arithmetic, pass-by-reference, arrays & pointers, malloc/free, double pointers, function pointers
> **K&R Chapters**: Chapter 5 (Pointers and Arrays) — THE most critical chapter
> **Programs to write**: 10-12
> **German**: Nicos Weg Lessons 11-15, articles (der/die/das), basic verbs
> **⚠️ MANDATORY**: Draw memory diagrams on PAPER every single day

---

## ⚠️ WEEK 3 SPECIAL RULES

1. **DRAW on paper FIRST, code SECOND.** Every program this week must start with a pencil diagram showing: variable name → memory address → value stored → pointer arrows.
2. **If you don't understand something, DO NOT SKIP IT.** Pointers are the foundation of everything that comes next: structs, linked lists, STM32 registers, memory-mapped I/O, RTOS task creation.
3. **Use `gdb` this week.** Learn to inspect addresses and values with the debugger.

---

## DAY 12 — Tuesday, May 12

### 🔶 Morning (5:10-6:30 AM) — Pointer Basics: `&` and `*`

**What to learn**: Every variable has an ADDRESS in memory. A pointer STORES that address. `&` gets the address. `*` follows the address to get the value.

**How to learn**:
1. **(5:10-5:20)** Read **K&R Chapter 5**, pages 93-98. Read SLOWLY. Draw every diagram they show.
2. **(5:20-5:25)** BEFORE writing any code, draw this on paper:
   ```
   Memory:
   Address    Name    Value
   0x1000     x       42
   0x1008     p       0x1000  ← p "points to" x
   ```
   Understand: `p = &x` means "p stores the address of x". `*p` means "go to the address stored in p and get the value there" = 42.

3. **(5:25-5:50)** Write `pointer_basics.c`:
   - Declare `int x = 42;` and `int *p = &x;`
   - Print: value of x, address of x (`%p`), value of p, value at p (`*p`)
   - Change x through the pointer: `*p = 100;` → now x == 100!
   - Print everything again to verify
   - Do the same with `float`, `char`, `double` — see how addresses change
   - **Ask Google AI**: "Explain the difference between `int *p = &x` and `*p = 5` — in the first, `*` means 'pointer type'. In the second, `*` means 'dereference'. Why does C reuse the same symbol?"

4. **(5:50-6:15)** Write `pointer_sizes.c`:
   - Print `sizeof(int*)`, `sizeof(char*)`, `sizeof(float*)`, `sizeof(double*)`
   - **DISCOVERY**: They're ALL the same size! (8 bytes on 64-bit, 4 bytes on 32-bit). A pointer is just an address — addresses are all the same width.
   - **Embedded insight**: On your STM32 (32-bit ARM), ALL pointers are 4 bytes. On your PC (64-bit), all pointers are 8 bytes.

5. **(6:15-6:30)** Debug with `gdb`:
   - Compile: `gcc -g pointer_basics.c -o pointer_basics`
   - Run: `gdb ./pointer_basics`
   - Commands: `break main`, `run`, `next`, `print x`, `print &x`, `print p`, `print *p`
   - **This is how professional firmware engineers debug.** Not printf, not AI — GDB.

### 🎧 Commute: Nicos Weg Lesson 11 | 📱 Lunch: Anki (articles: der/die/das rules) | 📖 Bed: K&R pp. 98-105

### ✅ Day 12: `pointer_basics.c` + `pointer_sizes.c` + first GDB session. Paper diagram drawn.

---

## DAY 13 — Wednesday, May 13

### 🔶 Morning (5:10-6:30 AM) — Pointer Arithmetic

**What to learn**: Adding 1 to a pointer does NOT add 1 byte — it adds `sizeof(type)` bytes. THIS is how arrays are traversed.

**How to learn**:
1. **(5:10-5:15)** Draw on paper:
   ```
   int arr[5] = {10, 20, 30, 40, 50};

   Address:  0x1000  0x1004  0x1008  0x100C  0x1010
   Index:    [0]     [1]     [2]     [3]     [4]
   Value:    10      20      30      40      50

   arr      = 0x1000  (address of first element)
   arr + 1  = 0x1004  (NOT 0x1001! It adds sizeof(int) = 4)
   arr + 2  = 0x1008
   *(arr+2) = 30      (same as arr[2])
   ```

2. **(5:15-5:45)** Write `pointer_arithmetic.c`:
   - Declare `int arr[5] = {10,20,30,40,50};`
   - Prove: `arr[i]` is IDENTICAL to `*(arr + i)` — print both for every `i`
   - Prove: `&arr[i]` is IDENTICAL to `(arr + i)` — print both addresses
   - Try with `char arr[]` and `double arr[]` — see how address increments differ (1 byte vs 8 bytes)
   - **KEY INSIGHT**: `arr[i]` is SYNTACTIC SUGAR for `*(arr + i)`. The compiler translates one to the other. This is why array indexing starts at 0 — if first element is at address `arr`, then `arr[0] = *(arr + 0) = *arr` = value at start.

3. **(5:45-6:15)** Write `pointer_vs_array.c`:
   - Array name IS a pointer to first element... mostly. But test: `sizeof(arr)` vs `sizeof(ptr)` — they're DIFFERENT!
   - `sizeof(arr)` = total array size (20 for `int[5]`)
   - `sizeof(ptr)` = pointer size (8 bytes on 64-bit)
   - **Trap discovered**: When you pass an array to a function, `sizeof` gives pointer size, not array size. This is why functions need a separate `int n` parameter for array length.

4. **(6:15-6:30)** Re-draw the memory diagram from step 1 from MEMORY. Can you do it?

### 🎧 Commute: Nicos Weg Lesson 12 | 📱 Lunch: Anki | 📖 Bed: K&R pp. 105-110

### ✅ Day 13: `pointer_arithmetic.c` + `pointer_vs_array.c`. Understand arr[i] == *(arr+i).

---

## DAY 14 — Thursday, May 14

### 🔶 Morning (5:10-6:30 AM) — Pass by Reference (Swap Function)

**What to learn**: C only passes copies of values to functions. To modify original variables, you MUST pass pointers (addresses).

**How to learn**:
1. **(5:10-5:20)** Draw on paper:
   ```
   WRONG (pass by value):           RIGHT (pass by reference):
   main: a=5, b=10                  main: a=5, b=10
   swap: x=5, y=10 (COPIES!)       swap: x=&a, y=&b (ADDRESSES!)
   swap: x=10, y=5 (copies swapped) swap: *x=10, *y=5 (ORIGINALS swapped!)
   main: a=5, b=10 (UNCHANGED!)    main: a=10, b=5 (CHANGED! ✅)
   ```

2. **(5:20-5:45)** Write `swap.c`:
   - Write `void swap_wrong(int x, int y)` — prove it doesn't work
   - Write `void swap_right(int *x, int *y)` — prove it works
   - Call both, print before and after
   - **This is the "aha!" moment** when pointers click. If swap works, you understand pointers.

3. **(5:45-6:10)** Write `pass_by_ref.c`:
   - Write `void get_min_max(int arr[], int n, int *min, int *max)` — function that finds BOTH min and max in one pass
   - In C, functions can only return ONE value. Pointers let you "return" multiple values through parameters!
   - Write `void string_stats(char *str, int *letters, int *digits, int *spaces)` — count each character type

4. **(6:10-6:30)** Debug `swap_right` with GDB:
   - Break before swap, print `a`, `b`, `&a`, `&b`
   - Step into swap function, print `x`, `y`, `*x`, `*y`
   - Verify: `x == &a` and `y == &b`

### 🎧 Commute: Nicos Weg Lesson 13 | 📱 Lunch: Anki (German verbs: sein, haben, machen, gehen, kommen)

### ✅ Day 14: `swap.c` + `pass_by_ref.c`. Both pass-by-value and pass-by-reference understood.

---

## DAY 15 — Friday, May 15

### 🔶 Morning (5:10-6:30 AM) — Arrays as Function Parameters

**What to learn**: When you pass an array to a function, you're really passing a pointer. Understanding this is essential for writing ANY non-trivial C program.

**How to learn**:
1. **(5:10-5:40)** Write `array_functions.c`:
   - Write `void print_array(int *arr, int n)` — use pointer notation to traverse
   - Write `void reverse_array(int *arr, int n)` — reverse in-place using pointer swaps
   - Write `int *find_element(int *arr, int n, int target)` — return pointer to found element, or `NULL` if not found
   - **KEY**: Notice `NULL` — this is the "pointer to nothing" (address 0). Checking for `NULL` is how C handles "not found" / "error" / "end of list". STM32 HAL functions return `NULL` on failure constantly.

2. **(5:40-6:10)** Write `const_pointers.c`:
   - `const int *p` — pointer to constant (can't change value through pointer)
   - `int * const p` — constant pointer (can't change what it points to)
   - `const int * const p` — both constant
   - **Where you see this in embedded**: `const uint8_t *data` — "I promise not to modify this data" (read-only buffer from sensor)
   - **Read Beej's Guide** section on const and pointers for clear explanation

3. **(6:10-6:30)** Write `string_pointers.c`:
   - `char str[] = "hello"` vs `char *str = "hello"` — what's the difference?
   - Array version: stored on stack, modifiable
   - Pointer version: stored in read-only memory, NOT modifiable (crash if you try!)
   - **This distinction crashes embedded programs ALL THE TIME**

### 🎧 Commute: Nicos Weg Lesson 14 | 📱 Lunch: Anki | 📖 Bed: K&R pp. 110-118

### ✅ Day 15: `array_functions.c` + `const_pointers.c` + `string_pointers.c`. Understand NULL.

---

## DAY 16 — Saturday, May 16 🟩 BIG DAY

### 💻 Warmup (6:30-7:30 AM) — Dynamic Memory: malloc and free

**What to learn**: Stack memory is limited and temporary. `malloc()` gives you memory from the HEAP that lives until you `free()` it. Forgetting to free = memory leak.

**How to learn**:
1. **(6:30-6:40)** Draw on paper:
   ```
   STACK (automatic, small, fast):    HEAP (manual, large, slower):
   ┌──────────┐                       ┌──────────────────┐
   │ main()   │                       │ malloc(20 bytes) │ ← you control this
   │  int x=5 │                       │ malloc(40 bytes) │ ← must free() when done
   │  int y=10│                       │ (leaked memory!) │ ← forgot to free!
   └──────────┘                       └──────────────────┘
   ```

2. **(6:40-7:10)** Write `malloc_demo.c`:
   - Allocate an array of N integers at runtime: `int *arr = malloc(n * sizeof(int));`
   - Check if malloc returned NULL (out of memory!)
   - Fill the array, print it, find sum
   - FREE the memory: `free(arr);`
   - **CRITICAL HABIT**: Every `malloc()` must have a matching `free()`. Write them together. `malloc` at top, `free` at bottom.
   - Set pointer to NULL after free: `arr = NULL;` — prevents use-after-free bugs

3. **(7:10-7:30)** Run with **Valgrind** to detect leaks:
   ```
   gcc -g malloc_demo.c -o malloc_demo
   valgrind --leak-check=full ./malloc_demo
   ```
   - If you forgot `free()`, Valgrind will tell you EXACTLY where the leak is
   - **Valgrind is the embedded developer's best friend.** It catches bugs that crash your STM32 after 12 hours of running.

4. **(7:30-7:45)** Write `dynamic_string.c`:
   - Use `malloc` to create a string of user-specified length
   - Copy a string into it using your `my_strcpy()`
   - Free it when done

> **Note**: This is Saturday — continue into Deep Sessions (7:45 AM onward) if you want to practice more malloc/free exercises. Follow the Saturday template from the overview.

### 📖 Evening: K&R pp. 118-125 (Dynamic allocation)

### ✅ Day 16: `malloc_demo.c` + `dynamic_string.c`. First Valgrind run. Zero leaks.

---

## DAY 17 — Sunday, May 17 🟨 REVIEW + PROJECT

### 💻 Warmup (6:30-7:30) — Review Pointers So Far
- Re-draw ALL memory diagrams from this week from MEMORY
- Re-write `swap_right()` from memory
- Can you explain to someone what a pointer is in 3 sentences?

### 💻 Deep Session 1 (7:45-9:15) — Double Pointers

**What to learn**: A pointer to a pointer. `int **pp` stores the address of a pointer, which stores the address of an int.

**How to learn**:
1. Draw on paper:
   ```
   int x = 42;
   int *p = &x;     // p points to x
   int **pp = &p;   // pp points to p

   Address:  0x1000    0x1008    0x1010
   Name:     x         p         pp
   Value:    42        0x1000    0x1008

   *pp  = p  = 0x1000
   **pp = *p = 42
   ```

2. Write `double_pointer.c`:
   - Create x, p, pp as above
   - Print everything: `x`, `*p`, `**pp` — all equal 42
   - Write `void allocate(int **ptr, int n)` — function that allocates memory and returns it through a pointer parameter
   - **Where this is used in embedded**: Passing buffer pointers out of functions. `HAL_UART_Receive()` uses similar patterns.

### 💻 Deep Session 2 (9:30-11:00) — Dynamic 2D Array

Write `dynamic_2d.c`:
- Allocate a 2D array at runtime using double pointers:
  ```
  int **matrix = malloc(rows * sizeof(int *));
  for (i = 0; i < rows; i++)
      matrix[i] = malloc(cols * sizeof(int));
  ```
- Fill with values, print it, then FREE everything in reverse order
- **This is how image buffers, sensor data matrices, and display framebuffers work in embedded**

### 💻 Deep Session 3 (11:15-12:45) — Function Pointers (Preview)

**What to learn**: In C, functions have addresses too. You can store a function's address in a pointer and call it later. This is how callbacks work in embedded (interrupt handlers, RTOS task functions).

Write `function_pointers.c`:
- Declare: `int (*operation)(int, int);`
- Point it at different functions: `operation = add;` then `operation = multiply;`
- Call through pointer: `result = operation(5, 3);`
- Write a `sort` function that takes a comparison function as a parameter — this is how `qsort()` works
- **Embedded connection**: Every `HAL_UART_RegisterCallback()`, every RTOS `xTaskCreate()`, every interrupt `NVIC_SetVector()` uses function pointers

### 🇩🇪 German (2:00-3:30) — Sunday template
- Nicos Weg Lessons 14-15
- Google AI: Practice verb conjugation in present tense
- Anki: Add 10 verb conjugation cards

### 💻 Mini-Project (3:30-5:00) — Phone Book

Write `phonebook.c`:
- Dynamically allocated array of names and phone numbers
- Menu: Add contact, Search by name, Delete contact, Display all, Exit
- Uses: malloc/free, char arrays, strcmp, pointer parameters, functions
- **Combines everything from Weeks 1-3**

### 💻 Git Push (5:00-5:30) — Push `week3/`
- `git add . → git commit → git push`
- Update README with Week 3 progress (pointers!)

### ✅ Day 17: `double_pointer.c` + `dynamic_2d.c` + `function_pointers.c` + `phonebook.c`. Git push. Memory diagrams for ALL.

---

## DAY 18 — Monday, May 18 🟦 WEEKDAY

### 🔶 Morning (5:10-6:30 AM) — Pointer Consolidation

Write a program that dynamically allocates an array, fills it from user input, sorts it, prints it, frees it. All from memory. No references.

> **Note**: Full review, Git push, and German mega review happen next Saturday (Day 23). For today, just reinforce this week’s pointer concepts.

### 🎧 Commute: Nicos Weg 16 | 📱 Lunch: Anki | 📖 Bed: K&R pp. 118-125

---

## 📊 WEEK 3 SUMMARY

| Metric | Target | Done? |
|:---|:---|:---|
| Programs written | 10+ (cumulative 30+) | [ ] |
| Memory diagrams drawn on paper | **At least 7** (one per day) | [ ] |
| Can write from memory | `swap`, `malloc+free`, `double pointer` | [ ] |
| GDB used for debugging | At least 3 sessions | [ ] |
| Valgrind used for leak detection | At least 2 runs | [ ] |
| K&R Chapter 5 | Read completely (pp. 93-125) | [ ] |
| Nicos Weg lessons | 11-15 (cumulative: 15) | [ ] |
| German words in Anki | 50+ (cumulative) | [ ] |
