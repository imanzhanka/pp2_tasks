#ex1
def changecase(func): #здесь аргументом является функция
  def myinner():
    return func().upper()
  return myinner

@changecase #calling the changecase function and apply as an argument myfunction()
def myfunction():
  return "Hello Sally"

print(myfunction())

#ex2
def changecase(func):
  def myinner():
    return func().upper()
  return myinner

@changecase
def myfunction():
  return "Hello Sally"

@changecase #calling decorator multiple times
def otherfunction():
  return "I am speed!"

print(myfunction())
print(otherfunction())

#ex3
def changecase(func):#decor
  def myinner(*args, **kwargs):
    return func(*args, **kwargs).upper() #to the uppercase everything that return myfunction
  return myinner

@changecase
def myfunction(nam):
  return "Hello " + nam

print(myfunction("John"))

#ex4
def changecase(n): #для того чтобы передать значение n
  def changecase(func): #это сам декоратор
    def myinner():
      if n == 1:
        a = func().lower()
      else:
        a = func().upper()
      return a
    return myinner
  return changecase

@changecase(1)
def myfunction():
  return "Hello Linus"

print(myfunction())

#ex5
def changecase(func):
  def myinner():
    return func().upper()
  return myinner

def addgreeting(func):
  def myinner():
    return "Hello " + func() + " Have a good day!"
  return myinner

@changecase
@addgreeting #will execute first
def myfunction():
  return "Tobias"

print(myfunction())