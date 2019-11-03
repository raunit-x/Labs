def compress(text, initial_dict):
    i, index, curr_index, curr_string, result = 0, max(len(initial_dict) - 1, 0), 1, '', []
    entries = initial_dict
    while i < len(text):
        flag = False
        while curr_string in entries:
            curr_index = entries[curr_string]
            curr_string += text[i]
            i += 1
        result.append(curr_index)
        entries[curr_string] = index + 1
        curr_string = curr_string[-1]
        index += 1
    print(entries)
    return result, entries


def expand(compressed_list, entries):
    reversed_dict = {val: key for key, val in zip(entries, entries.values())}
    return "".join([reversed_dict[index] for index in compressed_list])


def main():
    text = 'wabbaBwabbaBwabbaBwabbaBwooBwooBwoo'
    print("ORIGINAL TEXT: {}".format(text))
    initial_dict = {'': 0, 'B': 1, 'a': 2, 'b': 3, 'o': 4, 'w': 5}
    compressed_list, entries = compress(text, initial_dict)
    expanded_list = expand(compressed_list, entries)
    print("COMPRESSED TEXT: {}".format(compressed_list))
    print("RECOVERED STRING: {}".format(expanded_list))


if __name__ == '__main__':
    main()
