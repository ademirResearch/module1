import parameters as pmsg
from control.matlab import *
import matplotlib.pyplot as plt

T = []


def test(u):
    input_vector = list(u.array)
    for i in range(1):
        T.append(i)

    num = 1
    den = [pmsg.LD, pmsg.RS]
    sys = TransferFunction(num, den)
    yout, t = step(sys, 1)
    plt.plot(yout)
    plt.show()



