#VARIABLES
#DATA TYPES 
#CASTING
glob=True
def variables ():
    a1=1
    a_2=float(1)
    a_3=20j
    B1='Zhannur'
    variableNameB2="ZHannur"
    print(type(a1))
    print(type(a_2))
    print(type(a_3))
    print(type(B1))
    print(type(variableNameB2))

    c, d, e = 10, 5.0, "Cherry"
    print(c)
    print(d)
    print(e)
    c, d, e = 0, 0, 0
    print(c, d, e)

    numbers = [1, 2, 3]
    x, y, z = numbers
    print(x+y+z,numbers, type(numbers))
    numbers_1 = (1, 2, 3)
    print(numbers, type(numbers_1))

    num_2 = range(10)
    print(num_2, num_2)
    print(list(num_2))

    num_3 = {"name" : "John", "age" : 36}
    print(num_3)
    print(type(num_3)) 


    num_4 = frozenset({1,2, 3})
    print(num_4)
    print(type(num_4)) 

    num_5 = int("1")
    print(num_5)
    print(type(num_5)) 

    num_6 = float("1")
    print(num_6)
    print(type(num_6)) 
    
    t_7 = str(3.0)
    print(t_7)
    print(type(t_7))
    
    import random
    print(random.randrange(1, 10))

    global glob 
    glob = False
    
variables() 
print(glob)
print(type(glob)) 