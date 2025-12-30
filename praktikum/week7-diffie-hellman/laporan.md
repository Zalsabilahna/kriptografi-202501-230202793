# Laporan Praktikum Kriptografi
Minggu ke-: 7
Topik: [Diffie-Hellman Key Exchange
]  
Nama: [Zalsabilah nur aeni]  
NIM: [230202793]  
Kelas: [5ikka]  

---

## 1. Tujuan
1.Melakukan simulasi protokol Diffie-Hellman untuk pertukaran kunci publik.
2.Menjelaskan mekanisme pertukaran kunci rahasia menggunakan bilangan prima dan logaritma diskrit.
3.Menganalisis potensi serangan pada protokol Diffie-Hellman (termasuk serangan Man-in-the-Middle / MITM).

---

## 2. Dasar Teori
Diffie–Hellman Key Exchange merupakan algoritma kriptografi asimetris yang digunakan untuk melakukan pertukaran kunci rahasia melalui jaringan publik secara aman. Algoritma ini diperkenalkan oleh Diffie dan Hellman pada tahun 1976 untuk mengatasi permasalahan distribusi kunci dalam sistem keamanan data.

Keamanan Diffie–Hellman didasarkan pada operasi aritmetika modular dan sulitnya menyelesaikan masalah discrete logarithm. Dalam penerapannya, dua pihak terlebih dahulu menyepakati nilai publik berupa bilangan prima dan generator. Selanjutnya, masing-masing pihak memilih kunci privat dan menghasilkan nilai publik yang kemudian dipertukarkan.

Dari nilai publik yang diterima, kedua pihak dapat menghitung kunci rahasia yang sama tanpa harus mengirimkan kunci tersebut secara langsung. Kunci rahasia ini biasanya digunakan sebagai kunci simetris untuk proses enkripsi data, sehingga Diffie–Hellman banyak diterapkan pada sistem keamanan komunikasi modern seperti TLS dan VPN.

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
import random

# parameter umum (disepakati publik)
p = 23  # bilangan prima
g = 5   # generator

# private key masing-masing pihak
a = random.randint(1, p-1)  # secret Alice
b = random.randint(1, p-1)  # secret Bob

# public key
A = pow(g, a, p)
B = pow(g, b, p)

# exchange public key
shared_secret_A = pow(B, a, p)
shared_secret_B = pow(A, b, p)

print("Kunci bersama Alice :", shared_secret_A)
print("Kunci bersama Bob   :", shared_secret_B)
```
)

---

## 6. Hasil dan Pembahasan
-Hasil program sudah sesuai dengan ekspektasi. Kunci bersama yang dihitung oleh Alice dan Bob menghasilkan nilai yang sama, yaitu 16. Hal ini menunjukkan bahwa proses Diffie–Hellman berjalan dengan benar, karena meskipun kunci privat yang digunakan berbeda, perhitungan akhirnya menghasilkan shared secret yang sama.

-Pembahasan error
Pada program ini tidak ditemukan error. Kode dapat dijalankan dengan baik dan menghasilkan output yang sesuai dengan teori Diffie–Hellman.
Hasil eksekusi program Caesar Cipher:

![Hasil Eksekusi](screenshots/output.png)
![Hasil Input](screenshots/input.png)
![Hasil Output](screenshots/output.png)
)

---

## 7. Jawaban Pertanyaan
(Jawab pertanyaan diskusi yang diberikan pada modul.  
- Pertanyaan 1: Simulasi protokol Diffie–Hellman dilakukan untuk menunjukkan bagaimana dua pihak dapat bertukar kunci rahasia melalui jaringan publik tanpa mengirimkan kunci tersebut secara langsung. Dalam simulasi ini, kedua pihak menyepakati bilangan prima dan generator sebagai parameter publik, lalu masing-masing menghasilkan kunci privat dan kunci publik untuk dihitung bersama.
- Pertanyaan 2: Mekanisme pertukaran kunci rahasia pada Diffie–Hellman memanfaatkan bilangan prima dan konsep logaritma diskrit. Meskipun nilai publik dapat diketahui oleh pihak lain, kunci privat tetap sulit ditebak karena perhitungan logaritma diskrit pada bilangan besar sangat kompleks dan membutuhkan waktu yang lama.
- Pertanyaan 3: protokol Diffie–Hellman memiliki potensi serangan, salah satunya adalah serangan Man-in-the-Middle (MITM). Pada serangan ini, penyerang dapat menyamar sebagai pihak yang berkomunikasi dan menukar kunci palsu dengan kedua pihak. Akibatnya, penyerang dapat membaca atau memodifikasi pesan. Oleh karena itu, Diffie–Hellman biasanya dikombinasikan dengan mekanisme autentikasi seperti sertifikat digital untuk meningkatkan keamanan
)
---

## 8. Kesimpulan
simulasi protokol Diffie–Hellman berjalan dengan baik dan sesuai dengan teori. Dari hasil perhitungan terlihat bahwa Alice dan Bob berhasil memperoleh kunci rahasia yang sama walaupun masing-masing menggunakan kunci privat yang berbeda. Hal ini menunjukkan bahwa proses pertukaran kunci menggunakan bilangan prima dan operasi modulo telah berhasil dilakukan.

Praktik ini juga memperlihatkan bahwa nilai publik dapat dibagikan secara terbuka tanpa mengungkapkan kunci rahasia. Namun, karena simulasi masih menggunakan bilangan kecil dan belum dilengkapi mekanisme autentikasi, sistem ini masih rentan terhadap serangan seperti Man-in-the-Middle. Oleh sebab itu, pada penerapan nyata diperlukan penggunaan parameter yang lebih besar dan sistem keamanan tambahan agar komunikasi benar-benar aman.

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
