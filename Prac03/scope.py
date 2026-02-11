#ex1
def myfunc():
  x = 300
  def myinnerfunc():
    print(x) # x was created in myfunc, and we can use it
  myinnerfunc()

myfunc()

#ex2
x = "hi" #here x is global

def myfunc():
  print(x)

myfunc()

print(x)

#ex3
x = 300 #first x

def myfunc():
  x = 200
  print(x)# different from first x

myfunc()

print(x)

#ex4
def myfunc():
  global x # creating global variable inside the function
  x = 300
myfunc()
print(x)

#ex5
def myfunc1():
  x = "Jane"
  def myfunc2():
    nonlocal x # the same as global but for uotter function
    x = "hello"
  myfunc2()
  return x

print(myfunc1())
