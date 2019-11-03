def compress(text):
    entries, result, i, curr_string, index = {'': 0}, [], 0, '', 1
    while i < len(text):
        while curr_string in entries:
            curr_string += text[i]
            i += 1
        entries[curr_string] = index
        index += 1
        result.append((entries[curr_string[:-1]], bin(ord(curr_string[-1])).lstrip('0b')))
        curr_string = ''
    print(entries)
    return result


def expand(compressed_list):
    entries, result = {0: ''}, ''
    for i, val in enumerate(compressed_list):
        entries[i + 1] = entries[val[0]] + chr(int(val[1], 2))
        result += entries[i + 1]
    return result


def main():
    text = 'This is some sample text where the compression used is LZ78'
    print("ORIGINAL STRING: {}".format(text))
    compressed_text = compress(text)
    print("COMPRESSED LIST: ", end='')
    for val in compressed_text:
        print("[{}, '{}']".format(val[0], chr(int(val[1], 2))), end=' ')
    print()
    print("RECOVERED STRING: {}".format(expand(compressed_text)))


if __name__ == '__main__':
    main()
