from decimal import *
getcontext().prec = 100


def encoding(range_table: dict, text: str) -> float:
    low, high, diff = 0, 1, 1
    for c in text:
        high = Decimal(low + diff * range_table[c][1])
        low = Decimal(low + diff * range_table[c][0])
        diff = Decimal(high - low)
    return low


def decoding(range_table: dict, num: float) -> str:
    result = ''
    n = len(str(num).split('.')[-1])
    while len(result) < n:
        for key, val in zip(range_table, range_table.values()):
            if val[0] <= num <= val[1]:
                print(key, val, num)
                result += key
                num -= val[0]
                break
    return result


if __name__ == '__main__':
    input_table = [['y', 10], ['e', 20], ['r', 10], ['g', 10], ['n', 10], ['m', 10], ['a', 10], ['f', 10], ['c', 10]]
    total_sum = sum([it[1] for it in input_table])
    for i in range(len(input_table)):
        input_table[i][1] = Decimal(input_table[i][1]) / Decimal(total_sum)
    range_table, low = {}, 0
    for it in input_table:
        range_table[it[0]] = [low, low + it[1]]
        low += it[1]
    print(encoding(range_table, "german"))




