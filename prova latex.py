# voglio usare latex su un grafico di matplotlib


import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import math

# imposto il font di matplotlib
mpl.rcParams['font.family'] = 'serif'
mpl.rcParams['font.serif'] = 'Times New Roman'

# imposto il font di latex
plt.rcParams['text.usetex'] = True

# stampo sinx / x
x = np.linspace(0, 10 * math.pi, 10000)
y = np.sin(x) / x
plt.plot(x, y)
plt.xlabel(r'$x$')
plt.ylabel(r'$\frac{\sin x}{x}$')
plt.legend([r'$\frac{\sin x}{x}$'])
plt.title(r'$\frac{\sin x}{x}$')
plt.show()
