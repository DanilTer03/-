import matplotlib.pyplot as plt
import numpy as np

plt.style.use('_mpl-gallery')

#Создание графика двойной спирали, основа для графика взята из библиотеки numpy
n = 50
theta = np.linspace(0, 2*np.pi, n)
x1 = np.cos(theta)
y1 = np.sin(theta)
z1 = np.linspace(0, 1, n)
x2 = np.cos(theta + np.pi)
y2 = np.sin(theta + np.pi)
z2 = z1

# Построение графика
fig, ax = plt.subplots(subplot_kw={"projection": "3d"})

# Заполнение между двумя спиралями
ax.fill_between(x1, y1, z1, x2, y2, z2, alpha=0.5)

# Построение линий спиралей
ax.plot(x1, y1, z1, linewidth=2, color='blue')
ax.plot(x2, y2, z2, linewidth=2, color='red')

# Настройка меток осей
ax.set(xticklabels=[],
       yticklabels=[],
       zticklabels=[])

#Вывод графика
plt.show()