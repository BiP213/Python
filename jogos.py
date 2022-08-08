# importando os arquivos/módulos dos jogos
# importante: o python importa e executa o código automaticamente
# é preciso colocar os códigos em funções a serem chamadas.
import forca
import adivinhacao


def escolhe_jogo():
    print("*********************************")
    print("*******Escolha o seu jogo!*******")
    print("*********************************")

    print("(1) Forca (2) Adivinhação")

    jogo = int(input("Qual jogo: "))

    if (jogo == 1):
        print("Jogando forca")
        forca.jogar()  # chama a função jogar() do módulo forca importado.
    elif (jogo == 2):
        print("Jogando adivinhação")
        adivinhacao.jogar(
        )  # chama a função jogar() do módulo adivinhacao importado.


# verifica se o arquivo foi chamado diretamente, se sim, executa a função escolhe_jogo()
if (__name__ == "__main__"):
    escolhe_jogo()