## Cache Eviction Policy
A cache eviction policy is a set of rules or algorithms used to decide which data to remove from a cache when it becomes full or when certain conditions are met. Since caches have limited storage, eviction policies are crucial to maintaining efficient cache performance and ensuring the most relevant or frequently accessed data stays in the cache.

## Common Cache Eviction Policies
Here are the most widely used cache eviction policies:

1. Least Recently Used (LRU)
- **Description**: Removes the data that has not been accessed for the longest time.
- **Use Case**: Suitable for workloads where recent data is more likely to be accessed again.
- **Example**: If cache holds {A, B, C} and A is the least recently accessed, adding D evicts A.

2. Least Frequently Used (LFU)
- **Description**: Removes the data that has been accessed the least number of times.
- **Use Case**: Useful for cases where frequently accessed items are more important.
- **Example**: If cache holds {A (5 accesses), B (2 accesses), C (1 access)}, adding a new item will evict C.

3. First In, First Out (FIFO)
- **Description**: Evicts the data that was added to the cache the earliest, regardless of how often it's accessed.
- **Use Case**: Easy to implement and works well if data follows a predictable access pattern.
- **Example**: If cache holds {A, B, C} and a new item D needs to be added, A will be evicted because it was added first.

4. Random Replacement
- **Description**: Evicts a randomly selected item.
- **Use Case**: Often used in low-complexity systems or in combination with other policies.
- **Example**: Randomly removes any item when the cache is full.

5. Most Recently Used (MRU)
- **Description**: Evicts the data that was most recently accessed.
- **Use Case**: Used in situations where recently used data is less likely to be reused (rare cases).
- **Example**: If {A, B, C} are in the cache and C was just accessed, adding D evicts C.

6. Least Recently Added (LRA)
- **Description**: Removes the data that has been in the cache the longest.
- **Use Case**: Similar to FIFO but focuses more on the insertion time.
- **Example**: Evicts the item that has remained untouched since it was added.

7. Time-To-Live (TTL)
- **Description**: Removes data that has been in the cache for a predefined time, regardless of access.
- **Use Case**: Ideal for time-sensitive data, such as user session information.
- **Example**: An item in the cache expires after 30 seconds, even if it is frequently accessed.

8. Adaptive Replacement Cache (ARC)
- **Description**: Balances between LRU and LFU by maintaining two lists: one for frequently used items and one for recently used items.
- **Use Case**: Provides better performance for workloads with mixed access patterns.

## Choosing the Right Eviction Policy
- **Access Pattern**: Understand your application's data access pattern. For instance:
  - Use LRU if recent data is more important.
  - Use LFU if frequent access indicates importance.
- **Latency Tolerance**: If eviction delays are critical, simpler policies like FIFO or Random Replacement may be better.
- **Memory Constraints**: Adaptive policies (e.g., ARC) might use additional memory for maintaining metadata.