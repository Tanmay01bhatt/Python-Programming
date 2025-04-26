# Understanding Iterators

# for loop uses iterators behind the scenes for its implementation

numb = [34, 54, 67, 78, 89, 36]

# for loop
#  for x in numb:
#   print(x)


iterator = iter(numb)
while True:
    try:
        item = next(iterator)
        print(item)

    except StopIteration:
        break
