import re


def Eval(exp: str):
    exp_re = "^[0-9]+[ ]*([+]|[-]|[/]|[*])[ ]*[0-9]+[ ]*$"

    if not re.match(exp_re, exp):
        raise Exception("struct is wrong!!!")
    if '/' in exp:
        s = exp.split('/')
        if int(s[1]) == 0:
            raise Exception("division by zero!!!???")
    return eval(exp)


s = input()
print(Eval(s))
