% ----- Element-wise multiplication -----
A = [1 2; 3 4; 5 6]
B = [11 12; 13 14; 15 16]
C = [1 1; 2 2]

disp('matrix multiplication')
A * C
disp('element-wise multiplication')
A .* B
disp('quadratic of elementos of A')
A .^ 2

v = [1; 2; 3]
disp('element-wise divison')
1 ./ v

% ----- log() -----
disp('log function is a element-wise operation')
log(v)

% ----- exp() -----
disp('exp function returns e^elements of v')
exp(v)

% ----- abs() -----
disp('abs function returns the absolute number of v')
abs(v)

% ----- inverting signal (-1*v) -----
disp('inverting the signal of a structure also is a element-wise op')
-v

% ----- incrementing v -----
disp('incrementing a vector')
length(v) % 3
ones(length(v), 1) % [1; 1; 1]
v + ones(length(v), 1)

% ----- easy way to incrementing v -----
disp('easy way to incrementing a vector (v+1)')
v+1

% ----- transpose -----
M = [1, 2, 3; 4, 5, 6]
disp('transposing a matrix')
M'
disp('transposing again... = M')
(M')'

% ----- max() -----
a = [1 15 .5 2]
disp('maximum of a')
max(a)
disp('maximum and index')
[val, ind] = max(a)
a

% ----- element-wise comparison -----
disp('all elements of a < 3')
a < 3
disp('index of the elements above')
find(a < 3)

% ----- sum() and prod() -----
a
disp('sum elements of a')
sum(a)
disp('multiplying elements of a')
prod(a)

% ----- magic() -----
A = magic(3)

% ----- important max() -----
disp('returning the max of a specific matrix dimensions (cols)')
max(A, [], 1)
disp('returning the max of a specific matrix dimensions (rows)')
max(A, [], 2)

% ----- merging all elements of a matrix -----
disp('merging all elements of a matrix (:)')
A(:)

% ----- again max() -----
disp('finding the max elementos of the entire matrix')
max(A(:))

% ----- verifying magic sum -----
A = magic(9)
disp('sum elements of a magic function (columns)')
sum(A, 1)
disp('sum elements of a magic function (rows)')
sum(A, 2)
disp('sum elements of a magic function (diagonals)')
eye(length(A))
A.*eye(length(A))
sum(sum(A.*eye(length(A))))