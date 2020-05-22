import numpy as np
from matplotlib import pyplot as plt

for Ly in range(0,100,10):
    L = 12
    Lx = 80
    # Ly = 10
    v0 = 1
    m = np.loadtxt('data'+str(Ly)+'.txt')


    def color_in():
        for i in range(Lx, Lx + L):
            for j in range(Ly, Ly + L):
                m[i, j] = 0


    def stream_plot(m):
        grad = np.gradient(m)
        X, Y = np.meshgrid(np.arange(0, m.shape[0]), np.arange(0, m.shape[1]))
        return plt.streamplot(X, Y, grad[1], grad[0])

    plt.ion()
    color_in()
    plt.matshow(np.transpose(m))
    stream_plot(np.transpose(m))
    plt.ioff()
plt.show()
