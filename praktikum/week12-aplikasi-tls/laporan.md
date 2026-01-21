# Laporan Praktikum Kriptografi
Minggu ke-: X  
Topik: [ Aplikasi TLS & E-commerce]  
Nama: [Zalsabilah nur aeni]  
NIM: [230202793]  
Kelas: [5 IKKA]  

---

## 1. Tujuan
1.Menganalisis penggunaan kriptografi pada email dan SSL/TLS.
2.Menjelaskan enkripsi dalam transaksi e-commerce.
3.Mengevaluasi isu etika & privasi dalam penggunaan kriptografi di kehidupan sehari-hari.


## 2. Dasar Teori
TLS (Transport Layer Security) adalah protokol keamanan yang digunakan untuk melindungi komunikasi data melalui jaringan. TLS menyediakan tiga pilar utama: enkripsi untuk menjaga kerahasiaan data, integritas untuk memastikan data tidak diubah selama pengiriman, dan autentikasi untuk memverifikasi identitas server melalui sertifikat digital. Protokol ini banyak diterapkan pada website (HTTPS), email, dan aplikasi e-commerce agar komunikasi tetap aman dari serangan pihak ketiga seperti penyadapan dan man-in-the-middle.

Dalam konteks e-commerce, TLS memastikan bahwa data sensitif seperti login, informasi pembayaran, dan detail personal pengguna terlindungi saat dikirim melalui internet. Dengan sertifikat digital yang diterbitkan oleh Certificate Authority (CA) terpercaya, pengguna dapat memverifikasi identitas situs dan melakukan transaksi secara aman. Tanpa TLS, data dikirim dalam bentuk plaintext, sehingga rentan dicuri, dimodifikasi, atau disalahgunakan, sedangkan HTTPS memberikan kepercayaan dan keamanan bagi pengguna selama berbelanja online.
## 3. Alat dan Bahan
(- Python 3.x  
- Visual Studio Code / editor lain  
- Git dan akun GitHub  
- Library tambahan (misalnya pycryptodome, jika diperlukan)  )

---

## 4. Langkah Percobaan
1. Shopee (HTTPS – Aman)
Buka Website
Masuk ke https://shopee.co.id di browser.
Lihat di address bar ada ikon gembok → artinya koneksi aman.
Cek Sertifikat
Klik ikon gembok → pilih “Connection is secure” → “Certificate is valid”.
Catat info penting:
Issued To: nama domain Shopee
Issued By: Certificate Authority (CA) yang terpercaya
Validity: masa berlaku sertifikat
Public Key & Algoritma Signature
Analisis TLS / HTTPS
Tekan F12 → Tab Security
Lihat: versi TLS (misal TLS 1.2 atau TLS 1.3)
Lihat cipher suite yang dipakai
Pastikan data login, keranjang, atau pembayaran terenkripsi → aman dari hacker
2. NeverSSL (HTTP – Tidak Aman)
Buka Website
Masuk ke http://www.neverssl.com/ di browser.
Di address bar muncul peringatan “Not secure” → koneksi nggak terenkripsi.
Cek Peringatan Browser
Klik ikon info (i) → lihat peringatan & risiko:
Data dikirim plaintext, bisa dibaca orang lain di jaringan yang sama
Tidak ada verifikasi server → bisa jadi target phishing atau MITM
Analisis Risiko
Tekan F12 → Tab Security → hampir semua informasi TLS kosong / tidak tersedia
Artinya: login, password, atau data apapun yang dikirim lewat situs ini tidak aman

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
1 Analisis Shopee (HTTPS – Aman)
Observasi:
Di address bar ada ikon gembok → koneksi aman.
Sertifikat diterbitkan oleh trusted CA, masa berlaku masih aktif, public key kuat (RSA 2048-bit), dan algoritma hash SHA-256.
TLS 1.2 / TLS 1.3 aktif, cipher suite modern digunakan.
Analisis:
Data terenkripsi → password, info pembayaran, dan data pribadi aman dari hacker.
Autentikasi server → browser bisa pastikan ini benar-benar Shopee.
Integritas data → data tidak bisa diubah selama transmisi.
Kesimpulan:
Shopee aman buat transaksi online karena HTTPS + TLS aktif.
Risiko hacker / MITM sangat kecil.
Hasil eksekusi program Caesar Cipher:
2 Analisis NeverSSL (HTTP – Tidak Aman)
Observasi:
Di address bar muncul peringatan “Not secure” → koneksi tidak terenkripsi.
Tidak ada sertifikat digital, TLS tidak aktif, data dikirim plaintext.
Analisis:
Data mudah dicuri → hacker di jaringan yang sama bisa baca password atau informasi lain.
Tidak ada autentikasi server → bisa terjadi phishing atau impersonation.
Tidak ada integritas data → data bisa diubah hacker sebelum sampai ke user.
Kesimpulan:
NeverSSL tidak aman untuk login atau transaksi online.
Semua informasi yang dikirim bisa dicegat atau dimodifikasi.

![Hasil Eksekusi](screenshots/output.png)
![Hasil Input](screenshots/input.png)
![Hasil Output](screenshots/output.png)
)

---

## 7. Jawaban Pertanyaan
(Jawab pertanyaan diskusi yang diberikan pada modul.  
- Pertanyaan 1: Perbedaan HTTP vs HTTPS
HTTP: data dikirim tidak terenkripsi, gampang disadap, browser kasih tanda “Not Secure”.
HTTPS: data terenkripsi pakai TLS, ada gembok di browser, server terverifikasi pakai sertifikat digital → aman dari hacker dan MITM. 
- Pertanyaan 2:Pentingnya Sertifikat Digital
Sertifikat digital itu kayak ID resmi website. Browser pakai buat ngecek server asli, mencegah penipuan, dan pastiin enkripsi jalan dengan benar. Tanpa sertifikat, HTTPS nggak ada gunanya.
-Pertanyaan 3:Kriptografi & Privasi vs Tantangan Hukum
Kriptografi bikin data aman dan privasi terlindungi, misal chat atau transaksi online. Tapi bikin penegak hukum susah akses kalau terjadi kejahatan → dilema antara privasi dan keamanan publik. Solusi: kebijakan & oversight, bukan backdoor.  
)
---

## 8. Kesimpulan
TLS/SSL itu penting banget buat amankan komunikasi online. Website e-commerce pakai HTTPS supaya data user terenkripsi, transaksi aman, dan identitas server terverifikasi. Tanpa TLS, info sensitif seperti password dan kartu kredit gampang dicuri. Sertifikat digital jadi fondasi kepercayaan, sementara kriptografi menjaga privasi, walau ada tantangan hukum kalau penegak hukum butuh akses. Jadi, TLS + sertifikat = wajib untuk transaksi online yang aman dan terpercaya.
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
Author: zalsabilah nur aeni <zalsabilahna@gmail.com>
Date:   2025-09-20

    week2-cryptosystem: implementasi Caesar Cipher dan laporan )
```
