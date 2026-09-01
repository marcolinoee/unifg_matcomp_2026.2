# ============================================================
# STARTER KIT: CONTROLADOR SAFETRAFFIC (AULA 03)
# ============================================================
def decidir_sinal_verde(ambulancia: bool, fluxo_alto: bool,
                         pedestre: bool, cancela_trem: bool) -> bool:
    if cancela_trem:
        return False
    if ambulancia:
        return True
    return fluxo_alto and not pedestre

# Bateria de Asserções
assert decidir_sinal_verde(True, False, True, False) == True
assert decidir_sinal_verde(False, True, False, False) == True
assert decidir_sinal_verde(False, True, True, False) == False
assert decidir_sinal_verde(True, True, False, True) == False
assert decidir_sinal_verde(False, False, False, False) == False
#-----
# as baterias que faltavam
assert decidir_sinal_verde(False, False, False, True)  == False
assert decidir_sinal_verde(False, False, True,  False) == False
assert decidir_sinal_verde(False, False, True,  True)  == False
assert decidir_sinal_verde(False, True,  False, True)  == False
assert decidir_sinal_verde(False, True,  True,  True)  == False
assert decidir_sinal_verde(True,  False, False, False) == True
assert decidir_sinal_verde(True,  False, False, True)  == False
assert decidir_sinal_verde(True,  False, True,  True)  == False
assert decidir_sinal_verde(True,  True,  False, False) == True
assert decidir_sinal_verde(True,  True,  True,  False) == True
assert decidir_sinal_verde(True,  True,  True,  True)  == False
print("SUCESSO: TODAS AS REGRAS LÓGICAS HOMOLOGADAS!")