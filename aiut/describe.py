import random
import utils
from typing import Union


def desc_obj(obj):
    '''dispatch to desc_dict or desc_list'''
    if type(obj) in [int, float, str, bool]:
        return desc_basic(obj)
    elif type(obj) == list:
        return desc_list(obj)
    elif type(obj) == dict:
        return desc_dict(obj)
    else:
        pass


def desc_basic(obj: Union[int, float, str, bool]):
    return {
        'type': type(obj).__name__,
        'value': obj
    }


def desc_list(obj: list):
    length = len(obj)
    repeated = is_list_repeated(obj)
    children = get_list_children(obj, repeated)

    res = {
        'type': 'list',
        'length': length,
        'repeated': repeated,
        'children': children
    }
    return res


def is_list_repeated(l: list) -> bool:
    '''judge whether a list contains repeated elements'''
    if len(l) <= 1:
        return False

    if all(type(el) == type(l[0]) for el in l[:100]):
        return True
    return False


def get_list_children(l: list, repeated: bool) -> list:
    children = []
    if not len(l):
        return children
    if repeated:
        # if repeated, children will only show the first element
        children = [desc_obj(l[0])]
    else:
        # still, even if not repeated, children will show just top 100 elements
        if len(l) <= 100:
            children = [desc_obj(el) for el in l]
        else:
            children = [desc_obj(el) for el in l[:100]] + ["..."]
    return children


def desc_dict(obj: dict):
    length = len(obj)
    repeated = is_dict_repeated(obj)
    children = get_dict_children(obj, repeated)

    res = {
        'type': 'dict',
        'length': length,
        'repeated': repeated,
        'children': children
    }
    return res


def is_dict_repeated(d: dict) -> bool:
    '''judge whether a dict contains repeated elements'''

    # if all keys' length are the same (check first 100)
    #   elif levenshtein distance is less than 2 between two random consecutive keys
    # consider it is repeated
    if len(d) <= 1:
        return False

    keys = list(d.keys())
    if all(len(k) == len(keys[0]) for k in keys[:100]):
        return True

    indice = random.randint(0, len(keys) - 2)
    if utils.cal_levenshtein_distance(str(keys[indice]), str(keys[indice + 1])) <= 2:
        return True
    return False


def get_dict_children(d: dict, repeated: bool) -> dict:
    children = {}
    if not len(d):
        return children

    if repeated:
        # if repeated, children will only show the first element
        inst_k, inst_v = next(iter(d.items()))
        children = {inst_k: desc_obj(inst_v)}
    else:
        # still, even if not repeated, children will show just top 100 elements
        if(len(d)) <= 100:
            children = {k: desc_obj(v) for k, v in d.items()}
        else:
            it = iter(d.items())
            for _ in range(100):
                k, v = next(it)
                children[k] = desc_obj(v)
            children['...'] = '...'

    return children
