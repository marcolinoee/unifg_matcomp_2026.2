A_equipamentos = {"Trator", "Ambulância", "Caminhão de Lixo"}
B_bairros = {"Centro", "Zona Norte", "Zona Sul"}

produto_cartesiano = {(a, b) for a in A_equipamentos for b in B_bairros}

relacao_atendimento = {
    ("Trator", "Zona Norte"),
    ("Ambulância", "Centro"),
    ("Ambulância", "Zona Sul")
}

f_tombamento_ativo = {
    "TOMB-001": "Notebook Dell",
    "TOMB-002": "Mesa de Escritório"
}

f_inversa = {ativo: tombamento for tombamento, ativo in f_tombamento_ativo.items()}

is_bijetora = len(f_tombamento_ativo) == len(set(f_tombamento_ativo.values()))

f = {"TOMB-901": "Ambulância UTI", "TOMB-902": "Trator"}


g = {"Ambulância UTI": "Saúde", "Trator": "Obras"}


def pipeline_g_of_f(tombamento):
    try:
        ativo = f.get(tombamento) 
        if not ativo:
            return "Erro: Tombamento não encontrado (inexistente)."
            
        secretaria = g.get(ativo)
        if not secretaria:
            return f"Erro: Ativo '{ativo}' não possui secretaria vinculada."
            
        return f"Sucesso: O tombamento {tombamento} pertence à secretaria de {secretaria}."
        
    except Exception as e:
        return f"Erro inesperado: {str(e)}"

print(pipeline_g_of_f("TOMB-901")) 
print(pipeline_g_of_f("TOMB-999")) 