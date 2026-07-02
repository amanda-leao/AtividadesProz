def calculadora_interativa():
    while True:
        print("\n--- LISTA DE OPERAÇÕES ---")
        print("1: Soma")
        print("2: Subtração")
        print("3: Multiplicação")
        print("4: Divisão")
        print("0: Sair")
        
        opcao = input("\nDigite o número para a operação correspondente: ")
        
        if opcao == "0":
            print("Saindo do programa. Até logo!")
            break
            
        elif opcao in ["1", "2", "3", "4"]:
            try:
                num1 = float(input("Digite o primeiro valor: "))
                num2 = float(input("Digite o segundo valor: "))
                
                if opcao == "1":
                    resultado = num1 + num2
                    print(f"\nResultado da Soma: {resultado}")
                elif opcao == "2":
                    resultado = num1 - num2
                    print(f"\nResultado da Subtração: {resultado}")
                elif opcao == "3":
                    resultado = num1 * num2
                    print(f"\nResultado da Multiplicação: {resultado}")
                elif opcao == "4":
                    if num2 != 0:
                        resultado = num1 / num2
                        print(f"\nResultado da Divisão: {resultado}")
                    else:
                        print("\nErro: Não é possível dividir por zero!")
            except ValueError:
                print("\nErro: Por favor, digite apenas números válidos para os cálculos.")
                
      
        else:
            print("\nEssa opção não existe")

calculadora_interativa()