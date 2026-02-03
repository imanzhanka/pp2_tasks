#example 1 - arithmetic operations
x = 15
y = 4

print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x % y)
print(x ** y)
print(x // y)

#example 2 - assignment operators
numbers = [1, 2, 3, 4, 5]

if (count := len(numbers)) > 3:
    print(f"List has {count} elements")

#example 3 - comparison operators
x = 5

print(1 < x < 10) #chain comparison operators

print(1 < x and x < 10)#logical operation
 
#example 4 - identity operators
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)
print(x is not y)
print(x == y)

#example 5 - membership operators
text = "Hello World"

print("H" in text)
print("hello" in text)
print("z" not in text)
 


