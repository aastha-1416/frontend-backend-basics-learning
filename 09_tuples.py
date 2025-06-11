#Creating Empty Tuples
my_tuple = ()
print(my_tuple)

#Creating Tuples
my_tuple = (1, 2, 3)
print(my_tuple)

#Single Element Tuple
my_tuple = (1,)
print(my_tuple)

#Accessing Tuple Elements
my_tuple = (10, 20, 30)
print(my_tuple[0])
print(my_tuple[1])
print(my_tuple[0:])
print(my_tuple[-1])
print(my_tuple[0:2])

#Tuple Concatenation
tuple1 = (10, 20, 30)
tuple2 = (40, 50)
print(tuple1 + tuple2)

#Tuple Unpacking
tuple1 = (10, 20, 30)
a, b, c = tuple1
print(a)
print(b)
print(c)

#Nested Tuples
nested_tuple = ((10, 20), (30, 40), (50, 60))
print(nested_tuple)