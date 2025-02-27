# obtained from decompilation on dogbolt.org

def print_flag():
  _Str2 = "GRX14YcKLzXOlW5iaSlBIrN7"
  local_20 = [0] * 24
  local_20[0] = 6
  local_20[1] = 0x11
  local_20[2] = 0x1d
  local_20[3] = 0x72
  local_20[4] = 0x60
  local_20[5] = 0x1f
  local_20[6] = 0x18
  local_20[7] = 0x7c
  local_20[8] = 0x3e
  local_20[9] = 0xf
  local_20[10] = 0x6d
  local_20[0xb] = 0x78
  local_20[0xc] = 0x33
  local_20[0xd] = 0x35
  local_20[0xe] = 0x40
  local_20[0xf] = 0x5e
  local_20[0x10] = 0x3e
  local_20[0x11] = 0x25
  local_20[0x12] = 0x5f
  local_20[0x13] = 0x30
  local_20[0x14] = 0x78
  local_20[0x15] = 0x14
  local_20[0x16] = 0x37
  local_20[0x17] = 0x4a
  local_8 = 0
  flag = []
  for i, char in enumerate(_Str2):
    flag.append(chr(ord(char) ^ local_20[i]))
  print(''.join(flag))
  """
  while True:
    if (0x17 < local_8):
      break
    if len(_Str1) < local_8 or len(_Str2) < local_8:
      break
    if (_Str1[local_8] ^ local_20[local_8]) != _Str2[local_8]:
      break
    local_8 = local_8 + 1
  """

# ACECTF{7ru57_bu7_v3r1fy}
print_flag()