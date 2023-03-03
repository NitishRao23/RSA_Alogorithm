import random

def gcd(a, b):
    if (b == 0):
        return a
    else:
        return gcd(b, a % b)

def xgcd(a, b):
    x, old_x = 0, 1
    y, old_y = 1, 0

    while (b != 0):
        quotient = a // b
        a, b = b, a - quotient * b
        old_x, x = x, old_x - quotient * x
        old_y, y = y, old_y - quotient * y

    return a, old_x, old_y

def chooseE(totient):
    while (True):
        e = random.randrange(2, totient)

        if (gcd(e, totient) == 1):
            return e

def encrypt(message, filesName = 'public_keys.txt', block_size = 2):

    try:
        fo = open(filesName, 'r')

    except FileNotFoundError:
        print('That file is not found.')
    else:
        n = int(fo.readline())
        e = int(fo.readline())
        fo.close()

        encryptBlocks = []
        textCipher = -1

        if (len(message) > 0):
            textCipher = ord(message[0])

        for i in range(1, len(message)):
            if (i % block_size == 0):
                encryptBlocks.append(textCipher)
                textCipher = 0

            textCipher = textCipher * 1000 + ord(message[i])

        encryptBlocks.append(textCipher)

        for i in range(len(encryptBlocks)):
            encryptBlocks[i] = str((encryptBlocks[i]**e) % n)

        encrypted_message = " ".join(encryptBlocks)

        return encrypted_message

def decrypt(blocks, block_size = 2):

    fo = open('private_keys.txt', 'r')
    n = int(fo.readline())
    d = int(fo.readline())
    fo.close()

    blocksList = blocks.split(' ')
    initialized_blocks = []

    for s in blocksList:
        initialized_blocks.append(int(s))

    message = ""

    for i in range(len(initialized_blocks)):
        initialized_blocks[i] = (initialized_blocks[i]**d) % n
        
        tmp = ""
        for c in range(block_size):
            tmp = chr(initialized_blocks[i] % 1000) + tmp
            initialized_blocks[i] //= 1000
        message += tmp

    return message

def main():
    instruction_from_user = input('Would you like to encrypt or decrypt? (Enter e or d): ')
    if (instruction_from_user == 'e'):
        message = input('What would you like to encrypt?\n')
        option = input('Do you want to encrypt using your own public key? (y or n) ')

        if (option == 'y'):
            print('Encrypting...')
            print(encrypt(message))
        else:
            file_option = input('Enter the file name that stores the public key: ')
            print('Encrypting...')
            print(encrypt(message, file_option))

    elif (instruction_from_user == 'd'):
        message = input('What would you like to decrypt?\n')
        print('Decryption...')
        print(decrypt(message))
    else:
        print('That is not a proper instruction.')

main()