# encryption function, grabs the location of the text then adds the shift then regrabs from alphabet
def encrypt(clear_text, shift):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"
    shifted_text = ""
    shift_value = 0
    if shift >= 26:
            print("Shift amount shouldn't be greater then 26")
    else:
        for i in range(len(clear_text)):
            char = clear_text[shift_value]
            shifted_char = alphabet.find(str(char))
            shifted_char = alphabet[shifted_char+shift]
            shifted_text = shifted_text + str(shifted_char)
            shift_value = shift_value + 1

    print(shifted_text)
pass

# decryption function, grabs the location of the text then subtracts the shift then regrabs from alphabet
def decrypt(encrypted, decrypt_shift):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"
    shifted_text = ""
    shift_value = 0

    if decrypt_shift >= 26:
            print("Shift amount shouldn't be greater then 26")
    else:
        for i in range(len(encrypted)):
            char = encrypted[shift_value]
            shifted_char = alphabet.find(str(char))
            shifted_char = alphabet[shifted_char-decrypt_shift]
            shifted_text = shifted_text + str(shifted_char)
            shift_value = shift_value + 1  
    print(shifted_text)
pass

# the fun code
print("=====================================")
print("Caesar Cipher Encryption & Decryption")
print("=====================================")

encrypt_or_decrypt = input("(e)ncrypt or (d)ecrypt?")
if encrypt_or_decrypt == "e":
    clear_text = input("Unencrypted Phrase? ").upper()
    shift = int(input("Shift amount? "))
    encrypt(clear_text, shift)
elif encrypt_or_decrypt == "d":
    encrypted = input("Encrypted Phrase? ").upper()
    decrypt_shift = int(input("Shift amount? "))
    decrypt(encrypted, decrypt_shift)
else:
    print("(e)ncrypt or (d)ecrypt?")
