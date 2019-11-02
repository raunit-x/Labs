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


def print_tree(root):
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
    if root is None:
        return
    print(root)
    print_subtree(root, "")
    print()


# Character for NYT node is '*' and internal node is '$'
class DynamicHuffmanTree:
    def __init__(self):
        self.root = HuffmanNode('*', 0)
        self.characters = {}
        self.e, self.r = 4, 10
        self.nyt_code = ''
        self.encoding = ''
        self.decoded_text = ''
        self.index = 0

    def set_nyt_code(self, root, curr=''):
        if root is None:
            return
        if root.char == '*':
            self.nyt_code = curr
            return
        self.set_nyt_code(root.left, curr + '0')
        self.set_nyt_code(root.right, curr + '1')

    def decode_nyt_encountered(self):
        val = int(self.encoding[self.index:self.index + self.e], 2)
        if val < self.r:
            self.decoded_text += chr(int(self.encoding[self.index:self.index + self.e + 1], 2) + ord('a'))
        else:
            self.decoded_text += chr(val + self.r + ord('a'))
        self.index = len(self.encoding)

    def decode(self, root, curr_index):
        if root is None:
            return
        if root.char == '*':
            self.index = curr_index
            self.decode_nyt_encountered()
            return
        if root.left is None and root.right is None:
            self.index = len(self.encoding)
            self.decoded_text += root.char
            return
        next_node = root.left if self.encoding[curr_index] is '0' else root.right
        self.decode(next_node, curr_index + 1)

    def code(self, root, char, curr=''):
        if root is None:
            return None
        if root.char is char:
            return curr
        l, r = self.code(root.left, char, curr + '0'), self.code(root.right, char, curr + '1')
        return l if l is not None else r

    def get_code(self, char):
        if char in self.characters:
            self.encoding += self.code(self.root, char)
            return
        self.set_nyt_code(self.root)
        k = ord(char) - ord('a') + 1
        suffix = bin(k - 1).lstrip('0b').zfill(self.e + 1) if k <= 2 * self.r else \
            bin(k - self.r - 1).lstrip('0b').zfill(self.e)
        self.encoding += self.nyt_code + suffix

    def balance_tree(self, root):
        if root is None or root.left is None:
            return None
        if root.left.freq > root.right.freq:
            root.left, root.right = root.right, root.left
            return root
        self.balance_tree(root.right)
        self.balance_tree(root.left)
        return root

    def update_tree_helper(self, char, root, flag):
        if root is None:
            return None
        if root.char is '*' and not flag:
            root = HuffmanNode('$', 1)
            root.left, root.right = HuffmanNode('*', 0), HuffmanNode(char, 1)
            return root
        elif root.char == char:
            root.freq += 1
            return root
        if root.right is not None:
            root.left = self.update_tree_helper(char, root.left, flag)
            root.right = self.update_tree_helper(char, root.right, flag)
            root.freq = root.right.freq + root.left.freq
        return root

    def update_tree(self, char):
        flag = char in self.characters
        self.get_code(char)
        self.decode(self.root, self.index)
        print("Encoded till now(SENDER): {}".format(self.encoding))
        print("Decoded till now(RECEIVER): {}".format(self.decoded_text))
        self.root = self.update_tree_helper(char, self.root, flag)
        self.characters[char] = self.characters.get(char, 0) + 1
        self.root = self.balance_tree(self.root)
        print("TREE(after insertion of the character '{}'):".format(char))
        print_tree(self.root)


if __name__ == '__main__':
    text = ['a', 'a', 'r', 'd', 'v', 'a', 'r', 'k']
    tree = DynamicHuffmanTree()
    for c in text:
        tree.update_tree(c)
    print("FINAL ENCODING(SENDER): {}".format(tree.encoding))
    print("FINAL DECODING(RECEIVER): {}".format(tree.decoded_text))
    print("COMPRESSION RATIO: {}%".format((((len(text) * 8) - len(tree.encoding)) / (len(text) * 8)) * 100))


