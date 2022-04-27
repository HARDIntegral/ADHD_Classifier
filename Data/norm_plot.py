#!/usr/bin/env python3

from numpy import linspace
import matplotlib.pyplot as plt
import scipy.stats as ss

plt.style.use('seaborn') # pretty matplotlib plots
plt.rcParams['figure.figsize'] = (8,5)

def plot_normal(data_points,x_range,mu,sigma,color,label):
    
    x = x_range
    y = ss.norm.pdf(x,mu,sigma)
    
    plt.plot(x,500*y,color=color,label=label)
    plt.hist(data_points,color=color,alpha=0.4,bins = 20)

RBF = [
    67,62,67,58,62,62,62,71,67,62,62,62,50,62,58,71,58,62,58,71,
    62,71,67,54,62,54,67,67,71,75,62,79,42,58,75,58,71,58,58,54,
    58,62,62,58,62,79,62,50,67,62,58,71,62,67,58,58,58,67,67,58,
    67,71,67,67,75,67,71,67,62,46,71,62,67,67,67,58,71,58,75,67,
    54,67,62,75,54,62,62,67,54,58,62,67,62,79,67,58,71,71,62,83,
]

RBF_M = [
    62,67,67,54,62,58,71,71,62,62,62,75,38,62,54,71,58,62,58,67,
    67,67,62,54,67,58,71,62,71,79,54,79,42,62,71,58,67,58,58,67,
    67,67,58,54,71,67,62,58,67,62,54,67,58,71,67,67,58,67,67,62,
    67,67,62,62,67,58,67,67,67,54,67,62,71,62,62,62,62,58,71,71,
    50,62,71,75,62,67,67,54,58,67,71,75,62,75,71,54,62,79,71,79, 
]

POLY = [
    50,58,33,42,62,42,54,50,71,38,38,29,58,50,50,25,33,33,62,50,
    33,42,62,58,29,71,58,58,46,38,62,21,42,46,38,46,54,46,50,67,
    29,38,67,50,83,54,50,38,42,58,25,46,33,62,62,46,38,38,46,54,
    33,50,46,42,50,54,71,54,46,67,25,50,33,29,33,62,58,46,58,46,
    46,46,38,54,42,38,50,29,29,46,54,71,67,42,54,54,62,42,67,54,
]

HYBRID = [
    62,58,75,62,58,67,54,58,83,75,58,75,54,54,58,79,62,67,50,62,
    79,54,67,50,79,62,71,54,67,79,62,92,58,46,54,67,54,50,54,67,
    62,58,62,50,67,62,54,71,58,71,54,54,54,58,67,67,54,67,75,67,
    79,71,67,71,71,67,75,54,71,71,71,58,67,71,50,67,71,58,75,58,
    62,62,67,50,67,58,71,58,67,62,67,75,67,71,71,62,83,75,67,71,
]

data = [ RBF , RBF_M, POLY, HYBRID ]

x_min = 0.0
x_max = 100.0
m_rbf = 63.85
m_rbf_m = 64.06
m_poly = 47.92
m_hybrid = 64.45
s_rbf = 7.1567937632502
s_rbf_m = 7.25971310338324
s_poly = 12.5607051207849
s_hybrid = 8.96612592714457

x = linspace(x_min,x_max,5000)

plot_normal(RBF,x,m_rbf,s_rbf,'red','RBF Kernel')
plot_normal(RBF_M,x,m_rbf_m,s_rbf_m,'blue','RBF Kernel with Mask')
plot_normal(POLY,x,m_poly,s_poly,'green','Polynomial Kernel with Mask')
plot_normal(HYBRID,x,m_hybrid,s_hybrid,'orange','Polynomial and RBF Hybrid Kernel with Mask')

plt.xlim(x_min,x_max)
plt.ylim(0,40)

plt.xlabel('Accuacy (%)')
plt.ylabel('Frequency')
plt.legend()
plt.show()