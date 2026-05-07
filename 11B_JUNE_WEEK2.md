# 📅 WEEK 2 — Jun 8-14 (Mon-Sun): DYNAMIC MEMORY + LINKED LISTS + QUEUES

> **Topics**: malloc/calloc/realloc/free deep, linked lists (singly, doubly), stacks, queues, circular buffers
> **K.N. King Chapters**: Ch 17 (Advanced Uses of Pointers — linked lists, function pointers)
> **K&R Bed Reading**: Chapter 5 revisit (Pointers and Arrays), Chapter 6 start (Structures)
> **FastBit Udemy**: Pointer deep sections, structure sections
> **Programs to write**: 8-10
> **German**: Nicos Weg Lessons 31-35, daily Anki, introduce accusative case
> **⚠️ THIS WEEK**: Every data structure you build here is used in FreeRTOS and embedded firmware.
> **📚 Full resource details**: See `10_RESOURCES.md`

---

## DAY 8 — Monday, Jun 8

### 🔶 Morning Block (5:10 - 6:30 AM) — DYNAMIC MEMORY DEEP DIVE

#### 📺 WATCH FIRST (10 min)

**Neso Academy**: "Dynamic Memory Allocation in C" (~10 min)

#### 💻 CODE (1h 10m)

**Exercise 1 — malloc vs calloc vs realloc (5:20-5:50):**

Create `week7/memory_deep.c`:
```c
#include <stdio.h>
#include <stdlib.h>

int main(void) {
    // malloc — uninitialized memory
    int *arr1 = malloc(5 * sizeof(int));
    printf("malloc (uninitialized):\n");
    for (int i = 0; i < 5; i++) {
        printf("  arr1[%d] = %d\n", i, arr1[i]);  // Garbage values!
    }
    
    // calloc — zero-initialized memory
    int *arr2 = calloc(5, sizeof(int));
    printf("calloc (zero-initialized):\n");
    for (int i = 0; i < 5; i++) {
        printf("  arr2[%d] = %d\n", i, arr2[i]);  // All zeros!
    }
    
    // realloc — resize existing allocation
    arr1 = realloc(arr1, 10 * sizeof(int));
    for (int i = 5; i < 10; i++) {
        arr1[i] = i * 100;
    }
    printf("realloc (expanded to 10):\n");
    for (int i = 0; i < 10; i++) {
        printf("  arr1[%d] = %d\n", i, arr1[i]);
    }
    
    // ALWAYS free
    free(arr1);
    free(arr2);
    arr1 = NULL;  // Prevent dangling pointer
    arr2 = NULL;
    
    return 0;
}
```

**Exercise 2 — Dynamic 2D array (5:50-6:10):**

Create `dynamic_2d.c`:
```c
#include <stdio.h>
#include <stdlib.h>

int main(void) {
    int rows = 3, cols = 4;
    
    // Allocate array of pointers (rows)
    int **matrix = malloc(rows * sizeof(int *));
    
    // Allocate each row
    for (int i = 0; i < rows; i++) {
        matrix[i] = calloc(cols, sizeof(int));
    }
    
    // Fill with values
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            matrix[i][j] = i * cols + j;
        }
    }
    
    // Print
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            printf("%3d ", matrix[i][j]);
        }
        printf("\n");
    }
    
    // Free in REVERSE order (rows first, then array of pointers)
    for (int i = 0; i < rows; i++) {
        free(matrix[i]);
    }
    free(matrix);
    
    return 0;
}
```

**Draw the memory diagram on paper**: Show heap layout with `matrix` pointer → array of row pointers → each row's data.

#### 📖 READ (6:10-6:30)
- **K.N. King Ch 17**: Sections 17.1-17.3 (Dynamic storage allocation, dynamically allocated strings)

### ✅ Day 8 Checklist
- [ ] Understand malloc vs calloc vs realloc
- [ ] Dynamic 2D array allocated and freed correctly
- [ ] Memory diagram drawn on paper (pointer → row pointers → data)
- [ ] Ran with Valgrind — 0 leaks

---

## DAY 9 — Tuesday, Jun 9

### 🔶 Morning Block (5:10 - 6:30 AM) — SINGLY LINKED LIST (Part 1)

#### 💻 CODE (1h 20m)

Create `week7/linked_list.c` and `linked_list.h`:

**`linked_list.h`**:
```c
#ifndef LINKED_LIST_H
#define LINKED_LIST_H

typedef struct Node {
    int data;
    struct Node *next;
} Node;

// Core operations
Node *create_node(int data);
void insert_front(Node **head, int data);
void insert_back(Node **head, int data);
void insert_at(Node **head, int index, int data);
void delete_node(Node **head, int data);
void print_list(const Node *head);
int list_length(const Node *head);
void free_list(Node **head);

#endif
```

Implement ALL functions in `linked_list.c`. Write from scratch — do NOT use AI.

