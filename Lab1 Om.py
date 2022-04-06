import cmath
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

fig, ax = plt.subplots()
#ax.set_xlim(())
#ax.set_ylim(())
ax.grid()

# uslovie

x = np.linspace(-0.5, 0.5, 10000)
b = -100j
uslovie = np.exp(b * x)

# Graf

# amplituda
#y = abs(uslovie)
#ax.set_title("Амплитуда условия")

# faza
y = [cmath.phase(x) for x in uslovie]
plt.title("Фаза условия")

# Численый расчет 10 вариант



# VVod result

ax.plot(x, y)
plt.show()
