Aluno: Fernando Lauria de Souza 
RA:1352619991 
Data da tarefa: 24/08/2026
Dupla com Jhulya Gabriela Gomes Viana
Atividade: Fazer os desafios 1,2,3,4
tarefa 1:

A = { 
    "Hospital",
    "Posto de Saúde",
    "Escola",
    "CRAS"
}

B = {
    "Boa Viagem",
    "Pina",
    "Imbiribeira",
    "Jordão"
}

produto_cartesiano = {
    (equipamento, bairro)
    for equipamento in A
    for bairro in B
}

print("=" * 50)
print("CONJUNTO A - EQUIPAMENTOS")
print("=" * 50)

for equipamento in sorted(A):
    print("-", equipamento)

print("\n" + "=" * 50)
print("CONJUNTO B - BAIRROS")
print("=" * 50)

for bairro in sorted(B):
    print("-", bairro)

print("\n" + "=" * 50)
print("PRODUTO CARTESIANO A x B")
print("=" * 50)

for equipamento, bairro in sorted(produto_cartesiano):
    print(f"({equipamento}, {bairro})")

print(f"\nQuantidade de pares em A x B: {len(produto_cartesiano)}")

relacao_atendimento = {
    "Hospital": {
        "Boa Viagem",
        "Pina",
        "Imbiribeira"
    },

    "Posto de Saúde": {
        "Boa Viagem",
        "Jordão"
    },

    "Escola": {
        "Pina",
        "Imbiribeira",
        "Jordão"
    },

    "CRAS": {
        "Jordão",
        "Imbiribeira"
    }
}

print("\n" + "=" * 50)
print("RELAÇÃO DE ATENDIMENTO")
print("=" * 50)

for equipamento, bairros in relacao_atendimento.items():

    print(f"\n{equipamento} atende:")

    for bairro in sorted(bairros):
        print(f"  -> {bairro}")

R = {
    (equipamento, bairro)
    for equipamento, bairros in relacao_atendimento.items()
    for bairro in bairros
}

print("\n" + "=" * 50)
print("RELAÇÃO R COMO PARES ORDENADOS")
print("=" * 50)

for par in sorted(R):
    print(par)

print(f"\nQuantidade de relações de atendimento: {len(R)}")

print("\n" + "=" * 50)
print("VERIFICAÇÃO")
print("=" * 50)

print(f"A possui {len(A)} equipamentos.")
print(f"B possui {len(B)} bairros.")
print(f"A x B possui {len(produto_cartesiano)} combinações.")
print(f"A relação de atendimento possui {len(R)} pares.")

print("\nPrograma finalizado!")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------
Tarefa 2:

Ativo = {
    "Ativo 1",
    "Ativo 2",
    "Ativo 3",
    "Ativo 4",
    "Ativo 5"
}

Secretaria = {
    "Saúde",
    "Educação",
    "Obras",
    "Segurança"
}

f = {
    "Ativo 1": "Saúde",
    "Ativo 2": "Educação",
    "Ativo 3": "Obras",
    "Ativo 4": "Saúde",
    "Ativo 5": "Segurança"
}

print("=" * 60)
print("CONJUNTO DOS ATIVOS")
print("=" * 60)

for ativo in sorted(Ativo):
    print(ativo)

print("\n" + "=" * 60)
print("CONJUNTO DAS SECRETARIAS")
print("=" * 60)

for secretaria in sorted(Secretaria):
    print(secretaria)

print("\n" + "=" * 60)
print("FUNÇÃO f: ATIVO -> SECRETARIA")
print("=" * 60)

for ativo in sorted(Ativo):
    print(f"f({ativo}) = {f[ativo]}")

print("\n" + "=" * 60)
print("VERIFICAÇÃO DA FUNÇÃO")
print("=" * 60)

# Verifica se todos os elementos de Ativo possuem uma imagem
todos_possuem_imagem = all(ativo in f for ativo in Ativo)

# Verifica se todas as imagens pertencem ao conjunto Secretaria
todas_imagens_validas = all(
    f[ativo] in Secretaria
    for ativo in Ativo
)

if todos_possuem_imagem and todas_imagens_validas:
    print("f é realmente uma função f: Ativo -> Secretaria.")
else:
    print("f NÃO é uma função válida de Ativo -> Secretaria.")

imagem = {
    f[ativo]
    for ativo in Ativo
}

print("\n" + "=" * 60)
print("IMAGEM DA FUNÇÃO Im(f)")
print("=" * 60)

print("Im(f) =", imagem)

print("\n" + "=" * 60)
print("VERIFICAÇÃO DE INJETIVIDADE")
print("=" * 60)

valores = list(f.values())

eh_injetora = len(valores) == len(set(valores))

if eh_injetora:

    print("A função f É INJETORA.")

    print("\nJustificativa matemática:")
    print("Não existem dois ativos distintos associados")
    print("à mesma secretaria.")

