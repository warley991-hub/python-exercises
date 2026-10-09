from datetime import datetime
from time import sleep

class ContaBancaria:

    def __init__(self, numero_conta, agencia, nome_titular, cpf_titular):
        self.numero_conta = numero_conta
        self.agencia = agencia
        self.nome_titular = nome_titular
        self.cpf_titular = cpf_titular

        self.saldo = 0
        self.cheque_especial = 150
        self.id_historico = 1
        self.transacoes = []

    def _hora_atual(self):
        self.momento_deposito = datetime.now()

    def consultar_saldo(self):
        print(f'''
==========================================
Titular: {self.nome_titular}
CPF: XXX.XXX.XXX-{self.cpf_titular[-2:]}
==========================================
SALDO BANCÁRIO:
R$ {self.saldo:,.2f}\n''')

    def historico_transacoes(self):
        print(f'''
==========================================
Titular: {self.nome_titular}
CPF: XXX.XXX.XXX-{self.cpf_titular[-2:]}
==========================================
HISTÓRICO DE TRANSAÇÕES:''')    
        for transacao in self.transacoes:
            print(transacao)

    def depositar(self, valor):
        self._hora_atual()
        self.saldo += valor
        self.transacoes.append((self.id_historico,f'R${valor:,.2f}', self.momento_deposito.strftime('%d/%m/%Y às %H:%M:%S')))
        self.id_historico += 1

    def sacar(self,valor):
        self._hora_atual()
        self.saldo -= valor
        self.transacoes.append((self.id_historico,f'-R${valor:,.2f}', self.momento_deposito.strftime('%d/%m/%Y às %H:%M:%S')))

#PROGRAMA
breno = ContaBancaria(1234,123,'Breno Warley','111.222.333-45')

breno.depositar(500)
sleep(4)
breno.depositar(175)
sleep(2)
breno.depositar(1245)
sleep(1)
breno.depositar(3075)
sleep(1)
breno.depositar(4325)

breno.consultar_saldo()

breno.sacar(150)
breno.consultar_saldo()

breno.historico_transacoes()