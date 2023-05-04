# Gunicorn под Win не работает
# Для запуска кода:
# cd examples
# gunicorn -w 4 server:app, где 4 - количество потоков, server - имя файла

def hello():
    return b'Hello'


def world():
    return b'World'


urlpatterns = {
    '/hello/': hello, # пути /hello/ соответствует функция hello
    '/world/': world
}


def app(environ, start_response):  # environ выполняет функцию общения между сервером и кодом, это словарь
    path = environ['RAW_URI']
    view_func = urlpatterns.get(path)  # получаем введенный путь
    data = view_func()

    # data = b"Hello, World!\n"   # вывод сообщений обязательно прописывается в бинарном виде
    start_response("200 OK", [
        ("Content-Type", "text/plain"),
        ("Content-Length", str(len(data)))
    ])
    return iter([data])
