import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
'''Seaborn в основном используется для создания статических графиков, 
и он не поддерживает 3D-графики напрямую.Однако, можно использовать 
Matplotlib в сочетании с Seaborn для стилизации.'''
# Создание данных для двойной спирали
n = 50
theta = np.linspace(0, 2 * np.pi, n)
x1 = np.cos(theta)
y1 = np.sin(theta)
z1 = np.linspace(0, 1, n)
x2 = np.cos(theta + np.pi)
y2 = np.sin(theta + np.pi)
z2 = z1

# Настройка стиля Seaborn
sns.set(style="whitegrid")

# Построение графика
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Заполнение между двумя спиралями
ax.plot_surface(np.array([x1, x2]),
                np.array([y1, y2]),
                np.array([z1, z2]), alpha=0.5)

# Построение линий спиралей
ax.plot(x1, y1, z1, linewidth=2, color='C0')
ax.plot(x2, y2, z2, linewidth=2, color='C1')

# Настройка меток осей
ax.set(xticklabels=[], yticklabels=[], zticklabels=[])

plt.show()