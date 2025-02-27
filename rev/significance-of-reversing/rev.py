with open("Reverseme.png", "rb") as f:
    file_bytes = f.read()

with open("reverseme.exe", "wb") as f:
    f.write(bytearray(file_bytes)[::-1])
