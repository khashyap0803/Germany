# 📅 WEEK 4 — May 19-25 (Tue-Mon): STRUCTS + BITWISE — Gateway to STM32

> **Topics**: struct, typedef, nested structs, pointer to struct, bitwise operators, bit manipulation, register simulation
> **K&R Chapters**: Chapter 6 (Structures), Chapter 2 revisit (Bitwise section pp. 48-53)
> **Programs to write**: 10-12
> **German**: Nicos Weg Lessons 16-20, food vocab, daily routine sentences
> **Embedded Connection**: THIS week is the bridge to hardware. Structs = how STM32 peripheral registers are organized. Bitwise = how you read/write individual register bits.
> **📚 Full resource details**: See `10_RESOURCES.md`

---

## DAY 19 — Tuesday, May 19

### 🔶 Morning (5:10-6:30 AM) — struct Basics

---

#### 📺 WATCH FIRST (20 min) — 5:10 to 5:30 AM

1. **Neso Academy: "Structures in C (Part 1)"** (~10 min)
   - Focus on: Why structs exist (group related data), declaring, accessing members with `.`
2. **Neso Academy: "Structures in C (Part 2)"** (~8 min)
   - Focus on: Array of structs, initializing structs

> **Alternative**: **Jacob Sorber: "Structs in C — everything you need to know"** (~15 min) — more practical, terminal demos

---

#### 📖 READ (5 min)

- **K&R Chapter 6** pages 127-133 (Structure basics). Notice how K&R introduces structs for representing points and rectangles — very elegant.
- Or: **Beej's Guide** → "Structs" → https://beej.us/guide/bgc/html/split/structs.html

---

#### 💻 CODE (45 min) — 5:30 to 6:15 AM

**Program 1 — `struct_basics.c`:**
- Define: `struct Student { char name[50]; float cgpa; char branch[30]; int year; };`
- Use `typedef` to create a cleaner alias: `typedef struct Student Student;` — now you write `Student s;` instead of `struct Student s;`
- Create a student, fill in values, print everything
- Create an array of 3 students, fill them, print in table format
- **What to understand**: Struct members are stored contiguously in memory (with possible padding for alignment). Draw the memory layout on paper!
- **Ask Google AI**: "Explain struct padding and alignment in C. Why does `sizeof(struct)` sometimes give a larger number than I expect?"

---

#### 🧪 TEST YOURSELF

- **learn-c.org**: "Structures" → https://www.learn-c.org/en/Structures
- **HackerRank**: "Boxes through a Tunnel" → https://www.hackerrank.com/challenges/too-high-boxes (uses structs)

---

### 🎧 Commute: Nicos Weg Lesson 16 | 📱 Lunch: Anki | 📖 Bed: K&R pp. 133-140 (struct and pointers)

### ✅ Day 19: `struct_basics.c` with typedef and array of structs.

---

## DAY 20 — Wednesday, May 20

### 🔶 Morning (5:10-6:30 AM) — 🇩🇪 German + Struct Pointers

---

#### 📺 GERMAN (15 min) — 5:10 to 5:25 AM

- **DW Nicos Weg app**: Lesson 17
- **Learn German with Anja** (YouTube): Search "German Food Vocabulary" (~10 min)
  - New words: das Brot (bread), die Milch (milk), der Käse (cheese), das Wasser (water), der Kaffee (coffee)

---

#### 📺 WATCH (15 min) — 5:25 to 5:40 AM

1. **Neso Academy: "Pointer to Structure in C"** (~10 min)
   - Focus on: The `->` (arrow) operator. `ptr->name` is the same as `(*ptr).name` — arrow is cleaner.
2. **Neso Academy: "Passing Structures to Functions"** (~8 min)
   - Focus on: Pass by value (copies entire struct — wasteful!) vs pass by pointer (efficient, uses `->`)

---

#### 💻 CODE (40 min) — 5:40 to 6:20 AM

**Program 2 — `struct_functions.c`:**
- Write `void print_student(Student s)` — pass struct by VALUE (copies entire struct!)
- Write `void print_student_ptr(Student *s)` — pass by POINTER (efficient, no copy), use `s->name`, `s->cgpa`
- Write `void update_cgpa(Student *s, float new_cgpa)` — modify through pointer
- **Key learning**: In embedded, you ALWAYS pass structs by pointer. Copying 100-byte structs wastes precious stack space.

