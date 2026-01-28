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

# 1. Slice To the End
print("\nSlice to the end from index 6:", text[6:])

# 2. Negative Indexing
print("Last character (negative index):", text[-1])
print("Last 5 characters:", text[-5:])

# 3. Remove Whitespace
trimmed = text.strip()
print("\nWithout whitespace:", trimmed)

# 4. Upper Case
print("Upper case:", trimmed.upper())

# 5. String Concatenation
new_text = trimmed + " is awesome!"
print("\nConcatenation:", new_text)

# 6. F-Strings
name = "Alex"
age = 20
print(f"\nF-string: My name is {name} and I am {age} years old.")

# 7. Placeholders and Modifiers
price = 19.56789
print("Price: {:.2f}".format(price))  # 2 decimal places
print("Price with f-string: {price:.1f}")

# 8. Methods
sample = "hello123"

# isdigit
print("\nIs digit only?", sample.isdigit())

# islower
print("Is lowercase?", sample.islower())

# replace
print("Replace 'hello' -> 'hi':", sample.replace("hello", "hi"))

# rsplit
words = trimmed.rsplit(" ")
print("rsplit:", words)

# rstrip
right_trim = text.rstrip()
print("rstrip result:", right_trim)