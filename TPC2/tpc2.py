def soma_text(nome):
    soma = 0
    f = open(nome)
    lines = f.readlines()
    for line in lines:
        line_splitted = line[:-1].split(" ")
        for word in line_splitted:
            if word.isdigit():
                soma += int(word)
    f.close()
    return soma


def soma_input():
    soma = 0
    print("Insira os valores desejados")
    while (True):
        line = input()
        print(line)
        line_splitted = line.split(" ")
        for word in line_splitted:
            if word.isdigit():
                soma += int(word)
        print("O valor atual da soma é: " + str(soma))


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


def soma_input_Final():
    ligado = False
    soma = 0
    print("Insira os valores desejados: ")
    while (True):
        line = input()
        line_splitted = line.split(" ")
        for word in line_splitted:
            if ligado == False and tem_On(word):
                ligado = True
            if ligado == True and tem_OFF(word):
                ligado = False
            if ligado and word.isdigit():
                soma += int(word)
            for i in range(Nr_Igual(word)):
                print("O valor atual da soma é: " + str(soma))


def Nr_Igual(word):
    res = 0
    for char in word:
        if char == '=':
            res += 1
    return res


soma_input_Final()
