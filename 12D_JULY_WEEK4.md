# JULY WEEK 4 (Jul 21–27) — Phase 1 Week 7: DYNAMIC MEMORY + LINKED LISTS + QUEUES

> **Topics**: malloc/calloc/realloc/free deep, Valgrind, singly linked list (all operations), doubly linked list, queue, circular buffer (full implementation)
> **K.N. King Reading**: Chapter 17 (Advanced Uses of Pointers — linked lists, function pointers)
> **K&R Bed Reading**: Chapter 5 revisit (Pointers and Arrays), Chapter 6 (Structures revisit)
> **YouTube**: mycodeschool "Data Structures" playlist (linked lists section) + Jacob Sorber "Valgrind" video
> **AI Policy**: BANNED for code — AI may only explain concepts
> **Dates**: Tuesday July 21 → Monday July 27, 2026

---

## WEEKDAY READING SCHEDULE (Jul 21–25)

### Tuesday July 21 — Pre-Gym (5:00–5:25 AM)
**Read**: K.N. King Chapter 17 (pages 1–20)
- Dynamic storage allocation: malloc, calloc, realloc, free
- malloc returns `void *`: must cast in C++ but not required in C — just assign directly
- ALWAYS check for NULL: `if (ptr == NULL) { perror("malloc"); exit(1); }`
- Deallocating: `free(ptr)` followed immediately by `ptr = NULL` — prevents dangling pointer
- Memory leak: allocated but never freed — program accumulates RAM usage
- Double free: freeing same pointer twice — undefined behavior, often crash

**Bed Reading (9:30–10:00 PM)**: K&R Chapter 5 pages 93–110 (revisit — you should understand this more deeply now)

### Wednesday July 22 — Pre-Gym (5:00–5:25 AM)
**Read**: K.N. King Chapter 17 (pages 20–40)
- Linked list fundamentals: Node struct with data + pointer to next
- Why linked list over array: O(1) insertion/deletion at head, no fixed size limit
- Why array over linked list: O(1) random access, cache-friendly, no pointer overhead
- Head pointer: a `Node *` that always points to the first element (or NULL if empty)
- Traversal: `while (current != NULL) { process(current); current = current->next; }`

**Bed Reading**: K&R Chapter 6 pages 127–145 (Structures revisit — focus on self-referential structs)

### Thursday July 23 — Pre-Gym (5:00–5:25 AM)
**Read**: K.N. King Chapter 17 (pages 40–end)
- Ordered linked list: insert at the right position to keep sorted
- Doubly linked list: `prev` pointer enables O(1) deletion without traversal
- Circular linked list: tail->next points back to head
- When to use each variant: singly (simple, memory efficient), doubly (bidirectional traversal)

**Bed Reading**: K&R Chapter 5 pages 110–125 (Array and pointer relationship, revisit)

### Friday July 24 — Pre-Gym (5:00–5:25 AM)
**Read**: Valgrind quick reference (search: "Valgrind memcheck guide" online)
- `valgrind --leak-check=full ./program`: run program under Valgrind
- "definitely lost": memory that was malloc'd but never freed — your fault
- "still reachable": memory that's reachable at exit but not freed — still a leak
- "invalid read/write": accessing memory you don't own (off-by-one, dangling pointer)
- "double free": freeing same memory twice
- How to interpret the output: look for "definitely lost: N bytes in M blocks"
- Build with `-g` for file + line numbers in Valgrind output

**Bed Reading**: K&R Chapter 6 pages 145–165 (Arrays of Structures, Pointers to Structures)

### Monday July 27 — Pre-Gym (5:00–5:25 AM)
**Read**: K.N. King Chapter 17 — re-read the linked list section
Focus on: the double pointer pattern (`Node **head`) when inserting at front, and why it's needed (hint: you need to modify the caller's head pointer, so you pass its address).

**Bed Reading**: K.N. King Chapter 17 — function pointers section (preview for Week 8)

---

## SATURDAY JULY 25 — LINKED LISTS + QUEUE + CIRCULAR BUFFER (7:30 AM–6:30 PM)

### Warmup (7:30–8:00 AM): Jacob Sorber YouTube
- "Linked Lists in C" by Jacob Sorber or mycodeschool (~15 min)
- "Valgrind" — short intro video by Jacob Sorber (~8 min)

### BLOCK 1 (8:00–9:30 AM): Singly Linked List — Complete Implementation
Write ALL from scratch. NO copy-paste. NO AI code.

```
week7/
├── linked_list.h       — All declarations and Node typedef
└── linked_list.c       — All implementations
```

**linked_list.h**:
```c
#ifndef LINKED_LIST_H
#define LINKED_LIST_H

typedef struct Node {
    int data;
    struct Node *next;
} Node;

Node *create_node(int data);
void  insert_front(Node **head, int data);
void  insert_back(Node **head, int data);
void  insert_sorted(Node **head, int data);    // maintain sorted order
void  delete_node(Node **head, int data);       // delete first occurrence
void  print_list(const Node *head);
int   list_length(const Node *head);
int   list_contains(const Node *head, int data);
void  reverse_list(Node **head);               // reverse in-place
Node *find_middle(const Node *head);           // Floyd's slow/fast pointer
void  free_list(Node **head);                  // free all nodes, set head to NULL

#endif
```

