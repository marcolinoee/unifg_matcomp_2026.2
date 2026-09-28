equipamentos = [
    {"nome": "respirador_1", "setor": "UTI", "dias": 45, "revisado": "sim"},
    {"nome": "respirador_2", "setor": "UTI", "dias": 210, "revisado": "sim"},
    {"nome": "bomba_1", "setor": "triagem", "dias": 30, "revisado": "nao"},
    {"nome": "monitor_1", "setor": "UTI", "dias": 100, "revisado": "sim"},
]

# tarefa 1: all()
prazo = all(equipamento["dias"] <= 180 for equipamento in equipamentos)
print(prazo)

# tarefa 2: any()
revisao = any(
    equipamento["setor"] == "UTI" and equipamento["revisado"] == "nao"
    for equipamento in equipamentos
)
print(revisao)

# tarefa 3: list comprehension
equip_problem = [
    equipamento["nome"]
    for equipamento in equipamentos
    if equipamento["dias"] > 180 or equipamento["revisado"] == "nao"
]
print(equip_problem)
