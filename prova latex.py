# voglio usare latex su un grafico di matplotlib


import numpy as np
import matplotlib.pyplot as plt

import math

### PER FAR FUNZIONARE LATEX IN MATPLOTLIB USARE QUESTO CODICE ###

import matplotlib as mpl
# imposto il font di matplotlib
mpl.rcParams['font.family'] = 'serif'
mpl.rcParams['font.serif'] = 'Times New Roman'

# imposto il font di latex
plt.rcParams['text.usetex'] = True

### FINE CODICE PER LATEX ###

# voglio fare un grafico 3d con distribuzione gaussiana

# creo un array di 100 punti equispaziati tra -5 e 5
x = np.linspace(-5, 5, 1000)
y = np.linspace(-5, 5, 1000)

# creo una griglia di punti
X, Y = np.meshgrid(x, y)


# creo una funzione gaussiana
Z = np.exp(-(X**2 + Y**2))

# creo il grafico
fig, ax = plt.subplots(1, 1, figsize=(10, 10))
plt.figure(facecolor='gray')
ax.facecolor = 'gray'
ax.contourf(X, Y, Z, 100, cmap='jet')
ax.set_xlabel(r'$x$', fontsize=20, labelpad=10, color='red')
ax.set_ylabel(r'$y$')
# e^(x^2 + y^2)
ax.set_title(r'$e^{(x^2 + y^2)}$', fontsize=40)
plt.tight_layout()
plt.show()