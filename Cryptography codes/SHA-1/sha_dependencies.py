initial_hash_values = [0x67452301, 0xEFCDAB89, 0x98BADCFE, 0x10325476, 0xC3D2E1F0]
k_constants = [0x5A827999, 0x6ED9EBA1, 0x8F1BBCDC, 0xCA62C1D6]
f1, f2, f3 = lambda b, c, d: d ^ (b & (c ^ d)), lambda b, c, d: b ^ c ^ d, lambda b, c, d: (b & c) | (b & d) | (c & d)
stage_functions = [f1, f2, f3, f2]
