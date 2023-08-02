a = [1, 2, 3]
b = a
print(a)
print(b)
print(a is b)

b = a.clear()
print(b)
print(a is b)

# but there is a concept of shallow copy and deep copy
a = [[1, 2, 3] , 4, 5]
b = a.copy()
print(a)
print(b)
# both a and b have same value

a[2] = 6
print(a) # [[1,2,3], 4, 6]
print(b)  #  [[1, 2, 3], 4, 5]
# this proves  that if immutable element of 'a' is changed then nothing changes in 'b'

a[0][1] = 7
print(a)  # [[1,7,3], 4, 6]
print(b)  # [[1, 7, 3], 4, 5]
# but if mutable element of one lists is changed then the change is also reflected



# python provides a function  to entirely  make a new copy  of an object which is called
from copy import deepcopy
a = [[1, 2, 3], 4,, 5]
b = deepcopy(a)
print(a)
print(b)

 a[0][1] = 7
 print(a)  # [[1, 7, 3], 4, 5]
 print(b)  # [[1, 2, 3], 4, 5]
