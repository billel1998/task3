from math import*
r=[1 , 2 , 3 , 4 , 5 , 6 , 7]
v = []
k = 0
j = len(r)/2
   while j <= len(r)-1:
        v.insert(k, r[j])
        j += 1
        k += 1
l = 0
m = len(r) -1
   while l != m:
        r.insert(m,r[l])
        l += 1
        m -= 1
l = 0
z = 0
    while l <= len(r):
        r.insert(l, v[z])
        z +=1
        l +=1
print(r)
