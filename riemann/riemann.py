import math
n = 10


def est_pi_rm(n, mode="right"):
    # Riemann Sum
    pi_est = 0

    delta_x = 1 / n
    if mode == "right":
        x = 0
    elif mode == "mid":
        x = delta_x/2
    elif mode == "left":
        x = delta_x

    while x < 1:
        f_x = math.sqrt(1 - math.pow(x, 2))
        pi_est += f_x * delta_x
        x += delta_x
    return 4 * pi_est


pi_est = est_pi_rm(n, "centre")
print(pi_est)
