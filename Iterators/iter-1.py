# Iterators
# are objects that allow us to traverse through a collection(tuple,list,dict)
#  ONE item at a time without knowing the underlying structure


# There are two primary methods :

# 1- iter() : initializes an iterator (creates an instance) used for iterating

# 2- next() : returns the next element int the collection.


tup = ("apple", "banana", "grape")
myiter = iter(tup)
item1 = next(myiter)
item2 = next(myiter)
item3 = next(myiter)

print(item1, item2, item3)


st = "heloo world"
myiter2 = iter(st)
it1 = next(myiter2)
it2 = next(myiter2)
print(it1, it2)


# Loop through an iterator

num = [10, 20, 30, 40, 50]
iter3 = iter(num)

for x in iter3:
    print(x)
