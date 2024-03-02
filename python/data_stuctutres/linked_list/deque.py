from collections import deque

empty: deque[str] = deque()
print(empty)

empty.append("A")
print(empty)

empty.append("B")
print(empty)

empty.pop()
print(empty)

empty.appendleft("X")
print(empty)

empty.appendleft("Y")
print(empty)

empty.popleft()
print(empty)
