import sys
import numpy as np

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def Func(x, y):
    return x - y + 2.0 * pow(x, 2) + 2 * x * y + pow(y, 2)


def PxFunc(x, y):
    return 1 + 4.0 * x + 2 * y


def PyFunc(x, y):
    return - 1 + 2 * x + 2 * y


if __name__ == '__main__':

    X, Y = np.mgrid[-2:2:40j, -2:2:40j]
    Z = Func(X, Y)

    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='rainbow')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')

    # Gradient descent
    step = 0.0008
    x = 0
    y = 0
    tag_x = [x]
    tag_y = [y]
    tag_z = [Func(x, y)]

    next_x = x
    next_y = y
    Over = False

    while Over == False:
        next_x -= step * PxFunc(x, y)
        next_y -= step * PyFunc(x, y)
        if Func(x, y) - Func(next_x, next_y) < sys.float_info.min:
            Over = True
        x = next_x
        y = next_y

        tag_x.append(x)
        tag_y.append(y)
        tag_z.append(Func(x, y))

    print(x, y, Func(x, y))
    ax.plot(tag_x, tag_y, tag_z, 'r')
    plt.title('(x, y)~{' + str(x) + ',' + str(y) + ')')
    plt.show()
