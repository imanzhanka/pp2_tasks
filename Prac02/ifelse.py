#ex1: if in condition
is_logged_in = True
if is_logged_in:
  print("Welcome back!")

#ex2:elif skips all remaining conditions
a = 2
b = 330
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")


#ex3:short
print("A") if a > b else print("B")

#ex4:logical
if not a > b:
  print("a is NOT greater than b")


#ex5:nested if
x = 5
if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")

#ex6:pass
value = 50

if value < 0:
  print("Negative value")
elif value == 0:
  pass # Zero case - no action needed
else:
  print("Positive value")