# Conjunto T: Tombamentos (Codomínio)
conjunto_T = {"TOMB-901", "TOMB-902", "TOMB-903"}

# Função Direta (Deve ser Bijetora para permitir Inversa)
funcao_bijetora = {
    "Notebook": "TOMB-901",
    "Roteador": "TOMB-902",
    "Projetor": "TOMB-903"
}

def construir_inversa(funcao, codominio):
    dominio = set(funcao.keys())
    imagem = set(funcao.values())
    
    # Comprovação matemática via código:
    e_injetora = len(imagem) == len(dominio)
    e_sobrejetora = (imagem == codominio)
    
    if e_injetora and e_sobrejetora:
        print("Comprovação: A função é BIJETORA.")
        # Inversão: Chave vira Valor, Valor vira Chave
        inversa = {valor: chave for chave, valor in funcao.items()}
        return inversa
    else:
        raise ValueError("Erro: A função não cumpre as regras de bijetividade.")

funcao_inversa = construir_inversa(funcao_bijetora, conjunto_T)
print(f"Função Inversa f^-1 (Tombamento -> Ativo):")
print(funcao_inversa)
