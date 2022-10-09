import random


def jogar():
    print("*********************************")
    print("***Bem-vindo ao jogo da Forca!***")
    print("*********************************")

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

    letras_acertadas = ["_" for letra in palavra_secreta]
    # array, lista com as letras acertadas pelo usuário
    # cria uma lista e
    # adiciona dinamicamente de acordo com o tamanho da palavra
    # Funcionalidade List Comprehensions

    erros = 0

    while (True):
        chute = input("Qual letra? ")
        # trata a string removendo espaços do input do usuário
        # upper() transforma o input para maiúsculo
        chute = chute.strip().upper()

        if (chute in palavra_secreta):
            index = 0
            # devolve a posição da letra encontrada na palavra secreta
            for letra in palavra_secreta:
                if (chute == letra):
                    letras_acertadas[index] = letra
                index += 1  # index = index + 1

        else:
            erros += 1  # erros = erros + 1
            print("EROU! {} tentativas restantes.".format(6-erros))

        if (erros == 6):
            break
        if ("_" not in letras_acertadas):
            print(letras_acertadas)
            break

        print(letras_acertadas)

    if ("_" not in letras_acertadas):
        print("Você ganhou!")

    else:
        print("Você perdeu!")

    print("Fim do jogo")


# verifica se o arquivo foi chamado diretamente, se sim, executa a função jogar()
if (__name__ == "__main__"):
    jogar()
