import numpy as np
import cvxopt       # used to assist in optimization

def rbf(x1, x2, sigma=0.1):
    return np.exp(-np.linalg.norm(x1-x2)/(2*sigma**2))

class SVM():
    def __init__(self, kernel=rbf, C=1):
        self.kernel = kernel
        self.C = C
    
    def fit(self, X, y):
        self.X = X
        self.y = y
        m, n = X.shape

        # calculating the kernel
        self.K = np.zeros((m,m))
        for i in range(m):
            self.K[i,:] = self.kernel(X[i, np.newaxis], self.X)
        
        P = cvxopt.matrix(np.outer(y,y)*self.K)
        q = cvxopt.matrix(-np.ones((m,1)))
        G = cvxopt.matrix(np.vstack((np.eye(m)*-1, np.eye(m))))
        h = cvxopt.matrix(np.hstack((np.zeros(m), np.ones(m)*self.C)))
        A = cvxopt.matrix(y, (1,m), 'd')
        b = cvxopt.matrix(np.zeros(1))

        cvxopt.solvers.options['show_progress'] = False
        sol = cvxopt.solvers.qp(P, q, G, h, A, b)
        self.alphas = np.array(sol['x'])

    def predict(self, X):
        y_predict = np.zeros((X.shape[0]))
        sv = self.get_parameters(self.alphas)
        for i in range(X.shape[0]):
            y_predict[i] = np.sum(self.alphas[sv]*self.y[sv, np.newaxis]*self.kernel(X[i], self.X[sv])[:,np.newaxis])
        return np.sign(y_predict + self.b)

    def get_parameters(self, alphas):
        threshold = 1e-4
        sv = ((alphas>threshold)*(alphas<self.C)).flatten()
        self.w = np.dot(self.X[sv].T, alphas[sv]*self.y[sv, np.newaxis])
        self.b = np.mean(self.y[sv, np.newaxis] - self.alphas[sv]*self.y[sv, np.newaxis]*self.K[sv,sv][:,np.newaxis])
        return sv