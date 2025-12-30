# Laporan Praktikum Kriptografi
Minggu ke-: 6 
Topik: [Cipher Modern (DES, AES, RSA)
]  
Nama: [Zalsabilah nur aeni]  
NIM: [230202793]  
Kelas: [5ikka]  

---

## 1. Tujuan
1.Mengimplementasikan algoritma DES untuk blok data sederhana.
2.Menerapkan algoritma AES dengan panjang kunci 128 bit.
3.Menjelaskan proses pembangkitan kunci publik dan privat pada algoritma RSA.

---

## 2. Dasar Teori
Cipher modern seperti DES, AES, dan RSA dikembangkan untuk mengatasi kelemahan cipher klasik dengan memanfaatkan konsep matematika dan komputasi yang lebih kompleks. DES dan AES termasuk ke dalam cipher simetris, yaitu menggunakan kunci yang sama untuk proses enkripsi dan dekripsi. DES bekerja dengan blok 64-bit dan panjang kunci efektif 56-bit, namun kini dianggap kurang aman karena ruang kuncinya kecil. AES hadir sebagai pengganti DES dengan tingkat keamanan lebih tinggi karena mendukung panjang kunci 128, 192, dan 256 bit serta menggunakan kombinasi substitusi, permutasi, dan operasi matematika yang kompleks.

RSA termasuk cipher asimetris yang menggunakan sepasang kunci, yaitu kunci publik dan kunci privat. Keamanan RSA bergantung pada kesulitan memfaktorkan bilangan prima besar, sehingga sangat sulit dipecahkan dengan komputasi saat ini jika ukuran kunci cukup besar. Dalam praktiknya, cipher modern sering digunakan secara kombinasi, misalnya RSA untuk pertukaran kunci dan AES untuk enkripsi data, agar diperoleh sistem keamanan yang efisien dan kuat.

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
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

# Generate key pair
key = RSA.generate(2048)
private_key = key
public_key = key.publickey()

# Enkripsi dengan public key
cipher_rsa = PKCS1_OAEP.new(public_key)
plaintext = b"Zalsabilah na"
ciphertext = cipher_rsa.encrypt(plaintext)
print("Ciphertext:", ciphertext)

# Dekripsi dengan private key
decipher_rsa = PKCS1_OAEP.new(private_key)
decrypted = decipher_rsa.decrypt(ciphertext)
print("Decrypted:", decrypted.decode())


## 6. Hasil dan Pembahasan
Hasil program sudah sesuai dengan ekspektasi. Plaintext “RSA Example” berhasil dienkripsi menggunakan public key sehingga menghasilkan ciphertext berupa data acak, lalu berhasil didekripsi kembali menggunakan private key dan menghasilkan plaintext yang sama seperti input awal proses enkripsi dan dekripsi RSA berjalan dengan benar.

Error yang sempat muncul adalah No module named 'Crypto', yang disebabkan library belum terpasang. Error tersebut berhasil diatasi dengan menginstal pycryptodome menggunakan pip, sehingga program dapat dijalankan tanpa kendala

Hasil eksekusi program Caesar Cipher:

![Hasil Eksekusi](screenshots/output.png)
![Hasil Input](screenshots/input.png)
![Hasil Output](screenshots/output.png)
)

---

## 7. Jawaban Pertanyaan
(Jawab pertanyaan diskusi yang diberikan pada modul.  
- Pertanyaan 1: DES dan AES merupakan algoritma simetris yang menggunakan satu kunci yang sama, sedangkan RSA adalah algoritma asimetris yang menggunakan pasangan kunci publik dan privat. DES memiliki keamanan rendah karena panjang kuncinya pendek, AES lebih aman karena menggunakan kunci yang lebih panjang, sementara keamanan RSA bergantung pada kesulitan memfaktorkan bilangan prima besar. 
- Pertanyaan 2: AES lebih banyak digunakan dibanding DES karena tingkat keamanannya lebih tinggi dan masih efisien digunakan pada sistem modern. DES sudah tidak direkomendasikan karena mudah dipecahkan dengan brute force.
- Pertanyaan 3: RSA disebut asimetris karena proses enkripsi dan dekripsi menggunakan kunci yang berbeda. Kunci RSA dibangkitkan dari dua bilangan prima besar yang menghasilkan kunci publik untuk enkripsi dan kunci privat untuk dekripsi.  
)
---

## 8. Kesimpulan
implementasi algoritma RSA pada program ini telah berjalan dengan baik. Proses enkripsi menggunakan public key dan dekripsi menggunakan private key berhasil mengembalikan plaintext ke bentuk semula, sehingga membuktikan bahwa mekanisme kerja RSA telah diterapkan dengan benar dan library yang digunakan sudah sesuai.

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
