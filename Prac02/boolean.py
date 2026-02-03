#example 1 
print(10 > 9)
print(10 == 9)
print(10 < 9)

#example 2
print(bool("Hello"))
x = "Hello"
y = 15
print(bool(x))
print(bool(y))

#example 3 - false values
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})

#example 4 - false (addition)
class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))

#example 5
def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")
  