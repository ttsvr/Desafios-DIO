# Desafio proposto: Otimizando o Sistema Bancário com Funções Python

# Curso: Trabalhando com Coleções em Python
# https://web.dio.me/project/otimizando-o-sistema-bancario-com-funcoes-python/learning/82a55799-cfb8-479d-85a3-4982e29c90ba?back=/track/engenharia-dados-python&tab=undefined&moduleId=undefined

from datetime import datetime, timedelta, date
import textwrap

def menu():
    menu = """
    O que você deseja fazer?

    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Criar novo usuário
    [5] Criar nova conta
    [0] Sair

    => """
    return input(textwrap.dedent(menu))


def deposit (valor, 
              saldo,  
              extrato, 
              transacoes_disponiveis):

    if transacoes_disponiveis > 0:    
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
        
            saldo = saldo + valor
            transacoes_disponiveis = transacoes_disponiveis - 1
            datahora = datetime.today()
            extrato = extrato + f"Depósito: R$ {valor:.2f}    Data: {datahora.strftime("%d/%m/%Y %H:%M")}\n"

            print("Depósito realizado com sucesso!")
            print(f"Saldo atual: R$ {saldo:.2f}")
            print(f"Transações disponíveis: {transacoes_disponiveis}")

            return (saldo, extrato, transacoes_disponiveis)

        else:
            print("Operação falhou! O valor informado é inválido.")
            return (saldo, extrato, transacoes_disponiveis)
    else:
        print("Operação falhou! Limite de transações diárias atingido.")
        return (saldo, extrato, transacoes_disponiveis)


def withdraw (*, valor, saldo, limite, extrato, transacoes_disponiveis, saques_disponiveis):
    
    if transacoes_disponiveis > 0:
    
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
                saques_disponiveis = saques_disponiveis - 1
                transacoes_disponiveis = transacoes_disponiveis - 1
                datahora = datetime.today()
                extrato = extrato + f"Saque:    R$ {valor:.2f}    Data: {datahora.strftime("%d/%m/%Y %H:%M")}\n"

                print("Saque realizado com sucesso!")
                print(f"Saldo atual: R$ {saldo:.2f}")
                print(f"Quantidade de saques disponíveis: {int(saques_disponiveis)}")
                print(f"Transações disponíveis: {transacoes_disponiveis}")
                
    else:
        print("Operação falhou! Limite de transações diárias atingido.") 
        
    return(saldo, saques_disponiveis, transacoes_disponiveis, extrato)     


def extract (saldo, saques_disponiveis, transacoes_disponiveis, *, extrato):

    # data_solicitada_str = input("Você deseja visualizar o extrato de qual data? (Insira no formato dd/mm/yyyy): ")

    # data_solicitada_datetime = datetime.strptime(data_solicitada_str, "%d/%m/%Y")
    
    print("\n================= EXTRATO =================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"Saldo atual: R$ {saldo:.2f}")
    print(f"Você tem {int(saques_disponiveis)}", end="")
    print(f" saque disponível" if int(saques_disponiveis) == 1 else f" saques disponíveis")
    print(f"Você tem {int(transacoes_disponiveis)}", end="")
    print(f" transação disponível" if int(transacoes_disponiveis) == 1 else f" transações disponíveis")
    print("============================================") 


def address():
    confirmacao = "2"
    while confirmacao != "1":
        logradouro = input("Rua: ")
        numero_endereco = input("Número: ")
        bairro = input("Bairro: ")
        cidade = input("Cidade: ")
        estado = input("Estado (Sigla): ")

        endereco = f"{logradouro}, {numero_endereco} - {bairro} - {cidade}/{estado}."

        confirmacao_str = f"""
        Confirme o endereço abaixo:
        {endereco}
        Digite [1] para prosseguir ou digite [2] caso queira retornar: 
        """

        confirmacao = input(textwrap.dedent(confirmacao_str))

    return endereco


def create_user(usuarios, endereco):
    
    cpf = input("Digite seu CPF (Apenas os números): ")
    usuario = check_user(usuarios, cpf)

    if usuario:
        print("\n@@@ Já existe usuário com esse CPF! @@@")

    else:
        nome = input("Digite seu nome completo: ")
        data_nascimento_str = input("Digite sua data de nascimento (Apenas números [ddmmyyyy]): ")
        data_nascimento_date = datetime.strptime(data_nascimento_str, "%d%m%Y")
        
        while ValueError:
            data_nascimento_str = input("Insira um valor para data conforme exemplo (ddmmyyyy): ")
            data_nascimento_date = datetime.strptime(data_nascimento_str, "%d%m%Y")


        endereco = address()

        usuarios.append({"nome":nome, "data_nascimento":data_nascimento_date,"endereco":endereco,"CPF":cpf})

        print("Usuário criado com sucesso!")

    return(usuarios)
    

def check_user(usuarios,cpf):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["CPF"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def create_account(ultima_conta_aberta, contas, usuarios, AGENCIA):
    
    cpf = input("Digite seu CPF (Apenas os números): ")
    usuario = check_user(usuarios, cpf)

    if not usuario:
        print("Este CPF não está cadastrado, por favor crie um novo usuário")

    else:
        contas.append({"usuario":cpf, "agencia":AGENCIA, "conta":ultima_conta_aberta})
        ultima_conta_aberta = ultima_conta_aberta + 1
        print("Conta cadastrada com sucesso")

    return(ultima_conta_aberta, contas)


def check_account(usuarios, cpf):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["CPF"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def main():

    saldo = 0
    limite = 500
    extrato = ""
    LIMITE_SAQUES_DIARIO = 3
    LIMITE_TRANSACOES_DIARIO = 10
    saques_disponiveis = LIMITE_SAQUES_DIARIO
    transacoes_disponiveis = LIMITE_TRANSACOES_DIARIO
    usuarios = []
    contas = []
    AGENCIA = "0001"
    ultima_conta_aberta = 0


    while True:

        opcao = menu()

        if opcao == "1": #depositar
            saldo, extrato, transacoes_disponiveis = deposit(0,
                                                            saldo,  
                                                            extrato, 
                                                            transacoes_disponiveis)

        elif opcao == "2": #sacar
            saldo, saques_disponiveis, transacoes_disponiveis, extrato = withdraw(valor = 0,
                                                                                  saldo = saldo,
                                                                                  limite = limite,
                                                                                  extrato = extrato,
                                                                                  transacoes_disponiveis = transacoes_disponiveis,
                                                                                  saques_disponiveis = saques_disponiveis)

        elif opcao == "3": #exibir_extrato
            extract(saldo,
                    saques_disponiveis, 
                    transacoes_disponiveis, 
                    extrato = extrato)

        elif opcao == "4": #criar_usuário
            usuarios = create_user(usuarios, 0)

        elif opcao == "5": #Criar conta
            ultima_conta_aberta, contas = create_account(ultima_conta_aberta, contas, usuarios, AGENCIA)

        elif opcao == "0": #Fechar programa
            print("Obrigado por utilizar nossos serviços!")
            break

        else: #Dígito não programado
            print("Operação inválida, por favor selecione novamente a operação desejada.")


main()
