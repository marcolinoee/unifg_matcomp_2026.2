# Tabela verdade - sistema de trava das portas do carro

A = cinto de segurança colocado (1 sim, 0 não)
B = motor ligado (1 sim, 0 não)
C = botão de trava manual apertado (1 sim, 0 não)
S = portas travam (1 trava, 0 não trava)

S = (A AND B) OR C

| A | B | C | S |
|---|---|---|---|
| 0 | 0 | 0 | 0 |
| 0 | 0 | 1 | 1 |
| 0 | 1 | 0 | 0 |
| 0 | 1 | 1 | 1 |
| 1 | 0 | 0 | 0 |
| 1 | 0 | 1 | 1 |
| 1 | 1 | 0 | 1 |
| 1 | 1 | 1 | 1 |

A ideia é que as portas travam sozinhas quando o motorista coloca o cinto e liga o motor, que é a situação normal de quem vai dirigir. Mas também trava se alguém apertar o botão manual, independente do cinto ou do motor, porque é uma ação direta da pessoa. Só fica destravado mesmo quando nenhuma dessas coisas acontece.