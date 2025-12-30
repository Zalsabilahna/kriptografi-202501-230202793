# Laporan Praktikum Kriptografi
Minggu ke-: X  
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
(Salin kode program utama yang dibuat atau dimodifikasi.  
Gunakan blok kode:

```python
# contoh potongan kode
def encrypt(text, key):
    return ...
```
)

---

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
(Jawab pertanyaan diskusi yang diberikan pada modul.  
- Pertanyaan 1: …  
- Pertanyaan 2: …  
)
---

## 8. Kesimpulan
(Tuliskan kesimpulan singkat (2–3 kalimat) berdasarkan percobaan.  )

---

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
