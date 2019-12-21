% ----- CONTROL STATEMENTS -----

% ----- for loop -----
v = zeros(10, 1)
indices = 1:10
for i=indices,
  v(i) = 2^i;
endfor
v

% ----- while loop -----
i=1;
while i<= 5,
  v(i)=100;
  i = i+1;
endwhile
v

% ----- while ; break -----
i=1;
while true,
  v(i)=999;
  i = i+1;
  if i==6,
    break
  endif
endwhile
v

% ----- if; else -----
v(1)=2;
if v(1)==1
  disp('The value is one.');
elseif v(1)==2
  disp('The value is two.');
else
  disp('The value is not one or two.');
endif

% ----- calling functions -----
quad_test = squareThisNumber(5)
[quad, cube] = squareAndCubeThisNumber(4)

% ----- example Cost Function J -----
disp('')
disp('Real Example of calling a function that calculates Cost Function J');
X = [1, 1; 1, 2; 1, 3]
y = [1; 2; 3]
theta = [0; 1]
j = costFunctionJ(X, y, theta)
disp('j=0 because all the training examples fit exactly on y labels');