import string
import decimal
from decimal import Decimal


def get_attributes():
    count = dict.fromkeys(string.ascii_lowercase, 1)  # probability table
    cdf_range = dict.fromkeys(string.ascii_lowercase, [0, 0])
    pdf = dict.fromkeys(string.ascii_lowercase, 0)
    low = 0
    high = Decimal(1) / Decimal(26)
    for key, value in sorted(cdf_range.items()):
        cdf_range[key] = [low, high]
        low = high
        high += Decimal(1) / Decimal(26)
    for key, value in sorted(pdf.items()):
        pdf[key] = Decimal(1) / Decimal(26)
    return count, cdf_range, pdf


def encode(encode_str, N):
    count, cdf_range, pdf = get_attributes()
    i = 26
    lower_bound = 0
    upper_bound = 1
    u = 0
    for sym in encode_str:
        i += 1
        u += 1
        count[sym] += 1
        curr_range = upper_bound - lower_bound
        upper_bound = lower_bound + (curr_range * cdf_range[sym][1])
        lower_bound = lower_bound + (curr_range * cdf_range[sym][0])
        if u == N:
            u = 0
            for key, value in sorted(pdf.items()):
                pdf[key] = Decimal(count[key])/Decimal(i)
            low = 0
            for key, value in sorted(cdf_range.items()):
                high = pdf[key] + low
                cdf_range[key] = [low, high]
                low = high
    return lower_bound


def decode(encoded, str_len, every):
    decoded_str = ""
    count, cdf_range, pdf = get_attributes()
    lower_bound = 0
    upper_bound = 1
    k = 0
    while str_len != len(decoded_str):
        for key, value in sorted(pdf.items()):
            curr_range = upper_bound - lower_bound
            upper_cand = lower_bound + (curr_range * cdf_range[key][1])
            lower_cand = lower_bound + (curr_range * cdf_range[key][0])
            if lower_cand <= encoded < upper_cand:
                k += 1
                decoded_str += key
                if str_len == len(decoded_str):
                    break
                upper_bound = upper_cand
                lower_bound = lower_cand
                count[key] += 1
                if k == every:
                    k = 0
                    for key_local, v in sorted(pdf.items()):
                        pdf[key_local] = Decimal(count[key_local])/Decimal(26+len(decoded_str))
                    low = 0
                    for key_local, v in sorted(cdf_range.items()):
                        high = pdf[key_local] + low
                        cdf_range[key_local] = [low, high]
                        low = high
    return decoded_str


def main():
    encode_str = "inputs"
    decimal.getcontext().prec = 2 * len(encode_str)
    str_len = len(encode_str)
    every = 3
    encoded = encode(encode_str, every)
    print("INPUT STRING: {}".format(encode_str))
    print("ENCODING OF '{}' WITH PRECISION {} (2 * len(input_string)): {}".format(encode_str, decimal.getcontext().prec,
                                                                               encoded))
    decoded = decode(encoded, str_len, every)
    print("DECODED STRING: {}".format(decoded))


if __name__ == '__main__':
    main()
