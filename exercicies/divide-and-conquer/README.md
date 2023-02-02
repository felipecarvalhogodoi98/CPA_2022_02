A empresa Dunder Mifflin é uma das referências em comercialização de papel, e está com uma nova política de estabelecimento de contrato com seus fornecedores de matéria-prima. Devido à grandes flutuações de preços do mercado, a Dunder Mifflin decidiu que a cada duas semanas, selecionará dois fornecedores de matéria-prima cuja a soma dos preços oferecidos para a aquisição de materiais sejam exatamente igual ao orçamento determinado pela Dunder Mifflin.

A Dunder Mifflin é referência mundial no ramo de papel, a recebe diversas propostas de empresas com interesse em firmar parcerias. Diante disso, seu setor de Tecnologia de Informação propôs o seguinte desafio: desenvolva um algoritmo que retorne, a cada duas semanas, quais são os fornecedores escolhidos que respeitem a restrição estabelecida acima.

Detalhe: dado um quantidade de n fornecedores, seu algoritmo deve ter O(nlogn).

Entrada
Cada caso de teste inicia com o número de fornecedores, indicado por n, em que 2 ≤ n ≤ 10.000. A próxima linha contém n inteiros, representando o preço de venda que cada fornecedor estipula para a encomenda solicitada pela Dunder Mifflin. O preço de venda divulgado por um fornecedor não ultrapassa 1.000.001 unidades monetárias. A próxima linha contem o valor de orçamento da Dunder Mifflin, denotado por B.

Saída
Imprima o preço dos fornecedores i e j, denotados por pi e pj, tal que pi + pj = B, e pi ≤ pj. Caso hajam múltiplas soluções, a Dunder Mifflin priorizará o preço que minimize pj - pi.