# Functions-2

str1 = "Hello World"

pos = str1.find("o")
pos2 = str1.rfind("o")
pos3 = str1.find("t")

# specific positions
pos4 = str1.find("o", 5, 9)

print(pos, pos2, pos3, pos4)  # Output: 4 7 -1 7

##string to list

txt = "I am great"
list1 = txt.split()
print(list1)

txt2 = "hello,hi i am great,thank you"
list2 = txt2.split(",")
print(list2)
# Output: ['hello', 'hi i am great', 'thank you']
