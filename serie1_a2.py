import matplotlib.pyplot as plt
import numpy as np

def f(x,y):
    return np.cos(x) * np.cos(y) * np.cos(x+y)

def grad_X(x,y):
    return -np.cos(y) * np.sin(2*x + y)

def grad_Y(x,y):
    return -np.cos(x) * np.sin(x + 2*y)

X, Y = np.meshgrid(np.linspace(0, 2*np.pi, 256), np.linspace(0, 2*np.pi, 256))
Z = f(X,Y)
U = grad_X(X,Y)
V = grad_Y(X,Y)
levels = np.linspace(np.min(Z), np.max(Z), 15)

fig, ax = plt.subplots()

ax.contour(X, Y, Z, levels=levels)
ax.streamplot(X, Y, U, V)
tick_help = np.linspace(0, 2, 7)
ax.set_xticks(ticks=tick_help * np.pi, labels=[f"{x:.2f} π" for x in tick_help])
ax.set_yticks(ticks=tick_help * np.pi, labels=[f"{x:.2f} π" for x in tick_help])


plt.savefig("plot.pdf")