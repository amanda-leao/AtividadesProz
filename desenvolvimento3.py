print("=== OPÇÃO 1: Utilizando o laço FOR (Crescente) ===")
for andar in range(1, 21):
    if andar == 13:
        continue  
    print(f"{andar}º andar")

print("\n" + "="*50 + "\n")

print("=== OPÇÃO 2: Utilizando o laço WHILE (Crescente) ===")
andar = 1
while andar <= 20:
    if andar != 13:
        print(f"{andar}º andar")
    andar += 1  

print("\n" + "="*50 + "\n")

print("=== OPÇÃO 3: DESAFIO - Ordem Decrescente ===")
for andar in range(20, 0, -1):
    if andar == 13:
        continue
    print(f"{andar}º andar")