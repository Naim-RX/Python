li = [1,3,5,7,9,10,11,12,13,14,15]
print(type(li))

if 3 in li:
    print("YES")
else:
    print("NO") 

print(li[:])
print(li[0:11:2])

lsc = [i*i for i in range(5)]
print(lsc)

li.append(16)
li.index(1)
li.count(2)
m = li.copy()
li.sort(reverse=True)
print(li)
li.insert(1,100)
x = [100,200]
li.extend(x)
k = x + li
print(k)