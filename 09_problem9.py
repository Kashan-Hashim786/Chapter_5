s = {8, 7, 12, "Harry", [1,2]} 

'''
No, you cannot change the values inside a list contained in a set
because sets in Python require their elements to be hashable and immutable.
Lists are mutable (you can change their contents), so they are not allowed
as elements in a set.
'''
print(s)  # return TypeError