import matplotlib.pyplot as plt
import numpy as np

# Definir la función paramétrica para un corazón
t = np.linspace(0, 2 * np.pi, 1000)
x = 16 * np.sin(t)**3
y = 13 * np.cos(t) - 5 * np.cos(2*t) - 2 * np.cos(3*t) - np.cos(4*t)

# Crear el gráfico
plt.figure(figsize=(8, 6))
plt.plot(x, y, color='red')
plt.fill(x, y, color='pink', alpha=0.5)

# Personalizar el gráfico
plt.title("para ti <3", fontsize=20)
plt.xlabel("Eje X", fontsize=15)
plt.ylabel("Eje Y", fontsize=15)
plt.axis('equal')
plt.grid(True)
plt.gca().set_facecolor('lightyellow')

# Mostrar el gráfico
plt.show()
