import re
import math
import json

# Exercicio1 calcular o número de processos realizados por ano


def distribuicao_anos(file):
    dist = dict()
    fp = open(file)
    lines = fp.readlines()
    # para eliminar linhas repetidas. Optei por esta forma porque os registos estão ordenados pelo nome da pessoa associada ao registo.
    # Assim duas linhas iguais aparecem consecutivamente
    line_ant = ""
    for line in lines:
        if line == line_ant:
            continue
        # definição e  aplicação da expressão regular à linha para retirar o ano de processo através de um grupo de captura com nome
        er = re.compile(r"\d+::(?P<ano>\d+)-")
        res = er.match(line)
        # adicionar o valor ao dicionário (se não existir acrescenta chave e valor 1 caso contrário soma uma unidade ao valor atual )
        if res:
            # print(res.group("ano"))
            if res.group("ano") not in dist:
                dist[res.group("ano")] = 0
            dist[res.group("ano")] += 1
        # alteração da linha anterior para validação da proxima linha
        line_ant = line
    # ordenação das chaves do dicionário para uma melhor visualização dos resultados
    dist = dict(sorted(dist.items()))

    # Pretty Print (facilitar a legibilidade)
    print("+" + "-" * 24 + "+")
    print("|  ano  | Nr de Registos |")
    print("+" + "-" * 24 + "+")
    for ano in dist:
        print(f"|   {ano}   | {dist[ano]}" +
              " " * (12-len(str(dist[ano])))+"|")
    print("+" + "-" * 24 + "+")


# Exercicio 2
# Neste exercicio foi pedido para fazer uma distribuição dos nomes e apelidos mais utilizados de cada século. Depois, foi pedido
# que calculasse o top 5 dos nomes mais utilizados. Neste sentido, existiu alguma dúvida se o top 5 seria global ou se seria
# por cada século. Neste sentido, venho apenas justificar que o que me pareceu mais sensato foi fazer o top 5 por cada século.

def distribuicao_nomes(file):
    dist_nome = dict()  # a chave é o século
    dist_apelido = dict()
    fp = open(file)
    lines = fp.readlines()
    # para eliminar linhas repetidas. Optei por esta forma porque os registos estão ordenados pelo nome da pessoa associada ao registo.
    # Assim duas linhas iguais aparecem consecutivamente
    line_ant = ""
    for line in lines:
        if line == line_ant:
            continue
        er = re.compile(
            r".*?::(?P<ano>\d{4})-\d{2}-\d{2}::(?P<nome>\w+)[\w|\s]+?(?P<apelido>\w+)::.*?::.*?::.*?::")
        res = er.match(line)
        if res:
            ano = int(res.group("ano"))
            nome = res.group("nome")
            apelido = res.group("apelido")
            r = 0
            sec = math.ceil(ano/100)
            if sec not in dist_nome:
                dist_nome[sec] = dict()

            if sec not in dist_apelido:
                dist_apelido[sec] = dict()

            if nome not in dist_nome[sec]:
                (dist_nome[sec])[nome] = 1
            else:
                (dist_nome[sec])[nome] += 1
            if apelido not in dist_apelido[sec]:
                (dist_apelido[sec])[apelido] = 1
            else:
                (dist_apelido[sec])[apelido] += 1
        line_ant = line
    # retirar o top5 de nomes mais utilizador por século
    for key in dist_nome:
        lista = list(dist_nome[key].items())
        lista.sort(key=lambda x: x[1], reverse=True)
        dist_nome[key] = lista[:5]
    # retirar o top5 de apelidos mais utilizador por século
    for key in dist_apelido:
        lista = list(dist_apelido[key].items())
        lista.sort(key=lambda x: x[1], reverse=True)
        dist_apelido[key] = lista[:5]

    # ordenar o dicionário de acordo com as chaves
    dist_nome = dict(sorted(dist_nome.items()))
    dist_apelido = dict(sorted(dist_apelido.items()))

    # Pretty Print (facilitar a legibilidade) tabela dos nomes
    print("+" + "-" * 42 + "+")
    print("| Século |  |      Nome      | Nr registos |")
    print("+" + "-" * 42 + "+")
    for sec in dist_nome:
        i = 1
        for nome in dist_nome[sec]:
            if i == 1:
                print("|   " + str(sec)+"   |"+str(i)+"º|  " +
                      nome[0] + " "*(14-len(nome[0])) + "|   "+str(nome[1]) + " "*(10-len(str(nome[1]))) + "|")

            else:
                print("|        |"+str(i)+"º|  " +
                      nome[0] + " "*(14-len(nome[0]))+"|   " + str(nome[1]) + " "*(10-len(str(nome[1]))) + "|")
            i += 1
        print("+" + "-" * 42 + "+")

    # Pretty Print (facilitar a legibilidade) tabela dos apelidos
    print("\n\n+" + "-" * 42 + "+")
    print("| Século |  |     Apelido    | Nr registos |")
    print("+" + "-" * 42 + "+")
    for sec in dist_apelido:
        i = 1
        for apelido in dist_apelido[sec]:
            if i == 1:
                print("|   " + str(sec)+"   |"+str(i)+"º|  " +
                      apelido[0] + " "*(14-len(apelido[0])) + "|   "+str(apelido[1]) + " "*(10-len(str(apelido[1]))) + "|")

            else:
                print("|        |"+str(i)+"º|  " +
                      apelido[0] + " "*(14-len(apelido[0]))+"|   " + str(apelido[1]) + " "*(10-len(str(apelido[1]))) + "|")
            i += 1
        print("+" + "-" * 42 + "+")

# Exercicio 3, frequência dos vários tipos de relação


