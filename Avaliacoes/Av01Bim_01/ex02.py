k = 20
s = 1 
for d in range(1, 30):
    #print (d, s)
    if k % d == 0: print(s * d, end = " ")
    s = -s

print()

k = 18
s = -1 
for d in range(1, 30):
 if k % d == 0: print(s * d, end = " ")
 s = -s    