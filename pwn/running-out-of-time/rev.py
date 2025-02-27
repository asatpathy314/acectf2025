def print_flag(): 
    local_28 = [0] * 12
    local_28[0] = 0x1d
    local_28[1] = 0x1b
    local_28[2] = 0x47
    local_28[3] = 0x19
    local_28[4] = 0x75
    local_28[5] = 0x1f
    local_28[6] = 0x1d
    local_28[7] = 0x1a
    local_28[8] = 0x5a
    local_28[9] = 0x5a
    local_28[10] = 0x19
    local_28[11] = 0x4e
    local_d = 0x2a
    print("Success! Here is your output: ")
    for local_c in range(0, 0xC):
        local_28[local_c] = chr(local_28[local_c] ^ local_d)
    print("ACECTF{" + ''.join(local_28) + "}")

print_flag()
