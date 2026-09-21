# Conjunto A: Equipamentos (Ativos)
conjunto_A = {"Notebook", "Roteador", "Projetor"}

# Conjunto B: Bairros
conjunto_B = {"Centro", "Boa Viagem"}

# 1. Calculando o Produto Cartesiano (A x B)
produto_cartesiano = {(eq, bairro) for eq in conjunto_A for bairro in conjunto_B}

print(f"Produto Cartesiano A x B ({len(produto_cartesiano)} combinações):")
print(produto_cartesiano)

# 2. Definindo a Relação de Atendimento Real
relacao_atendimento = {
    ("Notebook", "Centro"),
    ("Roteador", "Centro"),
    ("Projetor", "Boa Viagem")
}
print(f"\nRelação de Atendimento Real:")
print(relacao_atendimento)
