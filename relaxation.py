import numpy as np
from matplotlib import pyplot as plt


def init():
    global v0
    global L
    global Lx
    global Ly
    L = 12
    Lx = 80
    # Ly = 60
    v0 = 1
    stm = np.zeros([120, 120])
    stm[-1, :] = v0
    stm[0, int(np.floor(stm.shape[0] / 4)): int(np.floor(3 * stm.shape[0] / 4))] = - v0 / 2
    return stm


def edge_correct(newm):
    newm[0, 0:int(np.floor(newm.shape[0] / 4))] = newm[1, 0:int(np.floor(newm.shape[0] / 4))]
    newm[0, int(np.floor(3 * newm.shape[0] / 4)):] = newm[1, int(np.floor(3 * newm.shape[0] / 4)):]
    newm[0, int(np.floor(newm.shape[0] / 4)): int(np.floor(3 * newm.shape[0] / 4))] = newm[1, int(
        np.floor(newm.shape[0] / 4)): int(np.floor(3 * newm.shape[0] / 4))] - v0 / 2
    newm[-1, :] = newm[-2, :] + v0
    newm[:, 0] = newm[:, 1]
    newm[:, -1] = newm[:, -2]
    newm[Lx, Ly:Ly + L + 1] = newm[Lx - 1, Ly:Ly + L + 1]
    newm[Lx + L, Ly:Ly + L + 1] = newm[Lx + L + 1, Ly:Ly + L + 1]
    newm[Lx + 1:Lx + L, Ly] = newm[Lx + 1:Lx + L, Ly - 1]
    newm[Lx + 1:Lx + L, Ly + L] = newm[Lx + 1:Lx + L, Ly + L + 1]
    newm = np.subtract(newm, np.average(newm))
    return newm


def step(stm):
    newm = np.copy(stm)
    for i in range(1, stm.shape[0] - 1):
        for j in range(1, stm.shape[1] - 1):
            newm[i, j] = (stm[i, j + 1] + stm[i + 1, j] + stm[i - 1, j] + stm[i, j - 1]) / 4
    newm = edge_correct(newm)
    return newm

    # if i==0 and j==0:
    #     pass
    # elif i==0 and j==stm.shape[1]:
    #     pass
    # elif i==stm.shape[0] and j==0:
    #     pass
    # elif i==stm.shape[0] and j==stm.shape[1]:
    #     pass
    # elif i==0 and j!=0 and j!=stm.shape[1]:
    #     pass
    # elif i==stm.shape[0] and j!=0 and j!=stm.shape[1]:
    #     pass
    # elif j==0 and i!=0 and i!=stm.shape[1]:
    #     pass
    # elif j==stm.shape[1] and i!=0 and i!=stm.shape[1]:
    #     pass
    # else:
    #     pass

for Ly in range(0,100,10):
    m = init()
    for l in range(1000):
        m = step(m)
    np.savetxt('data'+str(Ly)+'.txt', m)
