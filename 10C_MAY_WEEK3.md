# ARCHIVED — MAY WEEK 3 (NOT STARTED — See June 2026 files for actual Phase 1 Week 3)

> **ARCHIVE NOTE**: This week was never executed. Real start = June 9, 2026. See `11C_JUNE_WEEK3.md`.
> Content below is reference material for Phase 1 Week 3 topics (Pointers).

---

# WEEK 3 — May 12-18 (Tue-Mon): POINTERS — MOST IMPORTANT WEEK [REFERENCE ONLY]

> **Topics**: Addresses, dereferencing, pointer arithmetic, pass-by-reference, arrays & pointers, malloc/free, double pointers, function pointers
> **K.N. King Chapters**: Ch 11-13, 17 (Pointers, Pointers and Arrays, Strings, Advanced Uses of Pointers)
> **K&R Bed Reading**: Chapter 5 (Pointers and Arrays) — THE most critical chapter
> **FastBit Udemy**: Sections 9-13 (Functions, Pointers, Strings, Structures)
> **Programs to write**: 8-10 (1-2 per weekday, 3-4 on Saturday)
> **German**: Nicos Weg Lessons 11-15, articles (der/die/das), basic verbs
> **⚠️ MANDATORY**: Draw memory diagrams on PAPER every single day
> **📚 Full resource details**: See `10_RESOURCES.md`

---

## ⚠️ WEEK 3 SPECIAL RULES

1. **DRAW on paper FIRST, code SECOND.** Every program this week must start with a pencil diagram showing: variable name → memory address → value stored → pointer arrows.
2. **If you don't understand something, DO NOT SKIP IT.** Pointers are the foundation of everything that comes next: structs, linked lists, STM32 registers, memory-mapped I/O, RTOS task creation.
3. **Use `gdb` this week.** Learn to inspect addresses and values with the debugger.

---

## 📺 PRIMARY VIDEO SOURCE THIS WEEK

### mycodeschool — "Pointers in C/C++" Playlist ⭐⭐⭐⭐⭐

- **URL**: https://www.youtube.com/playlist?list=PL2_aWCzGMAwLZp6LMUKI3cc7pgGsasm2_
- **Videos**: ~15, each 10-20 min
- **Quality**: THE BEST pointers tutorial on the entire internet. Legendary channel.
- **Style**: Clean diagrams, step-by-step memory visualization, builds concepts layer by layer
- **You MUST watch ALL 15 videos this week.** 2-3 per day.

### Video Schedule

| Day | mycodeschool Videos to Watch | Topic |
|:---|:---|:---|
| Day 12 (Tue) | #1 "Introduction to pointers" + #2 "Working with pointers" | Basics: `&` and `*` |
| Day 13 (Wed) | #3 "Pointer types, void pointers" | Types + German day |
| Day 14 (Thu) | #4 "Pointers to Pointers" + #5 "Pointers as function arguments" | Double pointers, pass-by-ref |
| Day 15 (Fri) | #6 "Pointers and arrays" + #7 "Arrays as function arguments" | Array-pointer relationship |
| Day 16 (Sat) | #8 "Character arrays and pointers" + #9-#11 "Dynamic memory (malloc, calloc, realloc, free)" | Strings + heap memory |
| Day 17 (Sun) | #12 "Pointers as function returns" + #13-#14 "Function pointers and callbacks" | Advanced pointers |
| Day 18 (Mon) | #15 "Memory leak" + review any confusing video | Cleanup + review |

---

## DAY 12 — Tuesday, May 12

### 🔶 Morning (5:10-6:30 AM) — Pointer Basics: `&` and `*`

---

#### 📺 WATCH FIRST (25 min) — 5:10 to 5:35 AM

1. **mycodeschool #1: "Introduction to pointers in C/C++"** (~12 min)
   - Focus on: Every variable has an ADDRESS in memory. A pointer STORES that address.
2. **mycodeschool #2: "Working with pointers"** (~12 min)
   - Focus on: `&` gets the address. `*` follows the address to get/set the value (dereferencing).

> **Supplement** (if still confused after mycodeschool): **Neso Academy: "Introduction to Pointers"** (~10 min) — different explanation style, might click better.

