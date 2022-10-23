import string

atividade ={
        "pergunta 1":{
                "questao": "Quanto é 2+2 ?",
                "alternativas": { "a" : '4' , "b": '8' , "c" : '2'},
                "resposta": "a"
        },
        "pergunta 2":{
                "questao": "Quanto é 3 X 2 ?",
                "alternativas": { "a" : '4' , "b": '10' , "c" : '6'},
                "resposta": "c"

        }
}

for chavep , valorp in atividade.items():
        print(f'{chavep} : {valorp["questao"]} ')
        for chaver, valorr in valorp["alternativas"].items():
                print(f'[{chaver}] : {valorr}')
        cont = 0
        while cont == 0:
                resp_User = input('insira a sua resposta: ')
                resp_User = resp_User.lower()
                resp_User2 = string.punctuation
                resp = 0
                if resp_User2 == string.punctuation:
                        for c in resp_User2:
                                resp_User = resp_User.replace(c, "")
                else:
                        continue
                if resp_User.isnumeric():
                        print("não aceitamos números!")
                        pass
                elif "a" in resp_User:
                        resp =1
                        pass
                elif "b" in resp_User:
                        resp =1
                        pass
                elif "c" in resp_User:
                        resp =1
                        pass
                elif resp_User.isascii():
                        print("Por favor, escolha entre as alternativas [a], [b] ou [c]")
                if resp == 1:
                        if resp_User == valorp["resposta"]:
                                print("CORRETO")
                                cont =+1
                        else:
                                print(f"ERRADO, A RESPOSTA CORRETA É {valorp['resposta']}")
                                cont =+1
