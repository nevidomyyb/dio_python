operacoes = []
saldo = 0

def checar_quantidade_saques():
    qtnd = 0
    for indice in operacoes:
        if indice["tipo"] == "saque":
            qntd += 1
    return qntd

while True:
    print("")
    print("==================")
    print("[1] para depósito")
    print("[2] para saque")
    print("[3] para extrato")
    print("==================")
    try: 
        i = int(input(""))
    except:
        print("Operação inválida")
        continue
    match i:
        case 1:
            try: 
                valor = float(input("Digite a quantidade para o depósito: "))
            except:
                print("Valor inválido, reiniciando operação")
                continue
            saldo += valor
            operacoes.append({"tipo": "deposito", "valor": valor})
        case 2:
            if checar_quantidade_saques == 3:
                print("Limite máximo de saques diários atingidos (3).")
                continue
            try: 
                valor = float(input("Digite a quantidade para o saque: "))
            except:
                print("Valor inválido, reiniciando operação")
                continue
            if saldo < valor: 
                print("Não é possível realizar o saque, saldo insuficiente.")
                continue
            if valor > 500: 
                print("Não é possível realizar o saque, límite de R$500 por saque.")
                continue
            saldo -= valor
            operacoes.append({"tipo": "saque", "valor": valor})
        case 3:
            if len(operacoes)==0: print("Não foram realizadas movimentações.")
            else:
                print("")
                print("==================")
                for i, v in enumerate(operacoes):
                    if v["tipo"] == "saque":
                        valor = "{:.2f}".format(v["valor"])
                        print(f"{i+1}. - R$ {valor}.")
                    if v["tipo"] == "deposito":
                        valor = "{:.2f}".format(v["valor"])
                        print(f"{i+1}. + R$ {valor}.")
                print("Saldo atual: R% {:.2f}".format(saldo))

