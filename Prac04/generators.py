#1
def square_generator(N):
    for i in range(N + 1):
        yield i ** 2

# Usage
for square in square_generator(10):
    print(square)

#2
def even_generator(n):
    for i in range(0, n + 1, 2):
        yield i

n = int(input("Enter n: "))
print(", ".join(str(num) for num in even_generator(n)))

#3
def divisible_by_3_and_4(n):
    for i in range(0, n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

n = int(input("Enter n: "))
print(", ".join(str(num) for num in divisible_by_3_and_4(n)))

#4
def squares(a, b):
    for i in range(a, b + 1):
        yield i ** 2

a = int(input("Enter a: "))
b = int(input("Enter b: "))

for square in squares(a, b):
    print(square)

#5
def squares(a, b):
    for i in range(a, b + 1):
        yield i ** 2

a = int(input("Enter a: "))
b = int(input("Enter b: "))

for square in squares(a, b):
    print(square)
