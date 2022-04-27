cont = 0
while cont == 0:
    try:
        tempo1 = float(input("Insira um horário (Em formato de 24 Horas): "))
        tempo2 = "{:.2f}".format(tempo1)
        tempo = float(tempo2)
    except:
        pass
    try:
        if tempo <= 11.59:
            print(f"Tenha um Bom Dia (Horário: {tempo})")
            cont = 1
        elif tempo >=12 and tempo <= 17.59:
            print(f"Tenha uma Boa Tarde (Horário: {tempo})")
            cont = 1
        elif tempo >= 18 and tempo <= 24:
            print(f"Tenha uma Boa Noite (Horário: {tempo})")
            cont = 1
        else:
            print("Por favor, insira um horário válido")
    except:
        print("Por favor, insira um horário válido")
