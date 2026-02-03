#ordered*, changeable and do not allow duplicates
#ex1
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)

#ex2:accessing 
x = thisdict["age"] #by the key
x = thisdict.get("age")#the same result
x = thisdict.keys()#give all key values

#ex3:Change Values
thisdict["year"] = 2018
thisdict.update({"year": 2020})#we can use it when need to update a few items 

#ex4: adding and deleting 
thisdict["color"] = "red"#через присваивание новый индекс 
thisdict.update({"color": "red"})
thisdict.pop("age")#deleting item by key name
thisdict.popitem()#last
del thisdict["name"]
del thisdict #deletes completely

#ex5: looping
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict:
  print(x) #output all the keys
for x in thisdict.values():
  print(x)

for x in thisdict:
  print(thisdict[x])#values
for x in thisdict.keys():
  print(x)

for x, y in thisdict.items():
  print(x, y)

#ex6 - copying dictionaries  
mydict = thisdict.copy()
mydict = dict(thisdict) 
print(mydict)

#ex7 - nested dictionary
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}
print(myfamily["child2"]["name"])#accessing elements

for x, obj in myfamily.items():#looping through the nested dict
  print(x)

  for y in obj:
    print(y + ':', obj[y]) 