def distribuicao_relacao(file):
    dist = dict()
    fp = open(file)
    lines = fp.readlines()
    # para eliminar linhas repetidas. Optei por esta forma porque os registos estão ordenados pelo nome da pessoa associada ao registo.
    # Assim duas linhas iguais aparecem consecutivamente
    line_ant = ""
    for line in lines:
        if line_ant == line:
            continue
        # definição e  aplicação da expressão regular à linha para retirar as várias relações extra indicadas numa determinada linha.
        # Para tal, existiram alguns cuidados especiais que tive.
        # Em primeiro lugar, alguns registos possuíam informação que nada tinha a ver com uma relação de parentesco, mas que continuavam a ser escolhidos
        # devido ao facto da estrutura ser muito semelhante. Desta forma, considerei que eram válidos aqueles graus de parentesco que indicassem em seguida
        # o número de um processo, ou seja, como se aquilo fosse o comprovativo de relação.
        # Em segundo lugar, alguns campos tinham a informação de que o documento estava danificado. Esses processos não foram removidos da contagem, ou seja,
        # se mantivessem alguma relação que cumprisse os requisitos da regra 1, então este foi considerado
        er = re.compile(
            r"(:{2}|\.)\s*[\w\s]+?,\s*(?P<relacao>[\w\s]+?)\.\s*Proc\.\d+")
        res = er.finditer(line)
        # verificar se a linha fez "match" (não re.match) com a expressão regular contendo por isso dados válidos nos respetivos valores de grupo
        if res:
            # adicionar o valor ao dicionário (se não existir acrescenta chave e valor 1 caso contrário soma uma unidade ao valor atual )
            for elem in res:
                relacao = elem.group("relacao")
                if relacao not in dist:
                    dist[relacao] = 1
                else:
                    dist[relacao] += 1
        # alteração da linha anterior para validação da proxima linha
        line_ant = line

    # ordenação das chaves do dicionário para uma melhor visualização dos resultados
    dist = dict(sorted(dist.items()))

    # Pretty Print (facilitar a legibilidade)
    print("+" + "-" * 41 + "+")
    print("|          Relação           | Nr pessoas |")
    print("+" + "-" * 41 + "+")
    for relacao in dist:
        print(f"| {relacao}"+" "*(27-len(str(relacao))) +
              f"| {dist[relacao]}" + " " * (11-len(str(dist[relacao])))+"|")
    print("+" + "-" * 41 + "+")


def fich_json(file_name):
    fp = open(file_name, "r")
    f = open("dict.json", "w")
    i = 0
    lines = fp.readlines()
    lista = []
    # definição e  aplicação da expressão regular à linha para retirar os campos principais de um processo, tais como o numero da pasta,
    # a data, o nome da pessoa, o nome do pai, o nome da mãe, e todas as observações acerca dessa pessoa
    er = re.compile(
        r"(?P<pasta>\d+?)::(?P<data>\d{4}-\d{2}-\d{2})::(?P<nome>\w[\w|\s]+?)::(?P<pai>\w[\w|\s]+?)::(?P<mae>\w[\w|\s]+?)(?P<Observações>::.*?::)")
    # para eliminar linhas repetidas. Optei por esta forma porque os registos estão ordenados pelo nome da pessoa associada ao registo.
    # Assim duas linhas iguais aparecem consecutivamente
    line_ant = ""
    for line in lines:
        if line == line_ant:
            continue
        # para limitar o número de resultados que é dado no enunciado (20)
        elif i == 40:
            break
        res = er.match(line)
        # verificar se a linha fez "match" (não re.match) com a expressão regular contendo por isso dados válidos nos respetivos valores de grupo
        if res:
            dados = dict()
            # guardar os dados principais menos as observações que irão ser processadas
            dados['pasta'] = res.group("pasta")
            dados['data'] = res.group("data")
            dados['nome'] = res.group("nome")
            dados['pai'] = res.group("pai")
            dados['mae'] = res.group("mae")
            # definição e  aplicação da expressão regular à linha para separar todas as relações presentes num processo e as restantes infromações extra.
            # Por exemplo o caso que refere que uma pessoa alterou o seu nome aquando a realização da cerimónia do Crisma
            # Para tal existem dois grupos de captura, pois se um valor possuir número de confirmação então este pertence às relações e concatenam-se os dois campos.
            # Caso contrário, apenas se considera o grupo de captura com nome relação
            er_observacoes = re.compile(
                r"(:{2}|\.)?\s*(?P<relacao>[\w\s]+?,\s*[\w\s]+?\.)\s*(?P<processo>Proc\.\d+)?")
            dados["Observacoes"] = dict()
            dados["Observacoes"]["relacoes"] = []
            dados["Observacoes"]["outros"] = []
            res1 = er_observacoes.finditer(res.group("Observações"))
            # verificar se a linha fez "match" (não re.match) com a expressão regular contendo por isso dados válidos nos respetivos valores de grupo
            if res1:
                for elem in res1:
                    # construir a lista de relações e de outros dentro do campo Observações
                    if elem.group("processo"):
                        (dados["Observacoes"])["relacoes"].append(
                            elem.group("relacao")+elem.group("processo"))
                    else:
                        (dados["Observacoes"])["outros"].append(
                            elem.group("relacao"))
        # acrescentar o diconário do processo à lista final
        lista.append(dados)
        i += 1
        line_ant = line
    # acrescentar a lista de diciconários ao ficheiro dict.json (aberto em cima)
    json.dump(lista, f, indent=' ')


i = 0
fp = open("processos.txt", "r")
lines = fp.readlines()
lista = []
line_ant = ""
for line in lines:
    if line == line_ant:
        continue
    i += 1
    line_ant = line
print(i)


distribuicao_anos("processos.txt")
distribuicao_nomes("processos.txt")
distribuicao_relacao("processos.txt")
fich_json("processos.txt")
