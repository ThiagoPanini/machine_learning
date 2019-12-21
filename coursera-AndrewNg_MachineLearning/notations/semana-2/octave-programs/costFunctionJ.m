% Function to compute Cost Function J of a given data
function J = costFunctionJ(X, y, theta)
  % X is the "design matrix" containing our training examples
  % y is the class labels
  
  m = size(X, 1);                 % Number of training examples
  predictions = X*theta;          % Predictions of hypothesis on all m examples
  sqrErrors = (predictions-y).^2; % Squared errors
  
  J = 1/(2*m) * sum(sqrErrors);
endfunction
