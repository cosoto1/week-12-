# sets and tuples examples:
#sets examples:

set1 = {1, 2, 3, 4, 5}
print(set1) # {1, 2, 3, 4, 5}
print(type(set1)) # <class 'set'>
set1.add(6)
print(set1) # {1, 2, 3, 4, 5}
set1.remove(2)
print(set1) # {1, 2, 3, 4, 5}


tuple1= (1,2,3,4,5)
print(tuple1)
print(type(tuple1))
#tuple cannot be changed after creation
#so it is usful for sotring information that should't be modified)
social_security_number = (123444, 4444445, 5676789)
print(social_security_number)
