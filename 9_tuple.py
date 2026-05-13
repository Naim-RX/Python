tup = (1,2,3,4)
print(type(tup),tup)
print(len(tup))
tup2 = tup[1:3]
print(tup2)

temp = list(tup)
temp.append(5)
tup = tuple(temp)
print(tup)
res = tup.index(3 , 1 , 4)
print(res)