# SETS
import re

# Character Set = matches if even one of the character is pressent

txt = " a b c"
print(re.findall(r"[abc]", txt))  # a or b or c

vow = "find the vowels in this sentence"
print(re.findall(r"[aeiou]", vow))

# Range = matches any character within the specifed range

tt = " a b c d  f g h SDF G W ER   23 43 55 6 7"
print(re.findall(r"[a-zA-Z]", tt))

# Including numbers

print(re.findall(r"[a-zA-Z0-9]", tt))


# custom range with special characters

tt2 = " a b c df J KLMOP _?!"
print(re.findall(r"[a-d_!?]", tt2))

# Negating a Set  = use ^

tet = " abc def ghi"
print(re.findall("[^abc]", tet))

tet2 = " abcdfefghit 367234"
print(re.findall("[^0-9]", tet2))


# Set with Digits
# use [0-9] ot \d

txt = "1 234 34 5 566 6789"

print(re.findall(r"[0-9]+", txt))


# exact 3 digits will be exxtracted

print(re.findall(r"[0-9]{3}", txt))


# 2 to 4 digits

txt2 = " 1 12 123 1234 12345"
print(re.findall(r"[0-9]{2,4}", txt2))  # 2 to 4 digits


# CUSTOM TWO DIGIT NUMBER FROM 00 TO 59

txt2 = " 12 01 45 57 59 61 100"
print(re.findall(r"[0-5][0-9]", txt2))


tel = " 123-456-7890 123-456-7891 123-456-789"
mat = re.findall(r"[0-9]{3}-[0-9]{3}-[0-9]{4}", tel)
print(mat)


# In sets the symbols + , $*(){} have no speacial meaniing and are treated as normal characters
# Only ^ use used in negation and - is used in defining a range
