operacoes = []
saldo = 0
usuarios = {}

def criar_usuario(nome, cpf):
    if cpf in usuarios:
        print("Usuário já existe!")
        return None
    usuarios[cpf] = {"nome": nome, "contas": {}}
    print(f"Usuário {nome} criado com sucesso!")
    return cpf

def criar_conta(cpf, numero_conta):
    if cpf not in usuarios:
        print("Usuário não encontrado!")
        return None
    if numero_conta in usuarios[cpf]["contas"]:
        print("Conta já existe!")
        return None
    usuarios[cpf]["contas"][numero_conta] = {"saldo": 0, "operacoes": []}
    print(f"Conta {numero_conta} criada com sucesso!")
    return numero_conta

def checar_quantidade_saques(operacoes):
    qtnd = 0
    for operacao in operacoes:
        if operacao["tipo"] == "saque":
            qtnd += 1
    return qtnd

def depositar(conta, valor):
    conta["saldo"] += valor
    conta["operacoes"].append({"tipo": "deposito", "valor": valor})

def sacar(conta, valor):
    if checar_quantidade_saques(conta["operacoes"]) == 3:
        print("Limite máximo de saques diários atingidos (3).")
        return False
    if conta["saldo"] < valor:
        print("Não é possível realizar o saque, saldo insuficiente.")
        return False
    if valor > 500:
        print("Não é possível realizar o saque, limite de R$500 por saque.")
        return False
    conta["saldo"] -= valor
    conta["operacoes"].append({"tipo": "saque", "valor": valor})
    return True

def extrato(conta):
    if len(conta["operacoes"]) == 0:
        print("Não foram realizadas movimentações.")
    else:
        print("")
        print("==================")
        for i, v in enumerate(conta["operacoes"]):
            valor = "{:.2f}".format(v["valor"])
            if v["tipo"] == "saque":
                print(f"{i + 1}. - R$ {valor}.")
            if v["tipo"] == "deposito":
                print(f"{i + 1}. + R$ {valor}.")
        print("Saldo atual: R$ {:.2f}".format(conta["saldo"]))

while True:
    print("")
    print("==================")
    print("[1] para criar usuário")
    print("[2] para criar conta")
    print("[3] para depósito")
    print("[4] para saque")
    print("[5] para extrato")
    print("[6] para sair")
    print("==================")
    
    try: 
        i = int(input("Escolha a opção: "))
    except:
        print("Operação inválida")
        continue
    
    if i == 1:
        nome = input("Digite o nome do usuário: ")
        cpf = input("Digite o CPF do usuário: ")
        criar_usuario(nome, cpf)
    
    elif i == 2:
        cpf = input("Digite o CPF do usuário: ")
        numero_conta = input("Digite o número da conta: ")
        criar_conta(cpf, numero_conta)
    
    elif i in [3, 4, 5]:
        cpf = input("Digite o CPF do usuário: ")
        numero_conta = input("Digite o número da conta: ")
        if cpf not in usuarios or numero_conta not in usuarios[cpf]["contas"]:
            print("Conta não encontrada!")
            continue
        conta = usuarios[cpf]["contas"][numero_conta]
        
        if i == 3:
            try: 
                valor = float(input("Digite a quantidade para o depósito: "))
            except:
                print("Valor inválido, reiniciando operação")
                continue
            depositar(conta, valor)
        
        elif i == 4:
            try: 
                valor = float(input("Digite a quantidade para o saque: "))
            except:
                print("Valor inválido, reiniciando operação")
                continue
            sacar(conta, valor)
        
        elif i == 5:
            extrato(conta)
    
    elif i == 6:
        break
    
    else:
        print("Operação inválida")
