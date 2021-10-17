from math import*
def rav(r):
    v =[]
    k = 0
    j = len(r) - 1
    while j >= len(r)/2:
        v.insert(k, r[j])
        j -= 1
        k += 1
    l = 0
    m = len(r) -1
    while l != m:
        r.insert(m,r[l])
        l += 1
        m -= 1
    l = 0
    while l <= len(r):
        r.insert(l, v[l])
    return r
t=[1 , 2 , 3 , 4 , 5 , 6 , 7]
a = []
a = rav(t)
print("The reversed table is :",a)
print("The original table is : ",t)
