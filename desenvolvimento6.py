def cadastrar_usuario():
    nome_completo = input("Digite seu nome completo: ")

    while True:
        try:
            ano_nascimento = int(input("Digite seu ano de nascimento (entre 1922 e 2021): "))
            
            if 1922 <= ano_nascimento <= 2021:
                break  
            else:
                print("Erro: O ano deve ser um valor válido entre 1922 e 2021. Tente novamente.")
                
        except ValueError:
            print("Erro: Entrada inválida. Por favor, digite um número inteiro correspondente ao ano.")

    ano_atual = 2022
    idade = ano_atual - ano_nascimento

    print("\n" + "="*40)
    print(f"Nome do usuário: {nome_completo}")
    print(f"Idade completada (ou a completar) em {ano_atual}: {idade} anos")
    print("="*40)

cadastrar_usuario()