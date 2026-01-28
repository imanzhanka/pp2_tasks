#SYNTAX
#PYTHON OUTPUT
#COMMENTS TOPICS 

name=input("Type your name: ") 
#This is a statement

print('Hello,' , name, end='') #output in the same line 
print('! This program shows wich number is greater')
a=int(input("Type 1st number(except 0): "))
b=int(input("Type 2nd number(except 0): "))
if a>b:
    print(a)
if a<b:
    print(b)
if a==b:
    print(0)#output the number
    print(name, ", the numbers are equal. That is why the output is ", 0)
    '''
    combine text 
    and numbers in one 
    output
    '''