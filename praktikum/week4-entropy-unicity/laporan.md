# Laporan Praktikum Kriptografi
Minggu ke-:[ 4]
Topik: [Entropy & Unicity Distance ]  
Nama: [Zalsabilah nur aeni]  
NIM: [230202793]  
Kelas: [5 ikka]  

---

## 1. Tujuan
1.Menyelesaikan perhitungan sederhana terkait entropi kunci.
2.Menggunakan teorema Euler pada contoh perhitungan modular & invers.
3.Menghitung unicity distance untuk ciphertext tertentu.
4.Menganalisis kekuatan kunci berdasarkan entropi dan unicity distance.
5.Mengevaluasi potensi serangan brute force pada kriptosistem sederhana.


---

## 2. Dasar Teori
Entropy merupakan ukuran tingkat ketidakpastian atau keacakan suatu informasi. Dalam kriptografi, entropy digunakan untuk menilai seberapa acak data atau kunci yang dipakai dalam proses enkripsi. Semakin besar nilai entropy, maka semakin sulit pola data tersebut ditebak, sehingga tingkat keamanan informasi menjadi lebih tinggi.

Unicity Distance adalah ukuran yang menunjukkan jumlah minimum ciphertext yang diperlukan untuk menemukan kunci enkripsi secara unik. Konsep ini berkaitan dengan ukuran ruang kunci dan tingkat redundansi bahasa. Nilai unicity distance yang besar menandakan bahwa sistem kriptografi membutuhkan lebih banyak data untuk dipecahkan, sehingga lebih aman terhadap serangan kriptoanalisis

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
def brute_force_time(keyspace_size, attempts_per_second=1e6):
    seconds = keyspace_size / attempts_per_second
    days = seconds / (3600*24)
    return days

print("Waktu brute force Caesar Cipher (26 kunci) =", brute_force_time(26), "hari")
print("Waktu brute force AES-128 =", brute_force_time(2**128), "hari")
)

---

## 6. Hasil dan Pembahasan
Hasil perhitungan tersebut sudah sesuai dengan ekspektasi. Caesar Cipher memiliki ruang kunci yang sangat kecil, yaitu 26 kemungkinan, sehingga waktu yang dibutuhkan untuk melakukan brute force sangat singkat dan hampir tidak berarti. Sebaliknya, AES-128 memiliki ruang kunci sebesar 2^128 yang sangat besar, sehingga waktu brute force menjadi sangat lama dan secara praktis tidak mungkin dilakukan dengan kemampuan komputasi saat ini.

Kode program tidak mengalami kesalahan secara penulisan dan dapat dijalankan dengan baik. Namun, perhitungan ini menggunakan asumsi kecepatan brute force yang tetap, yaitu 1 juta percobaan per detik, yang belum tentu sesuai dengan kondisi nyata. Untuk meningkatkan akurasi, nilai kecepatan percobaan dapat disesuaikan atau hasil perhitungan dapat ditampilkan dalam satuan waktu yang lebih besar, seperti tahun, agar lebih mudah dipahami.

Hasil eksekusi program Caesar Cipher:

![Hasil Eksekusi](screenshots/output.png)
![Hasil Input](screenshots/input.png)
![Hasil Output](screenshots/output.png)
)

---

## 7. Jawaban Pertanyaan
(Jawab pertanyaan diskusi yang diberikan pada modul.  
- Pertanyaan 1: Entropy menunjukkan tingkat keacakan dan ketidakpastian sebuah kunci. Semakin besar nilai entropy, semakin banyak kemungkinan kunci yang harus ditebak sehingga kunci menjadi lebih sulit dipecahkan dan keamanannya lebih kuat.
- Pertanyaan 2: Unicity distance penting karena menunjukkan jumlah minimum ciphertext yang dibutuhkan untuk menentukan kunci secara unik. Jika data terenkripsi melebihi batas ini, maka secara teori cipher dapat dipecahkan, sehingga membantu menilai batas keamanan suatu sistem kriptografi.
- Pertanyaan 3: Brute force tetap menjadi ancaman meskipun algoritma kuat karena sering kali kunci yang digunakan lemah, terjadi kesalahan implementasi, atau adanya peningkatan kemampuan komputasi. Oleh karena itu, keamanan tidak hanya bergantung pada algoritma, tetapi juga pada kekuatan kunci dan cara penggunaannya.
)
---

## 8. Kesimpulan
Berdasarkan hasil perhitungan, Caesar Cipher memiliki waktu brute force yang sangat singkat (hampir nol hari) karena ruang kuncinya kecil, sehingga tidak aman untuk digunakan. Sebaliknya, AES-128 membutuhkan waktu brute force yang sangat lama (hingga triliunan tahun), sehingga secara praktis mustahil dipecahkan dengan brute force. Hal ini menunjukkan bahwa semakin besar ruang kunci (entropy), semakin kuat tingkat keamanannya terhadap serangan brute force.

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