else:

    print("A função f NÃO É INJETORA.")

    print("\nJustificativa matemática:")

    # Procura os ativos que possuem a mesma imagem
    for secretaria in Secretaria:

        ativos_mesma_secretaria = [
            ativo
            for ativo in Ativo
            if f[ativo] == secretaria
        ]

        if len(ativos_mesma_secretaria) > 1:

            print(
                f"Os ativos {ativos_mesma_secretaria} "
                f"possuem a mesma imagem: {secretaria}"
            )

print("\n" + "=" * 60)
print("RESUMO MATEMÁTICO")
print("=" * 60)

print(f"|Ativo| = {len(Ativo)}")
print(f"|Secretaria| = {len(Secretaria)}")
print(f"|Im(f)| = {len(imagem)}")

print("\nIm(f) =", imagem)

if eh_injetora:
    print("\nConclusão:")
    print("f é INJETORA porque |Ativo| = |Im(f)|.")
else:
    print("\nConclusão:")
    print("f NÃO é INJETORA porque |Ativo| > |Im(f)|.")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------
tarefa 3:

Ativo = {
    "Ativo 1",
    "Ativo 2",
    "Ativo 3",
    "Ativo 4",
    "Ativo 5"
}

Tombamento = {
    "T001",
    "T002",
    "T003",
    "T004",
    "T005"
}

f = {
    "Ativo 1": "T001",
    "Ativo 2": "T002",
    "Ativo 3": "T003",
    "Ativo 4": "T004",
    "Ativo 5": "T005"
}

print("=" * 60)
print("FUNÇÃO f: ATIVO -> TOMBAMENTO")
print("=" * 60)

for ativo in sorted(Ativo):
    print(f"f({ativo}) = {f[ativo]}")

funcao_valida = (
    set(f.keys()) == Ativo
    and all(f[ativo] in Tombamento for ativo in Ativo)
)

print("\n" + "=" * 60)
print("VERIFICAÇÃO DA FUNÇÃO")
print("=" * 60)

if funcao_valida:
    print("f é uma função válida de Ativo -> Tombamento.")
else:
    print("f NÃO é uma função válida.")

valores = list(f.values())

eh_injetora = len(valores) == len(set(valores))

print("\n" + "=" * 60)
print("VERIFICAÇÃO DA INJETIVIDADE")
print("=" * 60)

if eh_injetora:
    print("f É INJETORA.")
    print("Nenhum tombamento está associado a dois ativos diferentes.")
else:
    print("f NÃO É INJETORA.")
    print("Existem ativos diferentes com o mesmo tombamento.")

imagem = set(f.values())

print("\n" + "=" * 60)
print("IMAGEM DA FUNÇÃO")
print("=" * 60)

print("Im(f) =", imagem)

eh_sobrejetora = imagem == Tombamento

print("\n" + "=" * 60)
print("VERIFICAÇÃO DA SOBREJETIVIDADE")
print("=" * 60)

if eh_sobrejetora:
    print("f É SOBREJETORA.")
    print("Todo tombamento possui um ativo associado.")
else:
    print("f NÃO É SOBREJETORA.")
    print("Existe pelo menos um tombamento sem ativo associado.")

eh_bijetora = eh_injetora and eh_sobrejetora

print("\n" + "=" * 60)
print("VERIFICAÇÃO DA BIJETIVIDADE")
print("=" * 60)

if eh_bijetora:
    print("f É BIJETORA!")
    print("A função é simultaneamente injetora e sobrejetora.")
else:
    print("f NÃO É BIJETORA.")

print("\n" + "=" * 60)
print("FUNÇÃO INVERSA f⁻¹")
print("=" * 60)

if eh_bijetora:

    # Inverte chave e valor
    f_inversa = {
        tombamento: ativo
        for ativo, tombamento in f.items()
    }

    for tombamento in sorted(f_inversa):
        print(
            f"f⁻¹({tombamento}) = "
            f"{f_inversa[tombamento]}"
        )

else:

    print(
        "Não é possível construir uma função inversa "
        "porque f não é bijetora."
    )

if eh_bijetora:

    print("\n" + "=" * 60)
    print("VERIFICAÇÃO MATEMÁTICA DA INVERSA")
    print("=" * 60)

    inversa_valida = True

    for ativo in Ativo:

        tombamento = f[ativo]

        resultado = f_inversa[tombamento]

        if resultado == ativo:
            print(
                f"f⁻¹(f({ativo})) = {resultado} ✓"
            )
        else:
            inversa_valida = False
            print(
                f"f⁻¹(f({ativo})) = {resultado} ✗"
            )

    for tombamento in Tombamento:

        ativo = f_inversa[tombamento]

        resultado = f[ativo]

        if resultado == tombamento:
            print(
                f"f(f⁻¹({tombamento})) = {resultado} ✓"
            )
        else:
            inversa_valida = False
            print(
                f"f(f⁻¹({tombamento})) = {resultado} ✗"
            )

    print("\n" + "=" * 60)
    print("RESULTADO FINAL")
    print("=" * 60)

    if inversa_valida:
        print("A função inversa foi comprovada com sucesso!")
        print("f é BIJETORA e possui função inversa.")
    else:
        print("A função inversa não foi validada.")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------
Tarefa 4:

Ativo = {
    "Ativo 1",
    "Ativo 2",
    "Ativo 3",
    "Ativo 4",
    "Ativo 5",
    "Ativo 6"
}

