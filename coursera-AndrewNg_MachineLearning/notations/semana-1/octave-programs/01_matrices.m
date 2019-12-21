

 % Ponto e vírgula ';' indica a escrita em novas linhas de uma matriz
 A = [1 2; 3 4; 5 6; 7 8]

 % Inicializando um vetor
 v = [1 2 3 4 5]

% Retornando dimensões de uma matriz (m = linhas e n = colunas)
[m, n] = size(A)

% Outra forma de armazenar informações sobre a dimensão da matriz
dim_A = size(A)

% Indexando variável dim_A para retornar apenas linhas
rows = dim_A(1)

% Retornando dimensões do vetor v
dim_v = size(v)

% Retornando linha 2 coluna 2 da matriz e 2º elemento do vetor
A(2, 2)
v(2)

