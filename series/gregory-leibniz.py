import math
n = 10


def est_pi_gl(n):
    # Gregory-Leibniz Series
    pi_est = 0

    for i in range(1, n//2):
        pi_est += 4/(4*i - 3)

    for i in range(1, n-n//2):
        pi_est -= 4/(4*i - 1)

    return pi_est


pi_est = est_pi_gl(n)
print(pi_est)
