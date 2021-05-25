import re


def name_validation(name: str):
    pattern = r"([a-zA-Z_]){5,14}"
    x = re.search(pattern, name)
    if x:
        return x.group() == name
    else:
        return False


def email_validation(email: str):
    pattern = r"([\w_\.\+])+@([\w_\.])+\.([\w_\.])+"
    x = re.search(pattern, email)
    if x:
        return x.group() == email
    else:
        return False


def phone_validation(phone: str):
    pattern = r"(09|\+989)([0-9]){9}"
    x = re.search(pattern, phone)
    if x:
        return x.group() == phone
    else:
        return False


print(name_validation("amir_"))
print(email_validation("amir@email.ac.com"))
print(phone_validation("+989111236789"))