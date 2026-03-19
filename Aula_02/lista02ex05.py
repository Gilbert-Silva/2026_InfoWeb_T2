print("Digite quatro valores inteiros")
a = int(input())  # 10   3   1
b = int(input())  #  3  10
c = int(input())  #  8
d = int(input())  #  1       3

if a > b: a,b = b,a
if a > c: a,c = c,a
if a > d: a,d = d,a
if b > c: b,c = c,b
if b > d: b,d = d,b
if c > d: c,d = d,c
print(a, b, c, d)



