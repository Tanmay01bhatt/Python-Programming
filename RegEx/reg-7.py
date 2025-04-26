# search() = searches the string for a match and returns the match object.
import re

# re.search(pattern,string)

# group() = returns the matched string

txt = "Order id :4581"
match = re.search(r"\d+", txt)
print(match.group())


# start() = returns the starting index of the match
print(match.start())

# end() = returns the ending index of the match

print(match.end())

# span() = (start ,end) tuple is returned

print(match.span())
