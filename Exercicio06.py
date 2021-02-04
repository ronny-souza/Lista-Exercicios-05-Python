# QUESTÃO 06 - Crie uma função lambda que receba a base e a altura de um triângulo e retorne a área desse 
# triângulo.


base = int(input("Digite o valor da base: "))
altura = int(input("Digite o valor da altura: "))

triangulo = lambda base, altura: (base * altura) / 2

print(triangulo(base, altura))