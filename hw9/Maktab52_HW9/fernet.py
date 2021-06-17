from cryptography.fernet import Fernet
import argparse


# B
class Encrypt:
    def __init__(self, key):
        self.key = key
        self.__fernet = Fernet(self.key)

    def just_encript(self, txt):

        token = self.__fernet.encrypt(txt)
        return token

    def encrypt(self, txt, txt_name):
        # s = bytes(txt,encoding='utf8')
        token = self.just_encript(txt)
        with open(f'G:\maktab52\projects\hw9\Maktab52_HW9\encrypts\{txt_name}', 'wb' ) as f:
            f.write(token)
        return token

    def encrypt_file(self, file_path, save_name):
        with open(file_path, 'rb') as f:
            token = f.read()
        token = self.encrypt(token, save_name)

    def mydec(self, key):
        def wrapper(func):
            def inner(*args, **kwargs):
                s = bytes(func(*args, **kwargs), encoding='utf8')
                token = self.just_encript(s)
                return token

            return inner

        return wrapper


# c
class Decrypt:
    def __init__(self, key):
        self.key = key
        self.__fernet = Fernet(self.key)

    def decrypt(self, binary_txt):
        token = self.__fernet.decrypt(binary_txt)
        return token

    def decrypt_file(self, file_path):
        with open(file_path, 'rb') as f:
            token = f.read()
        return self.decrypt(token)


# context_manager
class open_crp:
    def __init__(self, file_path, key, mode='r'):
        self.file_path = file_path
        self.mode = mode
        self.key = key
        self.__fernet = Fernet(self.key)

    def __enter__(self):
        with open(self.file_path, 'rb') as file:
            s = file.read()

        s = self.__fernet.decrypt(s)

        with open(self.file_path, 'wb') as file:
            file.write(s)

        self._file = open(self.file_path, self.mode)
        return self._file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._file.close()
        with open(self.file_path, 'rb') as file:
            s = file.read()

        s = self.__fernet.encrypt(s)

        with open(self.file_path, 'wb') as file:
            file.write(s)


e = Encrypt(b'n3yWkgfPFA2LR-M37gzwTet1nkhgprWjcqkbHxIa294=')
d = Decrypt(b'n3yWkgfPFA2LR-M37gzwTet1nkhgprWjcqkbHxIa294=')
# e.encrypt('masoud', '1')

# e.encrypt_file('G:\maktab52\projects\hw9\Maktab52_HW9\decrypts\salam','2')

@e.mydec(b'n3yWkgfPFA2LR-M37gzwTet1nkhgprWjcqkbHxIa294=')
def salam():
    return 'salam'

# print(salam())

print(d.decrypt(b'gAAAAABgvM_RZV4Jl1c7p3q1A9HWji_SXqN8q9d7ZtEKJ4keD59z3HkqzIIXatE5K2Ur0yoNpF-IrxOoJ_YMzUL-Kcbdsec_fg=='))

# print(d.decrypt_file('encrypts/amir'))

# with open_crp('encrypts/amir',b'n3yWkgfPFA2LR-M37gzwTet1nkhgprWjcqkbHxIa294=','w') as f:
#     f.write('salam amirmasoud')


# A
parser_g = argparse.ArgumentParser(description='cryptography_generate key')
parser_g.add_argument('-g', '--generate_key', action='store_true', help='generate a key')

args = parser_g.parse_args()

if args.generate_key:
    """generate key and save in file"""
    key = Fernet.generate_key()
    with open('G:\maktab52\projects\hw9\Maktab52_HW9\keys/keys.key', 'ab') as file:
        file.write(key)
    with open('G:\maktab52\projects\hw9\Maktab52_HW9\keys/keys.key', 'a') as file:
        file.write('\n')
    print('your key is : ', key)
'''
# parser_en = argparse.ArgumentParser(description='cryptography_encrypting')
# parser_en.add_argument('-e', '--encrypt', action='store',type=bytes(encoding='utf8'),default=False, help='cryptography_encrypting')
# subparsers_en = parser_en.add_subparsers(help='encryption sub parsers')
# args_en = parser_en.parse_args()
# if args_en.encrypt:
#     e = Encrypt(args_en.encrypt)
# parser_en_txt = subparsers_en.add_parser('et')
# parser_en_txt.add_argument('-et','--encryoting_text',action='store',help='encrypting a text')
# args_en_txt = parser_en_txt.parse_args()
# e.encrypt(args_en_txt.encryoting_text,'my_en')



'''