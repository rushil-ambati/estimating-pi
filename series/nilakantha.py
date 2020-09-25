import math
n = 10


def est_pi_ni(n):
    # Nikolantha Series
    pi_est = 3
    cur = 2

    for i in range(1, n//2):
        cur = 4*i-2
        pi_est += 4/(cur*(cur+1)*(cur+2))

    for i in range(1, n-n//2):
        cur = 4*i
        pi_est -= 4/(cur*(cur+1)*(cur+2))

    return pi_est


pi_est = est_pi_ni(n)
print(pi_est)
