import numpy as np
n = 5; N = 50
# . Construct a random n-vector with non-negative entries and scale its entries so that the sum is 1. This computation gives us a probability distribution p
p = np.random.rand(n)
p = p / np.sum(p)

# Construct a random n × n (say n = 5) matrix with non-negative entries, and scale the entries so that
# the sum for each row is 1. This computation gives us a transition matrix P.
P = np.random.rand(n, n)
P = P / np.sum(P, axis=1, keepdims=True)

#Starting from p as the initial state, compute the transition for N (say N = 50) steps (i.e., compute p ← P^T p for N times).

p = np.dot(P.T, p)
for i in range(N):
    p = np.dot(P.T, p)

# Use the function np.linalg.eig to compute the eigenvector of P.T corresponding to the largest eigenvalue.
# Rescale the entries of the eigenvector so that its sum is equal to 1. Let the resulting vector be pstationary
# (or p_stationary).

p_stationary = np.linalg.eig(P.T)[1][:,0]
p_stationary = p_stationary / np.sum(p_stationary)
