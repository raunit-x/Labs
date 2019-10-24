def run_length_encoding(input_str: str) -> str:
    return ''.join(c + str(input_str.count(c)) for c in set(input_str))


def run_length_decoding(encoded_text: str) -> str:
    return "".join([encoded_text[i] * int(encoded_text[i + 1]) for i in range(0, len(encoded_text), 2)])


if __name__ == '__main__':
    input_text = input("Enter String: ")
    encoded_text = run_length_encoding(input_text)
    print("Compressed string using run length encoding: {}".format(encoded_text))
    expanded_text = run_length_decoding(encoded_text)
    print("Compressed string using run length encoding: {}".format(expanded_text))
