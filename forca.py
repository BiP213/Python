import random
import jogos


def jogar():

    mensagem_boas_vindas()
    palavra_secreta = carrega_palavra_secreta()

    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)
    # array, lista com as letras acertadas pelo usuário
    # cria uma lista e
    # adiciona dinamicamente de acordo com o tamanho da palavra
    # Funcionalidade List Comprehensions
    print(letras_acertadas)

    erros = 0

    while (True):
        chute = pede_chute()

        if (chute in palavra_secreta):
            acertou_chute(chute, letras_acertadas, palavra_secreta)

        else:
            erros += 1  # erros = erros + 1
            desenha_forca(erros)

        if (erros == 7):
            break
        if ("_" not in letras_acertadas):
            print(letras_acertadas)
            break

        print(letras_acertadas)

    if ("_" not in letras_acertadas):
        imprime_mensagem_vitoria()
        menu()

    else:
        imprime_mensagem_derrota(palavra_secreta)
        menu()


def mensagem_boas_vindas():
    print("*********************************")
    print("***Bem-vindo ao jogo da Forca!***")
    print("*********************************\n")


def carrega_palavra_secreta():
    arquivo = open("palavras.txt", "r")
    # abre o arquivo na variável no modo "r" leitura
    palavras = []
    # inicializa uma lista vazia

    for linha in arquivo:
        linha = linha.strip()
        # remove os \n das palavras
        palavras.append(linha)
        # adiciona as linhas na lista

    arquivo.close()
    # fecha o arquivo contendo as palavras

    numero = random.randrange(0, len(palavras))
    # gera um número aleatório entre determinado intervalo

    palavra_secreta = palavras[numero].upper()
    # pega o index da palavra na lista e transforma a palavra para maiúsculo
    return palavra_secreta


def inicializa_letras_acertadas(palavra):
    return ["_" for letra in palavra]


def pede_chute():
    chute = input("Digite uma letra: ")
    # trata a string removendo espaços do input do usuário
    # upper() transforma o input para maiúsculo
    chute = chute.strip().upper()
    return chute


def acertou_chute(chute, letras_acertadas, palavra_secreta):
    index = 0
    # devolve a posição da letra encontrada na palavra secreta
    for letra in palavra_secreta:
        if (chute == letra):
            letras_acertadas[index] = letra
        index += 1  # index = index + 1


def imprime_mensagem_vitoria():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       \n")


def imprime_mensagem_derrota(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           \n")


def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if (erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if (erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if (erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if (erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if (erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if (erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


def menu():
    print("(1) Novo jogo (2) Menu de jogos (3) Fechar")
    n = int(input("Opção: "))

    if (n == 1):
        print()
        jogar()

    elif (n == 2):
        print()
        jogos.escolhe_jogo()

    elif (n == 3):
        print()
        print("Finalizando...")

    else:
        print()
        print("Opção inválida! Digite novamente.\n")
        menu()


# verifica se o arquivo foi chamado diretamente, se sim, executa a função
if (__name__ == "__main__"):
    jogar()
