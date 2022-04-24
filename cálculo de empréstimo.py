V1 = float(input("insira o valor da casa: "))
Sa = float(input("insira o seu salário: "))
Qa = float(input("por quantos anos você pretende pagar?: "))
MQa = Qa*12
Tdg = (30/100)*Sa 
Tap = V1/MQa
if Tdg >= Tap:
    print("\033[0:31mEMPRÉSTIMO CONCEDIDO\033[m")
    print("seu saldo é de {:.2f}R$ por mês".format(Tdg))
    print("voce terá que pagar {:.2f}R$ por mês durante {} meses".format(Tap, MQa))
elif Tdg < Tap:
    Nap = Tap-Tdg
    print("\033[0:32mEMPRÉSTIMO NEGADO\033[m")
    print("seu saldo é de {:.2f}R$ por mês".format(Tdg))
    print("voce terá que pagar {:.2f}R$ por mês durante {} Meses".format(Tap, MQa))
    print("é necessário {:.2f}R$ a mais por mês".format(Nap))
else:
    print("por favor, insira um número da próxima vez!ºuº s2")
