from fake_math import divide as fake_divide
from true_math import divide as true_divide

# Вызываем функции с аргументами
result_fake = fake_divide(10, 0)
result_true = true_divide(10, 0)

# Выводим результаты на экран
print(f"Результат fake_divide: {result_fake}")
print(f"Результат true_divide: {result_true}")
