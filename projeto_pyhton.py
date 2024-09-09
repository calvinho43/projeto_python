
menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=>
"""
saldo = 0
limite = 4300
extrato = ""
num_saq = 0
lim_saq = 3

while True:
    opcao = input(menu)
    if opcao == "d":
        valor = float(input("Quanto deseja depositar? "))
        if valor > 0: 
            saldo += valor
            extrato += f"deposito: R$ {valor:.2f} \n"
        
        else: 
            print("Digite um valor válido.")
    
    elif opcao == "s":
        valor = float(input("Quanto deseja sacar? "))
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = num_saq >= lim_saq

        if excedeu_saldo:
            print("Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("O valor excede o limite.")
        
        elif excedeu_saques:
            print("Número máximo de saques excedido.")

        elif valor > 0: 
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            num_saq += 1

    elif opcao == "e":
        print("\r>>>>>>> EXTRATO <<<<<<<")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\n Saldo: R$: {saldo:.2f}")
        print(">>>>>>>>>>>><><<<<<<<<<<<")

    elif opcao == "q":
        break

    else: 
        print("Operação inválida, tente novamente")