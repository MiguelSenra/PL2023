import matplotlib.pyplot as plt
import numpy as np

# Não existe propriamente algum dado que seja único. Portanto não é fácil garantir a existência de uma chave pelo que guardar os dados num dicionário poderá
# não ser muito relevante pelo que estaríamos a adicionar mais um valor desnecsserário por cada campo. Analisando agora as operações que esperámos
# definir, podemos verificar que devido aos seguintes factos a única forma de determinar todos os valores que pretendemos será percorrer todos os dados. Desta
# forma, concluimos que será necessário um tempo linear para alcançar o nosso objetivo pelo que não achei que nenhuma estrutura fosse melhor que uma simples
# lista pelo que decidi utilizar a mesma. Em termos de validação de dados optei por não remover nenhum.


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
# o número de pessoas que possuem esse mesmo atributo e que possuem a doença. Para este caso concreto, considerando que não é um problema com muitos dados, a
# procura do mesmos não é muito difícil de realizar manualmente. No entanto, pensando numa expansão dos dados, decidi utilizar um dicionário pelo facto de
# poder procurar mais facilmente caso pretenda determinar algum valor concreto. Caso contrário, qualquer estrutura seria semelhante pelo facto de ser
# apenas necessário percorrer todos os valores.


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
    min = 2000
    max = 0
    for line in lista:
        if line[5]:
            val = line[0]
            resto = val % 10
            if resto < 5:
                min_intervalo = val-resto
            else:
                min_intervalo = val-resto+4+1
            max_intervalo = min_intervalo+4

            if min_intervalo < min:
                min = min_intervalo
            if max_intervalo > max:
                max = max_intervalo

            key = '['+str(min_intervalo)+'-'+str(max_intervalo)+']'
            if min >= 30:
                if (key not in res):
                    res[key] = 0
                res[key] += 1

    for i in range(min, max, 5):
        key = '['+str(i)+'-'+str(i+4)+']'
        if key not in res:
            res[key] = 0

    dictionary1 = sorted(res.items())
    return dict(dictionary1)

# A distribuição do colesterol foi muito semelhante às outras duas. No entanto, neste, tal como na distribuição em função da idade foi necessário considerar
# outro parâmetro, a existência de níveis de colesterol que não corresponde ao de qualuqer pessoa presente no estudo. No entanto, achei por bem acresccentá-
# -los de modo a não deixar dúvidas a quem visualiza a distribuição. Isto porque caso não tivesse colocado aqueles valores, os leitores poderiam interpretar
# que aquele intervalo de colesterol não foi alvo do nosso estudo, o que seria mentira.


def distporColesterol(lista):
    res = dict()
    min = 2000
    max = 0
    for line in lista:
        if line[5]:
            val = line[3]
            resto = val % 10
            min_intervalo = val-resto
            max_intervalo = min_intervalo+9

            if min_intervalo < min:
                min = min_intervalo
            if max_intervalo > max:
                max = max_intervalo

            key = '['+str(min_intervalo)+'-'+str(max_intervalo)+']'
            if (key not in res):
                res[key] = 0
            res[key] += 1

    for i in range(min, max, 10):
        key = '['+str(i)+'-'+str(i+9)+']'
        if key not in res:
            res[key] = 0

    dictionary1 = sorted(res.items(), key=lambda x: compare(x[0]))
    return dict(dictionary1)


def compare(str):
    str = str.split("-")[0]
    str = str.split("[")[1]
    return int(str)


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

    lista = list(distColesterol.keys())
    y1 = list(map(lambda x: 5+compare(x), lista))
    y2 = distColesterol.values()
    plt.xticks(y1, rotation=45, ha='right')
    # plt.yticks(y2)
    plt.bar(y1, y2, color="red")
    plt.xlabel("Valores de Colesterol")
    plt.ylabel("Número de pessoas com a doença")
    plt.title("Distribuição da doença por Idades")
    plt.show()

# Através dos gráficos de barras acima, fica mais fácil de visualizar os valores obtidos e as suas dependências. Quanto ao primeiro gráfico, há uma grande
# diferença em termos de valores entre os dois géneros pelo que se suspeita que a doença aparecerá com mais facilidade nos homens. Analisando os dois outros
# gráficos, rapidamente nos apercebemos que estamos aproximadamente perante uma distribuição Normal, onde temos um pico para as idades por volta dos 57 anos
# e para os níveis de colesterol um valor a rondar os 255. Desta forma, parece que existe uma relação entre a idade, o género e o nível de colesterol e a
# doença, pelo que estes são fatores de risco para o desenvolvimento desta doença.
# Por fim, gostaria de referir que uma boa forma de também analisar os dados obtidos seria ter uma noção de percentagem, sendo esta apenas obtida graficamente
# e através de alguma aproximação pelo que apenas dá para ter uma perceção.


main()
