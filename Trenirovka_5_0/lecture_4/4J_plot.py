# Визуализация для данных в задаче j

import matplotlib.pyplot as plt
import numpy as np


def solve():
    cnt, _ = input().split()
    xs = []
    ys = []


    for _ in range(int(cnt) + 1):
        x, y = map(float, input().split())
        xs.append(x)
        ys.append(y)

    plt.plot(np.array(xs), np.array(ys))
    plt.show()


solve()
