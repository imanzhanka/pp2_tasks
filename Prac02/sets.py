# is unordered, unchangeable*, and unindexed, unoque 
# CAN NOT CHANGE but you can add elements

#example1
thisset = {"apple", "banana", "cherry"}
print(thisset)
thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset)

thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)

#example 2 add = remove
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)


tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical) # add items from another set into the current set
print(thisset)
thisset.remove("banana")
print(thisset)

thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)

x = thisset.pop()#removing random

#example3 - joinig sets 
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)
set3 = set1 | set2
print(set3)

set1.update(set2)
print(set1)

set3 = set1.intersection(set2)
print(set3)
set3 = set1 & set2
print(set3)
set1.intersection_update(set2)
print(set1)

set3 = set1.difference(set2)
print(set3)
set1.difference_update(set2)

set3 = set1.symmetric_difference(set2)
print(set3)
set3 = set1 ^ set2
print(set3)

#example4 - frozenset
x = frozenset({"apple", "banana", "cherry"})
print(x)
print(type(x))

#example5 
s = {1, 2, 3}
s.add(4)
print(s)