def jogar():
    print("*********************************")
    print("***Bem-vindo ao jogo da Forca!***")
    print("*********************************")

    palavra_secreta = "banana"
    # array, lista com as letras acertadas pelo usuário.
    letras_acertadas = ["_", "_", "_", "_", "_", "_"]

    enforcou = False
    acertou = False

    print(letras_acertadas)

    while (not acertou and not enforcou):
        chute = input("Qual letra? ")
        # trata a string removendo espaços do input do usuário.
        chute = chute.strip()

        # devolve a posição da letra encontrada na palavra secreta.
        index = 0
        for letra in palavra_secreta:
            # upper() transforma o input para maiúsculo
            if (chute.upper() == letra.upper()):
                letras_acertadas[index] = letra
            index = index + 1

        print(letras_acertadas)

    print("Fim do jogo")


# verifica se o arquivo foi chamado diretamente, se sim, executa a função jogar()
if (__name__ == "__main__"):
    jogar()