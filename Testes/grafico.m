media = [0.1531049, 0.1000248, 0.2010095, 0.2473311]; 
desvio = [1.9691e-3, 5.14103e-3, 2.1455e-3, 0.0162869];  
figure
hold on
title('Tempo de execução')
xlabel('Algoritmo')
ylabel('Tempo(s)')
bar(media, 0.5, 'w')
errorbar(media,desvio, '.')