Tombamento = {
    "TOMB-901",
    "TOMB-902",
    "TOMB-903",
    "TOMB-904",
    "TOMB-905",
    "TOMB-906"
}

Secretaria = {
    "Saúde",
    "Educação",
    "Obras",
    "Segurança"
}

f = {
    "Ativo 1": "TOMB-901",
    "Ativo 2": "TOMB-902",
    "Ativo 3": "TOMB-903",
    "Ativo 4": "TOMB-904",
    "Ativo 5": "TOMB-905",
    "Ativo 6": "TOMB-906"
}

g = {
    "TOMB-901": "Saúde",
    "TOMB-902": "Educação",
    "TOMB-903": "Obras",
    "TOMB-904": "Segurança",
    "TOMB-905": "Saúde",
    "TOMB-906": "Obras"
}

composicao = {}

for ativo in Ativo:

    tombamento = f[ativo]

    secretaria = g[tombamento]

    composicao[ativo] = secretaria

print("=" * 70)
print("PIPELINE DE COMPOSIÇÃO (g o f)")
print("=" * 70)

for ativo in sorted(Ativo):

    tombamento = f[ativo]
    secretaria = g[tombamento]

    print(
        f"{ativo} "
        f"-> {tombamento} "
        f"-> {secretaria}"
    )

print("\n" + "=" * 70)
print("VALIDAÇÃO DO TOMBAMENTO TOMB-901")
print("=" * 70)

tombamento_teste = "TOMB-901"

ativos_encontrados = [
    ativo
    for ativo in Ativo
    if f[ativo] == tombamento_teste
]

if tombamento_teste in Tombamento:

    print(f"Tombamento {tombamento_teste}: VÁLIDO")

    if ativos_encontrados:

        ativo = ativos_encontrados[0]

        secretaria = g[tombamento_teste]

        print(f"Ativo encontrado: {ativo}")
        print(f"Secretaria responsável: {secretaria}")

        print(
            f"\n(g o f)({ativo}) = "
            f"g(f({ativo}))"
        )

        print(
            f"(g o f)({ativo}) = "
            f"g({tombamento_teste})"
        )

        print(
            f"(g o f)({ativo}) = "
            f"{secretaria}"
        )

    else:

        print(
            "O tombamento existe, mas não está associado "
            "a nenhum ativo."
        )

else:

    print(f"Tombamento {tombamento_teste}: INVÁLIDO")

def validar_tombamento(tombamento):

    print("\n" + "-" * 70)
    print(f"VALIDANDO: {tombamento}")
    print("-" * 70)

    if tombamento not in Tombamento:

        print("Resultado: TOMBAMENTO INEXISTENTE")
        print("O pipeline foi interrompido com segurança.")

        return None

    ativos = [
        ativo
        for ativo in Ativo
        if f[ativo] == tombamento
    ]

    if not ativos:

        print("Resultado: TOMBAMENTO SEM ATIVO ASSOCIADO.")

        return None

    secretaria = g.get(tombamento)

    if secretaria is None:

        print(
            "Erro: tombamento existe, mas não possui "
            "secretaria associada."
        )

        return None

    print("Resultado: TOMBAMENTO VÁLIDO")

    print(f"Ativo: {ativos[0]}")
    print(f"Tombamento: {tombamento}")
    print(f"Secretaria: {secretaria}")

    return secretaria

print("\n" + "=" * 70)
print("TESTE DE ROBUSTEZ DO PIPELINE")
print("=" * 70)

tombamentos_teste = [
    "TOMB-901",
    "TOMB-902",
    "TOMB-999",
    "TOMB-000",
    "TOMB-ABC"
]

for tombamento in tombamentos_teste:

    validar_tombamento(tombamento)

print("\n" + "=" * 70)
print("VERIFICAÇÃO MATEMÁTICA DE (g o f)")
print("=" * 70)

composicao_valida = True

for ativo in Ativo:

    resultado_f = f[ativo]

    resultado_g = g.get(resultado_f)

    resultado_composicao = composicao[ativo]

    print(
        f"\n{ativo}:"
    )

    print(
        f"f({ativo}) = {resultado_f}"
    )

    print(
        f"g({resultado_f}) = {resultado_g}"
    )

    print(
        f"(g o f)({ativo}) = {resultado_composicao}"
    )

    if resultado_g != resultado_composicao:

        composicao_valida = False

print("\n" + "=" * 70)
print("RESULTADO FINAL")
print("=" * 70)

if composicao_valida:

    print("A composição (g o f) foi validada com sucesso!")

    print(
        "\nPara todo ativo x pertencente a Ativo:"
    )

    print(
        "(g o f)(x) = g(f(x))"
    )

else:

    print("Erro na validação da composição.")
lo
print("\n" + "=" * 70)
print("RESUMO DO PIPELINE")
print("=" * 70)

print("""
Ativo
  |
  | f
  v
Tombamento
  |
  | g
  v
Secretaria

Composição:

(g o f)(Ativo) = g(f(Ativo))
""")

print("Pipeline concluído.")
