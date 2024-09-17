set1 = {1,23,4,5}
set2 = {9,8,7,5}
set3 = set1.union(set2)        # return all elements of both sets with no repetition 
print(set3)
set3 = set1.intersection(set2)  # return 5 which is common in both sets
print(set3)

print({23,4}.issubset(set1))  # return True
print({87}.issubset(set1))  # return True
print(set1.issuperset({1,23}))
