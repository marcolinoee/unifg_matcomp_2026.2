equipamentos=[
    {'nome':'respirador1','lugar': 'UTI', 'dias': 210, 'revisado': True },
    {'nome':'respirador2','lugar': 'UTI', 'dias': 210, 'revisado': True },
    {'nome':'respirador1','lugar': 'UTI', 'dias': 210, 'revisado': True },
    {'nome': 'bomba', 'lugar': 'triagem', 'dias': 30, 'revisado': False},
    {'nome':'monitor1','lugar': 'UTI', 'dias': 100, 'revisado': True }
]
equipamentos_no_prazo = all(
    equipamento['revisado'] for equipamento in equipamentos
    )
equipamento_sem_revisao = any(
    not equipamento['revisado'] for equipamento in equipamentos if equipamento['lugar'] == 'UTI'
)

equipamentos_problematicos = [
    equipamento['nome'] for equipamento in equipamentos if not equipamento['revisado']
]

print(f"Todos os equipamentos estão dentro do prazo de revisão?: {equipamentos_no_prazo}\nExiste algum equipamento da UTI sem revisão?: {equipamento_sem_revisao}\n ID dos esquipammentos defeituosos: {equipamentos_problematicos}")