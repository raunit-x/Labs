import numpy as np


def encryption(text: str, key: int) -> (str, dict):
    try:
        levels, index, incrementer = {i: "" for i in range(key)}, 0, -1
        for i, val in enumerate(text):
            if index == key - 1 or index == 0:
                incrementer *= -1
            levels[index] += text[i]
            index += incrementer
        return "".join(levels[i] for i in range(key)), levels
    except:
        return text, {}


def decryption(key: int, levels: dict, n: int) -> str:
    try:
        incrementer, index = -1, 0
        levels_index = [0 for i in range(key)]
        result = ''
        for i in range(n):
            if index == 0 or index == key - 1:
                incrementer *= -1
            result += levels[index][levels_index[index]]
            levels_index[index] += 1
            index += incrementer
        return result
    except:
        return text


if __name__ == '__main__':
    text = input("Enter the text: ")
    key = int(input("Key: "))
    print("Encrypted Text: {}".format(encryption(text, key)[0]))
    print("Decrypted Plain Text: {}".format(decryption(key, encryption(text, key)[1], len(text))))
