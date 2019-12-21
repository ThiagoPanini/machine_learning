% TUTORIAL 1 - OCTAVE

%--------- PRINTANDO NA TELA ---------
disp('Hello World!')

%--------- PRINT FORMATADO ---------
a = pi
disp(sprintf('Numero PI com 2 casas decimais: %.2f', a))
%format short
%format long

%--------- MATRIZES E VETORES ---------
A = [1, 2, 3; 4, 5, 6]
v = [1; 2; 3; 4; 5; 6]
v_range = [1:.2:2]
v_range_2 = [1:5]

%--------- FUNÇÕES ESPECÍFICAS ---------

% ------ ones() ------
C = ones(2, 3)
C = 2*ones(2, 3)

% ------ zeros() ------
w = zeros(1, 3)

% ------ rand() e randn() ------
z = rand(1, 3)
rand(3, 3)
n = randn(1, 3)

% ------ eye() ------
eye(4)

% ------ size() ------
A = [1, 2; 3, 4; 5, 6]
size(A)
size(A)(1)
size(A, 2)

% ------ length() ------
v = [0:2:10]
length(v)

% ------ help() ------
help eye

%--------- VISUALIZANDO DADOS ---------
f = -6+sqrt(10)*(randn(1, 10000));
hist(f, 50)



