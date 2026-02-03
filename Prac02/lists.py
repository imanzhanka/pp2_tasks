
#example 1 - creatibg a list
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)

mylist = ["apple", "banana", "cherry"]

#example 2 - change kist items + add items + remove

thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)


thislist.insert(2, "watermelon")
print(thislist)

thislist.append("orange")
print(thislist)

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist) #delete first accurance of specific 

thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)#remove by index or last

del thislist[0]
print(thislist)#remove by index or whole list

thislist.clear()

#example 3 - comprehension
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)

newlist = [x for x in range(10) if x < 5]

newlist = [x.upper() for x in fruits]


#example 4 - sort + copy + join
thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)

def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc) # sorting data that was implemented after a function
print(thislist)

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse() #dont look at letter
print(thislist)

mylist = thislist.copy()

thislist = ["apple", "banana", "cherry"]
mylist = list(thislist) #the same as copy
print(mylist)

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]


#example 5 - join tuples 

list3 = list1 + list2

for x in list2:
  list1.append(x)
print(list1)

list1.extend(list2)
print(list1)
