# Laporan Praktikum Kriptografi
Minggu ke-: 9
Topik: [Digital Signature ]  
Nama: [Zalsabilah Nur Aeni]  
NIM: [230202793]  
Kelas: [5 ikka]  

---

## 1. Tujuan
1.Mengimplementasikan tanda tangan digital menggunakan algoritma RSA/DSA.
2.Memverifikasi keaslian tanda tangan digital.
3.Menjelaskan manfaat tanda tangan digital dalam otentikasi pesan dan integritas data.

---

## 2. Dasar Teori
Digital signature atau tanda tangan digital adalah teknik kriptografi yang digunakan untuk memastikan keaslian pengirim, keutuhan data, dan mencegah penyangkalan terhadap suatu dokumen digital. Prosesnya dilakukan dengan membuat tanda tangan menggunakan kunci privat pengirim terhadap hash dari pesan. Penerima kemudian melakukan verifikasi menggunakan kunci publik untuk memastikan bahwa pesan tidak berubah dan benar berasal dari pengirim yang sah.

RSA dan DSA merupakan algoritma yang umum digunakan dalam digital signature. RSA bekerja dengan sistem kunci publik dan privat yang berbasis perhitungan bilangan prima besar. Sedangkan DSA dirancang khusus untuk tanda tangan digital dan menggunakan konsep logaritma diskret. Keduanya banyak diterapkan dalam sistem keamanan digital seperti transaksi online dan sertifikat digital.

## 3. Alat dan Bahan
(- Python 3.x  
- Visual Studio Code / editor lain  
- Git dan akun GitHub  
- Library tambahan (misalnya pycryptodome, jika diperlukan)  )

---

## 4. Langkah Percobaan
1.Membuat folder struktur praktikum/week9-digital-signature/src/ dan screenshots/.
2.Install library pycryptodome dengan perintah pip install pycryptodome.
3.Mengimplementasikan class DigitalSignature dalam file src/digital-signature.py.
4.Implementasi method hash_message() untuk menghasilkan hash SHA-256 dari pesan.
5.Implementasi method create_signature() untuk membuat tanda tangan digital menggunakan private key.
6.Implementasi method verify_signature() untuk memverifikasi tanda tangan menggunakan public key.
7.Melakukan uji verifikasi dengan pesan asli (harus berhasil).
8.Melakukan uji verifikasi dengan pesan yang dimodifikasi (harus gagal).
9.Menjalankan program dengan perintah python digital-signature.py.
10.Mengambil screenshot hasil eksekusi program.
## 5. Source Code
from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256


class DigitalSignature:
    def __init__(self, key_size=2048) -> None:
        self.key = RSA.generate(key_size)
        self.private_key = self.key
        self.public_key = self.key.publickey()

    def hash_message(self, message) -> SHA256.SHA256Hash:
        """
        Menghasilkan hash SHA-256 dari pesan yang diberikan.
        """
        return SHA256.new(message)
    
    def create_signature(self, message_hash) -> str:
        """
        Membuat tanda tangan digital menggunakan kunci privat dan hash pesan.
        """
        signature = pkcs1_15.new(self.private_key).sign(message_hash)
        return signature.hex()

    def verify_signature(self, message_hash, signature) -> str:
        """
        Memverifikasi tanda tangan digital menggunakan kunci publik, hash pesan, dan tanda tangan.
        """
        try:
            pkcs1_15.new(self.public_key).verify(message_hash, bytes.fromhex(signature))
            return "The signature is valid."
        except (ValueError, TypeError):
            return "The signature is not valid."


signer = DigitalSignature()

# verefikasi tanda tangan digital
message = b"hello, anggap saja ini adalah pesan penting"
msg_hash = signer.hash_message(message)
signature = signer.create_signature(msg_hash)
print(signature)
verification_result = signer.verify_signature(msg_hash, signature)
print(f"verefiasi true msg: {verification_result}")

# mencoba verifikasi dengan pesan yang diubah
fake_message = b"hello, anggap saja ini adalah pesan palsu"
fake_hash_message = signer.hash_message(fake_message)
verification_fake = signer.verify_signature(fake_hash_message, signature)
print(f"verefiasi fake msg: {verification_fake}")

---

## 6. Hasil dan Pembahasan
1. Pembuatan Tanda Tangan Digital
Pesan asli: "hello, anggap saja ini adalah pesan penting"
Key size: 2048 bit RSA
Hash algorithm: SHA-256
Signature: String heksadesimal panjang (256 byte = 512 karakter hex)
Status: Berhasil (tanda tangan digital berhasil dibuat menggunakan kunci privat)

2. Verifikasi Pesan Asli
Input: Hash pesan asli dan signature
Output: "The signature is valid."
Status: Berhasil (tanda tangan valid dan pesan tidak berubah)

3. Verifikasi Pesan Palsu
Pesan dimodifikasi: "hello, anggap saja ini adalah pesan palsu"
Input: Hash pesan palsu dan signature yang sama
Output: "The signature is not valid."
Status: Berhasil mendeteksi perubahan pesan (tanda tangan tidak valid)

Hasil eksekusi program Caesar Cipher:

![Hasil Eksekusi](screenshots/output.png)
![Hasil Input](screenshots/input.png)
![Hasil Output](screenshots/output.png)
)

---

## 7. Jawaban Pertanyaan
(Jawab pertanyaan diskusi yang diberikan pada modul.  
- Pertanyaan 1: Perbedaan enkripsi RSA dan tanda tangan digital RSA
Enkripsi RSA digunakan untuk menjaga kerahasiaan pesan agar tidak bisa dibaca orang lain. Tanda tangan digital RSA digunakan untuk memastikan pesan benar dari pengirim dan tidak diubah isinya  
- Pertanyaan 2: Mengapa tanda tangan digital menjamin integritas dan otentikasi
Integritas terjamin karena tanda tangan dibuat dari hash pesan, sehingga jika pesan diubah, tanda tangan tidak akan valid. Otentikasi terjamin karena hanya pemilik kunci privat yang bisa membuat tanda tangan tersebut.
- Pertanyaan 3: Peran Certificate Authority (CA)
CA adalah pihak tepercaya yang memastikan kunci publik benar milik seseorang atau organisasi. Dengan adanya CA, pengguna bisa yakin bahwa tanda tangan digital berasal dari pihak yang sah.
)
---

## 8. Kesimpulan
tanda tangan digital berbasis RSA berperan penting dalam menjaga keamanan komunikasi digital. Tanda tangan digital mampu menjamin keaslian pengirim dan keutuhan pesan, karena setiap perubahan data dapat terdeteksi melalui proses verifikasi. Selain itu, perbedaan antara enkripsi dan tanda tangan digital menunjukkan bahwa keamanan informasi tidak hanya tentang kerahasiaan, tetapi juga tentang kepercayaan dan keabsahan data. Peran Certificate Authority (CA) semakin memperkuat sistem ini dengan memastikan bahwa kunci publik yang digunakan benar-benar milik pihak yang sah, sehingga tanda tangan digital dapat diterapkan secara aman dalam sistem digital modern.

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
Author: Zalsabilah Nur Aeni <zalsabilahna@gmail.com>
Date:   2025-09-20

    week2-cryptosystem: implementasi Caesar Cipher dan laporan )
```
