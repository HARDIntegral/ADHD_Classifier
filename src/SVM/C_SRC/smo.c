#include "smo.h"

#define max(a,b)            (((a) > (b)) ? (a) : (b))
#define min(a,b)            (((a) < (b)) ? (a) : (b))

// Prototypes
double* L_H(input_data_t* input, gsl_vector* alphas, int alpha_i_idx, int alpha_j_idx);
double eta(input_data_t* input, int alpha_i_idx, int alpha_j_idx);
double opt_alpha_j(input_data_t* input, gsl_vector* alphas, int alpha_i_idx, int alpha_j_idx, double b);
double alpha_i_new(double alpha_i_old, double alpha_j_old, double alpha_j_new, int y_i, int y_j);
double b(input_data_t* input, double b_old, int i_idx, int j_idx, gsl_vector* alphas, double alpha_i_new, double alpha_j_new);

double f_x(input_data_t* input, int x_idx, gsl_vector* alphas, double b);
double rd();

// Main functions
opt_output* compute_alphas(input_data_t* input, double tol, int max_passes){
    opt_output* result = (opt_output*) malloc(sizeof(opt_output));
    result->alphas = gsl_vector_alloc(input->x[0]->size);
    gsl_vector_set_all(result->alphas, 0);
    result->b = 0;

    int passes = 0;
    do {
        int changed_alphas = 0;
        for (size_t i=0; i<input->x[0]->size; i++) {
            double E_i = f_x(input, i, result->alphas, result->b);
            if (
                (input->y[i]*E_i<-1*tol && gsl_vector_get(result->alphas, i)<input->C) || 
                (input->y[i]*E_i>tol && gsl_vector_get(result->alphas, i)>0)
            ) {

            }
        }
        if (changed_alphas) passes = 0; else passes++;
    } while (passes < max_passes);

    return result;
}

double* L_H(input_data_t* input, gsl_vector* alphas, int alpha_i_idx, int alpha_j_idx) {
    double* result = (double*) malloc(sizeof(double)*2);
    if (input->y[alpha_i_idx] == input->y[alpha_j_idx]) {
        result[0] = max(0, gsl_vector_get(alphas, alpha_j_idx) - gsl_vector_get(alphas, alpha_i_idx));
        result[1] = min(input->C, input->C + gsl_vector_get(alphas, alpha_j_idx) - gsl_vector_get(alphas, alpha_i_idx));
    } else {
        result[0] = max(0, gsl_vector_get(alphas, alpha_j_idx) + gsl_vector_get(alphas, alpha_i_idx) - input->C);
        result[1] = min(input->C, gsl_vector_get(alphas, alpha_j_idx) + gsl_vector_get(alphas, alpha_i_idx));
    }
    return result;    
}

double eta(input_data_t* input, int alpha_i_idx, int alpha_j_idx) {
    return 2 * dot_prod(input->x[alpha_i_idx], input->x[alpha_j_idx])
        - dot_prod(input->x[alpha_i_idx], input->x[alpha_i_idx])
        - dot_prod(input->x[alpha_j_idx], input->x[alpha_j_idx]);
}

double opt_alpha_j(input_data_t* input, gsl_vector* alphas, int alpha_i_idx, int alpha_j_idx, double b) {
    double new_alpha_j = gsl_vector_get(alphas, alpha_j_idx)
        -(f_x(input, alpha_i_idx, alphas, b)-f_x(input, alpha_j_idx, alphas, b)+input->y[alpha_j_idx]-input->y[alpha_i_idx]
        /eta(input, alpha_i_idx, alpha_j_idx));
    double* l_h = L_H(input, alphas, alpha_i_idx, alpha_j_idx);
    if (new_alpha_j>l_h[1])
        return l_h[1];
    if (new_alpha_j<l_h[0])
        return l_h[0];
    return new_alpha_j;
}

double alpha_i_new(double alpha_i_old, double alpha_j_old, double alpha_j_new, int y_i, int y_j) {
    return alpha_i_old + y_i * y_j * (alpha_j_old-alpha_j_new);
}

double b(input_data_t* input, double b_old, int i_idx, int j_idx, gsl_vector* alphas, double alpha_i_new, double alpha_j_new) {
    double b0 = b_old 
        - input->y[i_idx]*(alpha_i_new - gsl_vector_get(alphas, i_idx))*dot_prod(input->x[i_idx], input->x[i_idx]) 
        - input->y[j_idx]*(alpha_j_new - gsl_vector_get(alphas, j_idx))*dot_prod(input->x[j_idx], input->x[j_idx]);
    double b1 = b0 - f_x(input, i_idx, alphas, b_old) + input->y[i_idx];
    double b2 = b0 - f_x(input, j_idx, alphas, b_old) + input->y[j_idx];
    if (alpha_i_new > 0 && alpha_i_new < input->C)
        return b1;
    if (alpha_j_new > 0 && alpha_j_new < input->C)
        return b2;
    return (b1+b2) / 2;
}

// Helper functions
double f_x(input_data_t* input, int x_idx, gsl_vector* alphas, double b) {
    double result = 0;
    if (input->use_rbf) {
        for (int i=0; i<input->x[0]->size; i++)
            result += gsl_vector_get(alphas, i)*input->y[i]*k_rbf(input->x[i], input->x[x_idx]);
    } else {
        for (int i=0; i<input->x[0]->size; i++)
            result += gsl_vector_get(alphas, i)*input->y[i]*k_custom(input->x[i], input->x[x_idx]);
    }
    return result+b;
}

double rd() {
    time_t t;
    srand((unsigned int)time(&t));
    uint64_t r53 = ((uint64_t)(rand()) << 21) ^ (rand() >> 2);
    return (double)r53 / 9007199254740991.0; // 2^53 - 1
}