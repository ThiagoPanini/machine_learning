% TUTORIAL 2 - OCTAVE

% ------ cd ------
pwd
typeinfo(path = [pwd '\arquivos_octave'])
%cd 'C:\Users\thiagoPanini\data-science-courses\coursera\intro-ml-andew-ng\semana-2\arquivos_octave'
ls

% ------ load ------
load featuresX.dat
load priceY.dat

featuresX
priceY
size(featuresX)
size(priceY)

% ------ clear ------
%clear 

% ------ save ------
v = priceY(1:10)
save hello.mat v;