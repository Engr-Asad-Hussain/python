## Content
- [Sorting Algorithms](#sorting-algorithms)
  - [Bubble Sort](#bubble-sort)
  - [Insertion Sort](#insertion-sort)


## Sorting Algorithms

### Bubble Sort
- Comparison based algorithm
- Each pair of adjacemt elements is compared and the elements are swapped if they are not in order.
- Time complexity `O(n²)`
- [Example](./XX1_bubble_sort_algorithm.py)

## Insertion Sort
- Comparison based algorithm
- Insertion Sort works the same way you might sort playing cards in your hands:
  - Start with one card (element),
  - Pick the next card and insert it into the correct position relative to the sorted part.
- Time complexity `O(n²)`
- [Example](./XX2_insertion_sort.py)

## Selection Sort
- Comparison based algorithm
- Works by repeatedly selecting the smallest element from the unsorted part of the array and moving it to the sorted part.
  - Find the smallest item and put it at the front.
  - Then find the next smallest and place it after the first.
  - Repeat until the list is sorted.
- Time complexity `O(n²)`
- [Example](./XX3_selection_sort.py)



####
🔹 Comparison-Based Sorting Algorithms
Efficient (Divide and Conquer) Sorts
Merge Sort – Stable, O(n log n)

Quick Sort – Unstable, O(n log n) avg

Heap Sort – Unstable, O(n log n)

Other Comparison-Based Sorts
Shell Sort – An optimization of insertion sort

TimSort – Hybrid of merge sort + insertion sort (used in Python/Java)

Tree Sort – Uses binary search tree (BST)

Smooth Sort – Based on a heap-like structure

Comb Sort – Improves bubble sort

Gnome Sort – Similar to insertion but swaps like bubble

Cocktail Shaker Sort – Bidirectional bubble sort

Stooge Sort – Inefficient, academic

🔹 Non-Comparison-Based Sorting Algorithms
These don't use comparisons and can achieve O(n) time under certain conditions:

Counting Sort – Best for small integer ranges

Radix Sort – For numbers/strings, sorts digit by digit

Bucket Sort – Distributes input into buckets, then sorts

Pigeonhole Sort – Like counting sort, for known ranges

Flash Sort – Combines distribution and partitioning

🔹 Parallel & External Sorting (Advanced)
Bitonic Sort – Used in parallel computing

Odd-Even Sort (Brick Sort) – Parallel-friendly

External Merge Sort – For huge datasets (disk-based)


###
🔹 Search Algorithms
Linear Search

Binary Search

Ternary Search

Exponential Search

Jump Search

Interpolation Search

🔹 Sorting Algorithms
Bubble Sort

Selection Sort

Insertion Sort

Merge Sort

Quick Sort

Heap Sort

Counting Sort

Radix Sort

Bucket Sort

Shell Sort

TimSort (Python’s built-in)

🔹 Divide and Conquer Algorithms
Merge Sort

Quick Sort

Binary Search

Closest Pair of Points

Karatsuba Multiplication

Strassen’s Matrix Multiplication

🔹 Greedy Algorithms
Activity Selection

Kruskal’s Algorithm (MST)

Prim’s Algorithm (MST)

Huffman Coding

Fractional Knapsack

Job Sequencing with Deadlines

Dijkstra’s Algorithm (shortest path)

Egyptian Fraction

🔹 Dynamic Programming (DP) Algorithms
0/1 Knapsack

Longest Common Subsequence (LCS)

Longest Increasing Subsequence

Matrix Chain Multiplication

Edit Distance

Coin Change

Partition Equal Subset Sum

DP on Trees

DP on Bitmask

🔹 Backtracking Algorithms
N-Queens Problem

Sudoku Solver

Subset Sum

Permutations / Combinations

Word Search

Knight’s Tour

🔹 Graph Algorithms
Breadth First Search (BFS)

Depth First Search (DFS)

Dijkstra’s Algorithm

Bellman-Ford Algorithm

Floyd-Warshall Algorithm

Kruskal’s Algorithm

Prim’s Algorithm

Topological Sort

Tarjan’s Algorithm (SCC)

Kosaraju’s Algorithm (SCC)

Union-Find (Disjoint Set Union)

Johnson’s Algorithm (All pairs shortest paths)

A* Search Algorithm

🔹 String Algorithms
Naive Pattern Searching

Rabin-Karp Algorithm

Knuth-Morris-Pratt (KMP) Algorithm

Z Algorithm

Boyer-Moore Algorithm

Trie and Suffix Tree

Aho-Corasick Algorithm

Longest Palindromic Substring (Manacher's)

Suffix Array & LCP Array

🔹 Mathematical Algorithms
Euclidean Algorithm (GCD)

Sieve of Eratosthenes (Prime numbers)

Fast Exponentiation (Modular exponentiation)

Matrix Exponentiation

Fermat’s Little Theorem

Chinese Remainder Theorem

Miller-Rabin Primality Test

Euler’s Totient Function

🔹 Geometric Algorithms
Convex Hull (Graham’s scan, Jarvis march)

Line Intersection

Sweep Line Algorithm

Closest Pair of Points

Rotating Calipers

Point in Polygon Test

🔹 Bit Manipulation Algorithms
Count set bits

Check if power of 2

XOR trick problems

Subset generation using bits

🔹 Game Theory Algorithms
Minimax Algorithm

Alpha-Beta Pruning

Grundy Numbers

Sprague-Grundy Theorem

🔹 Machine Learning / AI Algorithms (for reference)
Linear Regression

Logistic Regression

Decision Trees

k-Nearest Neighbors

Support Vector Machines

Gradient Descent

K-Means Clustering

Random Forest

Neural Networks

A* Algorithm (AI pathfinding)