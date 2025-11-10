# Laporan Praktikum Kriptografi
Minggu ke-: X  
Topik: Cryptosystem (Komponen, Enkripsi & Dekripsi, Simetris & Asimetris)
Nama: zalsabilah nur aeni
NIM: 230202793
Kelas: 5 IKKA

---

## 1. Tujuan
Mengidentifikasi komponen dasar kriptosistem (plaintext, ciphertext, kunci, algoritma).
Menggambarkan proses enkripsi dan dekripsi sederhana.
Mengklasifikasikan jenis kriptosistem (simetris dan asimetris).


## 2. Dasar Teori
Cryptosystem adalah sistem keamanan data yang berfungsi untuk melindungi informasi dengan cara mengubah pesan asli (**plaintext**) menjadi bentuk yang tidak dapat dibaca (ciphertext) melalui proses enkripsi, dan sebaliknya melalui dekripsi. Dalam prosesnya, cryptosystem memanfaatkan algoritma matematika tertentu serta kunci rahasia (key) untuk memastikan bahwa hanya pihak yang memiliki kunci yang sesuai yang dapat membaca pesan tersebut. Tujuan utama dari sistem ini adalah menjaga kerahasiaan, keaslian, dan integritas data selama proses penyimpanan maupun pengiriman.

Salah satu dasar penting dalam cryptosystem, terutama pada cipher klasik, adalah penggunaan aritmetika modular, yaitu operasi matematika yang dilakukan berdasarkan sistem bilangan modulo. Contohnya pada Caesar Cipher*, setiap huruf digeser sejauh beberapa langkah sesuai nilai kunci dalam sistem alfabet yang dianggap sebagai bilangan 0–25, dan prosesnya dihitung menggunakan operasi mod 26. Prinsip aritmetika modular ini juga menjadi dasar bagi berbagai algoritma kriptografi modern, baik yang bersifat Simetris (menggunakan satu kunci) maupun asimetris (menggunakan pasangan kunci publik dan privat), seperti AES dan RSA. Dengan demikian, cryptosystem tidak hanya mengandalkan transformasi simbol, tetapi juga penerapan konsep matematika untuk mencapai keamanan yang kuat.


## 3. Alat dan Bahan
(- Python 3.x  
- Visual Studio Code / editor lain  
- Git dan akun GitHub  
- Library tambahan (misalnya pycryptodome, jika diperlukan)  )

---

## 4. Langkah Percobaan
1.Buat diagram sederhana (bisa pakai draw.io, excalidraw, atau digambar lalu screenshot) dengan elemen:
Plaintext → [Algoritma + Kunci] → Ciphertext
Ciphertext → [Algoritma + Kunci] → Plaintext
2.Simpan diagram di folder screenshots/diagram_kriptosistem.png.
3.jalankan source kode tersebut
---

## 5. Source Code
# ============================================
# Custom Cryptosystem (Huruf + Angka Random)
# ============================================

import string
import random

# Daftar karakter yang digunakan (huruf besar, kecil, angka)
CHARACTERS = string.ascii_letters + string.digits
CHAR_LEN = len(CHARACTERS)

# Fungsi untuk enkripsi
def encrypt(text, key):
    text = text.replace(" ", "")  # hapus spasi agar lebih aman
    result = ""
    for char in text:
        if char in CHARACTERS:
            index = CHARACTERS.index(char)
            new_index = (index + key) % CHAR_LEN
            encrypted_char = CHARACTERS[new_index]
            # Tambahkan angka acak di belakang setiap karakter terenkripsi
            result += encrypted_char + str(random.randint(0, 9))
        else:
            # Jika karakter tidak dikenal, tambahkan langsung
            result += char + str(random.randint(0, 9))
    return result

# Fungsi untuk dekripsi
def decrypt(ciphertext, key):
    result = ""
    # Karena setiap karakter terenkripsi diikuti satu angka acak,
    # kita ambil 2 karakter sekali (huruf terenkripsi + angka acak)
    for i in range(0, len(ciphertext), 2):
        char = ciphertext[i]  # ambil huruf terenkripsi saja
        if char in CHARACTERS:
            index = CHARACTERS.index(char)
            new_index = (index - key) % CHAR_LEN
            result += CHARACTERS[new_index]
        else:
            result += char
    return result

# --- Program utama ---
if __name__ == "__main__":
    print("=== Advanced Cryptosystem: Huruf + Angka Acak ===")
    text = input("Masukkan teks yang ingin dienkripsi: ")
    key = int(input("Masukkan kunci (angka bebas, misal 5): "))

    encrypted = encrypt(text, key)
    print(f"\nHasil Enkripsi : {encrypted}")

    decrypted = decrypt(encrypted, key)
    print(f"Hasil Dekripsi : {decrypted}")

