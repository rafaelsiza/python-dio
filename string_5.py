menu = ('''

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair


=>  ''')


saldo = 0
limite = 500
extrato =  ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)
    
    if opcao == "d":
        print ("d")

    elif opcao == "s":
        print ("s")
        
    elif opcao == "e":
        
        print ("e")
        
    elif opcao == "q":
        break

    else:
        print("Op. Inválida, por favor selecione novamente a operação desejada.")
a