# split() = splits the string to a list based on a seperator/pattern.
import re
# re.split(pattern,string)

tt = "It is raining cats and dogs"
x = re.split(r"\s", tt)
print(x)

# split on 2nd whitespace

y = re.split(r"\s", tt, 2)
print(y)
