from helpers import alphabet_position, rotate_character

def encrypt(text, rot):
    ciphertext = ''
    for letter in text:
        ciphertext = ciphertext + rotate_character(letter, rot)
    return ciphertext

def main():
    text = input("Type a message:\n")
    rot = input("Rotate by:\n")
    print(encrypt(text, int(rot)))

if __name__ == '__main__':
    main()
