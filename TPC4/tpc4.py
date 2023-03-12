import re
import json
import statistics
import math

# abrir o ficheiro de leitura
fp = open("alunos.csv", "r")
datalist_json = []
lines = fp.readlines()
# expressão regular para a separação de cada um dos campos
campos = re.split(r"(?<!\{\d)\s*,\s*(?!\\d\})", lines[0])
# dicionario para guardar os campos do cabeçalho
head = dict()
# expressão regular para retirar os dados extra de cada campo
sintax = re.compile(
    r"(?P<nome>\w+)({(?P<min>\d+)(,(?P<max>\d+))?}(::(?P<operation>\w+))?)?")
for elem in campos:
    res = sintax.match(elem)
    if res:
        # adicionar cada campo ao dicionario head
        head[res.group("nome")] = dict()
        if (res.group("min")):
            head[res.group("nome")]["min"] = res.group("min")
            if (res.group("max")):
                head[res.group("nome")]["max"] = res.group("max")
            if (res.group("operation")):
                head[res.group("nome")]["op"] = res.group("operation")
# percorrer cada uma das linhas de  dados
for line in lines[1:]:
    # retirar o '\n'
    line = line[:-1]
    data_json = dict()
    data = re.split(r"\s*,\s*", line)
    i = 0
    for key in head:
        nome = key
        # verificar se aquele campo é uma lista
        if "min" not in head[key]:
            data_json[key] = data[i]
            i += 1
        else:
            lista = []
            # verificar se a lista é de tamanho fixo
            if "max" not in head[key]:
                for j in range(i, i+int(head[key]["min"])):
                    lista.append(int(data[j]))
                i += int(head[key]["min"])
            else:
                # a lista é de tamanho variável
                for j in range(i, i+int(head[key]["min"])):
                    lista.append(int(data[j]))
                for j in range(i+int(head[key]["min"]), i+int(head[key]["max"])):
                    if (data[j]):
                        lista.append(int(data[j]))
                i += int(head[key]["max"])
                # verificar se a lista possui uma função de acumulador
                if "op" in head[key]:
                    if (head[key]["op"]):
                        match (head[key]["op"]):
                            case "sum":
                                lista = sum(lista)
                                nome += "_sum"
                                data_json[nome] = lista
                            case "media":
                                lista = statistics.mean(lista)
                                nome += "_media"
                                data_json[nome] = lista
                            case "produto":
                                lista = math.prod(lista)
                                nome += "_produto"
                                data_json[nome] = lista
                            case "mediana":
                                lista = statistics.median(lista)
                                nome += "_mediana"
                                data_json[nome] = lista
                            case "moda":
                                lista = statistics.mode(lista)
                                nome += "_mode"
                                data_json[nome] = lista

                else:
                    data_json[nome] = lista
    # contruir a nossa lista de dados
    datalist_json.append(data_json)

# colocar a lista de dados no ficheiro json
f = open("alunos.json", "w")
json.dump(datalist_json, f, indent=' ')
