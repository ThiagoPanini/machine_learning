% ----- PLOTTING DATA ON OCTAVE -----
t=[0:.01:.98];
y1=sin(2*pi*4*t);
y2=cos(2*pi*4*t);
plot(t, y1);
hold on;
plot(t, y2, 'r'); 
xlabel('Time');
ylabel('Value');
legend('sin', 'cos');
title('First Octave Plot');

% ----- saving file -----
% cd 'C:\Users\thiagoPanini\Desktop' change directory if needed
print -dpng 'myFirstOctavePlot.png'

% ----- figure() -----
figure(2); plot(t, y1);
figure(3); plot(t, y2);

% ----- subplot(grid_row, grid_col, element_selected) -----
figure(4);
subplot(1, 2, 1); % divides plot a 1x2 grid and access the first element
plot(t, y1);
subplot(1, 2, 2); % access the second element
plot(t, y2);
axis([.5 1 -1 1])
print -dpng 'subplots_sin_cos.png'

% ----- colorbar -----
figure(5);
A = magic(5);
imagesc(A), colorbar, colormap gray;
print -dpng 'imagesc_colormap_magic5.png'

figure(6)
imagesc(magic(15)), colorbar, colormap gray;
print -dpng 'imagesc_colormap_magic15.png'