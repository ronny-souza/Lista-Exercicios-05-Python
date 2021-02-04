# QUESTÃO 05 - Crie uma função que receba os seguintes dados de uma criança: nome, data de nascimento, sexo, 
# cidade de nascimento, nome da mãe e nome do pai. Caso a cidade não seja preenchida, considerar que a criança 
# nasceu em Jaboatão. Caso o nome do pai não seja preenchido, indicar “Não identificado”. A função deve 
# imprimir os dados da criança.

def dadosCrianca(nome, dataNascimento, sexo, cidade, nomeMae, nomePai):
    dados = [nome, dataNascimento, sexo, cidade, nomeMae, nomePai]

    if dados[3] == "":
        dados[3] = "Jaboatão"

    if dados[5] == "":
        dados[5] = "Não Identificado"
    
    print(f"DADOS DA CRIANÇA:\n\nNome: {dados[0]}\nData de Nascimento: {dados[1]}\nSexo: {dados[2]}\nCidade: {dados[3]}\nNome da Mãe: {dados[4]}\nNome do Pai: {dados[5]}")


nome = input("Nome da criança: ")
dataNascimento = input("Digite a data de nascimento: ")
sexo = input("Digite o sexo da criança: ")
cidade = input("Digite a cidade de nascimento: ")
nomeMae = input("Digite o nome da mãe: ")
nomePai = input("Digite o nome do pai: ")
dadosCrianca(nome, dataNascimento, sexo, cidade, nomeMae, nomePai)