# Metacharacters

# .- any characters except newline

import re

text = " cat cut bat b6t"

pattern = r"c.t"
match = re.findall(pattern, text)
match2 = re.findall(r".at", text)
print(match, match2)


# ^ - starts with

t2 = "the world is so big"
m1 = re.findall(r"^the", t2)
print(m1)
t3 = "1234 is my pin"
m2 = re.findall(r"^\d{4}", t3)
print(m2)


# $ - ends with

t4 = " this is the end of the line"
m3 = re.findall(r"line$", t4)
print(m3)


# * - 0 or more times
t5 = "hllo hello heeello heeeeeeello"
m4 = re.findall(r"he*llo", t5)
print(m4)


# + - 1 or more times
m5 = re.findall(r"he+llo", t5)
print(m5)


# ? - 0 or 1 time
t6 = " b ab aab aaab"
m6 = re.findall(r"a?b", t6)
print(m6)

t7 = "color colour"  # practical example
m7 = re.findall(r"colou?r", t7)
print(m7)


# {n} - exactly n times/ exact number of repetettions
t8 = "a aa aaa aaaa aaaaa aaaaaaa aaaaaaaaaaaaaa"
m8 = re.findall(r"a{3}", t8)
print(m8)
print(re.findall(r"a{2,4}", t8))  # between 2 and 4 times
print(re.findall(r"a{2,}", t8))  # 2 a's or more


t9 = "9897123456"
m9 = re.findall(r"\d{10}", t9)  # Exact 10 digits
print(m9)


# | = or
t10 = "cat bat rat mat"
m10 = re.findall(r"cat|bat", t10)  # either cat or bat
print(m10)

# () = grouping

txt = "abababababababab"
print(re.findall(r"(ab){3}", txt))

txt2 = " World id 123 1234 end."
print(re.findall(r"(\w+)", txt2))

print(re.findall(r"(cat|bat|mat)", t10))

tt = "Tanmay Bhatt"
print(re.findall(r"(\w+)\s(\w+)", tt))  # \s = space
