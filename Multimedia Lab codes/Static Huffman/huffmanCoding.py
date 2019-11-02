import heapq


class HuffmanNode:
    def __init__(self, char, freq, left=None, right=None):
        self.char, self.freq, self.left, self.right = char, freq, left, right

    def __repr__(self):
        return "(" + self.char + ':' + str(self.freq) + ")"

    def __le__(self, other):
        if other is None:
            return True
        return self.freq <= other.freq

    def __lt__(self, other):
        if other is None:
            return True
        return self.freq < other.freq


def get_huffman_tree(file: dict) -> HuffmanNode:
    file_nodes = [(HuffmanNode(key, value)) for key, value in file.items()]
    while len(file_nodes) > 1:
        left, right = heapq.heappop(file_nodes), heapq.heappop(file_nodes)
        heapq.heappush(file_nodes, (HuffmanNode('$', left.freq + right.freq, left, right)))
    return file_nodes[0]


def get_codes(root: HuffmanNode, code: str, code_list: dict):
    if root is None:
        return
    if root.left is None and root.right is None:
        code_list[root.char] = code
        return
    get_codes(root.left, code + '0', code_list)
    get_codes(root.right, code + '1', code_list)


def encode_text(code_list: dict, text: str) -> str:
    encoded = ''
    for c in text:
        encoded += code_list[c]
    return encoded


def print_subtree(root, prefix: str):
    if root is None:
        return
    has_left = root.left is not None
    has_right = root.right is not None
    if not has_left and not has_right:
        return
    print(prefix, end='')
    if has_right and has_left:
        print(" ├── ", end='')
    if not has_left and has_right:
        print(" └── ", end='')
    if has_right:
        print_strand = has_right and has_left and (root.right.right is not None or root.right.left is not None)
        new_prefix = prefix + " |   " if print_strand else "    "
        print(root.right)
        print_subtree(root.right, new_prefix)
    if has_left:
        if has_right:
            print(prefix + " └──", root.left)
        else:
            print(" └──", root.left)
        print_subtree(root.left, prefix + "   ")


def print_tree(root):
    if root is None:
        return
    print(root)
    print_subtree(root, "")
    print()


def decode_huffman_string(root: HuffmanNode, encoded: str) -> str:
    node, result = root, ''
    for c in encoded:
        if c == '0':
            node = node.left
        else:
            node = node.right
        if node.left is None and node.right is None:
            result += node.char
            node = root
    return result


if __name__ == '__main__':
    f = open('/Users/raunit_x/Desktop/random.txt', 'r')
    print("FILE TO BE COMPRESSED: {}".format('/Users/raunit_x/Desktop/random.txt'))
    data, file_dict = f.readlines(), dict()
    for line in data:
        for c in line:
            file_dict[c] = file_dict.get(c, 0) + 1
    print("FILE DICTIONARY: {}".format(file_dict))
    root_node = get_huffman_tree(file_dict)
    print("HUFFMAN TREE: ")
    print_tree(root_node)
    codes_dict = {}
    get_codes(root_node, '', codes_dict)
    print("CODES FOR THE CHARACTERS: {}".format(codes_dict))
    compressed_text = encode_text(codes_dict, ''.join(data))
    print("DECODED TEXT: \n{}".format(decode_huffman_string(root_node, compressed_text)))
    print("COMPRESSION RATIO: {}%".format(((len(''.join(data)) * 8 - sum([len(codes_dict[c]) * file_dict[c] for
                                             c in file_dict])) / len(''.join(data) * 8)) * 100))




