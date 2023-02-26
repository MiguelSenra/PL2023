# Exercicio 1

# As linhas são separadas por palavras e verfica-se se uma palavra é uma sequência de dígitos.
# Se for, então somo o valor, caso contrário a palavra é considerada como inválida e é ignorada.
def soma_text(nome):
    soma = 0
    f = open(nome)  # abrir o ficheiro
    lines = f.readlines()  # ler as linhas do ficheiro
    for line in lines:
        # separar uma linha por espaços e retirar o '\n'
        line_splitted = line[:-1].split(" ")
        for word in line_splitted:
            if word.isdigit():  # verificar se uma string só possui dígitos
                soma += int(word)
    f.close()
    return soma

# Exercicio 2

# Mesmo processo do exercicio 1 mas em vez de ler as linhas de um ficheiro, lê do standard input.


def soma_input():
    soma = 0
    print("Insira os valores desejados")
    while (True):
        line = input()  # leitura de linha
        # separar uma linha por espaços (o '\n' já é retirado automaticamente)
        line_splitted = line.split(" ")
        for word in line_splitted:
            if word.isdigit():  # verificar se uma string só possui dígitos
                soma += int(word)
        print("O valor atual da soma é: " + str(soma))  # indicação para debug


# Exercicio 3

# Neste exercício é premitida realizar uma nova funcionalidade. Desligar a calculadora
# Para tal, a mesma começa
def soma_input_OFF():
    ligado = True
    soma = 0
    print(soma)
    print("Insira os valores desejados")
    while (True):
        line = input()
        line_splitted = line.split(" ")
        for word in line_splitted:
            if ligado == True and tem_OFF(word):
                ligado = False
            if ligado and word.isdigit():
                soma += int(word)
        print("O valor atual da soma é: " + str(soma))

# A forma de identificar um On ou um Off é diferente pelo que a palavra Off poderá
# estar colocada entre outros caracteres


def tem_OFF(word):
    fase = 0
    res = False
    for char in word:
        if char == 'O' or char == 'o':
            fase += 1
        elif (fase == 1 or fase == 2) and (char == 'F' or char == 'f'):
            fase += 1
        else:
            fase = 0
        if fase == 3:
            res = True
            break
    return res


# Exercicio 4

# Neste exercício, ao contrário do anterior adicinei a funcionalidade de ligar a calculadora
def soma_input_ON():
    ligado = False
    soma = 0
    print(soma)
    print("Insira os valores desejados")
    while (True):
        line = input()
        line_splitted = line.split(" ")
        for word in line_splitted:
            if ligado == False and tem_On(word):
                ligado = True
            if ligado and word.isdigit():
                soma += int(word)
        print("O valor atual da soma é: " + str(soma))

# Funcionamento igual ao Off


def tem_On(word):
    fase = 0
    res = False
    for char in word:
        if char == 'O' or char == 'o':
            fase += 1
        elif fase == 1 and (char == 'N' or char == 'n'):
            fase += 1
        else:
            fase = 0
        if fase == 2:
            res = True
            break
    return res

# Exercicio 5
# Este é o exercício que junta todas as funcionalidades desenvolvidas anteriormente.
# Para além disso, foi adicionada a funcionalidade do caractere '=' que quando é encontrado um certo
# número de vezes numa palavra, é mostrado o resultado atual da soma esse número de vezes. No entanto,
# este não coloca o valor da soma a 0, pelo que este vai ser sempre incrementado.


def soma_input_Final():
    ligado = False  # A calculadora começa a sua atividade desligada
    soma = 0
    print("Insira os valores desejados: ")
    while (True):
        line = input()  # inserir o input do utilizador
        line_splitted = line.split(" ")
        for word in line_splitted:
            # verificar se há ON para ligar calculadora
            if ligado == False and tem_On(word):
                ligado = True
            # verificar se há Off para desligar calculadora
            if ligado == True and tem_OFF(word):
                ligado = False
            if ligado and word.isdigit():  # verificar se a calculadora está ligada e se a palavra é uma string
                soma += int(word)
            # conta o número de '=' numa palavra e imprime esse número de vezes o valor da soma
            for i in range(Nr_Igual(word)):
                print("O valor atual da soma é: " + str(soma))

# conta o número de '=' numa palavra


def Nr_Igual(word):
    res = 0
    for char in word:
        if char == '=':
            res += 1
    return res


soma_input_Final()
