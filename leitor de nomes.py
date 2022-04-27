import string
cont = 0
while cont == 0:
    nome = input("Escreva seu nome: ")
    if nome.find("1" or "2" or "3" or "4" or "5" or "6" or "7" or "8" or "9" or "0"):
        numname = len(nome)
        cont = 1
    else:
        print("por favor insira apenas letras")
if numname <= 4:
    print(f"Wow, {nome} é um nome múito curto... vai ser fácil de lembrar")
elif numname >= 5 and numname <= 6:
    print(f"{nome}, vai ser um nome meio difícil de lembrar")
elif numname > 6:
    print(f"{nome}.. qual é o seu nome mesmo?... é muito grande ;-;")