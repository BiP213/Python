import random
import jogos


def jogar():
    print("*********************************")
    print("Bem-vindo ao jogo de Adivinhação!")
    print("*********************************")

    # gera um número pseudo aleatório utilizando o módulo "random" importado
    numero_secreto = random.randrange(1, 101)
    total_de_tentativas = 0
    pontos = 1000

    print("Selecione o nível de dificuldade:")
    print("(1) Fácil (2) Médio (3) Difícil")

    nivel = int(input("Modo: "))

    if (nivel == 1):
        total_de_tentativas = 20
    elif (nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for rodada in range(1, total_de_tentativas + 1):
        print("Tentativa {} de {}\n".format(rodada, total_de_tentativas))

        chute_str = input("Digite um número entre 1 e 100: ")
        print("Você digitou", chute_str)
        chute = int(chute_str)

        if (chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100!\n")
            continue

        acertou = (chute == numero_secreto)
        maior = (chute > numero_secreto)
        menor = (chute < numero_secreto)

        if (acertou):
            print("Parabéns! Você acertou e fez {} pontos!\n".format(pontos))
            break
        else:
            if (maior):
                print("O seu chute foi maior do que o número secreto!\n")
                if (rodada == total_de_tentativas):
                    print(
                        "O número secreto era {}. Você fez {} pontos.\n".format(
                            numero_secreto, pontos))
            elif (menor):
                print("O seu chute foi menor do que o número secreto!\n")
                if (rodada == total_de_tentativas):
                    print(
                        "O número secreto era {}. Você fez {} pontos.\n".format(
                            numero_secreto, pontos))
            # abs() mostra o número absoluto, ou seja, sempre positivo
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

    menu()


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
