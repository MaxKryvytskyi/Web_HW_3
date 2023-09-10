# from threading import Thread
# import logging
# from time import sleep


# class MyThread(Thread):
#     def __init__(self, group=None, target=None, name=None, args=(), kwargs=None, *, daemon=None):
#         super().__init__(group=group, target=target, name=name, daemon=daemon)
#         self.args = args
#         self.kwargs = kwargs

#     def run(self) -> None:
#         sleep(2)
#         logging.debug('Wake up!')
#         logging.debug(f"args: {self.args}")


# if __name__ == '__main__':
#     logging.basicConfig(level=logging.DEBUG, format='%(threadName)s %(message)s')
#     for i in range(10):
#         thread = MyThread(args=(f"Count thread - {i}",))
#         thread.start()
#     print('Usefull message')



# from threading import Thread
# from time import sleep
# import logging


# class UsefulClass():
#     def __init__(self, second_num):
#         self.delay = second_num

#     def __call__(self):
#         sleep(self.delay)
#         logging.debug('Wake up!')


# if __name__ == '__main__':
#     logging.basicConfig(level=logging.DEBUG, format='%(threadName)s %(message)s')
#     for i in range(10):
#         t2 = UsefulClass(i)
#         thread = Thread(target=t2)
#         thread.start()
#     print('Some stuff')

# from threading import Thread
# from time import sleep
# import logging


# def example_work(delay):
#     sleep(delay)
#     logging.debug('Wake up!')


# if __name__ == '__main__':
#     logging.basicConfig(level=logging.DEBUG, format='%(threadName)s %(message)s')
#     for i in range(5):
#         thread = Thread(target=example_work, args=(i,))
#         thread.start()


# from threading import Thread
# import logging
# from time import sleep


# def example_work(params):
#     sleep(params)
#     logging.debug('Wake up!')


# if __name__ == '__main__':
#     logging.basicConfig(level=logging.DEBUG, format='%(threadName)s %(message)s')
#     logging.debug('Start program')
#     threads = []
#     for i in range(5):
#         thread = Thread(target=example_work, args=(i,))
#         thread.start()
#         threads.append(thread)

#     [el.join() for el in threads]

#     logging.debug('End program')



# from threading import Thread
# from time import sleep
# import logging


# class UsefulClass:
#     def __init__(self, second_num):
#         self.delay = second_num

#     def __call__(self):
#         sleep(self.delay)
#         logging.debug('Wake up!')


# if __name__ == '__main__':
#     logging.basicConfig(level=logging.DEBUG, format='%(threadName)s %(message)s')
#     t2 = UsefulClass(2)
#     thread = Thread(target=t2)
#     thread_locking = Thread(target=t2)

#     thread.start()
#     print(thread.is_alive(), thread_locking.is_alive())
#     thread_locking.start()
#     thread.join()
#     thread_locking.join()
#     print(thread.is_alive(), thread_locking.is_alive())
#     print('After all...')



# from threading import Timer
# import logging
# from time import sleep


# def example_work():
#     logging.debug('Start!')


# if __name__ == '__main__':
#     logging.basicConfig(level=logging.DEBUG, format='%(threadName)s %(message)s')

#     first = Timer(0.5, example_work)
#     first.name = 'First thread'
#     second = Timer(0.7, example_work)
#     second.name = 'Second thread'
#     logging.debug('Start timers')
#     first.start()
#     second.start()
#     sleep(0.7)
#     second.cancel()

#     logging.debug('End program')


# from threading import Thread, RLock
# import logging
# from time import time, sleep

# lock = RLock()


# def func(locker, delay):
#     timer = time()
#     locker.acquire()
#     sleep(delay)
#     locker.release()
#     logging.debug(f'Done {time() - timer}')


# if __name__ == '__main__':
#     logging.basicConfig(level=logging.DEBUG, format='%(threadName)s %(message)s')
#     t1 = Thread(target=func, args=(lock, 2))
#     t2 = Thread(target=func, args=(lock, 2))
#     t1.start()
#     t2.start()
#     logging.debug('Started')



