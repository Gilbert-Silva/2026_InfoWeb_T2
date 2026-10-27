try:
    a = int(input("Informe o dividendo: "))
    b = int(input("Informe o divisor: "))
    print(a/b)
except ValueError:
    print("Informe números inteiros")
except ZeroDivisionError:
    print("Informe um divisor não nulo")

    