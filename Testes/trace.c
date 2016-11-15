#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main () {
    int total = 64, virtual = 128, s = 4, p = 4;
    int i, j, linhas, n, pi, ti, t0, tf, b;
    printf("%d %d %d %d\n", total, virtual, s, p);
    srand((unsigned)time(NULL));
    linhas = 1+(rand()%100);       // número de processos (entre 1 e 100)
    for (i = 0; i < linhas; i++) {
        t0 = 1 + (rand()%5);       // tempo inicial (entre 1 e 5)
        tf = 1 + (rand()%10) + t0; // delta t + t0 (No máximo 10 seg de execução)
        b = 1 + (rand()%128);       // total de memória usado (entre 1 e 128)
        printf("%d proc%d %d %d ", t0, i, tf, b);
        n = 1 + (rand()%15);                // número de pags e instantes que ele as acessa (entre 1 e 15)
        for (j = 0; j < n; j++) {
            pi = 1 + (rand()%16);           // o numero da pag que ele acessa (entre 1 e 16 = 64/4) 
            ti = t0 + (rand()%(tf - t0));   // o tempo que ele acessa (entre t0 e tf)
            printf("%d %d ", pi, ti);
        }
        printf("\n");
    }
    return 0;
}