# Laporan Praktikum Kriptografi
Minggu ke-: X  
Topik: [Proyek Kelompok – TinyCoin ERC20]  
Nama: [Zalsabilah nur aeni]  
NIM: [230202793]  
Kelas: [5 IKKA]  

---

## 1. Tujuan
1. Mengembangkan proyek sederhana berbasis algoritma kriptografi.
2. Mendokumentasikan proses implementasi proyek ke dalam repository Git.
3.  Menyusun laporan teknis hasil proyek akhir

## 2. Dasar Teori
1.Blockchain Blockchain adalah teknologi pencatatan data terdistribusi yang menyimpan informasi dalam bentuk blok yang saling terhubung menggunakan kriptografi. Setiap blok berisi data transaksi, hash blok sebelumnya, timestamp, dan hash blok itu sendiri, sehingga membentuk rantai yang bersifat immutabel (tidak mudah diubah). Teknologi blockchain menyediakan transparansi, keamanan, dan desentralisasi tanpa memerlukan pihak ketiga.
2.Cryptocurrency Cryptocurrency merupakan aset digital yang menggunakan kriptografi untuk mengamankan transaksi dan mengontrol penciptaan unit baru. Cryptocurrency berjalan di atas blockchain dan memanfaatkan mekanisme konsensus untuk memvalidasi transaksi. Bitcoin adalah cryptocurrency pertama yang memperkenalkan konsep ini, diikuti oleh Ethereum yang memungkinkan pengembangan aplikasi terdesentralisasi (dApps).
3.Ethereum Ethereum adalah platform blockchain yang mendukung smart contract, yaitu program yang berjalan secara otomatis di jaringan blockchain ketika kondisi tertentu terpenuhi. Ethereum menggunakan Ethereum Virtual Machine (EVM) untuk mengeksekusi smart contract, sehingga pengembang dapat membuat token, aplikasi keuangan terdesentralisasi, dan berbagai layanan berbasis blockchain lainnya.
4.Smart Contract Smart contract adalah kontrak digital yang ditulis dalam bahasa pemrograman (umumnya Solidity) dan dijalankan di blockchain. Smart contract bersifat:
-Otomatis: dieksekusi tanpa perantara
-Transparan: kode dapat diverifikasi publik
-Tidak dapat diubah: setelah dideploy, kode tidak bisa diubah Dalam proyek TinyCoin, smart contract digunakan untuk mengatur logika token seperti transfer, saldo, dan total suplai.
5.Standar Token ERC20 ERC20 merupakan standar teknis untuk pembuatan token di jaringan Ethereum. Standar ini mendefinisikan sekumpulan fungsi dan event wajib agar token dapat berinteraksi dengan wallet dan aplikasi lain. Fungsi utama ERC20 meliputi:
-.totalSupply() : Menampilkan total suplai token
-.balanceOf(address) : Menampilkan saldo alamat tertentu
-.transfer(address, uint256) : Mengirim token
-.approve(address, uint256) : Memberi izin penggunaan token
-.transferFrom(address, address, uint256) : Transfer berdasarkan izin Dengan mengikuti standar ERC20, token seperti TinyCoin dapat digunakan secara luas di ekosistem Ethereum.
6.TinyCoin ERC20 TinyCoin ERC20 adalah token digital yang dikembangkan sebagai proyek pembelajaran berbasis blockchain. Token ini dibuat dengan mengikuti standar ERC20 agar kompatibel dengan wallet Ethereum dan tools pengembangan seperti MetaMask dan Remix IDE. Tujuan pengembangan TinyCoin antara lain:
-Memahami konsep dasar blockchain dan smart contract
-Mengimplementasikan standar ERC20
-Mempelajari mekanisme transaksi token
-Menguji keamanan dan logika smart contract
7.Keamanan Smart Contract Keamanan merupakan aspek penting dalam pengembangan token ERC20. Beberapa risiko yang umum terjadi meliputi:
-Integer overflow dan underflow
-Kesalahan logika pada fungsi transfer
-Penyalahgunaan fungsi approve
-Kurangnya validasi input Oleh karena itu, smart contract harus diuji secara menyeluruh dan mengikuti praktik keamanan yang baik.
8.Peran TinyCoin dalam Proyek Kelompok Dalam proyek kelompok, TinyCoin ERC20 digunakan sebagai studi kasus untuk:
-Pembagian tugas pengembangan
-Simulasi transaksi token
-Evaluasi keamanan smart contract
-Pemahaman kerja sistem keuangan terdesentralisasi Proyek ini membantu mahasiswa memahami penerapan blockchain dan cryptocurrency secara praktis.
9.Kesimpulan TinyCoin ERC20 merupakan implementasi token berbasis Ethereum yang mengikuti standar ERC20. Proyek ini memberikan pemahaman mendalam tentang blockchain, smart contract, dan sistem token digital. Dengan mengembangkan TinyCoin, mahasiswa dapat mempelajari konsep teknis sekaligus tantangan keamanan dalam ekosistem blockchain.

## 3. Alat dan Bahan
(- Python 3.x  
- Visual Studio Code / editor lain  
- Git dan akun GitHub  
- Library tambahan (misalnya pycryptodome, jika diperlukan)  )

---

## 4. Langkah Percobaan
Langkah 1 — Membuat Kontrak ERC20 Contoh kontrak sederhana TinyCoin.sol: // SPDX-License-Identifier: MIT pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";

