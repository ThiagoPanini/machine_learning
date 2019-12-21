% Somando matrizes
A = [1 0; 2 5; 3 1]
B = [4 .5; 2 5; 0 1]

A + B

% Subtraindo matrizes
C = [2 5; 3 2; 3 4]
D = [1 2.5; 0 2; 2 1]

C - D

% Multiplicação por escalar
E = [1 0; 2 5; 3 1]
3*E

% Divisão por escalar
F = [4 0; 6 3]
F/4

% Multiplicação matriz*vetor
G = [1 3; 4 0; 2 1]
h = [1; 5]

G*h

% Exemplo 2 - Multiplicação matrix*vetor
M = [1 2 1 5; 0 3 0 4; -1 -2 0 0]
vec = [1; 3; 2; 1]
M * vec

% Multiplicação matriz*matriz
mat_1 = [1 3 2; 4 0 1]
mat_2 = [1 3; 0 1; 5 2]
mat_1 * mat_2

% Exemplo prático - diferentes hypothesis
sizes = [1 2104; 1 1416; 1 1534; 1 852]
hypothesis = [-40 200 -150; .25 .1 .4]
predictions = sizes * hypothesis

% Inicializando duas matrizes
A = [1, 2; 4, 5]
B = [1, 1; 0, 2]

% Matriz identidade
I = eye(2)

% Testando multiplicação
A*I
I*A

% Matrizes não são comutativas
A = [1, 1; 0, 0]
B = [0, 0; 2, 0]

A*B
B*A

% Porém são associativas
C = [4, 3; 0, 1]

A*(B*C)
(A*B)*C

% Matriz inversa
A = [3, 4; 2, 16]
inv_A = pinv(A)

ident = A*inv_A

% Matriz transposta
A = [1, 2, 0; 3, 5, 9]
A_trans = A'









