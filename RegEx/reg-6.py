# sub() = replaces the matched string with the replacement.
# Mostly used in text cleaning
import re
# re.sub(pattern,replacement,string)

tt = "There is rain in Spain"

x = re.sub(r"\s", "--", tt)
print(x)


# remove punctuations

tt2 = "hello! how are you?"
clean = re.sub(r"[^\w\s]", "", tt2)
print(clean)

# Remove URLS
tt3 = "Chec it out at https://www.google.com"
clean2 = re.sub(r"https?://\S+", "", tt3)
print(clean2)


# Normalize Whitespace
tt4 = "too      much      whitespace"
cl = re.sub(r"\s+", " ", tt4)
print(cl)


# Remove Email Addresses

tt5 = "contact me at user@gmail.com"

cl2 = re.sub(r"\b[\w.-]+@gmail\.com\b", "", tt5)  # \b...\b = word boundary
print(
    cl2
)  # remove email address                      #[\w.-] = word character, dot, hyphen
mask = re.sub(r"\b[\w.-]+@gmail\.com\b", "[MASK]", tt5)  # @gmail = domain name
print(mask)


tt6 = "contact me at user@gmail.com  or  user01@email.co.in"
clean4 = re.sub(r"\b[\w.-]+@[\w.-]+\.\w+\b", "", tt6)
print(clean4)


"""
SPECIAL SEQUENCES

1 - \b ....\b = Word Boundary
         \B = non word boundary

2 - \w  = any word character (letter , digit, underscore)
       \W = non word character( speacial characters like !@?*)

3 - \d  = any digit (0-9)
         \D = non digit (anything other than 0-9)

4 - \s = any whitespace character(space ,tab ,newline)
            \S = non whitespace character (anything other than space ,tab ,newline)          

"""
