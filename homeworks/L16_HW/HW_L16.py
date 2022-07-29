
#  Task 1: написати декоратор exception_wrapper - його задача подавити всі ексепшини які можуть згенеруватись в функції
#  і видати якийсь прінт
from typing import Dict


def exception_wrapper(some_func):
    """ decorator that handles exceptions  Correct_entrance"""

    def wrap(login):
        try:
            result = some_func(login)
            print(result)
            return result
        except NameError:
            return 'Incorrect login'
        except Exception as element:
            print(element)

    return wrap


@exception_wrapper
def correct_entrance(login):
    """
    :param login: your login: expected 'suslik', when login is different NameError being raised
    : returns: a string with login
    decorator function handles NameError and prints 'Incorrect login'
    """
    if login != 'suslik':
        print('Incorrect login')
        raise NameError
    else:
        print('suslik')


print(correct_entrance('suslik'))


# Task 2: написати декоратор expect, його завдання перевірити на відповідність певній моделі,
# аргумент що передається в функцію

class ValidationError(Exception):
    pass


def cat(cat_dict: dict):
    def fluffy_wrap(func):
        def paw_wrap(paw_dict: dict):
            paw_key = paw_dict.keys()
            for key, value in cat_dict:
                if value.required:
                    try:
                        if value['type'] == type(paw_key[key]):
                            continue
                        else:
                            raise ValidationError
                    except KeyError:
                        raise ValidationError
            return func(paw_dict)

        return paw_wrap()

    return fluffy_wrap()

# Task 3: написати декоратор marshal, його завдання перевірити на відповідність певній моделі, те що повертає функція


def cat(cat_dict: dict):
    def fluffy_wrap(func):
        def paw_wrap(*args, **kwargs):
            paw_dict = func(*args, **kwargs)
            paw_key = paw_dict.keys()
            for key, value in cat_dict:
                if value.required:
                    try:
                        if value['type'] == type(paw_key[key]):
                            continue
                        else:
                            raise ValidationError
                    except KeyError:
                        raise ValidationError
            return paw_dict

        return paw_wrap

    return fluffy_wrap
