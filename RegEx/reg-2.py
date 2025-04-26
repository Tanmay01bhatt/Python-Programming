# COMBINATIONS
import re
# .* =  0 or more of any character

txt = "hello heeeello hllo heeeeeeello"
print(re.findall(r"he.*llo", txt))  # 0 or more of any character between he and llo

txt2 = "Error:404 Error:hello Error:not found"
m = re.findall(r"Error:.*", txt2)
print(m)

txt3 = "  https://www.google.com  https://www.facebook.com  https://www.instagram.com"
m2 = re.findall(r"https://.*\.com", txt3)
print(m2)


#  .+ = Matches 1 or more of any character

t = "Name:Tanmay Name:John  Name:Mike"
ma = re.findall(r"Name:.+", t)
print(ma)

t2 = "<div> <h1> <p>  <hello>"
ma2 = re.findall(r"<.+>", t2)
print(ma2)

t3 = " file.txt notes.txt hw.txt"
ma3 = re.findall(r".+\.txt", t3)
print(ma3)


#  .$ = Matches 0 or 1 of any character at the end of the string
tt = "yelllow"
mat = re.findall(r".*ow$", tt)
print(mat)

tt2 = "apple hello orange grape"
mat2 = re.findall(r"^.*[aeiou]$", tt2)  # start with antthing and end with a vowel
print(mat2)


# +$ = Matches 1 or more of any character at the end of the string


tt3 = " hel hell helll hellll hellllll"
print(re.findall(r"hel+$", tt3))


#  *$ = Matches 0 or more of any character at the end of the string

print(re.findall(r"hel*$", tt3))  # 0 or more of l at the end of the string

# prints only the last match
# if you want to print all matches use word boundary \b ... \b
