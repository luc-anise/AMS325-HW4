import numpy as np
import matplotlib.pyplot as plt

def markov_chain(n, N):
    """A function that takes n and N as input computes the markov chain."""
    
    # Construct a random n-vector with non-negative entries and scale its entries so that the sum is 1. This computation gives us a probability distribution p
    p = np.random.rand(n)
    p = p / np.sum(p)

    # Construct a random n × n (say n = 5) matrix with non-negative entries, and scale the entries so that
    # the sum for each row is 1. This computation gives us a transition matrix P.
    P = np.random.rand(n, n)
    P = P / np.sum(P, axis=1, keepdims=True)

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
    
    # Plot the norms against i.
    plt.plot(range(N), norms)
    plt.title(f"Markov Chain for n = {n} and N = {N}")
    plt.show()
    
    return p

markov_chain(5, 50)
markov_chain(10, 50)
markov_chain(20, 50)
markov_chain(50, 3)

