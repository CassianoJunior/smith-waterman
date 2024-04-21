# Teacher description

Titulo: Entrega do Algortimo Smith Waterman. Enviar fontes e resposta do exercicio de teste ** Avaliacao 2 ** 10,00 pontos

Entrega do Algortimo Smith Waterman. Enviar fontes e resposta do exercicio de teste em um unico arquivo ZIP ou RAR. Arquivo em anexo tem explicacao e o teste. Para alunos Bioinformática: Faça o alinhamento conforme seu número de chamada. Para alunos da computação, use as sequencias para teste e envie os resultados.

FAÇA O ALINHAMENTO GLOBAL
USE: Match = 3 | mismatch = -1 | Gap = -2
O Backtrace deve ser do aultima linha x ultima coluna, independente do score calculado nessa célula.

Exemplo de matriz de escores dizendo como deve ser feito o Backtrace:

------------------------
** valores de score **
========================
-8 -5 -2 1 (escolhido será sempre esse para backtrace)
-6 -3 0 -2
-4 -1 -2 -4
-2 -1 -3 -5
0 -2 -4 -6
=======================

*** COMO DEVE SER A ENTRADA ***:
arquivo texto com as duas sequencias. Uma sequencia em cada linha

Exemplo do arquivo de entrada, cujo nome DEVE SER input.tx:

Na linha 1 colocar a primeira sequencia (vertical)

Na linha 2 colocar a segunda sequencia (horizontal)

Na linha 3 colocar o valor de GAP

Na linha 4 colocar o valor de mismatch

Na linha 5 colocar o valor de match

Exemplo de arquivo:

ATC
TCG
-2
-1
1
 

*** COMO DEVE SER A SAIDA ***:

--------------------------------------------------------------------------------
** valores de score **
================================================================================
G -8 -5 -2 1 <-- pegue sempre o da ultima linha e coluna para backtrace
C -6 -3 0 -2
T -4 -1 -2 -4
A -2 -1 -3 -5
U 0 -2 -4 -6
X U T C G
================================================================================
------------------------------------------------------------------
Alinhamento ** score = 1 ** Match = 1 | mismatch = -1 | Gap = -2
------------------------------------------------------------------
A T C G
- T C G