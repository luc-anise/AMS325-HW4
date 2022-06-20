# import numpi as np
import numpy as np
# construct an n×n grid (2D array) of points (x, y) in range [−2, 1]×[−1.5, 1.5] (e.g., using numpy.meshgrid)
grid = np.meshgrid(np.linspace(-2, 1, 100), np.linspace(-1.5, 1.5, 100))

 #and corresponding complex values c = x + yi (note that the imaginary unit in Python is 1j);
# perform the iteration as outlined above to compute z for each complex value in the grid;
# store the result in a 2D array (the same shape as c)
mask = np.zeros(grid.shape)
for  x, y in zip(grid[0], grid[1]):
    c = x + y * 1j
    z = 0
    N_max = 50
    threshold = 50
    for n in range(N_max):
        z = z**2 + c
        if abs(z) > threshold:
            mask[n] = 1
            break
# form a 2-D boolean array mask indicating which points are in the set (i.e., |z| < threshoold)
mask = np.abs(z) < threshold

# import matplotlib.pyplot as plt
import matplotlib.pyplot as plt

# plot the grid and the mask
plt.imshow(mask, extent=[-2, 1, -1.5, 1.5], cmap='gray')
plt.gray()
plt.show()

""" # organize the statements into a function that takes n, N_max, and threshold as input, add docstring and comments to the function, and experiment the function with different n so that you get an image resembling the one above.
def mandelbrot(n, N_max, threshold):
    grid = np.meshgrid(np.linspace(-2, 1, n), np.linspace(-1.5, 1.5, n))
    c = grid[0] + grid[1] * 1j
    z = 0
    for j in range (N_max ) :
        z = z**2 + c
    mask = np.abs(z) < threshold
    return mask """
