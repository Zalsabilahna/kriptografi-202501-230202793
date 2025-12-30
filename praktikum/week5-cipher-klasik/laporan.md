# Laporan Praktikum Kriptografi
Minggu ke-: 5
Topik: [Cipher Klasik (Caesar, Vigenère, Transposisi)]  
Nama: [Zalsabilah nur aeni]  
NIM: [230202793]  
Kelas: [5 ikka]  

---

## 1. Tujuan
1.Menerapkan algoritma Caesar Cipher untuk enkripsi dan dekripsi teks.
2.Menerapkan algoritma Vigenère Cipher dengan variasi kunci.
3.Mengimplementasikan algoritma transposisi sederhana.
4.Menjelaskan kelemahan algoritma kriptografi klasik.

## 2. Dasar Teori
Cipher klasik merupakan metode kriptografi awal yang digunakan untuk mengamankan pesan dengan mengubah plaintext menjadi ciphertext menggunakan aturan tertentu. Meskipun sederhana dan sudah jarang digunakan untuk keamanan modern, cipher klasik penting untuk memahami konsep dasar enkripsi dan dekripsi dalam kriptografi.

Cipher Caesar dan Vigenère termasuk jenis cipher substitusi. Caesar cipher mengenkripsi pesan dengan menggeser huruf dalam alfabet dengan nilai tetap, sedangkan Vigenère cipher menggunakan kata kunci sehingga pergeseran huruf bersifat bervariasi dan lebih sulit ditebak. Sementara itu, cipher transposisi bekerja dengan mengubah urutan huruf tanpa mengubah karakter aslinya, sehingga pesan tersamarkan melalui pengacakan posisi huruf.


## 3. Alat dan Bahan
(- Python 3.x  
- Visual Studio Code / editor lain  
- Git dan akun GitHub  
- Library tambahan (misalnya pycryptodome, jika diperlukan)  )

---

## 4. Langkah Percobaan
(Tuliskan langkah yang dilakukan sesuai instruksi.  
Contoh format:
1. Membuat file `caesar_cipher.py` di folder `praktikum/week2-cryptosystem/src/`.
2. Menyalin kode program dari panduan praktikum.
3. Menjalankan program dengan perintah `python caesar_cipher.py`.)

---

## 5. Source Code
def transpose_encrypt(plaintext, key=5):
    ciphertext = [''] * key
    for col in range(key):
        pointer = col
        while pointer < len(plaintext):
            ciphertext[col] += plaintext[pointer]
            pointer += key
    return ''.join(ciphertext)

def transpose_decrypt(ciphertext, key=5):
    num_of_cols = int(len(ciphertext) / key + 0.9999)
    num_of_rows = key
    num_of_shaded_boxes = (num_of_cols * num_of_rows) - len(ciphertext)
    plaintext = [''] * num_of_cols
    col = 0
    row = 0
    for symbol in ciphertext:
        plaintext[col] += symbol
        col += 1
        if (col == num_of_cols) or (col == num_of_cols - 1 and row >= num_of_rows - num_of_shaded_boxes):
            col = 0
            row += 1
    return ''.join(plaintext)

# Contoh uji
msg = "TRANSPOSITIONCIPHER"
enc = transpose_encrypt(msg, key=5)
dec = transpose_decrypt(enc, key=5)
print("Plaintext :", msg)
print("Ciphertext:", enc)
print("Decrypted :", dec)
```
)

---

## 6. Hasil dan Pembahasan
Hasil program sudah sesuai dengan ekspektasi. Plaintext “TRANSPOSITIONCIPHER” berhasil dienkripsi menggunakan metode Transposition Cipher menjadi ciphertext “TPIPROOHASNENICRSTI”, dan setelah dilakukan dekripsi, hasilnya kembali sama dengan plaintext awal. Hal ini menunjukkan bahwa proses enkripsi dan dekripsi berjalan dengan benar serta algoritma bekerja sesuai konsep Transposition Cipher.

Selama eksekusi program tidak ditemukan error. Jika error muncul, umumnya disebabkan oleh penggunaan nilai key yang berbeda antara enkripsi dan dekripsi atau kesalahan dalam perhitungan jumlah kolom dan baris. Solusinya adalah memastikan nilai key konsisten serta logika indeks kolom, baris, dan shaded boxes pada proses dekripsi sudah tepat. 

Hasil eksekusi program Caesar Cipher:

![Hasil Eksekusi](screenshots/output.png)
![Hasil Input](screenshots/input.png)
![Hasil Output](screenshots/output.png)
)

---

## 7. Jawaban Pertanyaan
(Jawab pertanyaan diskusi yang diberikan pada modul.  
- Pertanyaan 1: Kelemahan utama Caesar Cipher adalah jumlah kuncinya sangat sedikit sehingga mudah dipecahkan dengan brute force dan pola huruf masih terlihat. Vigenère Cipher memang lebih kuat, tetapi tetap lemah karena pengulangan kunci dapat dianalisis sehingga memungkinkan serangan Kasiski dan analisis frekuensi. 
- Pertanyaan 2: Cipher klasik mudah diserang dengan analisis frekuensi karena pola statistik bahasa pada plaintext masih muncul pada ciphertext. Huruf yang sering muncul tetap dapat dikenali sehingga penyerang bisa menebak isi pesan
- Pertanyaan 3: Cipher substitusi memiliki kelebihan karena setiap huruf diganti sehingga tidak langsung terbaca, tetapi kelemahannya pola frekuensi huruf tetap terlihat. Cipher transposisi mempertahankan frekuensi huruf, namun hanya mengubah urutan sehingga pola kata masih dapat ditebak.
)
---

## 8. Kesimpulan
implementasi Transposition Cipher pada program ini sudah berjalan dengan baik. Proses enkripsi dan dekripsi menghasilkan output yang sesuai, di mana ciphertext dapat dikembalikan ke plaintext semula tanpa perubahan. Hal ini menunjukkan bahwa algoritma telah diterapkan dengan benar dan nilai kunci yang digunakan konsisten, sehingga metode transposisi bekerja sesuai dengan teori yang dipelajari.

## 9. Daftar Pustaka
(Cantumkan referensi yang digunakan.  
Contoh:  
- Katz, J., & Lindell, Y. *Introduction to Modern Cryptography*.  
- Stallings, W. *Cryptography and Network Security*.  )

---

## 10. Commit Log
(Tuliskan bukti commit Git yang relevan.  
Contoh:
```
commit abc12345
Author: Nama Mahasiswa <email>
Date:   2025-09-20

    week2-cryptosystem: implementasi Caesar Cipher dan laporan )
```
