import numpy as np
from matplotlib import pyplot as plt

x = np.linspace(-3, 3, 200)
y = x*(x + 2)*(x - 2)

fig, ax = plt.subplots()

ax.plot(x, y)

plt.show()

fig.savefig('мой график')