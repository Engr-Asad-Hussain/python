from collections import deque

# Single line garage
garage: deque[str] = deque()

input("Garage is empty at morning ... Garage has only single-lane parking space!")
print(garage)
print()

input("Honda Civic entered into the garage at 5:00 pm")
garage.appendleft("Honda Civic")
print(garage)
print()

input("Audi Q5 entered into the garage at 6:00 pm")
garage.appendleft("Audi Q5")
print(garage)
print()

input("Polestar entered into the garage at 12:00 pm")
garage.appendleft("Polestar")
print(garage)
print()

print("Next morning ...")
print()

input("Polestar leaved the garage 8:00 am")
garage.popleft()
print(garage)
print()

input("Audi Q5 leaved the garage 9:00 am")
garage.popleft()
print(garage)
print()

input("Honda Civic leaved the garage 10:00 am")
garage.popleft()
print(garage)
print()
