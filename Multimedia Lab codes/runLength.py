def run_length_compression(input: str) -> str:
    result = ''
    for c in input:
        if not result.count(c):
            result += c + str(input.count(c))
    return result


def run_length_expansion(compressed_text: str) -> str:
    result = ''
    for i in range(0, len(compressed_text), 2):
        result += "".join(compressed_text[i] for j in range(int(compressed_text[i + 1])))
    return result


input_text = input("Enter String: ")
compressed_text = run_length_compression(input_text)
print("Compressed string using run length encoding: {}".format(compressed_text))
expanded_text = run_length_expansion(compressed_text)
print("Compressed string using run length encoding: {}".format(expanded_text))