## 6. Hasil dan Pembahasan
Fungsi enkripsi bekerja baik — setiap karakter digeser berdasarkan kunci, lalu ditambah angka acak di belakang.
Dekripsi berhasil mengembalikan teks asli, karena kunci yang sama digunakan untuk menggeser kembali.
Spasi tidak dipertahankan, karena program menghapus spasi dengan text.replace(" ", "").
Simbol dan karakter non-alfanumerik tidak dienkripsi, tetapi tetap muncul utuh di hasil akhir.
Output berbeda setiap kali dijalankan, karena angka acak ditambahkan secara dinamis — hal ini meningkatkan keamanan dasar, tetapi membuat hasil tidak bisa direproduksi tanpa random seed.
Hasil eksekusi program Caesar Cipher:

![Hasil Eksekusi](screenshots/output.png)
![Hasil Input](screenshots/input.png)
![Hasil Output](screenshots/output.png)
)

---

## 7. Jawaban Pertanyaan
1. Komponen utama dalam sebuah kriptosistem
Komponen utama kriptosistem terdiri dari:
1.Plaintext → pesan asli yang akan dienkripsi.
2.Ciphertext → hasil enkripsi yang tidak dapat dibaca tanpa kunci.
3.Algoritma enkripsi → proses yang mengubah plaintext menjadi ciphertext menggunakan kunci.
4.Algoritma dekripsi → proses untuk mengembalikan ciphertext menjadi plaintext.
5Kunci (key) → nilai rahasia yang digunakan dalam proses enkripsi dan dekripsi.
2.. Kelebihan dan kelemahan sistem simetris dibandingkan asimetris
Aspek	Sistem Simetris	Sistem Asimetris
Kelebihan	- Proses enkripsi & dekripsi lebih cepat.
- Efisien untuk data dalam jumlah besar.	- Tidak perlu berbagi kunci rahasia secara langsung.
- Cocok untuk otentikasi & tanda tangan digital.
Kelemahan	- Distribusi kunci sulit karena kunci rahasia harus dikirim dengan aman ke penerima.
- Tidak cocok untuk komunikasi banyak pihak.	- Proses lebih lambat karena operasi matematis kompleks.
- Membutuhkan kunci lebih panjang untuk tingkat keamanan yang sama.
3.Mengapa distribusi kunci menjadi masalah utama dalam kriptografi simetris
Karena kriptografi simetris menggunakan satu kunci yang sama untuk enkripsi dan dekripsi, kunci tersebut harus dibagikan secara aman kepada kedua pihak sebelum komunikasi dimulai. Jika kunci tersebut disadap atau bocor selama proses distribusi, pihak ketiga dapat membaca semua pesan terenkripsi. Oleh karena itu, keamanan seluruh sistem bergantung pada kerahasiaan kunci saat dikirimkan, menjadikan distribusi kunci tantangan utama dalam sistem simetris.


## 8. Kesimpulan
rogram Custom Cryptosystem (Huruf + Angka Random) berhasil melakukan proses enkripsi dan dekripsi dengan baik. Setiap karakter pada teks berhasil diubah menggunakan pergeseran berbasis kunci (mirip Caesar cipher) dan disisipi angka acak untuk meningkatkan kerahasiaan. Hasil pengujian menunjukkan bahwa teks yang dienkripsi dapat dikembalikan ke bentuk aslinya dengan benar menggunakan kunci yang sama. Hal ini membuktikan bahwa algoritma enkripsi dan dekripsi berfungsi sesuai dengan rancangan, terutama untuk karakter huruf dan angka.
Namun, terdapat beberapa kelemahan minor dalam implementasi. Program secara otomatis menghapus spasi pada teks, sehingga hasil dekripsi tidak memunculkan jarak antar kata. Selain itu, karena penggunaan angka acak, hasil enkripsi berbeda setiap kali dijalankan sehingga tidak deterministik. Meski begitu, faktor ini sekaligus menambah tingkat keamanan sederhana terhadap pola karakter. Secara keseluruhan, sistem ini sudah efektif untuk demonstrasi konsep dasar kriptografi dengan sedikit potensi perbaikan pada pengelolaan spasi dan kontrol angka acak.

## 9. Daftar Pustaka
1.Understanding Cryptography: A Textbook for Students and Practitioners – Christof Paar & Jan Pelzl. Springer, 2nd edition. 
SpringerLink
+1
2.Introduction to Modern Cryptography – Jonathan Katz & Yehuda Lindell. 2nd Edition. 
eclass.uniwa.gr
3.Mathematics of Public Key Cryptography – Steven D. Galbraith. Version 2.0. 
math.auckland.ac.nz
4.Cryptography and Secure Communication – Conference proceedings / collected references. 
Cambridge University Press & Assessment
5.Encyclopedia of Cryptography and Security – Henk C.A. van Tilborg (Editor). Springer, 2005. 
en.wikipedia.org

## 10. Commit Log
commit: week2-cryptosystem
Author: zalsabilah nur aeni (zalsabilahna@gmail.com)
Date:   2025-11-10

    week2-cryptosystem: implementasi Caesar Cipher dan laporan )
```
