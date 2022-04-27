cont = 0
while cont == 0:
    num = input("Escreva um número: ")
    try:
        num1 = int(num)
        cont = 1
    except:
        print("Porfavor, insira um número inteiro")
if num1%2 == 0:
    print(f"O número {num1} é par")
else:
    print(f"O número {num1} é ímpar")
