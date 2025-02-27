def mode_1_decrypt(array):
    for i in range(len(array) -1, 0, -1):
        array[i] = array[i] ^ array[i-1]

def mode_2(array):
    array[0] = 0x6c
    array[1] = 0x2c
    array[2] = 0xe0
    array[3] = 0xef
    array[4] = 0x8d
    array[5] = 0x60
    array[6] = 0xdc
    array[7] = 0x75
    array[8] = 0xd
    array[9] = 0xff
    array[10] = 0xd6
    array[11] = 0x59
    array[12] = 0xf4
    array[13] = 0x5d
    array[14] = 0xde
    array[15] = 0x9b
    array[16] = 0xe3
    array[17] = 0xd7
    array[18] = 0x52
    array[19] = 0x99
    array[20] = 0x5a
    array[21] = 0x7c
    array[22] = 0xa3
    array[23] = 0xc9
    array[24] = 0x4e
    array[25] = 0x1b
    array[26] = 0x45
    array[27] = 0xe5
    array[28] = 0xc0
    array[29] = 0x29
    array[30] = 0x9a

def mode_3_decrypt(array):
    for i in range(0x27):
        if i < len(array):
            array[i] = array[i] ^ 0x56

def mode_5_decrypt(array):
    xor_key = [0] * 0x1f
    xor_key[0] = 0x7b;
    xor_key[1] = 0x2e;
    xor_key[2] = 0xf1;
    xor_key[3] = 0xeb;
    xor_key[4] = 0x8b;
    xor_key[5] = 0x76;
    xor_key[6] = 0xe7;
    xor_key[7] = 0x68;
    xor_key[8] = 0x77;
    xor_key[9] = 0xa3;
    xor_key[10] = 0xef;
    xor_key[0xb] = 0x52;
    xor_key[0xc] = 0xf6;
    xor_key[0xd] = 0x3c;
    xor_key[0xe] = 0xda;
    xor_key[0xf] = 0xaa;
    xor_key[0x10] = 0xf6;
    xor_key[0x11] = 0xa7;
    xor_key[0x12] = 0x43;
    xor_key[0x13] = 0xeb;
    xor_key[0x14] = 0x21;
    xor_key[0x15] = 0x24;
    xor_key[0x16] = 0xc3;
    xor_key[0x17] = 0x9c;
    xor_key[0x18] = 0x7d;
    xor_key[0x19] = 8;
    xor_key[0x1a] = 0x33;
    xor_key[0x1b] = 0xb7;
    xor_key[0x1c] = 0xf7;
    xor_key[0x1d] = 0x2c;
    xor_key[0x1e] = 0xb4;
    for i in range(len(array)):
        array[i] = array[i] ^ xor_key[i]

array = [0] * 0x1f
decryption_engine = [
    lambda array: mode_1_decrypt(array),
    lambda array: mode_3_decrypt(array),
    lambda array: mode_5_decrypt(array),
]

for i in range(0, 3):
    for j in range(0, 3):
        for k in range(0, 3):
            mode_2(array)
            decryption_engine[i](array)
            decryption_engine[j](array)
            decryption_engine[k](array)
            print(''.join(list(map(chr, array))))

mode_5_decrypt(array)
mode_1_decrypt(array)
mode_3_decrypt(array)
print(list(map(chr, array)))

# ['A', 'C', 'E', 'C', 'T', 'F', '{', 'p', '1', 'p', '3', 'd', '_', '5', '3', 'c', 'r', '3', '7', '5', '_', 'u', 'n', 'c', '0', 'v', '3', 'r', '3', 'd', '}']