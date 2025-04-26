# word by word processing
str1 = input("Enter a string: ")
str1 = str1 + " "
w = " "
for char in str1:
    w = w + char
    if char == " ":
        print(w)
        w = " "
