function [C, sigma] = dataset3Params(X, y, Xval, yval)
%DATASET3PARAMS returns your choice of C and sigma for Part 3 of the exercise
%where you select the optimal (C, sigma) learning parameters to use for SVM
%with RBF kernel
%   [C, sigma] = DATASET3PARAMS(X, y, Xval, yval) returns your choice of C and 
%   sigma. You should complete this function to return the optimal C and 
%   sigma based on a cross-validation set.
%

% You need to return the following variables correctly.

% ====================== YOUR CODE HERE ======================
% Instructions: Fill in this function to return the optimal C and sigma
%               learning parameters found using the cross validation set.
%               You can use svmPredict to predict the labels on the cross
%               validation set. For example, 
%                   predictions = svmPredict(model, Xval);
%               will return the predictions on the cross validation set.
%
%  Note: You can compute the prediction error using 
%        mean(double(predictions ~= yval))
%

# Treinando novamente o modelo e salvando os parâmetros
j = 1;
k = 1;
predictions = zeros(64)(:, 1:3);
lowest_error = 1;
C = 0;
sigma = 0;
params_values = [0.01; 0.03; 0.1; 0.3; 1; 3; 10; 30]

for i = 1:length(predictions)
    C_val = params_values(j)
    sigma_val = params_values(k)
    model = svmTrain(X, y, C_val, @(x1, x2) gaussianKernel(x1, x2, sigma_val));
    y_pred = svmPredict(model, Xval);
    performance = mean(double(y_pred ~= yval));
    
    predictions(i) = performance;
    predictions(i+64) = C_val;
    predictions(i+128) = sigma_val;
    
    if performance < lowest_error
        lowest_error = performance;
        C = C_val;
        sigma = sigma_val;
    endif
    
    k = k + 1;
    
    if k == 9
        k = 1;
        j = j + 1;
    endif
    
    if j == 9;
        break
    endif
    
endfor





% =========================================================================

end
