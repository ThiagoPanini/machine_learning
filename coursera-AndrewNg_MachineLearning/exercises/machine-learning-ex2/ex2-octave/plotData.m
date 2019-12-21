function plotData(X, y)
%PLOTDATA Plots the data points X and y into a new figure 
%   PLOTDATA(x,y) plots the data points with + for the positive examples
%   and o for the negative examples. X is assumed to be a Mx2 matrix.


% ====================== YOUR CODE HERE ======================
% Instructions: Plot the positive and negative examples on a
%               2D plot, using the option 'k+' for the positive
%               examples and 'ko' for the negative examples.
%

    % ---------------------
    %     Description
    % ---------------------
    % Fun��o respons�vel pela plotagem gr�fica da distribui��o das notas dos alunos (Exames 1 e 2).
    % Os valores ser�o distribu�dos e separados de acordo com a classifica��o proposta em y (aprovado/reprovado)
    
    % Encontra os �ndices dos aprovados e dos reprovados
    X_pass = find(y==1);
    X_rec = find(y==0);
    
    % Separa os dados de aprovados e reprovados por exame
    X_pass_e1 = X(X_pass, 1);
    X_pass_e2 = X(X_pass, 2);
    X_rec_e1 = X(X_rec, 1);
    X_rec_e2 = X(X_rec, 2);
    
    % Configura plotagem
    h = figure;
    set (h,'papertype', '<custom>');
    set (h,'paperunits','inches');
    set (h,'papersize',[3 2.5]);
    set (h,'paperposition', [0,0,[3 2.5]]);
    set (h,'defaultaxesposition', [0.15, 0.15, 0.75, 0.75]);
    set (0,'defaultaxesfontsize', 14);
    
    % Plota os dados
    plot(X_pass_e1, X_pass_e2, 'k+', ...
        'MarkerSize', 7, 'LineWidth', 8)
    hold on;
    plot(X_rec_e1, X_rec_e2, 'yo', ...
        'MarkerSize', 7, 'LineWidth', 3)
    
    # Legendas e labels
    xlabel('Nota no Exame 1')
    ylabel('Nota no Exame 2')
    title('Distribuicao de Notas e Classificacao dos Estudantes')

% =========================================================================

end
