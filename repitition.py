import numpy as np
t = ['a','b','c','d','a', 'a','d']
i = 0
j = 1
while i < len(t):
    while j <len(t):
        if t[i] == t[j]:
            print("this is a repitition of ", t[j])
        j +=1
    i +=1
    j = i+1
print(t)






