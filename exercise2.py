# **Упражнение 2:**<br/>Написать функцию с валидацией входных данных и генерацией исключений
#
#**Задание:**<br/>
#Создать функцию **`validate_user_input(data)`**, которая принимает словарь с данными пользователя.<br/>
#Функция должна проверять наличие и корректность ключей **`name`** (строка) и **`age`** (положительное число).<br/>
#В случае некорректных данных генерировать соответствующие исключения.
#
#**Пошаговая инструкция:**
#- Создайте функцию **`validate_user_input(data)`**.
#- Проверьте, что data является словарем.<br/>Если нет, вызовите **`TypeError`**.
#- Проверьте, что ключ name присутствует в словаре и его значение является строкой.<br/>Если нет, вызовите **`ValueError`**.
#- Проверьте, что ключ **`age`** присутствует в словаре и его значение является положительным числом.<br/>Если нет, вызовите **`ValueError`**.
#- Используйте ключевое слово **`from`**, чтобы создать цепочку исключений, если это необходимо.
#
#**Проверка:**
#- Протестируйте функцию с корректными данными, например, **`{"name": "Alice", "age": 30}`**.
#- Протестируйте функцию с отсутствующим ключом **`name`**.
#- Протестируйте функцию с некорректным значением для **`age`**<br/>(**например, строкой или отрицательным числом**).
#- Протестируйте функцию с некорректным типом входных данных<br/>(**например, строкой вместо словаря**).


from datetime import datetime
import logging

logging.basicConfig(
    level=logging.ERROR,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

SPLIT_LINE = "\n" + "#" * 100 + "\n"

class MyValidationException(Exception):
  pass

def validate_user_input(data):
  if not isinstance(data, dict):
    raise TypeError("Входные данные должны быть словарем")
  if "name" not in data or not isinstance(data["name"], str):
    raise ValueError("Ключ \"name\" должен быть строкой")
  if "age" not in data or not isinstance(data["age"], int) or data["age"] <= 0:
    raise ValueError("Ключ \"age\" должен быть целым положительным числом")

def test_validate_user_input(message: str, data):
  """Из соображений DRYS принял решение обернуть вызов validate_user_input в отдельную функцию,
     чтобы не дублировать обработку исключений в каждом тесте.
  """
  try:
    print(message)
    validate_user_input(data)
  except Exception as e:
    raise MyValidationException(f"Некорректное введённое значение:\n{"-"*50}\n{data}\n{"-"*50}") from e
  else:
    print("Валидация прошла успешно")

#####################################################

try:
  test_validate_user_input("1. Тестируем с корректными данными:", {"name": "John", "age": 30})
except Exception as e:
  logging.exception(e)

print(SPLIT_LINE)

#####################################################

try:
  test_validate_user_input("2. Тестируем с отсутствующим ключом name:", {"age": 30})
except Exception as e:
  logging.exception(e)

print(SPLIT_LINE)

#####################################################

try:
  test_validate_user_input("3. Тестируем с некорректным значением для age:", {"name": "John", "age": -5})
except Exception as e:
  logging.exception(e)

print(SPLIT_LINE)

#####################################################

try:
  test_validate_user_input("4. Тестируем с некорректным типом входных данных:", "Lorem-ipsum-dolor-sit-amet")
except Exception as e:
  logging.exception(e)

print(SPLIT_LINE)

#####################################################

print(f"\n{"="*50}\nFinished at: {datetime.now():%Y-%m-%d %H:%M:%S}\n\n")