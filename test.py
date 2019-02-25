# Успешный ответ от сервера:
# ok\npalm.cpu 10.5 1501864247\neardrum.cpu 15.3 1501864259\n\n
# Если ни одна метрика не удовлетворяет условиям поиска, то вернется ответ:
# ok\n\n

data = 'ok\npalm.cpu 10.5 1501864247\neardrum.cpu 15.3 1501864259\n\n'
str_values = data.splitlines()
resp = dict()
if str_values[0] == 'ok' and str_values[-1] == '':
    for

    print(str_values)
else:
    raise Exception








