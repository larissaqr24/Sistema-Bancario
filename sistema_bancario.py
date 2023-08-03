menu = '''\n
________Menu______
[D] = Depósito
[S] = Saque
[E] = Extrato
[Q] = Sair
__________________'''

saldo = 0
limite = 500
numero_saque = 0
limite_saque = 3
extrato = []

while True:
    opcao = input(f'Digite a opção desejada: {menu}')
    if opcao == 'D':
        saldotmp = int(input('Digite o valor para realizar o depósito:'))
        saldo += saldotmp
        print('Deposito realizado com sucesso.')
        extrato.append(saldotmp)
    elif opcao == 'S':
        valor_saque = int(input('Digite o valor para realizar o saque:'))
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
            extrato.append(valor_saque)
    elif opcao == 'E':
        print(f'Extrato detalhado: {extrato}')
    else:
        print('Sistema encerrado.')
        break
        

