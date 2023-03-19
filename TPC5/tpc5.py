import re
import math

# Função que verifica o número de telefone e determina se o mesmo é válido e caso seja, determina o custo da ligação para
# verificar se a chamada pode ser realizada com o saldo atual


def chamada(line):
    custo = 0
    if re.fullmatch(r"(0{2})?\d{9}", line):  # verificar a estrutura do número
        # vcalcular o custo da chamada
        if re.match(r"601", line) or re.match(r"641", line):
            print(
                "Esse número não é permitido neste telefone. Queira discar novo número!")
        elif re.match(r"00", line):
            custo += 1.5
        elif re.match(r"2", line):
            custo += 0.25
        elif re.match(r"808", line):
            custo += 0.10
        elif re.match(r"800", line):
            custo += 0
        else:
            print("O número para o qual ligou não está atribuído!")
    # o número não possui um formato válido
    else:
        print("O número apresentado não apresenta um formato correto! Por favor insira um novo número!")

    return custo

# função que processa a lista de moedas inseridas pelo utilizador


def soma_moedas(line):
    # valor inicial da soma da lista
    valor = 0
    print("maq:", end=" \"")
    for moeda in re.split(r",", line):
        # verificar se a moeda é correspondente a alguma moeda de cêntimos
        if res := re.fullmatch(r"\s*(10?|20?|50?)\s*c\s*", moeda):
            valor += int(res.group(1))/100
        # verificar se a moeda é correspondente a alguma moeda de euros
        elif res := re.fullmatch(r"\s*(1|2)\s*e\s*", moeda):
            valor += int(res.group(1))
        # caso contrário a moeda é inválida
        else:
            print(moeda + " - Moeda Inválida", end="; ")
    return valor

# função que imprime o valor do saldo para o formato (1e02c)


def print_valor(valor):
    valor_para_texto = math.modf(valor)
    return(str(int(valor_para_texto[1]))+"e" +
           str(int(valor_para_texto[0]*100))+"c")


# Variavel que indica se o telefone foi levantado (Não é possivel realizar nenhuma operação se o telefone
# não estiver levantado)
levantado = False
# variavel que verifica se p utilizador abortou o o pedido
abortou = False
# saldo do utilizador
saldo = 0
while(res := input()):
    # comando para levantar o telefone
    if re.fullmatch(r"\s*LEVANTAR\s*", res):
        if levantado:
            print(
                "maq: O telefone já está levantado!Por favor insira moedas ou ligue para um número!")
        else:
            print("maq: Introduza Moedas.")
            levantado = True
    else:
        # obrigar a que o utilizador pouse o telefone após abortar o pedido
        if abortou:
            if re.fullmatch((r"\s*POUSAR\s*"), res):
                print("maq: \"troco="+print_valor(saldo)+"; Volte sempre!\"")
                break
        else:
            # verificação de todos os outros comandos caso o telefone esteja levantado
            if levantado:
                if moedas := re.fullmatch(r"\s*MOEDA\s+([\w, ]*)\.?", res):
                    saldo += soma_moedas(moedas.group(1))
                    print(print_valor(saldo)+"\"")
                # verificar se é o comando para realizar uma chamada telefónica
                elif telefone := re.fullmatch(r"\s*T\s*=\s*(\w*)\s*", res):
                    # tratar a chamada
                    custo = chamada(telefone.group(1))
                    # verificar se o saldo permite realizar a comunicação
                    if custo > saldo:
                        print(
                            "maq: Saldo Insuficiente! Por favor introduza mais moedas.")
                    else:
                        saldo -= custo
                        print("maq: \"saldo = "+print_valor(saldo)+"\"")
                # verificar se é o comando para pousar o telefone.
                # O sistema determina o troco e devolve-o ao utilizador
                elif re.fullmatch((r"\s*POUSAR\s*"), res):
                    print("maq: \"troco="+print_valor(saldo)+"; Volte sempre!\"")
                    break
                # verificar se é o comando para abortar
                # este tem o mesmo funcionamento que o comando de pousar porque se o utilizador ja tiver realizado uma chamada,
                # o sistema terá que devolver o troco e não o dinheiro inserido
                elif re.fullmatch(r"ABORTAR", res):
                    print("maq: \"troco="+print_valor(saldo)+"; Volte sempre!\"")
                    abortou = True
                else:
                    print("maq: Operação Inválida")
            # quando o utilizador tentou realizar uma operaação o telefone encontrava-se pousado
            else:
                print("maq: Levante o telefone primeiro!")