# from threading import Thread, RLock
# import logging
# from time import time, sleep

# lock = RLock()


# def func(locker, delay):
#     timer = time()
#     with locker:
#         sleep(delay)
#     logging.debug(f'Done {time() - timer}')


# if __name__ == '__main__':
#     logging.basicConfig(level=logging.DEBUG, format='%(threadName)s %(message)s')
#     t1 = Thread(target=func, args=(lock, 2))
#     t2 = Thread(target=func, args=(lock, 2))
#     t1.start()
#     t2.start()
#     logging.debug('Started')


# from threading import Semaphore, Thread
# import logging
# from time import sleep


# def worker(condition):
#     with condition:
#         logging.debug(f'Got semaphore')
#         sleep(1)
#         logging.debug(f'finished')


# if __name__ == '__main__':
#     logging.basicConfig(level=logging.DEBUG, format='%(threadName)s %(message)s')
#     pool = Semaphore(1000)
#     for num in range(10000):
#         thread = Thread(name=f'Th-{num}', target=worker, args=(pool, ))
#         thread.start()



# from threading import Thread, Condition
# import logging
# from time import sleep


# def worker(condition: Condition):
#     logging.debug('Worker ready to work')
#     with condition:
#         condition.wait()
#         logging.debug('The worker can do the work')


# def master(condition: Condition):
#     logging.debug('Master doing some work')
#     sleep(2)
#     with condition:
#         logging.debug('Informing that workers can do the work')
#         condition.notify_all()


# if __name__ == '__main__':
#     logging.basicConfig(level=logging.DEBUG, format='%(threadName)s %(message)s')
#     condition = Condition()
#     master = Thread(name='master', target=master, args=(condition,))

#     worker_one = Thread(name='worker_one', target=worker, args=(condition, ))
#     worker_two = Thread(name='worker_two', target=worker, args=(condition,))
#     worker_tre = Thread(name='worker_tre', target=worker, args=(condition,))
#     worker_one.start()
#     worker_two.start()
#     worker_tre.start()
#     master.start()

#     logging.debug('End program')


from threading import Thread, Event
import logging
from time import sleep


# def worker(event: Event):
#     logging.debug('Worker ready to work')
#     event.wait()
#     logging.debug('The worker can do the work')


# def master(event: Event):
#     logging.debug('Master doing some work')
#     sleep(2)
#     logging.debug('Informing that workers can do the work')
#     event.set()


# if __name__ == '__main__':
#     logging.basicConfig(level=logging.DEBUG, format='%(threadName)s %(message)s')
#     event = Event()
#     master = Thread(name='master', target=master, args=(event, ))

#     worker_one = Thread(name='worker_one', target=worker, args=(event, ))
#     worker_two = Thread(name='worker_two', target=worker, args=(event,))
#     worker_one.start()
#     worker_two.start()
#     master.start()

#     logging.debug('End program')

# from random import randint
# from threading import Thread, Barrier
# import logging
# from time import sleep, ctime


# def worker(barrier: Barrier):
#     logging.debug(f'Start thread: {ctime()}')
#     sleep(randint(1, 3))  # Simulate some work
#     r = barrier.wait()
#     logging.debug(f'count: {r}')
#     logging.debug(f'Barrier overcome: {ctime()}')


# if __name__ == '__main__':
#     logging.basicConfig(level=logging.DEBUG, format='%(threadName)s %(message)s')
#     barrier = Barrier(5)

#     for num in range(10):
#         thread = Thread(name=f'Th-{num}', target=worker, args=(barrier, ))
#         thread.start()



import concurrent.futures
import logging
from random import randint
from time import sleep


def greeting(name):
    logging.debug(f'greeting for: {name}')
    sleep(randint(0, 3))
    return f"Hello {name}"


arguments = (
    "Bill",
    "Jill",
    "Till",
    "Sam",
    "Tom",
    "John",
)

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, format='%(threadName)s %(message)s')
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        results = list(executor.map(greeting, arguments))

    logging.debug(results)