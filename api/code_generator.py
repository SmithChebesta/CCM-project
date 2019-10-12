import random
import json


def get_code(amount=100, length=8, prefix='EN1'):
    CODE_AMOUNT = amount
    CODE_LENGTH = length
    CODE_PREFIX = prefix
    CHARACTER_SET = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                     't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    code_list = []

    def is_duplicate(list_):
        return len(set(list_)) != len(list_)

    repeate_time = 0
    while(repeate_time <= 100):
        for i in range(CODE_AMOUNT):
            code = CODE_PREFIX
            for j in range(abs(CODE_LENGTH - len(CODE_PREFIX))):
                code += str(CHARACTER_SET[random.randrange(0,
                                                           len(CHARACTER_SET))])

            code_list.append(code)
        if(is_duplicate(code_list) == False):
            break
        else:
            repeate_time += 1
            code_list = []
    return code_list
