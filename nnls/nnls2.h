#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int _nnls(double *a, int m, int n, double *b, double *x, double *rnorm, double *wp, double *zzp, int *indexp)
{
    if (m <= 0 || n <= 0 || a == NULL || b == NULL || x == NULL)
        return (2);

    
}