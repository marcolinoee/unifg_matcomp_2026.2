# Atividade de Fixação Extraclasse — Aula 06
**Disciplina:** Matemática Computacional Aplicada • UniFG 2026.2

---

## Parte 1: Exercícios Teóricos de Teoria dos Conjuntos

### Questão 1
Seja o conjunto universo U = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10} e os conjuntos A = {x | x é par} e B = {x | x é primo}.

Definindo os elementos:
* A = {2, 4, 6, 8, 10}
* B = {2, 3, 5, 7} *(O número 1 não é primo).*

Cálculos solicitados:
* **(a) A ∪ B (União):** {2, 3, 4, 5, 6, 7, 8, 10}
* **(b) A ∩ B (Intersecção):** {2}
* **(c) A \ B (Diferença):** {4, 6, 8, 10}
* **(d) (A ∪ B)' (Complementar da União):** {1, 9}

---

### Questão 2
Simplifique a expressão: (A ∩ B) ∪ (A ∩ B')

1. **Distributiva (Fatoração):** A ∩ (B ∪ B')
2. **Propriedade do Complementar:** B ∪ B' resulta no universo U, logo fica A ∩ U.
3. **Propriedade da Identidade:** A ∩ U resulta no próprio conjunto A.
* **Resultado:** A

---

### Questão 3
Como o CPython trata colisões de hash no `set` e por que a busca é O(1) médio?
* O `set` utiliza uma tabela hash de endereçamento aberto. Em caso de colisão de hash, o CPython aplica uma sequência de sondagem baseada em deslocamento pseudo-aleatório para encontrar um slot livre.
* A busca é O(1) médio porque o cálculo do hash mapeia o elemento diretamente para a posição na tabela em tempo constante, mantendo um fator de carga controlado que evita aglomerações e colisões excessivas.