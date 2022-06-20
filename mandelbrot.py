import numpy as np
import matplotlib.pyplot as plt

plt.close('all')

def madelbrot(n=1000, N_max=50, threshold=50):
    """A function that takes n, N_max and threshold as input computes the madelbrot set."""
    # construct an n×n grid (2D array) of points (x, y) in range [−2, 1]×[−1.5, 1.5] (e.g., using numpy.meshgrid)
    # and corresponding complex values c = x + yi (note that the imaginary unit in Python is 1j);
    grid = np.meshgrid(np.linspace(-2, 1, n), np.linspace(-1.5, 1.5, n))

    #  corresponding complex values c = x + yi (note that the imaginary unit in Python is 1j);
    c = grid[0] + 1j * grid[1]

    # initialize the array z to have the same shape as c
    z = np.zeros(c.shape, dtype=complex)
    
    # caculate the Mandelbrot set using the formula z = z^2 + c
    # and store the result in the array z
    for i in range(N_max):
        z = z**2 + c
    #  form a 2-D boolean array mask indicating which points are in the set (i.e., |z| < threshoold);
    mask = np.abs(z) < threshold

    # plot the Mandelbrot set using matplotlib.pyplot.imshow
    plt.imshow(mask.T, extent=[-2, 1, -1.5 ,1.5])
    plt.gray()
    plt.show()
    plt.savefig('mandelbrot.png')
    return z



madelbrot(1000, 50, 50)