---

#### 📖 READ (5 min)

- **K&R pp. 93-98** (Chapter 5 opening — pointers introduction). Read SLOWLY. Draw every diagram they show.

---

#### ✏️ DRAW FIRST (5 min) — 5:35 to 5:40 AM

BEFORE writing any code, draw this on paper:
```
Memory:
Address    Name    Value
0x1000     x       42
0x1008     p       0x1000   ← p stores the ADDRESS of x
                            ← *p gives us 42 (follows the arrow)
                            ← &x gives us 0x1000
```

---

#### 💻 CODE (40 min) — 5:40 to 6:20 AM

**Program 1 — `pointer_basics.c`:**
```
- Declare: `int x = 42;`
- Declare: `int *p = &x;`
- Print: x, &x, p, *p — understand what each prints
- Change value through pointer: `*p = 100;` → now x == 100!
- Use sizeof: `sizeof(p)` — always 8 bytes on 64-bit (it stores an address)
```

**Program 2 — `pointer_types.c`:**
```
- int *ip, float *fp, char *cp, double *dp
- Each points to its respective variable type
- Print all addresses and values using correct format specifiers
- Understand: pointer type tells the compiler HOW MANY BYTES to read when dereferencing
```

---

#### 🧪 TEST YOURSELF

- **learn-c.org**: "Pointers" → https://www.learn-c.org/en/Pointers
- **HackerRank**: "Pointers in C" → https://www.hackerrank.com/challenges/pointer-in-c
- In `gdb`: compile with `-g`, set breakpoint, inspect `&x` and `p` — are they the same address?

---

### 🎧 Commute: Nicos Weg Lesson 11 | 📱 Lunch: Anki | 📖 Bed: K&R pp. 98-104 (pointer arithmetic)

### ✅ Day 12: `pointer_basics.c` + `pointer_types.c`. Memory diagram drawn. GDB inspection done.

---

## DAY 13 — Wednesday, May 13

### 🔶 Morning (5:10-6:30 AM) — 🇩🇪 German + Pointer Arithmetic

---

#### 📺 GERMAN (20 min) — 5:10 to 5:30 AM

- **DW Nicos Weg app**: Lesson 12
- **Learn German with Anja** (YouTube): Search "German Articles der die das for beginners" (~15 min)
  - Start learning: der (masculine), die (feminine), das (neuter) — THE hardest part of German
  - Write 10 nouns with articles in Anki: der Tisch, die Lampe, das Buch, der Computer, die Tür...

---

#### 📺 WATCH (15 min) — 5:30 to 5:45 AM

- **mycodeschool #3: "Pointer types, pointer arithmetic, void pointers"** (~15 min)
  - Focus on: `p + 1` doesn't add 1 byte — it adds `sizeof(*p)` bytes. For `int *p`, `p+1` moves 4 bytes forward. This is HOW you traverse arrays with pointers.

---

#### 💻 CODE (40 min) — 5:45 to 6:25 AM

**Program 3 — `pointer_arithmetic.c`:**
- Declare an array: `int arr[] = {10, 20, 30, 40, 50};`
- Declare a pointer to first element: `int *p = arr;` (or `int *p = &arr[0];`)
- Print each element using pointer arithmetic: `*(p+0)`, `*(p+1)`, `*(p+2)` — same as `arr[0]`, `arr[1]`, `arr[2]`
- Increment pointer in a loop: `while (p < arr + 5) { printf("%d ", *p); p++; }`
- **What to understand**: `arr[i]` is literally syntactic sugar for `*(arr + i)`. They compile to the SAME machine code.
- **PRINT ADDRESSES**: `printf("arr[%d] is at address %p, value = %d\n", i, (void*)(arr+i), *(arr+i));`

---

#### 🧪 TEST YOURSELF

- Draw the array in memory with addresses, showing how `p+1` jumps by 4 bytes (not 1)
- **Ask Google AI**: "If `int *p` points to address 0x1000 and I do `p + 3`, what address does it point to? Explain why."

---

### 📖 Bed: K&R pp. 104-110 (arrays and pointers relationship)

