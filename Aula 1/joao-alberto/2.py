# Conjunto S: Secretarias (Conjunto de Chegada)
conjunto_S = {"Educacao", "Saude", "Administracao"}

# Mapeamento da função f: Ativo -> Secretaria
funcao_f = {
    "Notebook": "Educacao",
    "Roteador": "Saude",
    "Projetor": "Educacao"  # Repetido propositalmente para teste lógico
}

def verificar_funcao(funcao):
    # Calcula a Imagem (valores que a função assume)
    imagem = set(funcao.values())
    
    # Verifica Injetividade (elementos diferentes devem ir para imagens diferentes)
    valores_vistos = set()
    e_injetora = True
    for item in funcao.values():
        if item in valores_vistos:
            e_injetora = False
            break
        valores_vistos.add(item)
        
    return e_injetora, imagem

e_injetora, imagem_f = verificar_funcao(funcao_f)

print(f"Mapeamento f(Ativo): {funcao_f}")
print(f"Imagem Im(f): {imagem_f}")
print(f"A função é Injetora? {'Sim' if e_injetora else 'Não (Elementos distintos têm o mesmo destino)'}")
