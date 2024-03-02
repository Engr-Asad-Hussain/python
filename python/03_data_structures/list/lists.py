from sys import getsizeof

numbers: list[int] = []

for value in range(10):
    print(f"{numbers=} | {getsizeof(numbers)=}bytes")
    numbers.append(value)
    input("Press enter to continue ...")
