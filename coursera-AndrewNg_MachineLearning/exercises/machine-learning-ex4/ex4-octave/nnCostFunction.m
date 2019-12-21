% Implementando toda a função
function [J, grad] = nnCostFunction(theta_vec, input_layer_size, ...
                    hidden_layer_size, num_labels, X, y, lambda)

% Preparando dados X e y (adicionando bias e transformando target em matriz)
m = size(X, 1);
X_train = [ones(m, 1) X];
y_train = eye(num_labels) (y, :);

% Transformando vetor de parâmetros em duas matrizes novamente
theta1_x = 1;
theta1_y = hidden_layer_size * (input_layer_size + 1);

theta2_x = theta1_y;
theta2_y = theta2_x + num_labels * (hidden_layer_size + 1);

Theta1_unrolled = reshape(theta_vec(1:theta1_y), hidden_layer_size, input_layer_size+1);
Theta2_unrolled = reshape(theta_vec(theta2_x+1:theta2_y), num_labels, hidden_layer_size+1);

% Calculando hypothesis com forward propagation
a1 = X_train;
z2 = a1 * Theta1_unrolled';
a2 = sigmoid(z2);
a2 = [ones(m, 1) a2];
z3 = a2 * Theta2_unrolled';
a3 = sigmoid(z3);
h_theta = a3;

% Calculando função de custo 
unreg_J = sum(sum((-y_train .* log(h_theta)) - ((1 - y_train) .* log(1 - h_theta)))) / m;

t1_sem_bias = Theta1_unrolled(:, 2:size(Theta1_unrolled, 2));
t2_sem_bias = Theta2_unrolled(:, 2:size(Theta2_unrolled, 2));
reg_J = (lambda / (2*m)) * (sum(sum(t1_sem_bias .^ 2)) + sum(sum(t2_sem_bias .^ 2)));
J = unreg_J + reg_J;

% --------------------------------------------------
% Calculando Back Propagation

% Primeiro passo - calculando deltas
delta3 = h_theta - y_train;
delta2 = (delta3 * Theta2_unrolled)(:, 2:end) .* sigmoidGradient(z2); % excluindo termo bias
sigz2 = sigmoidGradient(z2);

% Segundo passo - calculando D1 e D2
D1 = delta2' * a1;
D2 = delta3' * a2;
% Calculando gradientes
Theta1_grad = D1 / m + lambda * [zeros(hidden_layer_size, 1) Theta1_unrolled(:, 2:end)] / m;
Theta2_grad = D2 / m + lambda * [zeros(num_labels, 1) Theta2_unrolled(:, 2:end)] / m;

% Retornando gradientes em matriz única (unrolling)
grad = [Theta1_grad(:); Theta2_grad(:)];

endfunction 