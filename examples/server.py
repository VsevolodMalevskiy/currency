def app(environ, start_response):  # environ выполняет функцию общения между сервером и кодом
    data = b"Hello, World!\n"   # вывод сообщений обязательно прописывается в бинарном виде
    start_response("200 OK", [
        ("Content-Type", "text/plain"),
        ("Content-Length", str(len(data)))
    ])
    return iter([data])
