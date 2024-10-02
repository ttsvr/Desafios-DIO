menu = """
O que você deseja fazer?

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

=> """

saldo = 0
limite = 500
extrato_texto = ""
LIMITE_SAQUES = 3
saques_disponiveis = LIMITE_SAQUES

def deposito ():
    
    global saldo 
    global extrato_texto

    valor = float(input("Informe o valor do depósito: "))

    if valor > 0:
        saldo = saldo + valor
        extrato_texto = extrato_texto + f"Depósito: R$ {valor:.2f}\n"
        print(f"Saldo atual: R$ {saldo:.2f}")

    else:
        print("Operação falhou! O valor informado é inválido.")

def saque ():
    
    global LIMITE_SAQUES
    global saques_disponiveis
    global limite
    global saldo
    global extrato_texto
    
    if saques_disponiveis == 0:
        print("Operação falhou! Número máximo de saques excedido.")
        
    else: 
        valor = float(input("Informe o valor do saque: "))

        if valor <= 0:
            print("Operação falhou! O valor informado é inválido.")
    
        elif valor > limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif valor > saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif valor > 0:
            saldo = saldo - valor
            extrato_texto = extrato_texto + f"Saque: R$ {valor:.2f}\n"
            saques_disponiveis = saques_disponiveis - 1

            print(f"Saldo atual: R$ {saldo:.2f}")
            print(f"Quantidade de saques disponível: {int(saques_disponiveis)}")

def extrato ():
    global extrato_texto
    global saldo
    global saques_disponiveis
    global LIMITE_SAQUES
    
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato_texto else extrato_texto)
    print(f"Saldo atual: R$ {saldo:.2f}")
    print(f"Você tem {int(saques_disponiveis)}",end="")
    print(f" saque disponível" if int(saques_disponiveis) == 1 else f" saques disponíveis")
    print("==========================================") 

while True:

    opcao = input(menu)

    if opcao == "1":
        deposito()

    elif opcao == "2":
        saque()

    elif opcao == "3":
        extrato()

    elif opcao == "0":
        print("Obrigado por utilizar nossos serviços!")
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")