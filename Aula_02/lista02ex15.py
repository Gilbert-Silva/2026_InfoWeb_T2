def Primo(n):
    primo = True
    for d in range(2, n):                  
        if n % d == 0:    # achou um divisor
            primo = False
            break 
    return primo    

print("Digite um número inteiro")
n = int(input())
if Primo(n) : print(n, "é primo") 
else: print(n, "não é primo")
