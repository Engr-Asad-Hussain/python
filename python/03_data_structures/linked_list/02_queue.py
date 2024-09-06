from collections import deque

patients: deque[str] = deque()
input("Opening the hospital ...")
print(patients)
print()

input("John comes into the hospital at 3:00 pm")
patients.append("John")
print(patients)
print()

input("Alex comes into the hospital at 3:05 pm")
patients.append("Alex")
print(patients)
print()

input("Crawl comes into the hospital at 3:10 pm")
patients.append("Crawl")
print(patients)
print()

input("John completed his checkup and departed at 3:15 pm")
patients.popleft()
print(patients)
print()

input("Tom comes into the hospital at 3:20 pm")
patients.append("Tom")
print(patients)
print()

input("Alex completed his checkup and departed at 3:25 pm")
patients.popleft()
print(patients)
print()

input("Crawl completed his checkup and departed at 3:30 pm")
patients.popleft()
print(patients)
print()
