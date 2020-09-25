import math
import random
import matplotlib.pyplot as plt

n = 10  # 2^0 -> 2^n


def est_pi_mc(n):
    random.seed(0)
    pts_in_circle = 0

    for _ in range(n):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)

        if math.sqrt(x**2 + y**2) < 1:
            pts_in_circle += 1

    return 4 * pts_in_circle / n


def est_pi_gl(n):
    # Gregory-Leibniz Series
    pi_est = 0

    for i in range(1, n//2):
        pi_est += 4/(4*i - 3)

    for i in range(1, n-n//2):
        pi_est -= 4/(4*i - 1)

    return pi_est


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


x = []
y_mc = []
y_gl = []
y_ni = []
for i in range(n+1):
    x.append(2**(i))
    y_mc.append((est_pi_mc(2**(i)) - math.pi) / math.pi * 100)
    y_gl.append((est_pi_gl(2**(i)) - math.pi) / math.pi * 100)
    y_ni.append((est_pi_ni(2**(i)) - math.pi) / math.pi * 100)


plt.title("Accuracy Plot of methods for estimating Pi")
plt.xlabel("Number of Iterations")
plt.ylabel("Error from Pi (%)")
plt.plot(x, y_mc, "r")
plt.plot(x, y_gl, "g")
plt.plot(x, y_ni, "b")

plt.legend(["Monte Carlo", "Gregory-Leibniz Series", "Nilakantha Series"])
# plt.legend(["Gregory-Leibniz Series", "Nilakantha Series"])

plt.grid(b=True, which='major', color='#CCCCCC', linestyle='-')

plt.show()
