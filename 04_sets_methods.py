# Sets are unordered => Element’s order doesn’t matter 

s = {1,3,6,7,8,0,4,3,5,7,8,"harry"} # print {0, 1, 3, 4, 5, 6, 7, 8} No repetition
print(s)
s.add(65)
print(s)
#print(s[0])  # can not access by index
# s[1] = 45 # 3. There is no way to change items in sets. 
 # print(s)

print(len(s))
s.remove(8)
print(s)
s.pop()   # remove a random element
print(s)
s.clear()
print(s) # return empty set() 

