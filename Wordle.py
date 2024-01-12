import random

# Ler palavras de um arquivo de texto
with open("C:\\Users\\ph112\\Downloads\\Wordle\\palavras.txt", "r", encoding="utf-8") as file:
    palavras = [linha.strip() for linha in file]

# Escolher uma palavra aleatória
palavra_aleatoria = random.choice(palavras)

print(" ## ")
print(" ## ")
print("#####    ####    ######   ##  ##    ####")
print(" ##     ##  ##    ##  ##  #######  ##  ##")
print(" ##     ######    ##      ## # ##  ##  ##")
print(" ## ##  ##        ##      ##   ##  ##  ##")
print(" ###    #####    ####     ##   ##   ####")

def verificar_acerto_erro(escolhida, aleatoria):
    if escolhida == aleatoria:
        letras_unicas_aleatoria = []
        
        for i, letra in enumerate(escolhida):
            if letra not in letras_unicas_aleatoria:
                letras_unicas_aleatoria.append(letra)
            if letra == aleatoria[i]:
                print(f'\033[32m{escolhida[i]}\033[0m', end=' ')  # Verde se estiver na posição correta
        
        return True

    else:   
        exibir_letras_corretas(escolhida, aleatoria)

    return False

def exibir_letras_corretas(escolhida, aleatoria):
    letras_unicas_aleatoria = []

    for i, letra in enumerate(escolhida):
        if letra not in letras_unicas_aleatoria:
            letras_unicas_aleatoria.append(letra)
        if letra == aleatoria[i]:
            print(f'\033[32m{escolhida[i]}\033[0m', end=' ')  # Verde se estiver na posição correta
        elif letra in aleatoria:
            print(f'\033[33m{escolhida[i]}\033[0m', end=' ')  # Amarelo se estiver na palavra, mas na posição errada
        else:
            print(f'\033[90m{escolhida[i]}\033[0m', end=' ')  # Cinza se não estiver na palavra

    print("\n")

tentativas = 5 # Número de tentativas permitidas

while tentativas > 0:
    # Solicitar ao usuário uma letra
    print("\n")
    palavra_escolhida = input("Digite uma palavra: ")
    print("\n")

    if len(palavra_escolhida) != 5:
        print("Por favor, digite uma palavra com exatamente 5 letras.")
        continue
    
    
    acerto = verificar_acerto_erro(palavra_escolhida, palavra_aleatoria)
    
    if acerto:
        break

    tentativas -= 1

    if tentativas == 0:
         print(f"Suas tentativas acabaram! A palavra era: {palavra_aleatoria}")


        
        
    
       