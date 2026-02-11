#ex1
def ex1(*sub): #use * when we do not know how many arguments will be, they stores in tuple
    print(sub[0])
ex1(1,2,3)

#ex2
def ex2(subj, *students):
    print(f"On {subj} class students:")
    for x in students:
        print(x)
ex2("Math", "Zhannur","Adina","Adelya")

#**kwars stores data via dictionary
#ex3
def ex3(**sub3):
    print(f"Your subject {sub3["su"]}")#здесь пишем su в " "
    print(f"Your professor {sub3["pr"]}")
ex3(su="Math",pr= "Meiirzhan Marat") # пишем = для словарей, для ключей "" не пишем

#ex4
def ex4(name,*people, **param): #* frist **second
    print("Your class:", name)
    for x,y in param.items():
        print(x,':', y)
    print("Your classmates:", people)
ex4("Math","Zhannur","Adina","Adelya", time=12, longliness="2h" )

#ex5
def my_function(a, b, c):
  return a + b + c

numbers = [1, 2, 3]
result = my_function(*numbers) # Same as: my_function(1, 2, 3), чтобы не возвращал значение всего листа в а
print(result)