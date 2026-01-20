# Laporan Praktikum Kriptografi
Minggu ke-: X  
Topik: [Secret Sharing]  
Nama: [Zalsabilah nur aeni]  
NIM: [230202793]  
Kelas: [5 IKKA]  

---

## 1. Tujuan
1. konsep Shamir Secret Sharing (SSS).
2.Melakukan simulasi pembagian rahasia ke beberapa pihak menggunakan skema SSS.
3.Menganalisis keamanan skema distribusi rahasia.

---

## 2. Dasar Teori
Secret Sharing adalah metode kriptografi untuk membagi sebuah informasi rahasia menjadi beberapa bagian (share) yang dibagikan ke beberapa pihak. Rahasia asli hanya dapat diketahui kembali jika sejumlah share tertentu digabungkan sesuai ketentuan, sedangkan satu atau beberapa share saja tidak cukup untuk mengetahui isi rahasia.

Metode ini bertujuan meningkatkan keamanan dan keandalan data, karena tidak ada satu pihak pun yang memegang rahasia secara utuh. Secret Sharing banyak digunakan pada sistem keamanan tingkat tinggi, seperti penyimpanan kunci kriptografi, sistem pemulihan data, dan pengelolaan akses bersama.

## 3. Alat dan Bahan
(- Python 3.x  
- Visual Studio Code / editor lain  
- Git dan akun GitHub  
- Library tambahan (misalnya pycryptodome, jika diperlukan)  )

---

## 4. Langkah Percobaan
1.Membuat folder struktur praktikum/week11-secret-sharing/src/ dan screenshots/.
2. file secret-sharing.py di folder src/.
3.Mengimplementasikan fungsi buat_polinomial() untuk membuat koefisien polinomial acak dengan rahasia sebagai konstanta.
4.Mengimplementasikan fungsi hitung_share() untuk mengevaluasi polinomial di titik x tertentu.
5.Mengimplementasikan fungsi rekonstruksi_rahasia() menggunakan Lagrange Interpolation.
6.Melakukan uji coba dengan rahasia = 1234, threshold = 3, dan total shares = 5.
7.Menguji rekonstruksi dengan mengambil random 3 shares dari 5 shares yang ada.
8.Menjalankan program dengan perintah python secret-sharing.py.
9.Mengambil screenshot hasil eksekusi program.
10.Membuat laporan dan melakukan commit ke Git.

## 5. Source Code
import random
from decimal import Decimal

def buat_polinomial(rahasia, threshold):
    """
    Membuat koefisien polinomial acak.
    Rahasia adalah a0 (konstanta).
    Persamaan: f(x) = rahasia + a1*x + a2*x^2 + ... + a(k-1)*x^(k-1)
    """
    koefisien = [rahasia]  
    for _ in range(threshold - 1):
        koefisien.append(random.randint(1, 100))
    return koefisien

def hitung_share(x, koefisien):
    """
    Menghitung y untuk nilai x tertentu berdasarkan polinomial.
    y = a0 + a1*x + a2*x^2 ...
    """
    y = 0
    for pangkat, koef in enumerate(koefisien):
        y += koef * (x ** pangkat)
    return y

def rekonstruksi_rahasia(shares):
    """
    Menggunakan Lagrange Interpolation untuk mencari nilai y saat x=0.
    """
    x_s = [s[0] for s in shares]
    y_s = [s[1] for s in shares]
    
    # Mencari f(0)
    rahasia = 0
    for i in range(len(shares)):
        pembilang, penyebut = 1, 1
        for j in range(len(shares)):
            if i != j:
                pembilang *= (0 - x_s[j])   
                penyebut *= (x_s[i] - x_s[j])
        
        lagrange_term = y_s[i] * (pembilang / penyebut)
        rahasia += lagrange_term
        
    return int(round(rahasia))


# Konfigurasi
RAHASIA_SAYA = 1234
JUMLAH_SHARE = 5
MINIMAL_BUTUH = 3 

