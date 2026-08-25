# Funções base do pipeline
f_equip_para_tomb = {
    "Notebook": "TOMB-901",
    "Roteador": "TOMB-902",
    "Projetor": "TOMB-903"
}

g_tomb_para_status = {
    "TOMB-901": "Ativo - Em Uso",
    "TOMB-902": "Ativo - Manutenção",
    "TOMB-903": "Baixado"
}

# Pipeline de composição (g o f)(x) com tratamento robusto de erros
def pipeline_composicao(equipamento):
    try:
        # 1. Executa f(x) e valida existência
        if equipamento not in f_equip_para_tomb:
            raise KeyError(f"Equipamento '{equipamento}' não localizado no inventário.")
        tombamento = f_equip_para_tomb[equipamento]
        
        # 2. Validação específica do TOMB-901 exigida no slide
        if tombamento == "TOMB-901":
            print(f"  [Validação] Alerta: Código Crítico TOMB-901 acessado.")
            
        # 3. Executa g(f(x))
        status_final = g_tomb_para_status[tombamento]
        return f"  [Sucesso] Status do Ativo: {status_final}"
        
    except KeyError as erro:
        return f"  [Erro de Robustez] Operação abortada: {erro}"

# Teste com o fluxo válido (TOMB-901)
print("Teste 1:")
print(pipeline_composicao("Notebook"))

# Teste de robustez com ativo inválido/inexistente
print("\nTeste 2:")
print(pipeline_composicao("Servidor_Fantasma"))
