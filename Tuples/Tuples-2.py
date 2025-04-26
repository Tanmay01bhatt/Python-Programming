# Update tuple elements
# since tuples are immutable there is a roundaboutway to update their values
# tuple=list=update(using list functions)=tuple

tup1 = (33, 67, 43, 88, 99, 2, 34, 5, 46)
x = list(tup1)
x.append(99999)
tup1 = tuple(x)
print(tup1)


# Adding a tuple to a tuple is possible

tup1 = ("apple", "cheery")
tup2 = ("banana",)
tup1 = tup1 + tup2
print("combined tuple is :", tup1)
