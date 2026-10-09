# Data Structures & Algorithms in Python

Six hands-on projects from a data structures and algorithms course (CEIS295). Each project implements a classic data structure or algorithm from scratch in Python, then **benchmarks it against realistic data** (up to 100,000 customer records) to compare real-world speed with theoretical Big-O behavior.

## Projects

| # | Folder | What it covers |
|---|--------|----------------|
| 1 | [`01-arraylist`](01-arraylist) | Custom resizable array-backed `ArrayList` (append, insert, remove, search), a timing harness and quicksort |
| 2 | [`02-linked-list`](02-linked-list) | Custom singly `LinkedList` built on a `Node` class, benchmarked on the same scenarios as the ArrayList |
| 3 | [`03-queue-call-distributor`](03-queue-call-distributor) | `Queue` built on the linked list, used in an **Automatic Call Distributor** simulation |
| 4 | [`04-sorting-algorithms`](04-sorting-algorithms) | Bubble, Selection, Insertion, Shell, Quick and Merge sort, timed at 100 to 100,000 records |
| 5 | [`05-searching-algorithms`](05-searching-algorithms) | Linear vs. binary search over sorted client records |
| 6 | [`06-binary-search-tree`](06-binary-search-tree) | Full binary search tree: insert, remove (leaf / one child / two children), search, min/max, in-/pre-/post-order traversal |

## Selected results

Sorting (seconds, measured on my machine; from `04-sorting-algorithms/Table of Sorting Speeds.xlsx`):

| Algorithm | 100 | 1,000 | 10,000 | 100,000 |
|-----------|-----|-------|--------|---------|
| Bubble Sort | 0.003 | 0.286 | 30.3 | ~50 min |
| Selection Sort | 0.002 | 0.203 | 20.4 | ~33 min |
| Insertion Sort | 0.002 | 0.159 | 16.2 | ~26 min |
| Shell Sort | 0.001 | 0.008 | 0.172 | 2.86 |
| Quicksort | 0.001 | 0.007 | 0.097 | 1.22 |
| Merge Sort | 0.001 | 0.006 | 0.092 | 1.22 |

The O(n²) sorts become unusable at 100,000 records, while O(n log n) sorts finish in about a second.

Searching 1,000 random records (seconds): linear search grows from 0.07 (100 records) to 9.47 (100,000 records), while binary search stays between 0.07 and 0.09 regardless of size.

## Running the code

Requires Python 3. Every project folder is self-contained; run scripts from inside their folder so the CSV files are found:

```bash
cd 04-sorting-algorithms
python SortingActualSpeeds.py
```

- `*ActualSpeed(s).py` are the benchmark scripts. In projects 4 and 5, switch datasets by uncommenting a different `ClientData*.csv` line at the top.
- Projects 1, 2 and 6 prompt `Continue (y/n)?` between scenarios.
- Project 3: `python AutomaticCallDistributor.py`, then enter how many seconds to simulate.
- The client records in the CSV files are sample/fake data supplied for the coursework.

## Notes

Originally written in Spyder as coursework (March–April 2022).
