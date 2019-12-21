

 % Ponto e v�rgula ';' indica a escrita em novas linhas de uma matriz
 A = [1 2; 3 4; 5 6; 7 8]

 % Inicializando um vetor
 v = [1 2 3 4 5]

% Retornando dimens�es de uma matriz (m = linhas e n = colunas)
[m, n] = size(A)

% Outra forma de armazenar informa��es sobre a dimens�o da matriz
dim_A = size(A)

% Indexando vari�vel dim_A para retornar apenas linhas
rows = dim_A(1)

% Retornando dimens�es do vetor v
dim_v = size(v)

% Retornando linha 2 coluna 2 da matriz e 2� elemento do vetor
A(2, 2)
v(2)

