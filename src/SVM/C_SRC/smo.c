#include "smo.h"

// Prototypes
double* L_H(input_data_t* input, int alpha_i_idx, int alpha_j_idx, double C);
gsl_vector* eta(input_data_t* input, int alpha_i_idx, int alpha_j_idx);
double opt_alpha_j(input_data_t* input, int alpha_i_idx, int alpha_j_idx);
double alpha_i_new(double alpha_i_old, double alpha_j_old, double alpha_j_new, int y_i, int y_j);
double b(input_data_t* input, int i_idx, int j_idx, double alpha_i_old, double alpha_j_old, double alpha_i_new, double alpha_j_new);

// Main functions
opt_output* compute_alphas(input_data_t* input, double tol, int max_passes){
    opt_output* result = (opt_output*) malloc(sizeof(opt_output));
    result->alphas = gsl_vector_alloc(input->x[0]->size);
    gsl_vector_set_all(result->alphas, 0.5);
    result->b = 1;
    return result;
}