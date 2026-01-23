# file: praktikum/week2-cryptosystem/src/simple_crypto.py

def encrypt(plaintext, key):
    result = ""
    for char in plaintext:
        if char.isalpha():
            shift = 65 if char.isupper() else 97
            result += chr((ord(char) - shift + key) % 26 + shift)
        else:
            result += char
    return result

def decrypt(ciphertext, key):
    result = ""
    for char in ciphertext:
        if char.isalpha():
            shift = 65 if char.isupper() else 97
            result += chr((ord(char) - shift - key) % 26 + shift)
        else:
            result += char
    return result


if __name__ == "__main__":
    print("=== Program Simple Cryptosystem ===")
    nim = input("Masukkan NIM  : ")
    nama = input("Masukkan Nama : ")
    key = int(input("Masukkan kunci (key) enkripsi: "))

    # Gabungkan NIM dan Nama menjadi satu pesan
    message = f"{nim}{nama}"

    # Proses enkripsi dan dekripsi
    enc = encrypt(message, key)
    dec = decrypt(enc, key)

    print("\n=== HASIL ===")
    print("Plaintext  :", message)
    print("Ciphertext :", enc)
    print("Decrypted  :", dec)
