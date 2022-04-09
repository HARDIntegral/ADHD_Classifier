#include "cv_opt.hpp"
#include "ortools/linear_solver/linear_solver.h"

extern "C" gsl_vector* compute_alphas(input_data_t* input) {
    gsl_vector* alphas = gsl_vector_alloc(input->x[0]->size);
    gsl_vector_set_all(alphas, 0.5);
    return alphas;
}