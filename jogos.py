# importando os arquivos/módulos dos jogos
# importante: o python importa e executa o código automaticamente
# é preciso colocar os códigos em funções a serem chamadas.
import forca
import adivinhacao


def escolhe_jogo():
    print("*********************************")
    print("*******Escolha o seu jogo!*******")
    print("*********************************\n")

    print("(1) Forca (2) Adivinhação")

    jogo = int(input("Digite o número do jogo: "))

    if (jogo == 1):
        print("Iniciando: Forca...\n")
        forca.jogar()  # chama a função jogar() do módulo forca importado.
    elif (jogo == 2):
        print("Iniciando: Adivinhação...\n")
        adivinhacao.jogar(
        )  # chama a função jogar() do módulo adivinhacao importado.


# verifica se o arquivo foi chamado diretamente, se sim, executa a função
if (__name__ == "__main__"):
    escolhe_jogo()
