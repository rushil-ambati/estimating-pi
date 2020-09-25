import math
import random

random.seed(0)

n = 50
n_c = 0
for _ in range(n):
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)

    if math.sqrt(x**2 + y**2) < 1:
        n_c += 1

    print(str(4 * (n_c / n)))
