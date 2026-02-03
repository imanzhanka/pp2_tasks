#tuples - ordered, unchangeable, and allow duplicate values, indexed

#examples 1
thistuple = ("apple", "banana", "cherry")
# you have to add a comma after the item, otherwise Python will not recognize it as a tuple.
thistuple = ("apple",)
print(type(thistuple))
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)

#example 2 - existance + convert tuples  
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")

# You can convert the tuple into a list, change the list,
#  and convert the list back into a tuple

x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

y = ("orange",) # You are allowed to add tuples to tuple
thistuple += y

print(thistuple)
del thistuple





#example 3 - unpack tuples 
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits # * to the variable name  as a list:
print(green)
print(yellow)
print(red)

#example 4 - join tuples 
mytuple = fruits * 2
print(mytuple)

#example 5 - methods
print(fruits.index("banana"))  
print(fruits.count("banana"))  

