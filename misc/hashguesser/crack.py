from pwn import *

def brute_force_hash():
    target_length = 32
    correct_hash = "88ef3cb6cbe5d99e6fee9f0000000000"
    correct_hash = list(correct_hash)
    incorrect_index = correct_hash.index("0")
    
    for position in range(incorrect_index, target_length):
        for char in "0123456789abcdef":
            current_attempt = ''.join(correct_hash)
            current_attempt = current_attempt[:position] + char + current_attempt[position+1:]
            
            # Send current_attempt to server via netcat
            matched, correct = send_to_server(current_attempt)
            correct_positions = int(correct.split(": ")[1].split("/")[0])
            matched_positions = int(matched.split(": ")[2].split("/")[0])
            if correct_positions > position:
                correct_hash[position] = char
                print(''.join(correct_hash))
                break
            else:
                print(f"Tried {char} with hash {current_attempt} at position {position}. It is incorrect.")
    return ''.join(correct_hash)

# Example server interaction (implementation required)
def send_to_server(hash_attempt):
    conn = remote('34.131.133.224', 5000)
    conn.sendline(hash_attempt.encode())
    matched = conn.recvline_contains("matched").decode()
    correct = conn.recvline_contains("correct").decode()
    conn.close()
    return matched, correct

print(brute_force_hash())