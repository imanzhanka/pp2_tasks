#ex1
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
#ex2
for x in "banana":
  print(x)

#ex3
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break

#ex4
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)

#ex5
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

  for x in range(6):
   print(x)
