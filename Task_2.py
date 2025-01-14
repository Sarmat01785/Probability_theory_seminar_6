"""
В результате 10 независимых измерений некоторой величины X, выполненных с одинаковой точностью, получены опытные данные:
6.9, 6.1, 6.2, 6.8, 7.5, 6.3, 6.4, 6.9, 6.7, 6.1
Предполагая, что результаты измерений подчинены нормальному закону распределения вероятностей,
оценить истинное значение величины X при помощи доверительного интервала,
покрывающего это значение с доверительной вероятностью 0,95.
"""

import numpy as np

# Опытные данные
data = [6.9, 6.1, 6.2, 6.8, 7.5, 6.3, 6.4, 6.9, 6.7, 6.1]

data = np.array(data)

# Среднее значение и стандартное отклонение
mean = np.mean(data)
std = np.std(data, ddof=1)

# Доверительный интервал
t_value = np.abs(np.random.standard_t(df=len(data) - 1))
interval = t_value * std / np.sqrt(len(data))

# Границы доверительного интервала
lower_bound = mean - interval
upper_bound = mean + interval

print("Истинное значение величины X:", mean)
print("Доверительный интервал:", [lower_bound, upper_bound])
