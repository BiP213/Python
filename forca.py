def jogar():
    print("*********************************")
    print("***Bem-vindo ao jogo da Forca!***")
    print("*********************************")

    palavra_secreta = "banana".upper()
    palavra_tamanho = len(palavra_secreta)
    # array, lista com as letras acertadas pelo usuário.
    letras_acertadas = ["_" for letra in palavra_secreta]
    # cria uma lista e
    # adiciona dinamicamente de acordo com o tamanho da palavra
    # Funcionalidade List Comprehensions

    erros = 0

    print("Total de letras da palavra secreta: {}".format(palavra_tamanho))
    print(letras_acertadas)

    while (True):
        chute = input("Qual letra? ")
        # trata a string removendo espaços do input do usuário.
        # upper() transforma o input para maiúsculo
        chute = chute.strip().upper()

        if (chute in palavra_secreta):
            index = 0
            # devolve a posição da letra encontrada na palavra secreta.
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
