# Crie uma função que receba a quantidade de linhas e de colunas que o computador deve imprimir com o 
# caractere *. Exemplo. Se receber 3 e 4, deve ser impresso:
#
# ****
# ****
# ****

def criaAsteriscos(linhas, colunas):
    lista = [["*"]*colunas for i in range(linhas)]
   
    for i in lista:
        print("\n")
        for j in i:
            print(j, end="")

quantidadeLinhas = int(input("Digite a quantidade de linhas: "))
quantidadeColunas = int(input("Digite a quantidade de colunas: "))
criaAsteriscos(quantidadeLinhas, quantidadeColunas)