Implement ALL functions. Key rules:
- `insert_front` and `delete_node` take `Node **head` because they may change the head pointer
- `delete_node` must handle: empty list, deleting head, deleting middle, deleting tail, value not found
- `free_list` must free EVERY node AND set *head = NULL
- `reverse_list` uses three-pointer technique: `prev, current, next`
- `find_middle` uses slow/fast pointer: slow advances 1, fast advances 2 — when fast reaches end, slow is at middle

Draw `reverse_list` on paper step by step before implementing.

Test file `week7/list_test.c`:
```c
int main(void) {
    Node *list = NULL;

    insert_back(&list, 30);
    insert_front(&list, 10);
    insert_front(&list, 20);
    insert_sorted(&list, 15);   // sorted: 10 -> 15 -> 20 -> 30
    print_list(list);           // Expected: 10 -> 15 -> 20 -> 30 -> NULL

    printf("Length: %d\n", list_length(list));     // Expected: 4
    printf("Middle: %d\n", find_middle(list)->data); // Expected: 15 or 20

    delete_node(&list, 15);
    print_list(list);           // Expected: 10 -> 20 -> 30 -> NULL

    reverse_list(&list);
    print_list(list);           // Expected: 30 -> 20 -> 10 -> NULL

    free_list(&list);
    printf("After free: list = %p\n", (void *)list);  // Expected: (nil)

    return 0;
}
```

Run under Valgrind: `valgrind --leak-check=full ./list_test` — must show 0 leaks.

### BREAK (9:30–9:45)

### BLOCK 2 (9:45–11:15 AM): Circular Buffer — The Embedded Essential
```
week7/
├── cbuf.h          — Circular buffer declaration
└── cbuf.c          — Implementation
```

**cbuf.h**:
```c
#ifndef CBUF_H
#define CBUF_H

#include <stdint.h>

#define CBUF_SIZE 16    // Power of 2 — wrap uses % operator

typedef struct {
    uint8_t  buf[CBUF_SIZE];
    int      head;   // write position (next byte goes here)
    int      tail;   // read position (next byte comes from here)
    int      count;  // number of bytes currently in buffer
} CircBuf;

void    cbuf_init(CircBuf *cb);
int     cbuf_write(CircBuf *cb, uint8_t data);   // returns -1 if full
int     cbuf_read(CircBuf *cb, uint8_t *data);   // returns -1 if empty
int     cbuf_is_full(const CircBuf *cb);
int     cbuf_is_empty(const CircBuf *cb);
int     cbuf_count(const CircBuf *cb);

#endif
```

**cbuf.c** key logic:
- Write: `buf[head] = data; head = (head + 1) % CBUF_SIZE; count++;`
- Read: `*data = buf[tail]; tail = (tail + 1) % CBUF_SIZE; count--;`
- Full check: `count == CBUF_SIZE`
- Empty check: `count == 0`

Draw this as a circle on paper: 16 slots arranged in a ring. Head chases tail around the ring.

Test: write 12 bytes, read 8, write 8 more — head should wrap around. Verify order of bytes read is correct FIFO order.

> This EXACT circular buffer is what you will use on STM32 for UART receive in Phase 2 (August).
> The only change: `uint8_t` stays, but writes will happen from an interrupt handler.

### BREAK (11:15–11:30)

### BLOCK 3 (11:30 AM–12:30 PM): Queue
```
week7/
├── queue.h         — Array-based queue
└── queue.c         — Implementation
```

**Array-based queue using a circular buffer internally**:
```c
#define QUEUE_MAX 50

typedef struct {
    int data[QUEUE_MAX];
    int front;   // dequeue from here
    int rear;    // enqueue here
    int count;
} Queue;

void queue_init(Queue *q);
int  enqueue(Queue *q, int value);     // returns -1 if full
int  dequeue(Queue *q, int *value);    // returns -1 if empty
int  queue_peek(const Queue *q, int *value);  // read front without removing
int  queue_is_empty(const Queue *q);
int  queue_is_full(const Queue *q);
```

Test: enqueue 10 items, dequeue 5, enqueue 5 more. Verify FIFO order throughout.

### LUNCH (12:30–1:30 PM)

### GERMAN BLOCK 1 (1:30–4:30 PM)
- Nicos Weg Lessons 41–42
- Modal verbs: können, müssen, wollen, dürfen, sollen — practice in sentences
- Write 10 sentences using 3+ different modal verbs
- Anki: add 15 new cards

### GERMAN BLOCK 2 (5:00–6:30 PM)
- Nicos Weg Lessons 43–44
- AnkiDroid: review ALL pending cards
- Write from memory: your study goals using modal verbs ("Ich will ... Ich muss ...")

