import numpy as np
# . Construct a random n-vector with non-negative entries and scale its entries so that the sum is 1. This computation gives us a probability distribution p
N = np.random.rand(100)
N = N / np.sum(N)

# Construct a random n × n (say n = 5) matrix with non-negative entries, and scale the entries so that
# the sum for each row is 1. This computation gives us a transition matrix P.
P = np.random.rand(5, 5)
P = P / np.sum(P, axis=1, keepdims=True)

#Starting from p as the initial state, compute the transition for N (say N = 50) steps (i.e., compute p ← PT p for N times).

