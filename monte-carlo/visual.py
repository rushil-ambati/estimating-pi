import math
import random
import matplotlib.pyplot as plt

n = 150
pi = math.pi


random.seed(0)


def monte_carlo(n):
    in_circle_x = []
    in_circle_y = []

    out_circle_x = []
    out_circle_y = []

    for _ in range(n):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)

        if math.sqrt(x**2 + y**2) < 1:
            in_circle_x.append(x)
            in_circle_y.append(y)
        else:
            out_circle_x.append(x)
            out_circle_y.append(y)

    return in_circle_x, in_circle_y, out_circle_x, out_circle_y


in_circle_x, in_circle_y, out_circle_x, out_circle_y = monte_carlo(n)

print("in_circle: " + str(len(in_circle_x)))
print("all: " + str(len(in_circle_x) + len(out_circle_x)))

pi_est = 4 * len(in_circle_x)/(len(in_circle_x) + len(out_circle_x))
print("pi: " + str(pi_est))
print("err: " + str(round(((pi_est - pi)/pi * 100), 3)) + "% (3 s.f.)")

plt.ylim(-2, 2)
plt.xlim(-2, 2)

draw_circle = plt.Circle((0, 0), 1, fill=False, fc="red")
plt.gcf().gca().add_artist(draw_circle)

square = plt.Rectangle((-1, -1), 2, 2, fill=False, ec="blue")
plt.gca().add_patch(square)

plt.scatter(in_circle_x, in_circle_y, c="r")
plt.scatter(out_circle_x, out_circle_y, c="b")

plt.savefig('visual_150.png')
plt.show()
