import math
import random
import matplotlib.pyplot as plt

n = 4  # 2^0 -> 2^n


def est_pi_rm(n, mode="right"):
    # Riemann Sum
    pi_est = 0

    delta_x = 1 / n
    if mode == "right":
        x = 0
    elif mode == "centre":
        x = delta_x/2
    elif mode == "left":
        x = delta_x
    else:
        return "Invalid mode"

    while x < 1:
        f_x = math.sqrt(1 - math.pow(x, 2))
        pi_est += f_x * delta_x
        x += delta_x
    return 4 * pi_est


x = []
y_l = []
y_c = []
y_r = []
for i in range(n+1):
    x.append(math.pow(2, i))
    y_l.append((est_pi_rm(math.pow(2, i), "right") - math.pi) / math.pi * 100)
    y_c.append((est_pi_rm(math.pow(2, i), "centre") - math.pi) / math.pi * 100)
    y_r.append((est_pi_rm(math.pow(2, i), "left") - math.pi) / math.pi * 100)


plt.title("Accuracy Plot of methods for estimating Pi")
plt.xlabel("Number of Iterations")
plt.ylabel("Error from Pi (%)")
plt.plot(x, y_l, "r")
plt.plot(x, y_c, "g")
plt.plot(x, y_r, "b")

plt.legend(["Right Hand Riemann Sum", "Centre Riemann Sum",
            "Left Hand Riemann Sum"])
# plt.legend(["Gregory-Leibniz Series", "Nilakantha Series"])

plt.grid(b=True, which='major', color='#CCCCCC', linestyle='-')

plt.show()
