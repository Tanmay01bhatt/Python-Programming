# Implementation in NLP

# findall() = returns a list containing all matches

# re.findall(pattern,string)

# Mainly used to find patterns in text

import re

# Tokenization

text = "regex is awesome for nlp"

tokens = re.findall(r"\b\w+\b", text)  # present at beg ....  present at end
print(tokens)


# Extract Hashtags

text2 = " #python #regex #nlp #awesome"
ha = re.findall(r"#\w+", text2)
print(ha)
text3 = "hello @tanmay how are you @end"
men = re.findall(r"@\w+", text3)
print(men)

text4 = "Error 404 not found"
print(re.findall(r"\d+", text4))
