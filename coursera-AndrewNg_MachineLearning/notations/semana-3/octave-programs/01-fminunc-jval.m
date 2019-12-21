% Código referente a sessão ADVANCE OPTIMIZATION

% ---------------------------------------
% Preparando para chamar a função fminunc
% ---------------------------------------

function [jVal, gradient] = costFunction(theta)
  % Description:
  % Describes J(theta) and its derivatives
  
  jVal = (theta(1)-5)^2 + (theta(2)-5)^2;
  
  gradient = zeros(2, 1);
  gradient(1) = 2*(theta(1)-5);
  gradient(2) = 2*(theta(2)-5);
  
endfunction

% Calling fminunc
options = optimset('GradObj', 'on', 'MaxIter', 100);
initialTheta = zeros(2, 1)
[optTheta, functionVal, exitFlag] = fminunc(@costFunction, initialTheta,
                                                  options)
                                                  
                                                  



