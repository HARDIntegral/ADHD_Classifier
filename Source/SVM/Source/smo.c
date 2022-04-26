#include "smo.h"

#define max(a,b)            (((a) > (b)) ? (a) : (b))
#define min(a,b)            (((a) < (b)) ? (a) : (b))
#define rand_r(a)           (rand() %  a)

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
    result->alphas = gsl_vector_alloc(input->x_size);
    gsl_vector_set_all(result->alphas, 0.1);
    result->b = 0.1;
    int passes = 0;
    do {
        int changed_alphas = 0;
        for (size_t i=0; i<input->x_size; i++) {
            double E_i = f_x(input, i, result->alphas, result->b);
            if (
                (input->y[i]*E_i<-1*tol && gsl_vector_get(result->alphas, i)<input->C) || 
                (input->y[i]*E_i>tol && gsl_vector_get(result->alphas, i)>0)
            ) {
                int j;
                do {j = rand_r(input->x_size);} while(j==i);
                double E_j = f_x(input, j, result->alphas, result->b);
                gsl_vector* old_alphas = gsl_vector_alloc(input->x_size);
                gsl_vector_memcpy(old_alphas, result->alphas);
                double* l_h = L_H(input, result->alphas, i, j);
                if (l_h[0]==l_h[2]) continue;
                double _eta = eta(input, i, j);
                if (_eta>=0) continue;
                gsl_vector_set(result->alphas, j, opt_alpha_j(input, result->alphas, i, j, result->b));
                if (abs(gsl_vector_get(result->alphas, j)-gsl_vector_get(old_alphas, j))<1e-5) continue;
                gsl_vector_set(result->alphas, i, alpha_i_new(
                    gsl_vector_get(old_alphas, i), gsl_vector_get(old_alphas, j), 
                    gsl_vector_get(result->alphas, j), input->y[i], input->y[j]
                ));
                result->b = b(input, result->b, i, j, old_alphas, gsl_vector_get(result->alphas, i), gsl_vector_get(result->alphas, j));
                gsl_vector_free(old_alphas);
                changed_alphas++;
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
    switch (input->k_type) {
        case 0:
            for (int i=0; i<input->x_size; i++)
                result += gsl_vector_get(alphas, i)*input->y[i]*k_rbf(input->x[i], input->x[x_idx]);
            break;
        case 1:
            for (int i=0; i<input->x_size; i++)
                result += gsl_vector_get(alphas, i)*input->y[i]*k_m_rbf(input->x[i], input->x[x_idx]);
            break;
        case 2:
            for (int i=0; i<input->x_size; i++)
                result += gsl_vector_get(alphas, i)*input->y[i]*k_m_poly_3(input->x[i], input->x[x_idx]);
            break;
        case 3:
            for (int i=0; i<input->x_size; i++)
                result += gsl_vector_get(alphas, i)*input->y[i]*k_m_rbf_poly_3_3(input->x[i], input->x[x_idx]);
            break;
    }
    return result+b;
}

double rd() {
    time_t t;
    srand((unsigned int)time(&t));
    uint64_t r53 = ((uint64_t)(rand()) << 21) ^ (rand() >> 2);
    return (double)r53 / 9007199254740991.0; // 2^53 - 1
}