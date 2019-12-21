% Normal Equation
%pinv(X'*X)*X'*y

% Exemplo
X = [1, 2104, 5, 1, 45;
1, 1416, 3, 2, 40;
1, 1534, 3, 2, 39;
1, 852, 2, 1, 36]

y = [460; 232; 315; 178]

theta = pinv(X'*X)*X'*y


