Projeto: Análise do Algoritmo MaxMin Select

Este projeto apresenta a implementação e análise de complexidade do algoritmo MaxMin Select, que encontra simultaneamente os elementos de menor e maior valor em uma lista. A abordagem utilizada é a de Divisão e Conquista, uma técnica poderosa para a criação de algoritmos eficientes.

Divisão e Conquista
Divisão e Conquista é uma estratégia de criação de algoritmos que consiste em três etapas:

Dividir: O problema principal é quebrado em subproblemas menores e de mesma natureza.

Conquistar: Os subproblemas são resolvidos recursivamente. Se forem pequenos o suficiente, são resolvidos diretamente (casos base).

Combinar: As soluções dos subproblemas são combinadas para formar a solução do problema original.

No caso do MaxMin Select, a lista é dividida ao meio recursivamente até que restem apenas um ou dois elementos. Em seguida, os resultados (pares de mínimo e máximo) de cada metade são combinados com apenas duas comparações.

Complexidade Assintótica
A complexidade assintótica descreve o comportamento de um algoritmo à medida que o tamanho da entrada tende ao infinito. Ela permite comparar a eficiência de diferentes algoritmos de forma objetiva, focando em sua taxa de crescimento. Para este projeto, a complexidade foi analisada tanto de forma teórica (matemática) quanto experimental (executando o código).

Como Executar o Projeto
Pré-requisitos
Python 3.x

Git (para clonar o repositório)

Passo 1: Clonar e Acessar o Repositório
# Clone este repositório para o seu ambiente local
git clone <https://github.com/Gmbferreira/minMaxSelect.git>

Passo 2: Instalar Dependências
O script de análise utiliza a biblioteca numpy para cálculos estatísticos. Instale-a com o seguinte comando:

pip install numpy

Passo 3: Executar o Script Principal
Após a instalação, execute o arquivo main.py para ver a demonstração do algoritmo e a análise de sua complexidade.

python main.py

Explicação dos Arquivos e Funções
Arquivo: minMaxSelect.py
Objetivo: Contém a implementação principal do algoritmo de Divisão e Conquista.

minMaxSelect(arr, inicio, fim)
Lógica: Função recursiva que encontra o menor e o maior valor em um sub-array arr[inicio...fim].

Casos Base:

Se inicio == fim: há apenas um elemento. Ele é retornado como mínimo e máximo.

Se fim == inicio + 1: há dois elementos. Uma única comparação determina o mínimo e o máximo.

Passos Recursivos:

Dividir: Calcula o índice do meio (meio).

Conquistar: Chama a si mesma para a metade esquerda (inicio a meio) e para a metade direita (meio + 1 a fim).

Combinar: Com os pares (min, max) de cada metade, realiza duas comparações para encontrar o (min, max) global do sub-array.

Arquivo: main.py
Objetivo: Orquestra a execução do projeto, demonstrando o algoritmo e medindo sua complexidade de forma experimental.

measure_complexity(func_instrumented)
Lógica: Mede a complexidade de uma função "instrumentada" (que conta suas próprias operações).

Funcionamento:

Executa a função minMaxSelect com listas de tamanhos crescentes (input_sizes).

Registra o número de comparações e o tempo de execução para cada tamanho.

Calcula a razão operações / f(n) para diferentes funções de complexidade (como n, n log n, etc.).

Identifica a complexidade mais provável como aquela cuja razão tem o menor desvio padrão, indicando um crescimento mais estável e previsível.

Relatório Técnico de Análise
Análise da Complexidade por Contagem de Operações
A complexidade do algoritmo é determinada pelo número de comparações T(n) para uma entrada de n elementos.

Casos Base:

T(1) = 0 (um elemento, zero comparações).

T(2) = 1 (dois elementos, uma comparação).

Caso Recursivo (n > 2):

Divisão: O problema de tamanho n é dividido em dois subproblemas de n/2. Custo: 2 * T(n/2).

Combinação: São necessárias 2 comparações para combinar os resultados.

A relação de recorrência é:
$$ T(n) = 2T(n/2) + 2 $$
Essa recorrência resolve para T(n) = 3n/2 - 2, o que demonstra um crescimento linear. Portanto, a complexidade de tempo é O(n).

Análise da Complexidade pelo Teorema Mestre
O Teorema Mestre resolve recorrências da forma: $$ T(n) = a \cdot T(n/b) + f(n) $$

Para o MaxMin Select, a recorrência é: $$ T(n) = 2T(n/2) + O(1) $$

1. Identificação de a, b, e f(n):

a = 2: Número de subproblemas.

b = 2: Fator de redução do tamanho da entrada.

f(n) = O(1): Custo do trabalho de combinação (constante, pois são 2 comparações).

2. Cálculo de log_b(a):
$$ \log_b(a) = \log_2(2) = 1 $$

3. Determinação do Caso do Teorema Mestre:
Comparamos f(n) com n^{\log_b(a)}, que é n^1.

Temos f(n) = O(1).

A condição para o Caso 1 é f(n) = O(n^{\log_b(a) - \epsilon}) para algum \epsilon > 0.

Se \epsilon = 1, temos O(n^{1-1}) = O(n^0) = O(1). Como f(n) é O(1), a condição é satisfeita.

Portanto, a recorrência se enquadra no Caso 1 do Teorema Mestre.

4. Solução Assintótica:

Pelo Caso 1, a solução é T(n)=
Theta(n 
log_b(a)
 ).

Substituindo o valor calculado, obtemos:
$$ T(n) = \Theta(n^1) = \Theta(n) $$

Ambas as análises teóricas confirmam que a complexidade do algoritmo é O(n).

Saída da Execução
A execução do main.py produzirá uma saída semelhante a esta:

--- Demonstração do Algoritmo MaxMin Select ---
Lista original: [10, 5, 25, 3, 47, 1, 98, 32, 12, 8]
Menor elemento: 1
Maior elemento: 98

--- Análise de Complexidade Assintótica ---
Iniciando a medição de complexidade...
Tamanho (n)   Comparações   Tempo (s)      
---------------------------------------------
100            148           0.000331       
200            298           0.000698       
400            598           0.001402       
800            1198          0.003110       
1600           2398          0.006587       
3200           4798          0.013401       
6400           9598          0.029854       

Análise da estabilidade da razão (contagem/função(n)):
- O(log n): Desvio Padrão = 0.0898
- O(n): Desvio Padrão = 0.0025
- O(n log n): Desvio Padrão = 0.0003
- O(n^2): Desvio Padrão = 0.0000

A complexidade que melhor se ajusta aos dados (menor desvio padrão) é a mais provável.

Complexidade estimada do algoritmo: O(n)