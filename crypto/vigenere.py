from helpers import alphabet_position, rotate_character

def encrypt(text, key):
    keylength = len(key)
    ciphertext = ''
    msg_idx = 0
    for msg_char in text:
        if msg_char.isalpha():
            key_idx = msg_idx % keylength
            msg_idx += 1
            key_char = key[key_idx]
            rot = alphabet_position(key_char)
            ciphertext = ciphertext + rotate_character(msg_char, rot)
        else:
            ciphertext = ciphertext + msg_char
    return ciphertext

def main():
    text = input("Type a message:\n")
    key = input("Encryption key:\n")
    print(encrypt(text, key))

if __name__ == '__main__':
    main()
