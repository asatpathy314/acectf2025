import binascii

def e1(t, b, o):
    t1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    if len(b) != 168:
        raise ValueError("Invalid Input")
    c = [b[i:i+4] for i in range(0, len(b), 4)]
    with open(o, "w") as f:
        for x, y in enumerate(t):
            z = f"{ord(y):08b}"
            if x < 42:
                a = z[:6]
                d = z[6:] + c[x]
                e = int(a, 2)
                g = int(d, 2)
                r = t1[e] + t1[g]
            print(r)
            f.write(r + "\n")

def r1(t, o):
    t1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    binary_flag = []
    with open(o, "r") as f:
        for i in range(0, 42):
            c1, c2 = list(f.readline().strip())
            e = t1.index(c1)
            g = t1.index(c2)
            a = f"{e:06b}"
            d = f"{g:06b}"
            char = d[2:]
            binary_flag.append(char)
    binary_int = int(''.join(binary_flag), 2)
    byte_number = (binary_int.bit_length() + 7) // 8
    binary_array = binary_int.to_bytes(byte_number, byteorder="big")
    ascii = binary_array.decode()
    print(ascii)



"""
t = "I TOLD YOU THAT BASE64 DECODING IS NO GOOD"
b = "{REDACTED}" # Should be 128 bits
o = "output.txt"

e1(t, b, o)
"""
t = "I TOLD YOU THAT BASE64 DECODING IS NO GOOD"
r1(t, "output.txt")