Key rules:
- `insert_front` modifies the head pointer → needs `Node **head` (pointer to pointer)
- `delete_node` must handle: empty list, delete head, delete middle, delete tail, not found
- `free_list` must free EVERY node and set head to NULL

**Test in `main.c`**:
```c
#include <stdio.h>
#include "linked_list.h"

int main(void) {
    Node *list = NULL;
    
    insert_front(&list, 10);
    insert_front(&list, 20);
    insert_back(&list, 30);
    insert_at(&list, 1, 15);
    print_list(list);  // Expected: 20 -> 15 -> 10 -> 30 -> NULL
    
    printf("Length: %d\n", list_length(list));
    
    delete_node(&list, 15);
    print_list(list);  // Expected: 20 -> 10 -> 30 -> NULL
    
    free_list(&list);
    print_list(list);  // Expected: (empty list)
    
    return 0;
}
```

Write a **Makefile** for this project.

### ✅ Day 9 Checklist
- [ ] Linked list header with all function declarations
- [ ] insert_front, insert_back, insert_at implemented
- [ ] delete_node handles all edge cases
- [ ] free_list frees everything
- [ ] Makefile written, project builds cleanly

---

## DAY 10 — Wednesday, Jun 10

### 🔶 Morning Block (5:10 - 6:30 AM) — LINKED LIST (Part 2) + ADVANCED OPS

#### 💻 CODE (1h 20m)

Add these functions to your linked list:

```c
// Advanced operations — add to linked_list.h
Node *search(const Node *head, int data);    // Returns node or NULL
void reverse(Node **head);                    // Reverse in-place
Node *find_middle(const Node *head);          // Floyd's algorithm
int has_cycle(const Node *head);              // Cycle detection
void sort_list(Node **head);                  // Insertion sort on linked list
void remove_duplicates(Node **head);          // Remove duplicate values
```

Implement each one. The tricky ones:

**`reverse`** — three pointer technique:
```
prev = NULL, current = head, next = NULL
while (current != NULL):
    next = current->next
    current->next = prev
    prev = current
    current = next
head = prev
```

**Draw this on paper step by step.** This is an interview classic.

