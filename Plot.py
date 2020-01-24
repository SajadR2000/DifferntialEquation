from matplotlib import pyplot as plt


def painter(xp, yp):
    fig, ax = plt.subplots()
    fig.set_figwidth(18)
    fig.set_figheight(18)
    ax.plot(xp, yp)
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.grid()
    ax.set_title("ODE")
    plt.show()