### ✅ Day 13: `pointer_arithmetic.c`. German articles started. Memory diagram with addresses.

---

## DAY 14 — Thursday, May 14

### 🔶 Morning (5:10-6:30 AM) — Pass-by-Reference + Double Pointers

---

#### 📺 WATCH FIRST (25 min) — 5:10 to 5:35 AM

1. **mycodeschool #4: "Pointers to Pointers in C/C++"** (~10 min)
   - Focus on: `int **pp` — a pointer that stores the address of another pointer. Draw the chain!
2. **mycodeschool #5: "Pointers as function arguments — call by reference"** (~12 min)
   - Focus on: This is HOW you make a function modify the caller's variable. The `swap(int *a, int *b)` pattern.

> **Deeper understanding**: **Jacob Sorber: "Pointers in C — finally understand them"** (~15 min) — excellent if mycodeschool wasn't enough

---

#### 📖 READ — K&R pp. 95-98 (function arguments with pointers)
- Or: **Beej's Guide** → "Pointers" → https://beej.us/guide/bgc/html/split/pointers.html

---

#### ✏️ DRAW FIRST — Before coding, draw the swap function on paper:
```
Before swap:       After swap:
a → [5]            a → [10]
b → [10]           b → [5]

Show HOW *a and *b allow the function to reach the original variables
```

---

#### 💻 CODE (40 min) — 5:35 to 6:15 AM

**Program 4 — `swap.c`:**
- Write `void swap_wrong(int a, int b)` — call by value, doesn't work. Prove it.
- Write `void swap_correct(int *a, int *b)` — call by reference, works. Prove it.
- **This is the MOST asked pointer interview question.** You MUST be able to explain it on a whiteboard.

**Program 5 — `double_pointer.c`:**
- `int x = 5; int *p = &x; int **pp = &p;`
- Print: `x`, `*p`, `**pp` — all give 5!
- Print: `&x`, `p`, `*pp` — all give the same address!
- Draw the 3-level chain on paper.

---

#### 🧪 TEST YOURSELF

- **HackerRank**: search "Pointer" challenges
- Explain to yourself (or record a voice note): "Why does `swap(int a, int b)` not work but `swap(int *a, int *b)` works?"

---

### 🎧 Commute: Nicos Weg Lesson 13 | 📱 Lunch: Anki (add verb conjugations: ich bin, du bist, er/sie ist) | 📖 Bed: K&R pp. 110-115

### ✅ Day 14: `swap.c` + `double_pointer.c`. Can explain swap on paper.

---

## DAY 15 — Friday, May 15

### 🔶 Morning (5:10-6:30 AM) — 🇩🇪 German + Arrays & Pointers

---

#### 📺 GERMAN (15 min) — 5:10 to 5:25 AM

- **DW Nicos Weg app**: Lesson 14
- Practice verbs: sein (to be), haben (to have), machen (to do/make)
  - ich bin, du bist, er/sie/es ist, wir sind, ihr seid, sie/Sie sind

---

#### 📺 WATCH (20 min) — 5:25 to 5:45 AM

1. **mycodeschool #6: "Pointers and arrays"** (~12 min)
   - Focus on: Array name IS a pointer to the first element. `arr` == `&arr[0]`.
2. **mycodeschool #7: "Arrays as function arguments"** (~10 min)
   - Focus on: When you pass an array to a function, you're passing a POINTER. That's why the function can modify the original array.

---

#### 💻 CODE (40 min) — 5:45 to 6:25 AM

**Program 6 — `array_pointer.c`:**
- Declare array and pointer: `int arr[] = {1,2,3,4,5}; int *p = arr;`
- Access elements three ways: `arr[i]`, `*(arr+i)`, `*(p+i)` — all identical!
- Pass array to function both ways: `void print_arr(int arr[], int n)` and `void print_arr(int *arr, int n)` — SAME thing!
- **The big revelation**: `arr[i]` is just `*(arr + i)`. C arrays ARE pointers in disguise.

**Program 7 — `reverse_array_pointer.c`:**
- Reverse an array using two pointers: `int *left = arr;` `int *right = arr + n - 1;`
- Swap `*left` and `*right`, move inward
- This is the two-pointer technique you'll use constantly in embedded data processing

