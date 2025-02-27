
local_76 = [0] * 0x3e
local_76[0] = 0x7b
local_76[1] = 0x2e
local_76[2] = 0xf1
local_76[3] = 0xeb
local_76[4] = 0x8b
local_76[5] = 0x76
local_76[6] = 0xe7
local_76[7] = 0x68
local_76[8] = 0x77
local_76[9] = 0xa3
local_76[10] = 0xef
local_76[0xb] = 0x52
local_76[0xc] = 0xf6
local_76[0xd] = 0x3c
local_76[0xe] = 0xda
local_76[0xf] = 0xaa
local_76[0x10] = 0xf6
local_76[0x11] = 0xa7
local_76[0x12] = 0x43
local_76[0x13] = 0xeb
local_76[0x14] = 0x21
local_76[0x15] = 0x24
local_76[0x16] = 0xc3
local_76[0x17] = 0x9c
local_76[0x18] = 0x7d
local_76[0x19] = 8
local_76[0x1a] = 0x33
local_76[0x1b] = 0xb7
local_76[0x1c] = 0xf7
local_76[0x1d] = 0x2c
local_76[0x1e] = 0xb4
local_76[0x1f] = 0x6c
local_76[0x20] = 0x2c
local_76[0x21] = 0xe0
local_76[0x22] = 0xef
local_76[0x23] = 0x8d
local_76[0x24] = 0x60
local_76[0x25] = 0xdc
local_76[0x26] = 0x75
local_76[0x27] = 0xd
local_76[0x28] = 0xff
local_76[0x29] = 0xd6
local_76[0x2a] = 0x59
local_76[0x2b] = 0xf4
local_76[0x2c] = 0x5d
local_76[0x2d] = 0xde
local_76[0x2e] = 0x9b
local_76[0x2f] = 0xe3
local_76[0x30] = 0xd7
local_76[0x31] = 0x52
local_76[0x32] = 0x99
local_76[0x33] = 0x5a
local_76[0x34] = 0x7c
local_76[0x35] = 0xa3
local_76[0x36] = 0xc9
local_76[0x37] = 0x4e
local_76[0x38] = 0x1b
local_76[0x39] = 0x45
local_76[0x3a] = 0xe5
local_76[0x3b] = 0xc0
local_76[0x3c] = 0x29
local_76[0x3d] = 0x9a

chars = []
print(''.join(map(chr, local_76[0x1f:])))

for i in range(0, 0x1f):
    chars.append(local_76[i] ^ local_76[i + 0x1f])



for i in range(len(chars) -1, 0, -1):
    chars[i] = chars[i] ^ chars[i-1]

print(list(map(chr, chars)))