**Program 3 — `nested_structs.c`:**
- Define `struct Address { char city[30]; int pincode; };`
- Define `struct Employee { char name[50]; struct Address addr; float salary; };`
- Access: `emp.addr.city` or with pointer: `emp_ptr->addr.city`

---

#### 🧪 TEST YOURSELF

- **HackerRank**: "Small Triangles, Large Triangles" → https://www.hackerrank.com/challenges/small-triangles-large-triangles (sorting structs)

---

### 📖 Bed: K&R pp. 48-53 (bitwise operators section — read this TONIGHT for tomorrow!)

### ✅ Day 20: `struct_functions.c` + `nested_structs.c`. German food vocab started.

---

## DAY 21 — Thursday, May 21

### 🔶 Morning (5:10-6:30 AM) — Bitwise Operators

---

#### 📺 WATCH FIRST (25 min) — 5:10 to 5:35 AM

1. **Neso Academy: "Bitwise Operators in C (Part 1)"** (~12 min)
   - Focus on: AND `&`, OR `|`, XOR `^`, NOT `~` — with truth tables
2. **Neso Academy: "Bitwise Operators in C (Part 2)"** (~10 min)
   - Focus on: Left shift `<<`, Right shift `>>` — these are multiply/divide by powers of 2!

> **Supplement**: **Jacob Sorber: "Bit manipulation in C"** (~12 min) — practical embedded examples

---

#### 📖 READ — K&R pp. 48-53 (Bitwise Operators section in Chapter 2)

---

#### 💻 CODE (40 min) — 5:35 to 6:15 AM

**Program 4 — `bitwise_basics.c`:**
- Print a number in binary (write a function that prints each bit)
- Demonstrate AND: `a & b` — used for MASKING (checking if a specific bit is set)
- Demonstrate OR: `a | b` — used for SETTING bits
- Demonstrate XOR: `a ^ b` — used for TOGGLING bits
- Demonstrate NOT: `~a` — inverts all bits
- Demonstrate shifts: `1 << 3` = 8 (set bit 3), `16 >> 2` = 4