---

#### 🧪 TEST YOURSELF

- **HackerRank**: "Array Reversal" but implement with pointers this time
- **learn-c.org**: "Pointers" → verify your understanding

---

### 📖 Bed: K&R pp. 115-122 (character pointers, function pointers preview)

### ✅ Day 15: `array_pointer.c` + `reverse_array_pointer.c`. German verbs started.

---

## DAY 16 — Saturday, May 16 🟩 DYNAMIC MEMORY DAY

### 💻 Warmup (6:30-7:30 AM) — Character Pointers (Strings as Pointers)

---

#### 📺 WATCH (12 min) — 6:30 to 6:42 AM

- **mycodeschool #8: "Character arrays and pointers"** (~12 min)
  - Focus on: `char *s = "Hello"` vs `char s[] = "Hello"` — they are NOT the same! One is read-only, the other is modifiable.

---

#### 💻 CODE (45 min) — 6:42 to 7:30 AM

**Program 8 — `char_pointers.c`:**
- `char s1[] = "Hello";` — array (modifiable, on stack)
- `char *s2 = "Hello";` — pointer to string literal (READ-ONLY! Modifying crashes)
- Demonstrate: `s1[0] = 'J';` works. `s2[0] = 'J';` causes segfault.
- **Why this matters**: In embedded, string literals go to FLASH memory (read-only). Variables go to RAM. This distinction is critical.

---

### 💻 Deep Session 1 (7:45-9:15 AM) — Dynamic Memory: malloc, calloc, free

---

#### 📺 WATCH FIRST (30 min) — 7:45 to 8:15 AM

1. **mycodeschool #9: "Dynamic memory allocation in C — malloc"** (~15 min)
2. **mycodeschool #10: "Dynamic memory allocation — calloc, realloc"** (~12 min)
3. **mycodeschool #11: "Dynamic memory allocation — realloc, free"** (~10 min)

> **Supplement**: **Jacob Sorber: "Dynamic Memory Allocation in C (malloc, calloc, realloc, free)"** (~20 min) — practical terminal demo, very clear

---

#### 📖 READ — K&R pp. 167-169 (storage allocator)
- Or: **Beej's Guide** → "Manual Memory Allocation" → https://beej.us/guide/bgc/html/split/manual-memory-allocation.html

---

#### ✏️ DRAW FIRST — Before coding, draw on paper:
```
STACK (automatic, fast, limited)     HEAP (manual, slower, large)
┌──────────────┐                     ┌──────────────┐
│ int x = 5;   │                     │ malloc(40)   │ ← you must free() this!
│ int arr[10]; │                     │              │
│ (auto freed) │                     │ (you manage) │
└──────────────┘                     └──────────────┘
```

---

#### 💻 CODE (55 min) — 8:15 to 9:10 AM

**Program 9 — `dynamic_array.c`:**
- Ask user for array size `n` at runtime
- Allocate: `int *arr = (int *)malloc(n * sizeof(int));`
- Check if `malloc` returned NULL (out of memory!)
- Fill array, print it, find sum/avg/max/min
- FREE the memory: `free(arr);`
- **Common bug**: Forgetting `free()` → memory leak. In embedded, you run out of RAM and crash.

**Program 10 — `realloc_demo.c`:**
- Start with `malloc(5 * sizeof(int))` for 5 elements
- Need more? `realloc(arr, 10 * sizeof(int))` — grows the array
- Understand: `realloc` may MOVE the data to a new address!

---

#### 🧪 TEST YOURSELF — 9:10-9:15 AM

- **HackerRank**: "Dynamic Array in C" → https://www.hackerrank.com/challenges/dynamic-array-in-c
- **learn-c.org**: "Dynamic allocation" → https://www.learn-c.org/en/Dynamic_allocation

---

### 💻 Deep Session 2 (9:30-11:00 AM) — GDB with Pointers

---

#### 📺 WATCH (15 min) — 9:30 to 9:45 AM

- **Jacob Sorber: "GDB Tutorial: Finding Bugs in C Programs"** (~15 min)
  - Focus on: `break`, `run`, `print`, `x` (examine memory), `step`, `next`

