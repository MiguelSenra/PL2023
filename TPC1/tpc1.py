import matplotlib.pyplot as plt
import numpy as np

# Não existe propriamente algum dado que seja único. Portanto não é fácil garantir a existência de uma chave pelo que guardar os dados num dicionário poderá
# não ser muito relevante pelo que estaríamos a adicionar mais um valor desnecsserário por cada campo. Analisando agora as operações que esperámos
# definir, podemos verificar que devido aos seguintes factos a única forma de determinar todos os valores que pretendemos será percorrer todos os dados. Desta
# forma, concluimos que será necessário um tempo linear para alcançar o nosso objetivo pelo que não achei que nenhuma estrutura fosse melhor que uma simples
# lista pelo que decidi utilizar a mesma. 


def ler():
    fd = open("myheart.csv")
    lines = fd.readlines()
    pessoas = []
    lines.pop(0)
    for line in lines:
        data = []
        line = line.split(",")
        for char in line:
            if char != "M" and char != "F":
                char = int(char)
            data.append(char)
        pessoas.append(data)
    return pessoas

# Após concluir o armazenamento dos dados, é necessário determinar uma estrutura que consiga guardar as distribuições de forma inteligente. Em primeiro lugar,
# a distribuição consistirá em guardar os atributos da população de forma a tentar determinar algumas possíveis dependências, e depois associará a cada valor,
# o número de pessoas que possuem esse mesmo atributo e que possuem a doença. 


def distporsexo(lista):
    res = dict()

    for line in lista:
        if line[5]:
            key = line[1]
            if (key not in res):
                res[key] = 0
            res[key] += 1
    dictionary1 = sorted(res.items())
    return dict(dictionary1)


def distporIdade(lista):
    res = dict()
    for line in lista:
        if line[5]:
            val = line[0]
            resto = val % 10
            if resto < 5:
                min = val-resto
            else:
                min = val-resto+4+1
            max = min+4
            key = '['+str(min)+'-'+str(max)+']'
            if (key not in res):
                res[key] = 0
            res[key] += 1
    dictionary1 = sorted(res.items())
    return dict(dictionary1)


def distporColesterol(lista):
    res = dict()
    for line in lista:
        if line[5]:
            val = line[3]
            resto = val % 10
            min = val-resto
            max = min+9
            key = '['+str(min)+'-'+str(max)+']'
            if (key not in res):
                res[key] = 0
            res[key] += 1
    dictionary1 = sorted(res.items())
    return dict(dictionary1)


def printTable(dist):
    for key in dist:
        print("-----------------------------")
        string = '|'
        comp = int((13-len(key))/2)
        for i in range(comp):
            string += ' '
        string += key
        for i in range(comp):
            string += ' '
        string += "|"
        comp = 13-len(str(dist[key]))
        if comp % 2 != 0:
            comp = int(comp/2)
            comp1 = comp+1
        else:
            comp = int(comp/2)
            comp1 = comp
        for i in range(comp):
            string += ' '
        string += str(dist[key])
        for i in range(comp1):
            string += ' '
        print(string+"|")
    print("-----------------------------")


def main():
    lista = ler()
    distSexo = distporsexo(lista)
    distIdade = distporIdade(lista)
    distColesterol = distporColesterol(lista)
    print("-----------------------------")
    print("|   Distribuição Por Sexo   |")
    print("-----------------------------")
    printTable(distSexo)

    y1 = ["Feminino", "Masculino"]
    y2 = distSexo.values()
    plt.bar(y1, y2, color="red")
    plt.xlabel("Género")
    plt.ylabel("Número de pessoas com a doença")
    plt.title("Distribuição da doença por Género")
    plt.show()

    print()
    print("-----------------------------")
    print("|  Distribuição Por Idade   |")
    print("-----------------------------")
    printTable(distIdade)

    y1 = distIdade.keys()
    y2 = distIdade.values()
    plt.bar(y1, y2, color="red")
    plt.xlabel("Faixa Etária (anos)")
    plt.ylabel("Número de pessoas com a doença")
    plt.title("Distribuição da doença por Idades")
    plt.show()

    print()
    print("-----------------------------")
    print("|Distribuição Por Colesterol|")
    print("-----------------------------")
    printTable(distColesterol)

    y1 = distColesterol.keys()
    y2 = distColesterol.values()
    plt.bar(y1, y2, color="red")
    plt.xlabel("Valores de Colesterol")
    plt.ylabel("Número de pessoas com a doença")
    plt.title("Distribuição da doença por Idades")
    plt.show()


main()
