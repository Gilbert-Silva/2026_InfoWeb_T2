# 0 1 2 3
# cada linha é um input

s = input()   # "0 1 2 3"
x = s.split() # ["0", "1", "2", "3"]
a = int(x[0])
b = int(x[1])
c = int(x[2])
d = int(x[3])
print(a + b + c + d)

a, b, c, d = map(int, input().split())
print(a + b + c + d)


