import inspect
import timeit


def execution_time(number: int = 1000):
    def wrapper(func):
        def inner(*args, **kwargs):
            x = inspect.getsource(func).index('\n')
            return timeit.timeit(stmt=inspect.getsource(func)[x + 1:], number=number)

        return inner

    return wrapper


@execution_time(100000)
def hsg(n: int):
    yield n
    while n > 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        yield n


def len_hail_stone(n: int):
    l = []
    for i in hsg(n):
        l.append(i)
    len_hail = len(l)
    del l
    return len_hail


@execution_time(100000)
class his:
    def __init__(self, n):
        self.n = n

    def __iter__(self):
        self.n = self.n * 2
        return self

    def __next__(self):
        if self.n == 1:
            raise StopIteration("seri is end")
        if self.n % 2 == 0:
            self.n = self.n // 2
        else:
            self.n = 3 * self.n + 1
        if self.n >= 1:
            return self.n
        raise StopIteration("seri is end")


# print('hsg : ', end=" ")
# for i in hsg(3):
#     print(i, end=' ')
# print('\n------------------------------------')
# print("seri len : ", len_hail_stone(3))
# print('------------------------------------')
# print('his : ', end=" ")
# for i in his(3):
#     print(i, end=" ")
# print('\n------------------------------------')
# print(inspect.getsource(his))
# print('\n------------------------------------')
# print(timeit.timeit(stmt=inspect.getsource(his), number=1))
print("his time : ", his(3))
print('\n------------------------------------')
print("hsg time : ", hsg(3))
