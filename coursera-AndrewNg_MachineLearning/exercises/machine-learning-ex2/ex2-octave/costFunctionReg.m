function [J, grad] = costFunctionReg(theta, X, y, lambda)
%COSTFUNCTION Compute cost and gradient for logistic regression
%   J = COSTFUNCTION(theta, X, y) computes the cost of using theta as the
%   parameter for logistic regression and the gradient of the cost
%   w.r.t. to the parameters.

% Initialize some useful values
m = length(y); % number of training examples

% You need to return the following variables correctly 
J = 0;
grad = zeros(size(theta, 1), 1);

% ====================== YOUR CODE HERE ======================
% Instructions: Compute the cost of a particular choice of theta.
%               You should set J to the cost.
%               Compute the partial derivatives and set grad to the partial
%               derivatives of the cost w.r.t. each parameter in theta
%
% Note: grad should have the same dimensions as theta
%
    
# Calcula hypothesis
z = X * theta;
h = sigmoid(z);

% We want the regularization to exclude the bias feature, so we can set theta(1) to zero
% or change the whole vector theta1 = [0 ; theta(2:size(theta), :)];
theta(1) = 0;

# Calcula função de custo J
unreg_J = (1 / m) * (-y' * log(h) - (1 - y)' * log(1 - h)); % Custo sem regularização
reg_J = (lambda / (2 * m)) * (theta' * theta); % Custo da regularização

J = unreg_J + reg_J; % Somando os termos

# Calcula gradiente para theta_0
grad = (X' * (h - y) + lambda * theta) / m; % Termo (lambda*theta/2) aplicado


% =============================================================

end