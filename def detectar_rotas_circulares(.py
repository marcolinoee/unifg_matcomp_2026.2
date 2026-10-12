def detectar_rotas_circulares(
    linhas: dict[str, list[str]],
) -> set[tuple[str, str]]:
  pares_diretos = set()

  # Extrai todas as conexões diretas (adjacentes) de cada linha
  for estacoes in linhas.values():
    for i in range(len(estacoes) - 1):
      origem = estacoes[i]
      destino = estacoes[i + 1]
      pares_diretos.add((origem, destino))

  # Cria o conjunto com os pares invertidos
  pares_invertidos = {(destino, origem) for origem, destino in pares_diretos}

  # A intersecção revela quais pares possuem tráfego bidirecional direto
  return pares_diretos.intersection(pares_invertidos)


# Teste rápido da função
if __name__ == "__main__":
  redes_metro = {
      "Linha Azul": ["Estacao A", "Estacao B", "Estacao C"],
      "Linha Vermelha": ["Estacao C", "Estacao B", "Estacao D"],
  }
  print("Rotas bidirecionais detectadas:", detectar_rotas_circulares(redes_metro))