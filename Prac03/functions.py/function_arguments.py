#Function arguments (positional, default)
#Passing list and other types 
#Return values and statements
#example1
def sample(subject = "math"): # we are creating the default value 
    print("You chose", subject)
sample("programming")
sample()
 
#example2
def ex2(subj, num):
    print(f"Your subject is {subj} and it will be {num} times a week")
ex2(num=3, subj = "histor") # we may chanhe the order

#example3
def ex3(sub1, prof):
    print(f"your subject {sub1} and professor {prof}")
ex3("math","Nick Calvin") # we can not chage the order

#example4
def ex4(subj, num, ass):
    print(f"Your subject is {subj} and it will be {num} times a week")
ex4(num=3, subj = "histor", ass=5) # как только мы присвоили через = subj все последующие также должны быть присвоены 

#example5
def ex5(li): #we can give lists and other data types
    print(f"Yout subject is  {dict[0]}")
    print(f"Yout professor is  {dict[1]}")
li=["math", "Meiirzhan Marat"]
ex5(li)

#example6
def ex6():
  return ["math", "pp2", "eng"]#we can return list
subj = ex6() 
print(subj[0])
print(subj[1])
print(subj[2])

#example7
def my_function(name, /): #positional only arguments ( ставить / после запятой)
  print("Hello", name)
my_function("Emil")

def my_function(*, name): #keyword only
  print("Hello", name)
my_function(name = "Emil")