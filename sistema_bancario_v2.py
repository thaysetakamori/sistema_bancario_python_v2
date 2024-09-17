from datetime import datetime


def depositar(valor, saldo, extrato, num_transacoes):
    if valor > 0:
        saldo += valor
        data_formada = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        extrato += f"[{data_formada}] Depósito:\tR$ {valor:.2f}\n"
        num_transacoes += 1
        print("\nDepósito realizado com sucesso!\n")
    else:
        print("\nFalha na operação! O valor informado é inválido.\n")
    return saldo, extrato, num_transacoes


def sacar(valor, saldo, extrato, num_saques, num_transacoes):
    if valor > LIMITE:
        print("\nFalha na operação! O valor do saque excede o limite.\n")
    elif valor > saldo:
        print("\nFalha na operação! Você não tem saldo suficiente.\n")
    elif valor > 0:
        saldo -= valor
        data_formada = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        extrato += f"[{data_formada}] Saque:\tR$ {valor:.2f}\n"
        num_saques += 1
        num_transacoes += 1
        print("\nSaque realizado com sucesso!\n")
    else:
        print("\nFalha na operação! O valor informado é inválido.\n")
    return saldo, extrato, num_saques, num_transacoes


def exibir_extrato(saldo, extrato):
    print(" EXTRATO ".center(45, "="))
    print("Não foram realizadas movimentações.\n" if not extrato else extrato)
    print(f"Saldo: R$ {saldo:.2f}")
    print("="*45)
    print()


def criar_usuario(usuarios):
    cpf = validar_cpf()

    usuario = filtrar_usuario(cpf, usuarios)
    if usuario:
        print("\nJá existe um usuário com esse CPF.\n")
        return
    
    nome = input("Nome completo: ")
    data_nascimento = input("Data de nascimento (dd/mm/aaaa): ")
    endereco = input("Endereço (Logradouro, Nº - Bairro - Cidade/UF): ")
    novo_usuario = {"nome": nome, "cpf": cpf, "data_nascimento": data_nascimento, "endereco": endereco}
    usuarios.append(novo_usuario)
    print("\nUsuário criado com sucesso!\n")
    return novo_usuario


def validar_cpf():
    cpf = input("Informe seu CPF (somente número): ")
    while not (cpf.isdigit() and len(cpf) == 11):
        print("\nCPF inválido! Certifique-se de digitar 11 números.\n")
        cpf = input("Informe seu CPF (somente número): ")
    return cpf


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta(usuarios, contas):
    cpf = validar_cpf()
    
    usuario = filtrar_usuario(cpf, usuarios)
    if usuario:
        num_conta = len(contas) + 1
        nova_conta = {"agencia": AGENCIA, "num_conta": num_conta, "usuario": usuario}
        contas.append(nova_conta)
        
        dados_conta = {"agencia": AGENCIA, "num_conta": num_conta}
        if 'conta' not in usuario:
            usuario['conta'] = []
        usuario['conta'].append(dados_conta)
        
        print("\nConta criada com sucesso!\n")
        print(f"Agência: {AGENCIA}\nConta Corrente: {num_conta}\n")
        return nova_conta
    else:
        print("\nUsuário não encontrado! Fluxo de criação de conta encerrado.\n")


def listar_usuarios(usuarios):
    if not usuarios:
        print("Não existem usuários cadastrados!\n")
    for usuario in usuarios:
        print("=" * 43)
        print("Nome:", usuario['nome'])
        print("Data de nascimento:", usuario['data_nascimento'])
        print("Endereço:", usuario['endereco'])
        if 'conta' in usuario:
            print("-" * 43)
            for conta in usuario['conta']:
                print("Agência:", conta['agencia'], "\tC/C:", conta['num_conta'])
        print()


def listar_contas(contas):
    if not contas:
        print("Não existem contas cadastradas!\n")
    for conta in contas:
        print("=" * 43)
        print("Agência:", conta['agencia'])
        print("C/C:", conta['num_conta'])
        print("Titular:", conta['usuario']['nome'])
        print()


menu = """
Insira o número da operação desejada.
[1] Depositar
[2] Sacar
[3] Extrato
[4] Novo Usuário
[5] Nova Conta
[6] Listar Usuários
[7] Listar Contas
[0] Sair
=> """


LIMITE = 500
LIMITE_SAQUES = 3
LIMITE_TRANSACOES = 10
AGENCIA = "0001"

saldo = 0
extrato = ""
num_saques = 0
num_transacoes = 0
usuarios = []
contas = []


while True:
    opcao = input(menu)
    print()
    
    if opcao == "1":
        if num_transacoes >= LIMITE_TRANSACOES:
            print("Falha na operação! Você excedeu o número de transações permitidas para hoje.\n")
        else:
            valor = float(input("Informe o valor do depósito: "))
            saldo, extrato, num_transacoes = depositar(valor, saldo, extrato, num_transacoes)
    
    elif opcao == "2":
        if num_saques >= LIMITE_SAQUES:
            print("Falha na operação! Número máximo de saques excedido.\n")
        elif num_transacoes >= LIMITE_TRANSACOES:
            print("Falha na operação! Você excedeu o número de transações permitidas para hoje.\n")
        else:
            valor = float(input("Informe o valor do saque: "))
            saldo, extrato, num_saques, num_transacoes = sacar(valor, saldo, extrato, num_saques, num_transacoes)
        
    elif opcao == "3":
        exibir_extrato(saldo, extrato)
        
    elif opcao == "4":
        criar_usuario(usuarios)
        
    elif opcao == "5":
        criar_conta(usuarios, contas)
        
    elif opcao == "6":
        listar_usuarios(usuarios)
    
    elif opcao == "7":
        listar_contas(contas)
        
    elif opcao == "0":
        break
    
    else:
        print("Opção inválida. Tente novamente.\n")