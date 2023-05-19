#
# from time import sleep, time
# import threading
# from multiprocessing import Process, Pool, Queue
#
# import requests

# def slow(n):
#     sleep(n)
#
#
# start = time()
#
# th1 = threading.Thread(target=slow, args=[4])  # slow(4)
# th2 = threading.Thread(target=slow, args=[5])
# th3 = threading.Thread(target=slow, kwargs={'n': 6})  # slow(n=6)
#
# th1.start()
# th2.start()
# th3.start()
#
# th1.join()
# th2.join()
# th3.join()
#
# print(f'Execution: {time() - start}')


# def slow(n):
#     sleep(n)
#
#
# start = time()
#
# threads = []
#
# for t in range(1, 11):
#     th1 = threading.Thread(target=slow, args=[t])
#     threads.append(th1)
#     th1.start()
#
#
# for th in threads:
#     th.join()
#
# print(f'Execution: {time() - start}')


# urls = [
#     'https://uk.wikipedia.org/wiki/%D0%93%D0%BE%D0%BB%D0%BE%D0%B2%D0%BD%D0%B0_%D1%81%D1%82%D0%BE%D1%80%D1%96%D0%BD%D0%BA%D0%B0',
#     'https://wiki.nazk.gov.ua/',
#     'https://commons.wikimedia.org/wiki/Main_Page'
# ] * 20
#
# start = time()
#
#
# def foo(url_):
#     response = requests.get(url_)
#     # print(response.status_code)
#     print(threading.current_thread())
#
#
# threads = []
#
# for url in urls:
#     th1 = threading.Thread(target=foo, args=[url])
#     threads.append(th1)
#     th1.start()
#
# for th in threads:
#     th.join()
#
#
# print(f'Execution: {time() - start}')
#
# '''
# GIL - Global Interpreter Lock
# '''
#

# def countdown(n):
#     while n:
#         n -= 1
#
#
# start = time()
# N = 100_000_000
#
# # countdown(N)
#
# if __name__ == '__main__':
#     th1 = Process(target=countdown, args=[500_000_000_000])
#     th2 = Process(target=countdown, args=[500_000_000_000])
#
#     th1.start()
#     th2.start()
#
#     th1.join()
#     th2.join()
#
#     print(f'Execution: {time() - start}')


# urls = [
#     'https://uk.wikipedia.org/wiki/%D0%93%D0%BE%D0%BB%D0%BE%D0%B2%D0%BD%D0%B0_%D1%81%D1%82%D0%BE%D1%80%D1%96%D0%BD%D0%BA%D0%B0',
#     'https://wiki.nazk.gov.ua/',
#     'https://commons.wikimedia.org/wiki/Main_Page'
# ] * 100
#
# start = time()
#
#
# def foo(url_):
#     response = requests.get(url_)
#
# if __name__ == '__main__':
#     with Pool(20) as p:
#         print(p.map(foo, urls))
#
#     print(f'Execution: {time() - start}')


# urls = [
#     'https://uk.wikipedia.org/wiki/%D0%93%D0%BE%D0%BB%D0%BE%D0%B2%D0%BD%D0%B0_%D1%81%D1%82%D0%BE%D1%80%D1%96%D0%BD%D0%BA%D0%B0',
#     'https://wiki.nazk.gov.ua/',
#     'https://commons.wikimedia.org/wiki/Main_Page'
# ] * 50
# que = Queue()
#
# start = time()
#
#
# def foo(queue):
#     while True:
#         u = queue.get()
#         print(f'foo: {u}')
#         if u is None:
#             break
#         response = requests.get(u)
#
#
# if __name__ == '__main__':
#     pr = Process(target=foo, args=[que])
#     pr2 = Process(target=foo, args=[que])
#     pr.start()
#     pr2.start()
#
#     for url in urls:
#         print(f'send to foo: {url}')
#         que.put(url)
#
#     que.put(None)
#     que.put(None)
#
#     pr.join()
#     pr2.join()
#
#     print(f'Execution: {time() - start}')


# import sys
#
# worker_type = sys.argv[1]
#
#
# def slow(n):
#     sleep(n)
#
# if worker_type == 'fork':
#     concurrency_class = Process
# elif worker_type == 'thread':
#     concurrency_class = threading.Thread
#
# print(concurrency_class)
#
# start = time()
#
# if __name__ == '__main__':
#     th1 = concurrency_class(target=slow, args=[4])  # slow(4)
#     th2 = concurrency_class(target=slow, args=[5])
#     th3 = concurrency_class(target=slow, kwargs={'n': 6})  # slow(n=6)
#
#     th1.start()
#     th2.start()
#     th3.start()
#
#     th1.join()
#     th2.join()
#     th3.join()
#
#     print(f'Execution: {time() - start}')
