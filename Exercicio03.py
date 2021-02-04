# Crie uma função que receba do usuário a base (b) e o expoente ​(n), e calcule e retorne ​b​^n.

def calculoPotencia(base, expoente):
    return base**expoente


base = int(input("Digite o valor da base: "))
expoente = int(input("Digite o valor do expoente: "))

print(calculoPotencia(base, expoente))