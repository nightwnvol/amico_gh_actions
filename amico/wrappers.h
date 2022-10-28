#include "nnls.h"
#include "spams.h"

// INPUT
// A = (m, n)   Matrix stored as 1D contiguous array (column-major order)
// y = (m)     Vector stored as 1D contiguous array

// OUTPUT
// x = (n)     Solution vector
void nnls
(
    const double *A,
    const double *y,
    const int m,
    const int n,
    double *x,
    double *rnorm
)
{
    // NOTE make a copy of A and y cause _nnls call will modify them
    // double *_A = (double *) malloc(sizeof(double) * m * n);
    // double *_y = (double *) malloc(sizeof(double) * m);
    double *_A = new double[m * n];
    double *_y = new double[m];
    std::copy(A, A + m * n, _A);
    std::copy(y, y + m, _y);

    // TODO move this into _nnls
    // Instantiate more working space (there will be allocated later by _nnls call)
    double *wp = NULL;
    double *zzp = NULL;
    int *indexp = NULL;

    _nnls(_A, m, n, _y, x, rnorm, wp, zzp, indexp);

    // free(_A);
    // free(_y);
    delete[] _A;
    delete[] _y;
}

// INPUT
// A = (m, n)   Matrix stored as 1D contiguous array (column-major order)
// y = (m)     Vector stored as 1D contiguous array

// OUTPUT
// x = (n)     Solution vector
void lasso
(
    double *A,
    double *y,
    const int m,
    const int n,
    const double lambda1,
    const double lambda2,
    double *x
)
{
    Matrix<double> *_A = new Matrix<double>(A, m, n);
    Matrix<double> *_y = new Matrix<double>(y, m, 1);

    Matrix<double> **path = 0;
    Matrix<double> *path_data;
    path = &path_data;

    const bool return_reg_path = false;
    const int L = -1;
    const constraint_type mode = PENALTY;
    const bool pos = true;
    const bool ols = false;
    const int n_threads = 1;
    const int max_length_path = -1;
    const bool verbose = false;
    const bool cholevsky = false;

    // SpMatrix<double> *_x = (SpMatrix<double> *) _lassoD(_y, _A, path, return_reg_path, L, lambda1, lambda2, mode, pos, ols, n_threads, max_length_path, verbose, cholevsky);
    // Matrix<double> _x_dense;
    // _x->toFull(_x_dense);
    // std::copy(_x_dense.rawX(), _x_dense.rawX() + _x_dense.m() * _x_dense.n(), x);

    // Matrix<double> _x;
    // _lassoD(_y, _A, path, return_reg_path, L, lambda1, lambda2, mode, pos, ols, n_threads, max_length_path, verbose, cholevsky)->toFull(_x);
    // std::copy(_x.X(), _x.X() + _x.m() * _x.n(), x);

    Matrix<double> *_x = new Matrix<double>(x, n, 1);
    _lassoD(_y, _A, path, return_reg_path, L, lambda1, lambda2, mode, pos, ols, n_threads, max_length_path, verbose, cholevsky)->toFull(*_x);

    delete _A;
    delete _y;
    delete _x;
}
