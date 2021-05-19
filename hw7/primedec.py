import os


def remainder(n=None):
    def wrapper(func):
        def inner(*arg, **kwarg):
            if n == None:
                num = int(input("Enter a number for mod : "))
                return func(*arg, **kwarg) % num
            return func(*arg, **kwarg) % n

        return inner

    return wrapper


def string_p(func):
    def inner(*arg, **kwargs):
        dic = {0: '', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven',
               8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen',
               14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen',
               19: 'nineteen', 20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty',
               70: 'seventy', 80: 'eighty', 90: 'ninety', 100: 'one hundred', 200: 'two hundred',
               300: 'three hundred', 400: 'four hundred', 500: 'five hundred', 600: 'six hundred',
               700: 'seven hundred', 800: 'eight hundred', 900: 'nine hundred', 1000: 'one thousand',
               2000: 'two thousand', 3000: 'three thousand', 4000: 'four thousand', 5000: 'five thousand'
               }
        l = []
        n = func(*arg, **kwargs)
        if n == 0:
            return 'the result is zero'
        x = 1
        if (n % 100) < 20:
            x = 100
            l.insert(0, n % x)
            n -= n % x
        while n > 0:
            x *= 10
            l.insert(0, n % x)
            n -= n % x
        s = ''
        for i in l:
            s = s + dic[i]
            s += ' '
        s = 'the result is ' + s
        return s

    return inner


def cache(max_size=5):
    def wrapper(func):
        def inner(*arg, **kwarg):
            arg_=arg[1:]
            flag = True
            if os.path.exists('cache.txt'):
                with open('cache.txt', 'r') as cache_file:
                    s = cache_file.readlines()
                    for i in s:
                        x = eval(i)
                        if x[0] == arg_ and x[1] == kwarg:
                            flag = False
                            return x[2]
            if flag:
                if os.path.exists('cache.txt'):
                    with open('cache.txt', 'r') as cache_file:
                        cache_count = cache_file.readlines()
                        cache_count = len(cache_count)
                else:
                    cache_count = 0
                if cache_count >= max_size:
                    with open('cache.txt', 'r') as cache_file:
                        s = cache_file.readlines()
                        del s[0]
                        s = ''.join(s)
                    with open('cache.txt', 'w') as cache_file:
                        cache_file.write(s)
                with open('cache.txt', 'a') as cache_file:
                    lis = [arg_, kwarg, func(*arg, **kwarg)]
                    cache_file.write(str(lis) + '\n')
                    cache_count += 1
                return func(*arg, **kwarg)

        return inner

    return wrapper
