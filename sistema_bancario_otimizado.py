#SEPARAR AS FUNÇÕES DE SAQUE,DEPÓSITO, E EXTRATO EM FUNÇÕES.
#CRIAR DUAS NOVAS FUNÇÕES: CADASTRAR USUÁRIO(CLIENTE) E CADASTRAR  CONTA BANCÁRIA.
import datetime

saldo = 0
limite = 500
numero_saque = 0
limite_saque = 3
extrato = []
usuarios = []
contas = []
AGENCIA = '0001'
num_conta = 0


def check_usuario(cpf, usuarios):
    list_user = []
    for x in usuarios:
        if x['cpf'] == cpf:
            list_user.append(x)

    if list_user:
        return list_user[0]
    
    return None


def criar_usuario(usuarios):
    cpf = input('Digite o cpf: ')
    usuario = check_usuario(cpf, usuarios)

    if usuario:
        print('Cpf já cadastrado.')
    else:
        nome = input('Digite o nome do usuário: ')
        data_nascimento = input('Data de nascimento: ')
        endereco = input('Endereço: ')
        usuarios.append({'cpf': cpf,
                         'nome': nome,
                          'data_nascimento': data_nascimento,
                          'endrereco': endereco})


def criar_conta(agencia, num_conta, usuarios):
    cpf = input('Digite o cpf: ')
    usuario = check_usuario(cpf, usuarios)
    
    if usuario:
        num_conta += 1
        return num_conta, [{'agencia': agencia, 'numero_conta': num_conta, 'usuario': usuario}]

    return None



def deposito (saldo, saldotmp, extrato):
    saldo += saldotmp
    extrato.append(f'Deposito efetuado no valor: {saldo}')
    print('Depósito realizado com sucesso.')
    return saldo, extrato


def saque (*, valor_saque, numero_saque, limite_saque, limite,saldo):
    if numero_saque >= limite_saque:
        print('Numero de saques excedido no dia.')
    elif valor_saque > limite:
        print('Limite máximo para saque é de R$500,00.')
    elif saldo < valor_saque:
        print('Saldo insuficiente')
    else:
        print('Saque efetuado com sucesso.')
        saldo -= valor_saque
        numero_saque += 1
        extrato.append(f'Saque efetuado no valor de: {valor_saque}')
        return numero_saque
        
def extrato_detalhado(extrato):
    for e in range(len(extrato)):
        print(f'Extrato Detalhado: {extrato[e]}')



menu = '''\n
________Menu______
[D] = Depósito
[S] = Saque
[E] = Extrato
[U] = Criar Usuário
[C] = Criar Conta
[X] = Sair
__________________'''

while True:
    opcao = input(f'Digite a opção desejada: {menu}')
    if opcao == 'D':
        saldotmp = int(input('Digite o valor para realizar o depósito:'))
        saldo, extrato = deposito(saldo, saldotmp, extrato)
    elif opcao == 'S':
        valor_saque = int(input('Digite o valor para realizar o saque:'))
        # numero_saque =  saque(valor_saque, numero_saque, limite_saque, limite,saldo)
        numero_saque = saque(valor_saque = valor_saque,
                             numero_saque = numero_saque,
                             limite_saque = limite_saque,
                             limite = limite,
                             saldo = saldo
                             )
    elif opcao == 'E':
        extrato_detalhado(extrato)
    elif opcao == 'U':
        criar_usuario(usuarios)
    elif opcao == 'C':
        # num_conta += 1
        num_conta, conta = criar_conta(AGENCIA, num_conta, usuarios)
        if conta:
            contas.append(conta)
            print('Conta criada com sucesso.') 
        else:
            print('Cpf não cadastrado.')
    else:
        print('Sistema encerrado.')
        break