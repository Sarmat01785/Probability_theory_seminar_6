"""
3. Рост дочерей 175, 167, 154, 174, 178, 148, 160, 167, 169, 170
Рост матерей 178, 165, 165, 173, 168, 155, 160, 164, 178, 175
Используя эти данные построить 95% доверительный интервал для разности среднего роста родителей и детей.
"""
import numpy as np

# Данные
daughters_data = [175, 167, 154, 174, 178, 148, 160, 167, 169, 170]
mothers_data = [178, 165, 165, 173, 168, 155, 160, 164, 178, 175]

daughters_data = np.array(daughters_data)
mothers_data = np.array(mothers_data)

# Среднее значение для дочерей и матерей
daughters_mean = np.mean(daughters_data)
mothers_mean = np.mean(mothers_data)

# Стандартное отклонение для дочерей и матерей
daughters_std = np.std(daughters_data, ddof=1)
mothers_std = np.std(mothers_data, ddof=1)

# Доверительный интервал
t_value = np.abs(np.random.standard_t(df=len(daughters_data) - 1))
interval = t_value * np.sqrt(daughters_std ** 2 + mothers_std ** 2) / np.sqrt(len(daughters_data))

# Границы доверительного интервала
lower_bound = daughters_mean - interval
upper_bound = daughters_mean + interval

print("Доверительный интервал для разности среднего роста родителей и детей:", [lower_bound, upper_bound])
