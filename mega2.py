import random

def jogar_mega_sena():
    print("Jogo da Mega-Sena")
    print("=" * 15)
    print("Gerando 6 números aleatórios entre 1 e 60...")

    numeros_sorteados = sorted(random.sample(range(1, 61), 6))

    print("Os números sorteados são:", numeros_sorteados)

jogar_mega_sena()