**`find_middle`** — slow/fast pointer (Floyd's):
```
slow = head, fast = head
while (fast != NULL && fast->next != NULL):
    slow = slow->next
    fast = fast->next->next
return slow  // slow is at the middle
```

### 🇩🇪 German (if Wednesday is German morning)
- Nicos Weg Lesson 31-32

### ✅ Day 10 Checklist
- [ ] reverse implemented — can draw the 3-pointer technique on paper
- [ ] find_middle using Floyd's slow/fast pointers
- [ ] sort_list working (insertion sort on linked list)
- [ ] All functions tested and debugged with GDB

---

## DAY 11 — Thursday, Jun 11

### 🔶 Morning Block (5:10 - 6:30 AM) — STACK IMPLEMENTATION

#### 💻 CODE (1h 20m)

Create `week7/stack.c` and `stack.h`:

Implement stack TWO ways:

**Method 1 — Array-based stack:**
```c
#define STACK_MAX 100

typedef struct {
    int data[STACK_MAX];
    int top;  // Index of top element (-1 when empty)
} ArrayStack;

void stack_init(ArrayStack *s);
int stack_push(ArrayStack *s, int value);  // Returns 0 on success, -1 on overflow
int stack_pop(ArrayStack *s, int *value);  // Returns 0 on success, -1 on underflow
int stack_peek(const ArrayStack *s, int *value);
int stack_is_empty(const ArrayStack *s);
int stack_is_full(const ArrayStack *s);
```

**Method 2 — Linked list-based stack:**
```c
typedef struct StackNode {
    int data;
    struct StackNode *next;
} StackNode;

typedef struct {
    StackNode *top;
    int size;
} LinkedStack;

void lstack_init(LinkedStack *s);
void lstack_push(LinkedStack *s, int value);
int lstack_pop(LinkedStack *s, int *value);
int lstack_is_empty(const LinkedStack *s);
void lstack_free(LinkedStack *s);
```

**Application — Balanced parentheses checker:**

Use your stack to check if a string has balanced brackets: `{[()]}` → valid, `{[(])}` → invalid

### ✅ Day 11 Checklist
- [ ] Array-based stack working with overflow/underflow protection
- [ ] Linked list-based stack working with dynamic memory
- [ ] Balanced parentheses checker using your stack
- [ ] Can explain: why stack for function calls? (preview for STM32 call stack)

---

## DAY 12 — Friday, Jun 12

### 🔶 Morning Block (5:10 - 6:30 AM) — QUEUE + CIRCULAR BUFFER

#### 💻 CODE (1h 20m)

**Exercise 1 — Array-based queue (5:10-5:40):**

Create `week7/queue.c`:
```c
#define QUEUE_MAX 100

typedef struct {
    int data[QUEUE_MAX];
    int front;
    int rear;
    int count;
} Queue;

void queue_init(Queue *q);
int enqueue(Queue *q, int value);
int dequeue(Queue *q, int *value);
int queue_peek(const Queue *q, int *value);
int queue_is_empty(const Queue *q);
int queue_is_full(const Queue *q);
```

**Exercise 2 — Circular buffer (5:40-6:20):**

This is THE most important data structure for embedded. Used for UART RX buffers, sensor data pipes, audio streams.

Create `week7/circular_buffer.c` and `circular_buffer.h`:
```c
#define CBUF_SIZE 16  // Power of 2 for efficiency

typedef struct {
    uint8_t buffer[CBUF_SIZE];
    int head;   // Write position
    int tail;   // Read position
    int count;  // Number of elements
} CircularBuffer;

void cbuf_init(CircularBuffer *cb);
int cbuf_write(CircularBuffer *cb, uint8_t data);
int cbuf_read(CircularBuffer *cb, uint8_t *data);
int cbuf_is_full(const CircularBuffer *cb);
int cbuf_is_empty(const CircularBuffer *cb);
int cbuf_count(const CircularBuffer *cb);
```

**Key insight**: `head = (head + 1) % CBUF_SIZE` wraps around. Draw this on paper as a circle.

> **⚠️ YOU WILL USE THIS EXACT circular buffer on STM32 for UART receive in Phase 2.**

### ✅ Day 12 Checklist
- [ ] Queue with enqueue/dequeue working
- [ ] Circular buffer with wrap-around working
- [ ] Drew circular buffer diagram on paper (the ring)
- [ ] Understand why circular buffer is essential for embedded

---

## DAY 13 — Saturday, Jun 13 (DEEP STUDY DAY)

### 💻 C Deep Sessions (6:30 AM - 12:45 PM)

**Session 1 (6:30-7:30)**: Doubly linked list implementation
- Add `prev` pointer to Node struct
- Implement insert, delete, reverse for doubly linked list
- Compare with singly linked list — when is each better?

**Session 2 (7:45-9:15)**: K.N. King Ch 17 exercises
- Do every exercise in Chapter 17
- Focus on: linked list manipulation, dynamic array resizing

**Session 3 (9:30-11:00)**: Hash table (stretch goal)
- Implement a simple hash table with chaining (array of linked lists)
- `hash(key) = key % TABLE_SIZE`
- insert, search, delete operations

**Session 4 (11:15-12:45)**: Interview prep — Data structure questions
Write answers for:
1. "When would you use a linked list vs an array?"
2. "Explain how a circular buffer works and where it's used in embedded"
3. "What is a stack overflow and how do you prevent it on a microcontroller?"
4. "Implement a queue using two stacks" (classic!)
5. "What is the time complexity of insert/delete/search for linked list vs array?"

### 🇩🇪 German (2:00-5:00 PM)
- Nicos Weg Lessons 33-35
- Write 5 sentences using new vocabulary
- Anki review (aim for 130+ cards total)

### ✅ Day 13 Checklist
- [ ] Doubly linked list working
- [ ] K.N. King Ch 17 exercises done
- [ ] Hash table implemented (bonus)
- [ ] 5 interview answers written

---

## DAY 14 — Sunday, Jun 14 (REVIEW + GIT)

### 💻 Morning (7:30 AM - 12:30 PM)

**7:30-9:00**: From a blank file, implement linked list from MEMORY. No reference. Time yourself.
- Target: complete singly linked list (insert, delete, search, reverse, free) in < 30 minutes
- If you can't → repeat until you can. This is interview prep.

**9:15-10:45**: From a blank file, implement circular buffer from MEMORY.
- Target: complete in < 15 minutes

**11:00-12:30**: Git push. Write README for week7 folder explaining every data structure.

### 🇩🇪 German (2:00-4:00 PM)
- Full A1 review (lessons 1-35)
- Anki mega review
- By now: ~135 words, simple past tense, can introduce yourself + daily routine

### ✅ Day 14 Checklist
- [ ] Linked list from memory in < 30 min
- [ ] Circular buffer from memory in < 15 min
- [ ] All week 7 code pushed to GitHub
- [ ] README documenting each data structure

---

## 📋 WEEK 2 CHECKPOINT

- [ ] ✅ malloc/calloc/realloc/free — understand all, can draw heap diagrams
- [ ] ✅ Singly linked list: insert, delete, search, reverse, sort, find_middle — ALL from scratch
- [ ] ✅ Stack: array-based AND linked list-based
- [ ] ✅ Queue: array-based with enqueue/dequeue
- [ ] ✅ Circular buffer — THE embedded essential. Can write from memory.
- [ ] ✅ All tested with GDB and Valgrind (0 memory leaks)
- [ ] ✅ Nicos Weg lessons 31-35, 130+ Anki cards
- [ ] ✅ Can re-implement linked list and circular buffer from memory under time pressure
