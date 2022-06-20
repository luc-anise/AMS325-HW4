import numpy as np
import matplotlib.pyplot as plt

n = 5
N = 50
# . Construct a random n-vector with non-negative entries and scale its entries so that the sum is 1. This computation gives us a probability distribution p

p = np.random.rand(n)
p = p / np.sum(p)

# Construct a random n × n (say n = 5) matrix with non-negative entries, and scale the entries so that
# the sum for each row is 1. This computation gives us a transition matrix P.
P = np.random.rand(n, n)
P = P / np.sum(P, axis=1, keepdims=True)

# Starting from p as the initial state, compute the transition for N (say N = 50) steps (i.e., compute p ← P^T p for N times).

for i in range(N):
    p = np.dot(P.T, p)

# Use the function np.linalg.eig to compute the eigenvector of P.T corresponding to the largest eigenvalue.

eigenvalues, eigenvectors = np.linalg.eig(P.T)
max_eigenvalue = np.max(eigenvalues)
max_eigenvector = eigenvectors[:, np.argmax(eigenvalues)]

# Rescale the entries of the eigenvector so that its sum is equal to 1. Let the resulting vector be p_stationary.
p_stationary = max_eigenvector / np.sum(max_eigenvector)

# Change the loop in step 3 to compute the norm of p − pstationary and plot the norms against i. Check
# whether the difference diminishes as the number of iterations increases.

norms = []

for i in range(N):
    p = np.dot(P.T, p)
    norms.append(np.linalg.norm(p - p_stationary))

# plot the norms against i
plt.plot(range(N), norms)
plt.show()

# Organize your code into a function so that it would take n and N as input and call the function by
# passing in n = 5 and N = 50. Document the function and test it with some other values of n and N.


def markov(n, N):
    """A function that takes n and N as input computes the markov chain."""
    p = np.random.rand(n)
    p = p / np.sum(p)
    P = np.random.rand(n, n)
    P = P / np.sum(P, axis=1, keepdims=True)
    eigenvalues, eigenvectors = np.linalg.eig(P.T)
    max_eigenvalue = np.max(eigenvalues)
    max_eigenvector = eigenvectors[:, np.argmax(eigenvalues)]
    p_stationary = max_eigenvector / np.sum(max_eigenvector)
    norms = []
    for i in range(N):
        p = np.dot(P.T, p)
        norms.append(np.linalg.norm(p - p_stationary))
    plt.plot(range(N), norms)
    plt.title(f"Markov Chain for n = {n} and N = {N}")
    plt.show()

markov(5, 50)
markov(10, 50)