---

## SUNDAY JULY 26 — DOUBLY LINKED LIST + GIT + REVIEW (7:30 AM–4:00 PM)

### BLOCK 1 (7:30–9:00 AM): Doubly Linked List
```
week7/
├── dlist.h         — Doubly linked list
└── dlist.c         — Implementation
```

**dlist.h**:
```c
typedef struct DNode {
    int data;
    struct DNode *prev;
    struct DNode *next;
} DNode;

void  dlist_insert_back(DNode **head, DNode **tail, int data);
void  dlist_insert_front(DNode **head, DNode **tail, int data);
void  dlist_delete(DNode **head, DNode **tail, DNode *node);
void  dlist_print_forward(const DNode *head);
void  dlist_print_backward(const DNode *tail);
void  dlist_free(DNode **head, DNode **tail);
```

The key advantage: `dlist_delete` doesn't need to traverse to find the previous node — it already has `node->prev`. This makes deletion O(1).

Test: insert 5 nodes, print forward and backward, delete the middle node, print again.

### BLOCK 2 (9:15–10:30 AM): From Memory Challenges
Without looking at any previous code:
1. **Circular buffer** from memory — 20 min max. Write `cbuf.h` and `cbuf.c` completely.
2. **Singly linked list insert_front and free_list** — 10 min max.

If circular buffer in under 15 min → you're ready for Phase 2.

### GIT PUSH (10:30–11:00 AM)
```bash
cd ~/C-Practice
git add week7/
git commit -m "Week 7: singly linked list (all ops), doubly linked list, queue, circular buffer — all Valgrind clean"
git push origin main
```

Write `week7/README.md`:
- List every file
- One sentence per data structure: what it is and when to use it vs alternatives
- Section: "Circular buffer for embedded UART" — explain why embedded systems use this

### REST + LUNCH (11:00 AM–12:00 PM)

### GERMAN (12:00–2:00 PM)
- Nicos Weg Lessons 45–46
- Anki mega review (aim for 100+ words total)
- Write German from memory: what you implemented this week and why it matters for embedded

### EXTENDED CODING (2:00–4:00 PM): Dynamic Array
```
week7/
└── dynamic_array.c   — Growable array: start at 4, double when full, shrink when < 25% used
```

Implement a dynamic array (like C++ `std::vector` but in C):
```c
typedef struct {
    int    *data;
    int     size;       // number of elements currently stored
    int     capacity;   // total allocated slots
} DynArray;

void da_init(DynArray *a, int initial_capacity);
void da_push(DynArray *a, int value);      // grows if needed (double capacity)
int  da_pop(DynArray *a);                  // shrinks if < 25% used
int  da_get(const DynArray *a, int index);
void da_free(DynArray *a);
int  da_size(const DynArray *a);
```

Growth rule: when `size == capacity`, `realloc` to `capacity * 2`
Shrink rule: when `size < capacity / 4`, `realloc` to `capacity / 2` (minimum 4)

Test: push 20 items, pop 15 items (watch it shrink), verify all remaining items correct.
Run under Valgrind: 0 leaks, 0 invalid reads.

---

## WEEK 7 CHECKPOINT (Monday July 27, 4:00 PM)

Update PROGRESS.md now. Be honest.

| Checkpoint Item | Done? |
|:---|:---|
| Singly linked list: insert_front, insert_back, delete, reverse, free — from scratch | |
| Circular buffer: write/read with wraparound — Valgrind clean | |
| Can implement circular buffer from memory in under 20 minutes | |
| Queue: enqueue/dequeue with full/empty checks | |
| Doubly linked list: O(1) deletion with prev pointer | |
| Dynamic array: push/pop with automatic resize | |
| All programs run under Valgrind with 0 leaks | |
| GitHub: week7 pushed with README | |
| Nicos Weg: Lessons 41–46 done | |
| Anki: 100+ German words total | |
| K.N. King Ch 17 read | |

**Self-rating (data structures 1–10)**: ___ (minimum 6 before Week 8)

---

## WEEKDAY THEORY FOCUS (Week 7)

| Day | Read Before Gym | Bed Read |
|:---|:---|:---|
| Tue Jul 21 | K.N. King Ch 17 pp. 1–20 | K&R Ch 5 pp. 93–110 |
| Wed Jul 22 | K.N. King Ch 17 pp. 20–40 | K&R Ch 6 pp. 127–145 |
| Thu Jul 23 | K.N. King Ch 17 pp. 40–end | K&R Ch 5 pp. 110–125 |
| Fri Jul 24 | Valgrind guide (online) | K&R Ch 6 pp. 145–165 |
| Mon Jul 27 | K.N. King Ch 17 re-read linked list + double pointer | K.N. King Ch 17 — function pointers preview |

> The circular buffer you write this week is not just practice.
> You WILL use it on STM32 in August for UART interrupt-driven receive.
> Write it carefully. Learn it completely.
