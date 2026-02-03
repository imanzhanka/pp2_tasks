print('Hello!')
print("Tooday we introduce 'strings'")
t="""Here we have following topics:
 python strings 
 slicing strings 
 modify strings
 concatenate strings
 format strings
 escape characters
 string methods
 string evercises"""
print(t)
text = input("Give a sentance ")
print("Length", len(text))
print("Your sentance by loop: ")
for char in text:
    print(char)
word =  input("Give a word ")
if word in text:
    print(f"\nWord '{word}'is here!")
else:
    print(f"\nWord '{word}' not here.")


text = "   hello python 123   "



print("Original text:", text)


print("\nSlice to the end from index 6:", text[6:])


print("Last character (negative index):", text[-1])
print("Last 5 characters:", text[-5:])

trimmed = text.strip()
print("\nWithout whitespace:", trimmed)


print("Upper case:", trimmed.upper())


new_text = trimmed + " is awesome!"
print("\nConcatenation:", new_text)

name = "Alex"
age = 20
print(f"\nF-string: My name is {name} and I am {age} years old.")


price = 19.56789
print("Price: {:.2f}".format(price)) 

sample = "hello123"


print("\nIs digit only?", sample.isdigit())

print("Is lowercase?", sample.islower())

print("Replace 'hello' -> 'hi':", sample.replace("hello", "hi"))

words = trimmed.rsplit(" ")
print("rsplit:", words)

right_trim = text.rstrip()
print("rstrip result:", right_trim)