---

#### 💻 PRACTICE GDB (70 min) — 9:45 to 10:55 AM

Compile all your pointer programs with `-g`:
```bash
gcc -g pointer_basics.c -o pointer_basics
gdb ./pointer_basics
```

Practice these GDB commands:
- `break main` → `run` → `print x` → `print &x` → `print p` → `print *p`
- `x/4xb &x` — examine 4 bytes at address of x in hex (see the actual bytes!)
- Step through `swap.c` and watch the values change in real-time

**This is real debugging.** Professional embedded engineers use GDB (or its ARM variant `arm-none-eabi-gdb`) daily.

---

### 💻 Deep Session 3 (11:15 AM-12:45 PM) — Circular Buffer (Preview for Embedded)

---

#### 📺 WATCH (10 min) — 11:15 to 11:25 AM

- Search YouTube: **"Circular buffer in C explained"** — watch any video under 10 min
- Focus on: head/tail pointers, wrapping around, full vs empty detection

---

#### 💻 CODE — `circular_buffer.c`

This is THE most used data structure in embedded systems (UART RX buffer, sensor data buffer, audio buffer):
- Fixed-size array with `head` and `tail` indices
- `push()`: add to head, wrap around if needed
- `pop()`: remove from tail
- Handle full and empty conditions
- **You built this in pure C on a PC. In July, you'll use the EXACT same code on STM32 for UART.**

---

### 🇩🇪 German (2:00-5:00 PM)

- **DW Nicos Weg**: Lessons 14-15 (2:00-3:30 PM)
- **Learn German with Anja** (YouTube): "Present Tense Verbs in German" (~15 min)
- **Google AI Pro** voice mode (3:45-5:00 PM): Practice saying where you live, what you do, what you're learning
- **Anki**: Add 10 new cards (verbs: lernen, arbeiten, wohnen, sprechen, verstehen)

---

### ✅ Day 16: `char_pointers.c` + `dynamic_array.c` + `realloc_demo.c` + GDB practice + `circular_buffer.c`. MASSIVE day.

---

## DAY 17 — Sunday, May 17 🟨 FUNCTION POINTERS + REVIEW

### 💻 Practice (7:30-9:00 AM) — Function Pointers

---

#### 📺 WATCH FIRST (25 min) — 7:30 to 7:55 AM

1. **mycodeschool #12: "Pointers as function returns"** (~10 min)
   - Focus on: NEVER return a pointer to a local variable! (dangling pointer)
2. **mycodeschool #13: "Function pointers in C"** (~15 min)
   - Focus on: Storing the address of a FUNCTION in a pointer variable. Used for callbacks.
3. **mycodeschool #14: "Function pointers and callbacks"** (~12 min)
   - Focus on: Passing a function as an argument to another function.

> **Supplement**: **Jacob Sorber: "Function Pointers in C"** (~12 min) — more practical examples

---

#### 📖 READ — K&R pp. 118-122 (function pointers and qsort example)

---

#### 💻 CODE (55 min) — 7:55 to 8:50 AM

**Program 11 — `function_pointers.c`:**
- Declare a function pointer: `int (*op)(int, int);`
- Point it to different functions: `op = add;` then `op = multiply;`
- Call through pointer: `result = op(5, 3);`
- **Build a calculator using function pointers** — no switch/case needed!

**Program 12 — `callback_sort.c`:**
- Write a generic sort function that takes a comparison function pointer:
  - `void sort(int arr[], int n, int (*compare)(int, int))`
- Pass different comparators: `ascending`, `descending`, `by_abs_value`
- **This pattern is how STM32 HAL callbacks work**: you register a function, the hardware calls it when an event happens.

---

### 💻 Pointer Review (9:15-12:30 PM)

#### 📺 WATCH (12 min) — 9:15 to 9:30 AM

- **mycodeschool #15: "Memory leak"** (~12 min)
  - Focus on: What happens when you malloc but never free. The program slowly eats all RAM.

#### ✏️ MASTER DIAGRAM — Draw this complete picture:

