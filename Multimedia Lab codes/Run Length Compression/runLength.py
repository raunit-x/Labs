def run_length_encoding(input_str):
    index, result = 0, []
    while index < len(input_str):
        count, c = 0, input_str[index]
        while index < len(input_str) and input_str[index] == c:
            index += 1
            count += 1
        result.extend([c, str(count)])
    return result


def run_length_decoding(encoded_list):
    return "".join(encoded_list[i] * int(encoded_list[i + 1]) for i in range(0, len(encoded_list), 2))


if __name__ == '__main__':
    input_text = input("Enter String: ")
    encoded_text = run_length_encoding(input_text)
    print("Compressed string using run length encoding: {}".format(encoded_text))
    print("Length before compression: {}".format(len(input_text)))
    print("Length after compression: {}".format(len(''.join(encoded_text))))
    print("Compression Ratio: {}%".format(((len(input_text) - len(''.join(encoded_text))) / len(input_text)) * 100))
    expanded_text = run_length_decoding(encoded_text)
    print("Compressed string using run length encoding: {}".format(expanded_text))


