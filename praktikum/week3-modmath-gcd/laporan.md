# Laporan Praktikum Kriptografi
Minggu ke-: X  
Topik: [modular math]  
Nama: [zalsabilah nur aeni]  
NIM: [230202793]  
Kelas: [5 IKKA]  

---

## 1. Tujuan
1.Menyelesaikan operasi aritmetika modular.
2.Menentukan bilangan prima dan menghitung GCD (Greatest Common Divisor).
3.Menerapkan logaritma diskrit sederhana dalam simulasi kriptografi.

## 2. Dasar Teori
Aritmetika modulo adalah sistem perhitungan yang mengambil hasil berdasarkan sisa pembagian suatu bilangan terhadap modulus tertentu. Dua bilangan dianggap kongruen jika selisihnya merupakan kelipatan modulus, ditulis sebagai a ≡ b (mod n). Prinsip ini membuat perhitungan bersifat siklik, karena setiap operasi selalu dipetakan kembali ke rentang 0 sampai n−1.

Konsep ini banyak dipakai dalam berbagai bidang, mulai dari hitungan sehari-hari seperti sistem jam hingga komputasi yang lebih kompleks. Dalam kriptografi, modular math menjadi dasar algoritma penting seperti RSA, terutama karena operasi perpangkatan dan invers modulo sangat sulit dibalik tanpa informasi khusus. Hal inilah yang menjadikan aritmetika modulo sebagai konsep fundamental dalam keamanan data dan matematika terapan.

---

## 3. Alat dan Bahan
(- Python 3.x  
- Visual Studio Code / editor lain  
- Git dan akun GitHub  
- Library tambahan (misalnya pycryptodome, jika diperlukan)  )

---

## 4. Langkah Percobaan
1.Tuliskan fungsi untuk menghitung operasi modular dasar.
2.Implementasikan fungsi GCD dengan algoritma Euclidean.
3.Tambahkan fungsi untuk mencari invers modular.
4.Simulasikan logaritma diskrit sederhana


---

## 5. Source Code
def gcd(a, b):
    """Menghitung GCD menggunakan algoritma Euclidean"""
    while b != 0:
        a, b = b, a % b
    return abs(a)

def extended_gcd(a, b):
    """Versi extended untuk mencari x, y sehingga ax + by = gcd(a, b)"""
    if b == 0:
        return a, 1, 0
    else:
        g, x1, y1 = extended_gcd(b, a % b)
        return g, y1, x1 - (a // b) * y1

def mod_inv(a, m):
    """Mencari invers modular dari a (jika ada)"""
    g, x, _ = extended_gcd(a, m)
    if g != 1:
        raise ValueError(f"Tidak ada invers modular untuk {a} mod {m}")
    return x % m


## 6. Hasil dan Pembahasan
(- Lampirkan screenshot hasil eksekusi program (taruh di folder `screenshots/`).  
- Berikan tabel atau ringkasan hasil uji jika diperlukan.  
- Jelaskan apakah hasil sesuai ekspektasi.  
- Bahas error (jika ada) dan solusinya. 

Hasil eksekusi program Caesar Cipher:

![Hasil Eksekusi](screenshots/output.png)
![Hasil Input](screenshots/input.png)
![Hasil Output](screenshots/output.png)
)

---

## 7. Jawaban Pertanyaan
- Pertanyaan 1: Aritmetika modular menjadi dasar utama berbagai algoritma kriptografi karena sifatnya yang “siklik” dan sulit dibalik ketika melibatkan bilangan besar. Operasi seperti perpangkatan modular, invers modular, dan kongruensi banyak digunakan untuk membuat proses enkripsi dan dekripsi aman. Algoritma besar seperti RSA, Diffie–Hellman, dan ElGamal semuanya bergantung pada perhitungan modulo dengan bilangan prima besar untuk menciptakan fungsi satu arah yang sulit dipecahkan tanpa kunci rahasia.
- Pertanyaan 2: Invers modular diperlukan untuk menghitung kunci dekripsi pada RSA. Setelah menentukan e dan φ(n), kita harus mencari nilai d sehingga d ≡ e⁻¹ (mod φ(n)). Nilai d inilah yang memungkinkan pesan yang sudah dipangkatkan dengan e dapat dikembalikan ke bentuk aslinya. Tanpa invers modular, proses mencocokkan kunci publik dan kunci privat tidak bisa dilakukan, sehingga mekanisme RSA tidak akan berfungsi
- pertanyaan 3: Kesulitan terbesar ada pada kompleksitas komputasi. Logaritma diskrit sangat sulit diselesaikan ketika modulusnya besar (ratusan hingga ribuan bit), karena tidak ada algoritma efisien yang mampu menyelesaikannya dalam waktu wajar. Metode brute-force atau algoritma klasik membutuhkan waktu eksponensial, sehingga memecah kunci yang berbasis logaritma diskrit dianggap sangat tidak praktis. Inilah yang membuat protokol seperti Diffie–Hellman dan ElGamal tetap aman.
)
---

## 8. Kesimpulan
Kode tersebut mengimplementasikan tiga fungsi utama dalam aritmetika modul, yaitu perhitungan GCD, extended GCD, dan invers modular. Fungsi gcd() menentukan pembagi terbesar dari dua bilangan, sedangkan extended_gcd() memperluas proses tersebut untuk menemukan koefisien yang memenuhi persamaan ax + by = gcd(a, b), sehingga dapat digunakan untuk operasi lanjutan.

Fungsi mod_inv() memanfaatkan hasil extended GCD untuk menentukan apakah sebuah bilangan memiliki invers modulo terhadap suatu modulus. Jika GCD bernilai 1, invers dapat dihitung dan dikembalikan; jika tidak, invers tidak ada. Secara keseluruhan, ketiga fungsi ini merupakan dasar penting dalam banyak algoritma kriptografi yang membutuhkan operasi modulo tingkat lanjut

---

## 9. Daftar Pustaka
1,Rosen, K. H. Discrete Mathematics and Its Applications. McGraw-Hill.
https://books.google.com/books?id=8Y0VMwEACAAJ

2.Stallings, W. Cryptography and Network Security: Principles and Practice. Pearson.
https://www.pearson.com/en-us/subject-catalog/p/cryptography-and-network-security/P200000006584/9780134444284

---

## 10. Commit Log
(Tuliskan bukti commit Git yang relevan.  
Contoh:
```
commit week 3
Author: zalsabilah nur aeni <230202793>
Date:   2025-011-2

    week2-cryptosystem: implementasi Caesar Cipher dan laporan )
```
