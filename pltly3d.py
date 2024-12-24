import plotly.graph_objects as go
import numpy as np

# Создание данных для двойной спирали
n = 50
theta = np.linspace(0, 2 * np.pi, n)
x1 = np.cos(theta)
y1 = np.sin(theta)
z1 = np.linspace(0, 1, n)
x2 = np.cos(theta + np.pi)
y2 = np.sin(theta + np.pi)
z2 = z1

# Создание графика
fig = go.Figure()

# Добавление спиралей
fig.add_trace(go.Scatter3d(x=x1, y=y1, z=z1, mode='lines',
                           line=dict(color='blue', width=2),
                           name='Spiral 1'))
fig.add_trace(go.Scatter3d(x=x2, y=y2, z=z2, mode='lines',
                           line=dict(color='red', width=2),
                           name='Spiral 2'))

# Заполнение между спиралями, передаем двумерные массивы для координат x, y и z,
# чтобы создать поверхность между спиралями.
x_surface = np.array([x1, x2])
y_surface = np.array([y1, y2])
z_surface = np.array([z1, z2])

#Создание поверхности
fig.add_trace(go.Surface(x=x_surface, y=y_surface, z=z_surface,
                         opacity=0.5, colorscale='Blues', showscale=False))

# Настройка осей
fig.update_layout(scene=dict(xaxis=dict(showticklabels=False),
                            yaxis=dict(showticklabels=False),
                            zaxis=dict(showticklabels=False)),
                  title='Двойная спираль')

fig.show()

# import plotly.graph_objects as go
# import numpy as np
# import pandas as pd
#
# # Загрузка данных о высотах
# # Предположим, что у вас есть файл 'everest_elevation.csv' с колонками 'latitude', 'longitude', 'elevation'
# data = pd.read_csv('everest_elevation.csv')
#
# # Извлечение координат и высот
# latitudes = data['latitude']
# longitudes = data['longitude']
# elevations = data['elevation']
#
# # Создание 3D графика
# fig = go.Figure(data=[go.Scatter3d(
#     x=longitudes,
#     y=latitudes,
#     z=elevations,
#     mode='markers',
#     marker=dict(
#         size=2,
#         color=elevations,  # Цвет по высоте
#         colorscale='Viridis',
#         colorbar=dict(title='Elevation (m)'),
#         opacity=0.8
#     )
# )])
#
# # Настройка осей
# fig.update_layout(
#     scene=dict(
#         xaxis_title='Longitude',
#         yaxis_title='Latitude',
#         zaxis_title='Elevation (m)',
#     ),
#     title='3D Map of Mount Everest'
# )
#
# fig.show()