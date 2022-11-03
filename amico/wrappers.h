/*
Wrappers for NNLS and LASSO (SPAMS) functions
*/

#ifndef WRAPPERS_H
#define WRAPPERS_H

#include "nnls.h"
#include "spams.h"

// INPUT
// A = (m, n)   Matrix stored as 1D contiguous array (column-major order)
// y = (m)      Vector stored as 1D contiguous array

// OUTPUT
// x = (n)      Solution vector
void nnls(const double *A, const double *y, const int m, const int n, double *x, double &rnorm)
{
    // NOTE work on a copy of 'A' and 'y' because the '_nnls()' call will modify them
    double *_A = new double[m * n];
    double *_y = new double[m];
    std::copy(A, A + m * n, _A);
    std::copy(y, y + m, _y);

    _nnls(_A, _y, m, n, x, rnorm);
    // if (ret == 1)
    //     std::cout << "WARNING: NNLS max iterations exceeded" << std::endl;
    // if (ret == 2)
    //     throw std::runtime_error("NNLS failed");

    delete[] _A;
    delete[] _y;
}

// INPUT
// A = (m, p)   Matrix stored as 1D contiguous array (column-major order)
// y = (m, n)   Vector stored as 1D contiguous array

// OUTPUT
// x = (p, n)   Solution vector
void lasso(double *A, double *y, const int m, const int p, const int n, const double lambda1, const double lambda2, double *x)
{
    Matrix<double> *_A = new Matrix<double>(A, m, p);
    Matrix<double> *_y = new Matrix<double>(y, m, n);

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

    Matrix<double> *_x = new Matrix<double>(x, p, n);
    _lassoD(_y, _A, path, return_reg_path, L, lambda1, lambda2, mode, pos, ols, n_threads, max_length_path, verbose, cholevsky)->toFull(*_x);

    delete _A;
    delete _y;
    delete _x;
}

#endif
