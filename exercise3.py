# Упражнение 3:
# Написать класс собственного исключения и использовать его в примере кода:
#
# Задание:
# Создать класс NegativeNumberError, который будет генерироваться, если переданное число отрицательное.
# Использовать это исключение в функции check_positive_number.
#
# Пошаговая инструкция:
# - Создайте класс NegativeNumberError, наследующий от Exception.
# - Переопределите конструктор, чтобы принимать значение числа и сообщение об ошибке.
# - Переопределите метод __str__, чтобы возвращать информативное сообщение.
# - Создайте функцию check_positive_number, которая проверяет, является ли число положительным.
#   Если число отрицательное, функция должна вызывать исключение NegativeNumberError.
#
# Проверка:
# - Протестируйте функцию с отрицательным числом.
# - Протестируйте функцию с положительным числом.
# - Убедитесь, что исключение NegativeNumberError правильно обрабатывается и выводит информативное сообщение.

from datetime import datetime
import logging

logging.basicConfig(
    level=logging.ERROR,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

SPLIT_LINE = "\n" + "#" * 100 + "\n"

class NegativeNumberError(Exception):

  def __init__(self, value, message="Число не должно быть отрицательным"):
    self.value = value
    self.message = message
    super().__init__(self.message)

  def __str__(self):
    return f"{self.message}: {self.value}"


def check_positive_number(number: float) -> bool:
  """
  Проверяет, является ли число положительным.
  Если число отрицательное, вызывает исключение NegativeNumberError.
  """
  if number < 0:
    raise NegativeNumberError(number)
  return True

#####################################################

try:
  print("1. Тестируем с положительным числом:")
  result = check_positive_number(10)
  print(f"\tРезультат: {result}")
except NegativeNumberError as e:
  logging.exception(e)

print(SPLIT_LINE)

#####################################################

try:
  print("2. Тестируем с отрицательным числом:")
  result = check_positive_number(-5)
  print(f"\tРезультат: {result}")
except NegativeNumberError as e:
  logging.exception(e)

print(SPLIT_LINE)

#####################################################

print(f"\n{'='*50}\nFinished at: {datetime.now():%Y-%m-%d %H:%M:%S}\n\n")
