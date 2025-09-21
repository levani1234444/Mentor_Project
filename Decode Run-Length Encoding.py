# Task 2: Decode Run-Length Encoding
# Write a function decode_rle(s) that decodes a run-length encoded string.
#  Example: "a3b2c1" → "aaabbc"
# Test Cases:
# decode_rle("a3b2c1") == "aaabbc"
# decode_rle("x5y1") == "xxxxxy"
# decode_rle("") == ""


def decode_rle(st):
    numbers = '1234567890'
    s = []
    for i in st:
        s.append(i)
    
    s = s[::2]
    num = []
    result = []
    for i in st:
        if i in numbers:
            num.append(i)

    for i in range(len(s)):
        result.append(int(num[i]) * s[i])
    
    return "".join(result)


print(decode_rle("a3b2c1"))