```
MEMORY MAP OF A C PROGRAM:
┌─────────────────────┐  High Address
│       STACK          │  ← Local variables, function calls (grows DOWN)
│  int x = 5;         │
│  int *p = &x;       │
├─────────────────────┤
│       HEAP           │  ← malloc/calloc (grows UP)
│  malloc(100);       │
├─────────────────────┤
│       BSS            │  ← Uninitialized globals (auto zero)
├─────────────────────┤
│       DATA           │  ← Initialized globals, static vars
├─────────────────────┤
│       TEXT            │  ← Your compiled code (read-only)
│  Function pointers   │
│  point HERE          │
└─────────────────────┘  Low Address
```

#### 💻 COMPLETE REVIEW (10:00-12:30)

- Re-write `swap.c` from memory
- Re-write `circular_buffer.c` from memory
- Write answers to these interview questions (in a file `pointer_interview_answers.c`):
  1. What is a pointer?
  2. What is the difference between `*p` and `&x`?
  3. What is a dangling pointer?
  4. What is a memory leak?
  5. What is the difference between stack and heap?
  6. What is a function pointer and when do you use one?
  7. What does `const int *p` vs `int * const p` mean?
  8. What is a void pointer?

---

### 🇩🇪 German (2:00-4:00 PM)
- Anki mega review
- Write 15 sentences using present tense verbs

### 📋 Weekly Review (4:00-4:30 PM)
- This was the HARDEST week. Log everything in `PROGRESS.md`.
- Rate your pointer understanding: 1-10. Below 7? Re-watch mycodeschool videos.

---

### ✅ Day 17: `function_pointers.c` + `callback_sort.c` + `pointer_interview_answers.c`. Complete pointer review.

---

## DAY 18 — Monday, May 18 🟦 WEEKDAY

### 🔶 Morning (5:10-6:30 AM) — Pointer Consolidation + GDB

---

#### 📺 WATCH (10 min) — 5:10 to 5:20 AM

- Re-watch whichever mycodeschool video you found hardest. Just one.

---

#### 💻 CODE (60 min) — 5:20 to 6:20 AM

**Memory test**: Close ALL references. Write from memory:
1. A program that uses `malloc` to create an array, fills it, prints it, frees it
2. A swap function using pointers
3. A function that takes a function pointer as callback

If you can't write #3 from memory, that's OK — function pointers are the hardest part. Re-watch mycodeschool #13 tonight.

**GDB practice**: Pick your hardest program, compile with `-g`, step through in GDB, print all pointer values.

---

#### 🧪 PREPARE FOR WEEK 4

- Preview K&R Chapter 6 (Structures) — read pp. 127-130
- Search YouTube: **Neso Academy "Structures in C"** — bookmark for tomorrow
- **Mindset**: Week 4 connects pointers to real hardware. Structs define how STM32 registers are organized. Bitwise ops manipulate individual register bits. This is where C meets embedded.

---

### 🎧 Commute: Nicos Weg Lesson 15 | 📱 Lunch: Anki | 📖 Bed: K&R pp. 127-130 (structs preview)

### ✅ Day 18: Pointer programs from memory. GDB practice. Week 4 previewed.

---

## 📊 WEEK 3 SUMMARY

| Metric | Target | Done? |
|:---|:---|:---|
| Programs written | 10+ (cumulative 30+) | [ ] |
| mycodeschool videos watched | ALL 15 | [ ] |
| Can explain pointer on paper with diagram | YES | [ ] |
| Can write swap function from memory | YES | [ ] |
| Understand malloc/free | YES | [ ] |
| Can use GDB to inspect pointers | YES | [ ] |
| Circular buffer working | YES | [ ] |
| Function pointers understood | YES | [ ] |
| Interview Q&A file written | 8+ answers | [ ] |
| K&R pp. 93-126 read | YES | [ ] |
| Nicos Weg lessons | 11-15 (cumulative: 15) | [ ] |
| German words in Anki | 50+ (cumulative) | [ ] |
| German articles (der/die/das) started | YES | [ ] |

> [!CAUTION]
> **If you rate your pointer understanding below 7/10 after this week, DO NOT MOVE ON.** Spend the first 2 days of Week 4 re-watching mycodeschool and re-doing the exercises. Pointers are non-negotiable. Everything after this builds on them.
