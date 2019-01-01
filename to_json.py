# Чтобы передавать данные между функциями, модулями или
#  разными системами используются форматы данных. Одним
#   из самых популярных форматов является JSON. Напишите
#    декоратор to_json, который можно применить к различным
#     функциям, чтобы преобразовывать их возвращаемое значение
#      в JSON-формат. Не забудьте про сохранение корректного
#       имени декорируемой функции.


import json
import functools

def to_json(func):
    @functools.wraps(func)
    def wrapped(*args, **kwargs):
        result = func(*args, **kwargs)
        return json.dumps(result)
    return wrapped


@to_json
def get_data():
  return {
    'data': 42
  }
  
get_data()  # вернёт '{"data": 42}'