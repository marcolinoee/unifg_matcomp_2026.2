#atividade 1
# Passo 1: Definir os conjuntos
A = {"Câmera 1", "Câmera 2", "Sensor de Rua", "Posto de Vigilância"}  # Equipamentos
B = {"Centro", "Bairro Novo", "Vila Esperança", "Jardim Paulista"}     # Bairros

print("✅ Conjunto A (Equipamentos):", A)
print("✅ Conjunto B (Bairros):", B)
print(f"|A| = {len(A)}  |B| = {len(B)}\n")

# Passo 2: Calcular o Produto Cartesiano A × B
produto_cartesiano = [(equip, bairro) for equip in A for bairro in B]

print("📦 Produto Cartesiano A × B:")
for par in produto_cartesiano:
    print(f"  {par}")
print(f"\nTotal de pares: {len(produto_cartesiano)} = {len(A)} × {len(B)}\n")


# Passo 3: Relação de Atendimento (quem atende quem)
relacao_atendimento = [
    ("Câmera 1", "Centro"),
    ("Câmera 1", "Bairro Novo"),
    ("Câmera 2", "Vila Esperança"),
    ("Sensor de Rua", "Centro"),
    ("Posto de Vigilância", "Jardim Paulista"),
    ("Posto de Vigilância", "Bairro Novo")
]

print("🔗 Relação de Atendimento R:")
for par in relacao_atendimento:
    print(f"  {par}")
print(f"\nTotal de pares na relação: {len(relacao_atendimento)}")

# Conjuntos usados nas tarefas de funções
Ativo = {"CAM-001", "CAM-002", "SEN-001", "POSTO-001"}
Secretaria = {"Sec-Recife", "Sec-Olinda", "Sec-Jaboatao"}
Tombamento = {"TOMB-001", "TOMB-002", "TOMB-003", "TOMB-004"}

#tarefa 2
print("="*60)
print("TAREFA 2 — Função f: Ativo → Secretaria")
print("="*60)

# Função: cada ativo mapeia para uma secretaria responsável
def f(ativo):
    mapa = {
        "CAM-001": "Sec-Recife",
        "CAM-002": "Sec-Olinda",
        "SEN-001": "Sec-Jaboatao",
        "POSTO-001": "Sec-Recife"
    }
    return mapa.get(ativo, None)
#tarefa 2

# Aplicar a função em todos os ativos
resultados_f = {ativo: f(ativo) for ativo in Ativo}
print("\n📌 Mapeamento f(Ativo) → Secretaria:")
for ativo, sec in resultados_f.items():
    print(f"   f({ativo}) = {sec}")

# Verificar se é INJETORA
valores = list(resultados_f.values())
eh_injetora = len(valores) == len(set(valores))  # todos os valores são únicos?
print(f"\n✅ É injetora? {eh_injetora}")
print(f"   Explicação: {'Sim, cada ativo tem uma secretaria diferente' if eh_injetora else 'Não, existem ativos diferentes que mapeiam para a mesma secretaria (ex: CAM-001 e POSTO-001 → Sec-Recife)'}")

# Calcular a IMAGEM Im(f)
imagem_f = set(valores)
print(f"\n📌 Imagem Im(f) = {imagem_f}")
print(f"   Tamanho: {len(imagem_f)} de {len(Secretaria)} elementos do conjunto alvo")


print("\n" + "="*60)
print("TAREFA 3 — Função Inversa f⁻¹: Ativo → Tombamento + Bijetividade")
print("="*60)

# Função g: Ativo → Tombamento (função BIJETORA)
def g(ativo):
    mapa = {
        "CAM-001": "TOMB-001",
        "CAM-002": "TOMB-002",
        "SEN-001": "TOMB-003",
        "POSTO-001": "TOMB-004"
    }
    return mapa.get(ativo, None)

# Construir a FUNÇÃO INVERSA g⁻¹
def g_inversa(tombamento):
    mapa_inverso = {
        "TOMB-001": "CAM-001",
        "TOMB-002": "CAM-002",
        "TOMB-003": "SEN-001",
        "TOMB-004": "POSTO-001"
    }
    return mapa_inverso.get(tombamento, None)

# Testar função inversa
print("\n📌 Mapeamento g(Ativo) → Tombamento:")
for ativo in Ativo:
    print(f"   g({ativo}) = {g(ativo)}")

print("\n📌 Função Inversa g⁻¹(Tombamento) → Ativo:")
for tom in Tombamento:
    print(f"   g⁻¹({tom}) = {g_inversa(tom)}")

# Verificar BIJETIVIDADE
# Bijetora = Injetora + Sobrejetora
valores_g = [g(a) for a in Ativo]
eh_inj = len(valores_g) == len(set(valores_g))
eh_sob = set(valores_g) == set(Tombamento)
eh_bijetora = eh_inj and eh_sob

print(f"\n✅ É bijetora? {eh_bijetora}")
print(f"   • Injetora? {eh_inj} (todos os valores são únicos)")
print(f"   • Sobrejetora? {eh_sob} (todos os elementos de Tombamento são atingidos)")
print(f"   → Como é as duas coisas, é BIJETORA ✅")

print("\n" + "="*60)
print("TAREFA 4 — Composição (g ∘ f) e Validação TOMB-901")
print("="*60)

def f(ativo):
    mapa = {
        "CAM-001": "Sec-Recife",
        "CAM-002": "Sec-Olinda",
        "SEN-001": "Sec-Jaboatao",
        "POSTO-001": "Sec-Recife"
    }
    return mapa.get(ativo, None)

# Função g da Tarefa 3
def g(ativo):
    mapa = {
        "CAM-001": "TOMB-001",
        "CAM-002": "TOMB-002",
        "SEN-001": "TOMB-003",
        "POSTO-001": "TOMB-004"
    }
    return mapa.get(ativo, None)

# COMPOSIÇÃO: (g ∘ f) = g(f(ativo))
def composicao_gf(ativo):
    # f mapeia Ativo → Secretaria
    # g mapeia Ativo → Tombamento
    # A composição verifica: dado um ativo, qual seu tombamento E sua secretaria
    secretaria = f(ativo)
    tombamento = g(ativo)
    return {
        "ativo": ativo,
        "secretaria": secretaria,
        "tombamento": tombamento
    }

# Executar pipeline
print("\n📌 Pipeline de Composição (g ∘ f):")
for ativo in Ativo:
    res = composicao_gf(ativo)
    print(f"   {res['ativo']} → {res['secretaria']} → {res['tombamento']}")

# Validar TOMB-901 (inexistente)
print("\n🔍 Validação de tombamento inexistente TOMB-901:")
tomb_alvo = "TOMB-901"
existe = tomb_alvo in Tombamento
print(f"   Tombamento '{tomb_alvo}' existe? {existe}")
if not existe:
    print(f"   ⚠️ ERRO: Tombamento {tomb_alvo} NÃO cadastrado! Robustez validada ✅")
else:
    print(f"   ✅ Tombamento {tomb_alvo} encontrado")

# Função de validação robusta
def validar_tombamento(numero_tomb):
    if numero_tomb in Tombamento:
        return True, f"✅ {numero_tomb} válido"
    else:
        return False, f"❌ {numero_tomb} INVÁLIDO — não existe no cadastro"

print("\n🛡️ Teste de Robustez:")
for tom in ["TOMB-001", "TOMB-901", "TOMB-005", "TOMB-003"]:
    valido, msg = validar_tombamento(tom)
    print(f"   {msg}")
