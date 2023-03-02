# Um jogo lúdico

Eder e Wando são dois alunos de graduação em Matemática que se divertem através de joguinhos lúdicos. O mais recente que a dupla descobriu consiste em: dado um conjunto de n números inteiros, {1,...,n}, define-se uma sequência gerada ao acaso denotada por s1,s2,...,sn, si ∈ {1,...,n}. Wando sempre é o primeiro a jogar. A jogada consiste em um movimento que seleciona dois elementos da sequência, si, sj, i < j , tal que si > sj, e os troca de posição, fazendo com que sj apareça antes de si na sequência atualizada. Como exemplo, suponha uma sequência formada por 1,5,3,4,2. Um dos jogadores pode fazer, em sua jogada, a troca de 5 com 3, ou 4 com 2. Imagine que a troca escolhida fosse 5 com 3. Logo, a nova sequência seria 1,3,5,4,2. Em algum momento posterior, a sequência será ordenada de forma ascendente. Então, o jogador que não for capaz de fazer o seu movimento, é declarado perdedor. Sua tarefa consiste em determinar o vencedor de uma rodada do jogo, dada uma permutação inicial s1,s2,...,sn. Detalhe: seu algoritmo deve ser implementado com complexidade de tempo de O(nlogn).

### Entradas:

A entrada do problema consiste em vários casos de teste. Cada caso de teste é composto por uma linha, indicando primeiramente o valor de n (2 ≤ n ≤ 100). Em seguida, a sequência de inteiros é apresentada.

### Saídas:

Para cada caso de teste, imprima o ganhador do jogo: “Eder” ou “Wando”.
Exemplo de Entrada:
```
5 1 5 3 4 2 
5 5 1 3 4 2 
5 1 2 3 4 5 
6 3 5 2 1 4 6 
5 5 4 3 2 1 
6 6 5 4 3 2 1
```

### Exemplo de Saída:
```
Wando
Eder 
Eder 
Eder 
Eder
Wando
```