# Gunicorn под Win не работает
# https://gunicorn.org
# Для запуска кода:
# cd examples
# gunicorn -w 4 server:app, где 4 - количество потоков, server - имя файла
# или возможен запуск через внутренний wsgi-,  а не runserver, но runserver запускает только один worker
# cd ..
# cd app
# gunicorn -w 4 settings.wsgi
# для запуска 4 процессов и 4 потоков в каждом:
# gunicorn --workers 4 --threads 4 settings.wsgi
# если необходимо через время убивать неиспользованный процесс (по умолчанию 30 секунд):
# gunicorn --workers 4 --threads 4 settings.wsgi --timeout 10
# если необходимо ограничить количество запросов (по умолчанию 1 запрос):
# gunicorn --workers 4 --threads 4 settings.wsgi --timeout 10 --max-requests 2
# если необходимо отслеживать логи (notset, debug, info, warning, error, critical - уровни логов (debug - все логи):
# gunicorn --workers 4 --threads 4 settings.wsgi --timeout 10 --log-level debug

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

    if not view_func:  # если путь не введен, а введен  http://127.0.0.1:8000/
        data = b'Not Found'
        start_response("404 Not Found", [
            ("Content-Type", "text/plain"),
            ("Content-Length", str(len(data)))
        ])
        return iter([data])

    data = view_func()
    # data = b"Hello, World!\n"   # вывод сообщений обязательно прописывается в бинарном виде
    start_response("200 OK", [
        ("Content-Type", "text/plain"),
        ("Content-Length", str(len(data)))
    ])
    return iter([data])