# Generate polynomial dan shares
koefisien = buat_polinomial(RAHASIA_SAYA, MINIMAL_BUTUH)

daftar_share = []
for i in range(1, JUMLAH_SHARE + 1):
    y = hitung_share(i, koefisien)
    daftar_share.append((i, y))

print(f"Rahasia Asli: {RAHASIA_SAYA}")
print(f"Shares dibagikan: {daftar_share}")

# Test rekonstruksi dengan random 3 shares
share_yang_ada = random.sample(daftar_share, 3) 
print(f"Mencoba membuka dengan share: {share_yang_ada}")

hasil = rekonstruksi_rahasia(share_yang_ada)
print(f"Rahasia terungkap: {hasil}")

---

## 6. Hasil dan Pembahasan
Program ini membagi sebuah rahasia (1234) ke dalam 5 share menggunakan polinomial derajat 2 (threshold = 3). Rahasia disimpan sebagai konstanta polinomial (a₀), sedangkan koefisien lainnya dibuat secara acak. Setiap share berbentuk pasangan (x, y) yang dihitung dari nilai polinomial.

Rekonstruksi rahasia dilakukan menggunakan Interpolasi Lagrange dengan mengambil 3 share secara acak. Saat interpolasi dihitung pada x = 0, nilai rahasia asli berhasil diperoleh kembali. Hasil ini menunjukkan bahwa minimal 3 share dapat membuka rahasia, sedangkan jumlah share di bawah threshold tidak cukup untuk mengungkap rahasia, sesuai konsep Shamir Secret Sharing. 

Hasil eksekusi program Caesar Cipher:

![Hasil Eksekusi](screenshots/output.png)
![Hasil Input](screenshots/input.png)
![Hasil Output](screenshots/output.png)
)

---

## 7. Jawaban Pertanyaan
(Jawab pertanyaan diskusi yang diberikan pada modul.  
- Pertanyaan 1: Keuntungan utama Shamir Secret Sharing (SSS)
Keuntungan utama SSS adalah meningkatkan keamanan karena kunci rahasia tidak disimpan dalam satu salinan utuh. Setiap pihak hanya memegang sebagian rahasia, sehingga jika satu share bocor, kunci asli tetap aman. Berbeda dengan membagikan salinan kunci secara langsung yang berisiko tinggi jika salah satu salinan dicuri.
- Pertanyaan 2: Peran threshold (k) dalam keamanan secret sharing
Threshold (k) menentukan jumlah minimum share yang harus digabungkan untuk membentuk kembali rahasia. Jika jumlah share kurang dari k, rahasia tidak dapat diketahui sama sekali. Semakin besar nilai k, semakin tinggi tingkat keamanannya, karena dibutuhkan lebih banyak pihak untuk membuka rahasia.
- Pertanyaan 3:Contoh skenario nyata penggunaan SSS
SSS sangat bermanfaat dalam penyimpanan kunci master perusahaan, misalnya kunci akses server pusat dibagi kepada beberapa manajer. Kunci hanya bisa digunakan jika minimal beberapa manajer hadir bersama, sehingga mencegah penyalahgunaan oleh satu orang saja.
)
---

## 8. Kesimpulan
Berdasarkan implementasi dan pengujian Shamir Secret Sharing, dapat disimpulkan bahwa metode ini efektif untuk mengamankan sebuah rahasia dengan cara membaginya menjadi beberapa share. Rahasia hanya dapat direkonstruksi jika jumlah share yang digunakan memenuhi nilai threshold yang ditentukan. Dengan demikian, Shamir Secret Sharing mampu meningkatkan keamanan data karena mencegah satu pihak saja memiliki akses penuh terhadap rahasia dan dapat diterapkan pada berbagai sistem keamanan digital.

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
Author: Zalsabilah nur aeni <zalsabilahna@gmail.com>
Date:   2025-09-20

    week2-cryptosystem: implementasi Caesar Cipher dan laporan )
```
