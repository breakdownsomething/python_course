# Успешный ответ от сервера:
# ok\npalm.cpu 10.5 1501864247\neardrum.cpu 15.3 1501864259\n\n
# Если ни одна метрика не удовлетворяет условиям поиска, то вернется ответ:
# ok\n\n

def parse(in_list):

    resp = dict()
    if len(in_list) > 0:
        for cur_line in in_list:
            v = cur_line.split(" ")
            key = v[0]
            cur_val = (int(v[2]), float(v[1]))

            ex_values = resp.get(key)
            if ex_values is not None:
                ex_values.append(cur_val)
            else:
                ex_values = [cur_val]
            resp.update({key: ex_values})
    return resp


data = 'ok\npalm.cpu 10.5 1501864247\npalm.cpu 11.0 1501864999\neardrum.cpu 15.3 1501864259\n\n'
data = 'ok\n\n'

str_values = data.splitlines()
resp = dict()
if str_values[0] == 'ok' and str_values[-1] == '':
    print(parse(str_values[1: -1]))
else:
    raise Exception


# {
#   'palm.cpu': [
#     (1150864247, 0.5),
#     (1150864248, 0.5)
#   ],
#   'eardrum.cpu': [
#     (1150864250, 3.0),
#     (1150864251, 4.0)
#   ],
#   'eardrum.memory': [
#     (1503320872, 4200000.0)
#   ]
# }





