import pandas as pd
import matplotlib.pyplot as plt

# Загрузка данных из файла flights.csv
data = pd.read_csv('flights.csv')

# Создание словаря для преобразования названий месяцев в числовые значения
month_mapping = {
    'January': 1,
    'February': 2,
    'March': 3,
    'April': 4,
    'May': 5,
    'June': 6,
    'July': 7,
    'August': 8,
    'September': 9,
    'October': 10,
    'November': 11,
    'December': 12
}

# Преобразование названий месяцев в числовые значения
data['month'] = data['month'].map(month_mapping)

# Объединяем год и месяц для создания даты
data['date'] = pd.to_datetime(data[['year', 'month']].assign(Day=1))

# Построение графика
plt.plot(data['date'], data['passengers'], marker='o')

# Настройка заголовка и подписей осей
plt.title('Количество пассажиров в месяц')
plt.xlabel('Дата')
plt.ylabel('Количество пассажиров')

# Показать график с сеткой
plt.grid()
plt.show()