contract TinyCoin is ERC20 { constructor(uint256 initialSupply) ERC20("TinyCoin", "TNC") { _mint(msg.sender, initialSupply); } }
Langkah 2 — Deploy Kontrak
-Buka Remix IDE → buat file TinyCoin.sol.
-Kompilasi dengan Solidity Compiler.
-Deploy ke jaringan JavaScript VM atau testnet Ethereum.
Catat alamat kontrak hasil deployment.
Langkah 3 — Uji Fungsionalitas
-Cek saldo awal dengan fungsi balanceOf(address).
-Lakukan transfer token dengan fungsi transfer(address, amount).
-Uji apakah total supply tetap konsisten setelah transaksi.
Langkah 4 — Dokumentasi
-Simpan tangkapan layar proses deployment & transaksi.
-Dokumentasikan alur kontrak (fungsi utama: constructor, mint, transfer).
-Tambahkan analisis singkat tentang potensi keamanan smart contract (contoh: reentrancy, overflow – walaupun mitigasi sudah ada di Solidity >=0.8).-

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
Hasil pengujian menunjukkan bahwa perubahan data pada salah satu block menyebabkan ketidaksesuaian nilai hash dan merusak keterkaitan antar block, sehingga sistem blockchain secara otomatis mendeteksi manipulasi data dan menyatakan blockchain tidak valid.. 

Hasil eksekusi program Caesar Cipher:

![Hasil Eksekusi](screenshots/output.png)
![Hasil Input](screenshots/input.png)
![Hasil Output](screenshots/output.png)
)

---

## 7. Jawaban Pertanyaan
(Jawab pertanyaan diskusi yang diberikan pada modul.  
- Pertanyaan 1:  Apa fungsi utama ERC20 dalam ekosistem blockchain? Fungsi utama ERC20 dalam ekosistem blockchain adalah menyediakan standar teknis yang memungkinkan interoperabilitas antara token yang berbeda di jaringan Ethereum. Dengan mengikuti standar ERC20, token dapat dengan mudah digunakan, diperdagangkan, dan diintegrasikan dengan berbagai aplikasi, wallet, dan platform DeFi tanpa memerlukan penyesuaian khusus. Hal ini memfasilitasi adopsi luas dan pengembangan ekosistem token yang lebih dinamis.  
- Pertanyaan 2: Bagaimana mekanisme transfer token bekerja dalam kontrak ERC20? Mekanisme transfer token dalam kontrak ERC20 bekerja melalui fungsi transfer(address recipient, uint256 amount). Ketika fungsi ini dipanggil, kontrak memeriksa apakah pengirim memiliki saldo yang cukup untuk melakukan transfer. Jika saldo mencukupi, jumlah token yang ditransfer dikurangi dari saldo pengirim dan ditambahkan ke saldo penerima. Selain itu, event Transfer dicatat untuk mencatat transaksi tersebut di blockchain. Mekanisme ini memastikan transparansi dan keamanan dalam proses transfer token.
- Pertanyaan 3:Apa risiko utama dalam implementasi smart contract dan bagaimana cara mitigasinya? Risiko utama dalam implementasi smart contract meliputi:
-Reentrancy Attack: Dimana penyerang dapat memanggil kembali fungsi kontrak sebelum eksekusi sebelumnya selesai, yang dapat menyebabkan pencurian dana. Mitigasinya adalah dengan menggunakan pola "checks-effects-interactions" dan mengunci kontrak selama eksekusi.
-Integer Overflow/Underflow: Kesalahan dalam perhitungan angka yang dapat dimanfaatkan untuk menciptakan token secara ilegal. Mitigasinya adalah dengan menggunakan versi Solidity terbaru (>=0.8) yang memiliki pemeriksaan bawaan untuk overflow/underflow.
-Kurangnya Validasi Input: Memungkinkan input yang tidak valid atau berbahaya untuk dieksekusi. Mitigasinya adalah dengan menambahkan validasi ketat pada semua input fungsi.
-Privilege Escalation: Kesalahan dalam pengaturan hak akses yang memungkinkan pengguna tidak sah untuk mengakses fungsi sensitif. Mitigasinya adalah dengan menerapkan kontrol akses yang ketat menggunakan modifier seperti onlyOwner. )

)
---

## 8. Kesimpulan
(Blockchain memiliki tingkat keamanan yang tinggi karena setiap perubahan data akan memengaruhi nilai hash dan keterkaitan antar block, sehingga manipulasi data dapat terdeteksi secara otomatis.)

## 9. Daftar Pustaka
1.Nakamoto, S. (2008). Bitcoin: A Peer-to-Peer Electronic Cash System. https://bitcoin.org/bitcoin.pdf
2.Antonopoulos, A. M. (2017). Mastering Bitcoin: Programming the Open Blockchain (2nd ed.). O’Reilly Media.
3.Antonopoulos, A. M., & Wood, G. (2018). Mastering Ethereum: Building Smart Contracts and DApps. O’Reilly Media.
4.Drescher, D. (2017). Blockchain Basics: A Non-Technical Introduction in 25 Steps. Apress.
5.Tapscott, D., & Tapscott, A. (2016). Blockchain Revolution: How the Technology Behind Bitcoin Is Changing Money, Business, and the World. Penguin Random House.
6.Narayanan, A., Bonneau, J., Felten, E., Miller, A., & Goldfeder, S. (2016). Bitcoin and Cryptocurrency Technologies. Princeton University Press.

## 10. Commit Log
(Tuliskan bukti commit Git yang relevan.  
Contoh:
```
commit abc12345
Author: zalsabilah nur aeni <zalsabilahna@gmail.com>
Date:   2025-09-20

    week2-cryptosystem: implementasi Caesar Cipher dan laporan )
```
