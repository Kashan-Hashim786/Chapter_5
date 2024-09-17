s = set()
s.add(20)
s.add(20.0)   # 20 == 20.0 return true
s.add('20')
print(len(s))