import numpy as np
import random
from numba import njit, prange

@njit
def approx_pi(N):
    M = 0
    for i in range(N):
        # Simulate impact coordinates
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)

        # True if impact happens inside the circle
        if np.sqrt(x**2 + y**2) <= 1.0:
            M += 1

    #print('pi estimate {}'.format(4*M/N))
    return 4*M/N 

approx_pi(10**7)
