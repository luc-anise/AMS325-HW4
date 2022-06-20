""" The Mandelbrot set is the set of complex numbers c for which the function fc(z) = z
2+c does not diverge
when iterated from z = 0. In other words, the sequence fc(0), fc(fc(0)), etc. remains bounded in absolute
value. In this task, you will write a Python script mandelbrot.py to compute the Mandelbrot fractal with the
following Mandelbrot iteration on each point: """

# . construct an n×n grid (2D array) of points (x, y) in range [−2, 1]×[−1.5, 1.5] (e.g., using numpy.meshgrid)
# and corresponding complex values c = x + yi (note that the imaginary unit in Python is 1j);
import numpy as np
grid = np.meshgrid(np.linspace(-2, 1, 100), np.linspace(-1.5, 1.5, 100))
print(grid[1][1])