**Program 5 — `bit_manipulation.c`:**
Write these 4 essential macros (you'll use them on STM32!):
```c
#define SET_BIT(reg, bit)    ((reg) |=  (1 << (bit)))
#define CLEAR_BIT(reg, bit)  ((reg) &= ~(1 << (bit)))
#define TOGGLE_BIT(reg, bit) ((reg) ^=  (1 << (bit)))
#define CHECK_BIT(reg, bit)  ((reg) &   (1 << (bit)))
```
- Test each: set bit 3, clear bit 3, toggle bit 5, check if bit 7 is set
- Print the number in binary before and after each operation

---

#### 🧪 TEST YOURSELF

- **HackerRank**: "Bitwise Operators" → https://www.hackerrank.com/challenges/bitwise-operators-in-c
- **Ask Google AI**: "In STM32, how do I set GPIO pin 5 HIGH using bitwise operations on the BSRR register?"

---

### 🎧 Commute: Nicos Weg Lesson 18 | 📖 Bed: K&R bitwise section re-read

### ✅ Day 21: `bitwise_basics.c` + `bit_manipulation.c` with 4 essential macros. **THIS IS DIRECT STM32 PREP.**

---

## DAY 22 — Friday, May 22

### 🔶 Morning (5:10-6:30 AM) — 🇩🇪 German + Bit Fields & Structs Combined

---

#### 📺 GERMAN (15 min) — 5:10 to 5:25 AM

- **DW Nicos Weg app**: Lesson 19
- Practice: "Ich lerne Deutsch." "Ich arbeite bei Unistring." "Ich möchte in Deutschland studieren."

---

#### 📺 WATCH (12 min) — 5:25 to 5:37 AM

- **Neso Academy: "Bit Fields in C"** (~10 min)
  - Focus on: Controlling exactly how many bits each struct member uses. Used in embedded for memory-mapped I/O.
- Search YouTube: **"Bit manipulation for embedded systems"** — any short video (<10 min)

---

#### 💻 CODE (45 min) — 5:37 to 6:22 AM

**Program 6 — `bit_fields.c`:**
```c
typedef struct {
    unsigned int led_on    : 1;  // 1 bit: 0 or 1
    unsigned int mode      : 3;  // 3 bits: 0-7
    unsigned int speed     : 4;  // 4 bits: 0-15
    unsigned int reserved  : 24; // remaining bits
} GPIO_Config;
```
- Set `config.led_on = 1;` `config.mode = 5;` `config.speed = 10;`
- Print `sizeof(GPIO_Config)` — it's 4 bytes (32 bits total), packed!
- **This is EXACTLY how STM32 peripheral registers are defined in the CMSIS headers.**

**Program 7 — `register_simulator.c`:**
- Create a struct representing a 32-bit hardware register
- Write functions: `set_bit()`, `clear_bit()`, `toggle_bit()`, `read_bit()`
- Print the register in binary after each operation
- Simulate: "Turn on LED on pin 5" → `SET_BIT(GPIOA_ODR, 5)`
- **THIS program simulates EXACTLY what you'll do on STM32 in July.**

---

#### 🧪 TEST YOURSELF

- Look at the actual STM32F411 reference manual GPIO chapter (just skim the register description page) — can you see how the struct/bitwise patterns you just wrote map to real hardware?

---

### 📖 Bed: K&R Chapter 6 self-referential structures (pp. 140-145 — linked lists preview)

### ✅ Day 22: `bit_fields.c` + `register_simulator.c`. The bridge to real hardware.

---

## DAY 23 — Saturday, May 23 🟩 BIG DAY

### 💻 Warmup (6:30-7:30 AM) — Linked List Part 1

---

#### 📺 WATCH FIRST (25 min) — 6:30 to 6:55 AM

1. **mycodeschool: "Introduction to Linked List"** (~11 min)
   - Search: https://www.youtube.com/watch?v=NobHlGUjV3g
   - Focus on: Why linked lists exist (dynamic size, efficient insert/delete), vs arrays (random access, contiguous)
2. **mycodeschool: "Inserting a node at beginning"** (~12 min)
   - Focus on: Creating a node with `malloc`, setting `next` pointer, updating `head`

> **Alternative**: **Neso Academy: "Linked List in C"** (~15 min)

---

#### 📖 READ — K&R pp. 140-145 (self-referential structures, linked allocation)

---

#### 💻 CODE (35 min) — 6:55 to 7:30 AM

**Program 8 — `linked_list.c`** (Part 1):
```c
typedef struct Node {
    int data;
    struct Node *next;  // self-referential!
} Node;
```
- Create nodes with `malloc`
- Link them: `node1->next = node2;`
- Traverse and print all nodes
- Insert at beginning (update head pointer)

---

### 💻 Deep Session 1 (7:45-9:15 AM) — Linked List Part 2

---

#### 📺 WATCH (20 min) — 7:45 to 8:05 AM

1. **mycodeschool: "Inserting a node at nth position"** (~12 min)
2. **mycodeschool: "Deleting a node at nth position"** (~10 min)

---

#### 💻 CODE (65 min) — 8:05 to 9:10 AM

Continue `linked_list.c`:
- Insert at end
- Insert at position N
- Delete by value
- Delete by position
- Reverse the list (the classic interview question!)
- Print count of nodes

---

### 💻 Deep Session 2 (9:30-11:00 AM) — Combined Struct + Bitwise Project

---

#### 💻 CODE — **"Hardware Register Simulator"** (extended weekend project)

Build a complete register simulation combining everything from this week:
- Define a `Peripheral` struct with multiple 32-bit registers
- Simulate GPIO: ODR (output data register), IDR (input data register), MODER (mode register)
- Write functions: `gpio_set_mode(pin, mode)`, `gpio_write(pin, value)`, `gpio_read(pin)`
- Print register state in binary/hex after each operation
- **This is your first "embedded" program** — even though it runs on your PC, the logic is identical to real STM32 driver code.

---

### 💻 Deep Session 3 (11:15 AM-12:45 PM) — More Linked List Practice

---

#### 📺 WATCH (10 min)

- **mycodeschool: "Reverse a linked list (iterative)"** (~10 min)

---

#### 💻 CODE

- Implement reverse linked list from scratch (iterative, using 3 pointers)
- If time: implement reverse recursively
- Push all code to GitHub with README updates

---

### 🇩🇪 German (2:00-5:00 PM)

- **DW Nicos Weg**: Lessons 19-20 (2:00-3:30 PM)
- **Learn German with Anja** (YouTube): "German Daily Routine Vocabulary" (~12 min)
  - aufstehen (wake up), frühstücken (have breakfast), arbeiten (work), lernen (study), schlafen (sleep)
- **Google AI Pro** voice mode (3:45-5:00 PM): Describe your daily routine in German
- **Anki**: Add 10 new cards (daily routine verbs + food vocab)

---

### ✅ Day 23: `linked_list.c` (full CRUD) + hardware register simulator project + Git push. German daily routine.

---

## DAY 24 — Sunday, May 24 🟨 REVIEW + PRACTICE

### 💻 Practice (7:30-9:00 AM) — typedef Patterns + Enum Preview

---

#### 📺 WATCH (15 min) — 7:30 to 7:45 AM

- **Neso Academy: "typedef in C"** (~8 min)
  - Focus on: `typedef` creates aliases. `typedef unsigned int uint32_t;` — THIS is how STM32 header files define types.
- **Neso Academy: "Unions in C"** (~10 min)
  - Focus on: Union members share the SAME memory (unlike struct where each gets its own)

---

#### 💻 CODE (60 min) — 7:45 to 8:45 AM

**Program 9 — `typedef_patterns.c`:**
- `typedef unsigned char  uint8_t;`  ← 8-bit unsigned (used everywhere in embedded)
- `typedef unsigned short uint16_t;` ← 16-bit unsigned
- `typedef unsigned int   uint32_t;` ← 32-bit unsigned
- `typedef void (*callback_t)(void);` ← function pointer typedef
- **This is EXACTLY what `<stdint.h>` defines.** Embedded code uses `uint8_t`, `uint16_t`, `uint32_t` instead of `int`, `short`, etc. for portability.

**Program 10 — `union_demo.c`:**
- Show that union members share space: changing one changes the other
- Use case: Parse a 32-bit register as either a whole `uint32_t` or 4 separate `uint8_t` bytes

---

### 💻 MEMORY TEST (9:15-12:00 PM)

Close ALL references. Write from memory:
1. A struct with typedef, passed to function by pointer (using `->`)
2. The 4 bitwise macros: SET, CLEAR, TOGGLE, CHECK
3. A linked list: create 3 nodes, print all, reverse the list
4. The circular buffer from last week

**Rate yourself**:
- Can you write all 4? → Ready for Week 5
- Can write 2-3? → OK, review the weak ones tonight
- Can write 0-1? → STOP. Re-watch videos and practice before moving on.

---

### 🇩🇪 German (2:00-4:00 PM) + 📋 Weekly Review (4:00-4:30 PM)

- Anki mega review. Target: 60+ cards reviewed.
- **Notion**: Log Week 4 metrics, rate understanding of structs/bitwise, plan Week 5

---

### ✅ Day 24: `typedef_patterns.c` + `union_demo.c` + memory re-write test. Weekly review.

---

## DAY 25 — Monday, May 25 🟦 WEEKDAY

### 🔶 Morning (5:10-6:30 AM) — Refactor ALL Programs with typedef

---

#### 💻 CODE (70 min) — 5:10 to 6:20 AM

Go through your Week 4 programs and:
1. Replace all `int` with `int32_t` (from `<stdint.h>`) where appropriate
2. Replace all `unsigned int` with `uint32_t`
3. Add `const` to function parameters that shouldn't be modified
4. This is **embedded coding style** — start writing like a firmware engineer

---

#### 🧪 PREPARE FOR WEEK 5

- Preview: K&R Chapter 4 (preprocessor section, pp. 86-92) — read tonight before bed
- Search YouTube: **Jacob Sorber "volatile in C"** — bookmark for Day 27
- Search YouTube: **Jacob Sorber "State Machines in C"** — bookmark for Day 26

---

### 🎧 Commute: Nicos Weg Lesson 20 | 📱 Lunch: Anki | 📖 Bed: K&R pp. 86-92 (preprocessor preview)

### ✅ Day 25: Refactored code with stdint.h types. Week 5 resources bookmarked.

---

## 📊 WEEK 4 SUMMARY

| Metric | Target | Done? |
|:---|:---|:---|
| Programs written | 10+ (cumulative 40+) | [ ] |
| Neso Academy videos watched | 8-10 | [ ] |
| mycodeschool linked list videos | 4-5 | [ ] |
| Comfortable with structs and typedef | YES | [ ] |
| Can do bitwise SET/CLEAR/TOGGLE/CHECK | YES — essential for STM32 | [ ] |
| Hardware register simulator working | YES | [ ] |
| Linked list implemented from scratch | YES (insert, delete, print, reverse) | [ ] |
| Understand unions and bit fields | YES | [ ] |
| K&R pp. 48-53 + 127-150 read | YES | [ ] |
| Nicos Weg lessons | 16-20 (cumulative: 20) | [ ] |
| German words in Anki | 70+ (cumulative) | [ ] |
| **PUSH 3+ programs to GitHub** | YES | [ ] |
