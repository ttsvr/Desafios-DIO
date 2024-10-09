from abc import ABC, abstractmethod
from datetime import datetime

class Cliente():
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def Realizar_Saque (self, conta, tipo_transacao):
        tipo_transacao.Salvar(self, conta)

    def Adicionar_Conta(self, conta):
        self.contas.append(conta)

    def __str__(self) -> str:
        return f"{self.__class__.__name__}: {", ".join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}" 


class PessoaFisica(Cliente):
    def __init__(self, cpf, nome, ano_nascimento):
        self._cpf = cpf
        self._nome = nome
        self._ano_nascimento = ano_nascimento


    @property
    def CPF(self):
        return self._cpf
    
    
    @property
    def Nome(self):
        return self._nome
    

    @property
    def Idade(self):
        _ano_atual = 2024
        return _ano_atual - self._ano_nascimento


    def __str__(self) -> str:
        return f"{self.__class__.__name__}: {", ".join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"
    

class Conta(PessoaFisica):
    def __init__(self, numero, nome):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._nome = nome
        self._historico = Historico()


    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)


    @property
    def Saldo(self):
        return self._saldo
    

    @property
    def NumeroConta(self):
        return self._numero_conta


    @property
    def Agencia(self):
        return self._agencia
    

    @property
    def cliente(self):
        return self._cliente
    

    @property
    def Historico(self):
        return self._historico
    

    def MostrarSaldo(Saldo):
        return f"Seu saldo atual é: R${Saldo:.2f}."


    def NovaConta():
        pass


class ContaCorrente(Conta):
    def __init__(self, numero, nome, limite, limite_saques):
        super().__init__(numero, nome)
        self.limite = limite
        self.limite_saques = limite_saques

    def Sacar(self, valor):
        numero_saques = len([transacao for transacao in self.Historico._transacoes if transacao["tipo"] == Saque.__name__])

        verificacao_numero_saques = numero_saques >= self.limite_saques
        verificacao_valor = valor > self.limite
        verificacao_saque_negativo = valor <= 0

        if verificacao_numero_saques:
            print("\n@@@ Operação falhou! Número máximo de saques excedido. @@@")
            return False

        elif verificacao_saque_negativo:
            print("\n@@@ Operação falhou! Insira um valor válido para realizar o saque. @@@")
            return False

        elif verificacao_valor:
            print("\n@@@ Operação falhou! O valor do saque excede o limite. @@@")
            return False

        else:
            self._saldo -= valor
            print(f"\n=== Saque de R$ {valor:.2f} realizado com sucesso! ===")
            return True

    def Depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print(f"\n=== Depósito de R$ {valor:.2f} realizado com sucesso! ===")
            return True
        else:
            print("\n@@@ Operação falhou! Insira um valor válido para realizar o depósito. @@@")
            return False

    def __str__(self):
        return f"""\
            Agência:\t{self._agencia}
            C/C:\t\t{self._numero_conta}
            Titular:\t{self._nome}
        """


class Historico():
    def __init__(self):
        self._transacoes = []

    @property
    def historico_transacoes(self):
        return self._transacoes

    def realizar_transacao(self, Transacao):
        self._transacoes.append(
            {
                "tipo": Transacao.__class__.__name__,
                "valor": Transacao.valor,
                "data": datetime.now().strftime("%d-%m-%Y %H:%M:%s")
            }
        )


class Transacao(ABC):
    @property
    @abstractmethod
    def valor(self):
        pass

    @classmethod
    @abstractmethod
    def Salvar(self, conta):
        pass


class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def Salvar(self, ContaCorrente):
        transacao_concluida = ContaCorrente.Sacar(self._valor)

        if transacao_concluida:
            Historico.realizar_transacao(self)


class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def Salvar(self, ContaCorrente):
        transacao_concluida = ContaCorrente.Depositar(self._valor)

        if transacao_concluida:
            Historico.realizar_transacao(self)

CC = ContaCorrente(1, "Thiago", 500, 3)
CC.Depositar(5000)
CC.Sacar(450)
Historico_1 = Historico()

print(Historico_1._transacoes)
