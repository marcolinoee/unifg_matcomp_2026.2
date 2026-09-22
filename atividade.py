#PRIMEIRA QUESTÃO
A = {"Computador", "Impressora", "Projetor"}
B = {"Centro", "Boa Vista", "Madalena"}

def criar_produto_cartesiano(A, B):
    produto_cartesiano = []
    for equipamentos in A:
        for bairros in B:
            produto_cartesiano.append((equipamentos, bairros))
    return produto_cartesiano

print(f"PRIMEIRA QUESTÃO\nProduto cartesiano: {criar_produto_cartesiano(A, B)}\n")

#SEGUNDA QUESTÃO
f = {
    "Computador-001": "Secretaria de Educacao",
    "Impressora-002": "Secretaria de Saude",
    "Projetor-003": "Secretaria de Educacao",
}

def verificar_injetora(f):
    valores = f.values()
    conjunto_valores = set(valores)
    return len(valores) == len(conjunto_valores)

def retornar_imagem(f):
    conjunto_valores = set(f.values())
    return conjunto_valores
print(f"SEGUNDA QUESTAO\nFunção f é injetora? : {verificar_injetora(f)}\nImagem de f: {retornar_imagem(f)}\n")

#TERCEIRA QUESTÃO
f_2 = {
    "Computador-001": "TOMB-101",
    "Impressora-002": "TOMB-205",
    "Projetor-003": "TOMB-330",
}

# Contradomínio: todos os tombamentos que existem no sistema
contradominio_tombamentos = {
    "TOMB-101",
    "TOMB-205",
    "TOMB-330"
}


def verificar_injetora_sobrejetora(f_2, contradominio_tombamentos):
    valores = set(f_2.values())

    injetora = len(f_2) == len(valores)
    sobrejetora = valores == contradominio_tombamentos

    if injetora and sobrejetora:
        return "Bijetiva"
    elif injetora:
        return "Injetora"
    elif sobrejetora:
        return "Sobrejetora"
    else:
        return "Não é injetora nem sobrejetora"


print(f"TERCEIRA QUESTAO\nFunção é: {verificar_injetora_sobrejetora(f_2, contradominio_tombamentos)}\n")
# QUARTA QUESTÃO
dominio_questao4 = {
    "computador" : "TOMB-901",
    "monitor" : "TOMB-435",
    "mouse" : "TOMB-983",
    "tablet" : "TOMB-123",
    "teclado" : "TOMB-345" }
contradominio_questao4 = {
    "computador" : "Ipsep",
    "monitor" : "Ibura",
    "mouse" : "Madalena",
    "tablet" : "Boa viagem",
    "teclado" : "UR-11",
    }
tombamento = input("QUARTA QUESTÃO\ndigite o tombamento do aparelho que deseja saber o bairro: ")
def pegar_aparelho(dominio_questao4, tombamento):
    perifericos = dominio_questao4.keys()
    if tombamento not in dominio_questao4.values():
        return "Tombamento inexistente"
    else:
        for aparelhos, periferico in zip(dominio_questao4.values(), perifericos):
            if tombamento == aparelhos:
                return  periferico
periferico = pegar_aparelho(dominio_questao4, tombamento)
def pegar_bairro(periferico):
    for aparelho, cidade in zip(contradominio_questao4.keys(), contradominio_questao4.values()):
        if periferico == aparelho:
            return cidade

print(f"Sua bairro é: {pegar_bairro(periferico)}")

