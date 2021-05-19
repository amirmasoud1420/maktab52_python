from primedec import *


class MulPrime:

    @staticmethod
    def is_prime(n):
        for i in range(2, n // 2 + 1):
            if n % i == 0:
                return False
        return True

    @string_p
    @remainder(5)
    @cache(max_size=5)
    def __call__(self, a, b):
        if not (isinstance(a, int) and isinstance(b, int)):
            raise Exception("Invalid input!!!")
        if (not MulPrime.is_prime(a)) or (not MulPrime.is_prime(b)):
            raise Exception("The number is not prime!!!")
        return a * b


mul_obj = MulPrime()
print(mul_obj(3, 5))
