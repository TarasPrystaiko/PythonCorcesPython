# # Identity The operators is and is not test for an object’s identity: x is y is true if and only if x and y are the same object. An Object’s identity is determined using the id() function. x is not y yields the inverse truth value. [4]
a = [1, 3, 5]
b = [1, 3, 5]
c = a
print(a is b)
print(a is c)
print(b is c)
print(b == c)
# print(id(a) == id(b))
# print(id(a) == id(c))
# print(id(b) == id(c))
#
print(a == b)
print(a == c)
print(b == c)
