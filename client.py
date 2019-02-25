import socket
import time


class ClientError(Exception):
    pass


class Client:
    def __init__(self, host, port, timeout=None):
        self._host = host
        self._port = port
        self._timeout = timeout

    def put(self, key, value, timestamp=None):
        if timestamp is None:
            timestamp = int(time.time())
        msg = "put "+str(key)+" "+str(value)+" "+str(timestamp)+"\n"
        with socket.create_connection((self._host, self._port), self._timeout) as sock:
            try:
                sock.sendall(msg.encode("utf8"))
                data = sock.recv(1024)
                print(data.decode("utf8")) #debug
            except socket.error:
                raise ClientError

    def get(self, key):
        msg = "get "+str(key)+"\n"
        with socket.create_connection((self._host, self._port), self._timeout) as sock:
            try:
                sock.sendall(msg.encode("utf8"))
                data = sock.recv(1024)
                print(data.decode("utf8"))  # debug
            except socket.error:
                raise ClientError
        # Успешный ответ от сервера:
        # ok\npalm.cpu 10.5 1501864247\neardrum.cpu 15.3 1501864259\n\n
        # Если ни одна метрика не удовлетворяет условиям поиска, то вернется ответ:
        # ok\n\n
        str_values = data.splitlines()
        if str_values[0] == 'ok' and str_values[-1] == '':
            pass
        else:
            raise ClientError


        resp = dict()
        return resp



# client = Client("127.0.0.1", 8888)
# client.put("palm.cpu", 0.5, timestamp=1150864247)