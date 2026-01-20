# Laporan Praktikum Kriptografi
Minggu ke-: X  
Topik: [TinyChain – Proof of Work (PoW)]  
Nama: [zalsabilah nur aeni]  
NIM: [230202793]  
Kelas: [5 IKKA]  

---

## 1. Tujuan
1.Menjelaskan peran hash function dalam blockchain.
2.Melakukan simulasi sederhana Proof of Work (PoW).
3.Menganalisis keamanan cryptocurrency berbasis kriptografi.

---

## 2. Dasar Teori
TinyChain – Proof of Work (PoW) merupakan simulasi sederhana dari teknologi blockchain yang menerapkan mekanisme Proof of Work untuk menambahkan blok baru ke dalam rantai. Dalam sistem ini, setiap blok harus melalui proses penambangan, yaitu pencarian nilai tertentu yang memenuhi syarat yang telah ditentukan sebelumnya.

Pada mekanisme PoW, penambang harus melakukan perhitungan komputasi sebagai bukti usaha sebelum sebuah blok dinyatakan valid. Proses ini berfungsi untuk menjaga keamanan blockchain, karena perubahan data pada satu blok akan membutuhkan usaha komputasi ulang yang besar, sehingga mencegah manipulasi data secara sepihak.

---

## 3. Alat dan Bahan
(- Python 3.x  
- Visual Studio Code / editor lain  
- Git dan akun GitHub  
- Library tambahan (misalnya pycryptodome, jika diperlukan)  )

---

## 4. Langkah Percobaan
1. Membuat Struktur Project
Struktur folder dibuat pada direktori praktikum/week13-tinychain/ yang terdiri dari file program utama tinychain.py, file blockchain.json untuk penyimpanan data blockchain, folder screenshots untuk dokumentasi hasil eksekusi, serta laporan.md sebagai laporan praktikum.

2. Implementasi Class Block
Class Block dibuat dengan atribut index, previous_hash, data, timestamp, nonce, dan hash. Method calculate_hash() digunakan untuk menghasilkan hash menggunakan SHA-256. Method mine_block(difficulty) menerapkan Proof of Work. Method to_dict() dan from_dict() digunakan untuk proses penyimpanan dan pemanggilan data blok.

3. Implementasi Class Blockchain
Class Blockchain berisi list chain dan parameter difficulty. Method create_genesis_block() membuat blok pertama. Method add_block() menambahkan blok baru melalui proses mining. Method is_chain_valid() digunakan untuk memeriksa keutuhan blockchain. Fitur penyimpanan data ditangani dengan save_to_file() dan load_from_file().

4. Testing dan Mining
Program dijalankan menggunakan python tinychain.py untuk melakukan mining 3 blok dengan data transaksi berbeda. Setelah itu, integritas blockchain diuji, data disimpan ke file JSON, lalu dilakukan pengujian load dari file. Hasil eksekusi diambil dalam bentuk screenshot.

5. Dokumentasi
Screenshot hasil mining dan isi blockchain disertakan dalam laporan analisis. Seluruh file project kemudian di-commit ke repository Git sebagai dokumentasi akhir praktikum.
---

## 5. Source Code
import hashlib
import time
import json


class Block:
    def __init__(self, index, previous_hash, data, timestamp=None):
        self.index = index
        self.previous_hash = previous_hash
        self.data = data
        self.timestamp = timestamp or time.time()
        self.nonce = 0
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        """
        Menghitung SHA-256 hash dari block contents.
        Hash dihitung dari: index + timestamp + data + nonce
        """
        value = str(self.index) + str(self.timestamp) + str(self.data) + str(self.nonce)
        return hashlib.sha256(value.encode()).hexdigest()

    def mine_block(self, difficulty):
        """
        Implementasi Proof of Work.
        Mencari nonce sehingga hash dimulai dengan 'difficulty' leading zeros.
        """
        target = "0" * difficulty
        while self.hash[:difficulty] != target:
            self.nonce += 1
            self.hash = self.calculate_hash()
        print(f"Block mined: {self.hash}")

    def to_dict(self):
        """Konversi block ke dictionary untuk serialization"""
        return {
            'index': self.index,
            'previous_hash': self.previous_hash,
            'data': self.data,
            'timestamp': self.timestamp,
            'nonce': self.nonce,
            'hash': self.hash
        }

    @staticmethod
    def from_dict(block_dict):
        """Rekonstruksi block dari dictionary"""
        block = Block.__new__(Block)
        block.index = block_dict['index']
        block.previous_hash = block_dict['previous_hash']
        block.data = block_dict['data']
        block.timestamp = block_dict['timestamp']
        block.nonce = block_dict['nonce']
        block.hash = block_dict['hash']
        return block


class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
        self.difficulty = 4  # Difficulty level (jumlah leading zeros)

    def create_genesis_block(self):
        """Membuat genesis block (blok pertama dalam chain)"""
        return Block(0, "0", "Genesis Block")

    def get_last_block(self):
        """Mengambil blok terakhir dalam chain"""
        return self.chain[-1]

    def add_block(self, new_block):
        """
        Menambahkan blok baru ke chain.
        Blok akan di-mine dengan Proof of Work sebelum ditambahkan.
        """
        new_block.previous_hash = self.get_last_block().hash
        new_block.mine_block(self.difficulty)
        self.chain.append(new_block)

    def is_chain_valid(self):
        """
        Validasi integritas blockchain.
        Memeriksa:
        1. Hash setiap blok benar (recalculate dan compare)
        2. Previous hash link valid (tidak ada broken chain)
        """
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i - 1]

            # Validasi hash integrity
            if current.hash != current.calculate_hash():
                return False
            
            # Validasi chain link
            if current.previous_hash != previous.hash:
                return False
        
        return True

    def save_to_file(self, filename="praktikum/week13-tinychain/logs/blockchain.json"):
        """Menyimpan blockchain ke file JSON"""
        data = {
            'difficulty': self.difficulty,
            'chain': [block.to_dict() for block in self.chain]
        }
        with open(filename, 'w') as f:
            json.dump(data, f, indent=2)
        print(f"Blockchain saved to {filename}")

    def load_from_file(self, filename="praktikum/week13-tinychain/logs/blockchain.json"):
        """Memuat blockchain dari file JSON"""
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
            
            self.difficulty = data['difficulty']
            self.chain = [Block.from_dict(block_dict) for block_dict in data['chain']]
            print(f"Blockchain loaded from {filename}")
            return True
        except FileNotFoundError:
            print(f"File {filename} not found")
            return False
        except Exception as e:
            print(f"Error loading blockchain: {e}")
            return False


if __name__ == "__main__":
    # Inisialisasi blockchain
    my_chain = Blockchain()
    
    # Mining block 1
    print("Mining block 1...")
    my_chain.add_block(Block(1, "", "Transaksi A -> B: 10 koin"))

    # Mining block 2
    print("Mining block 2...")
    my_chain.add_block(Block(2, "", "Transaksi B -> C: 5 koin"))

    # Mining block 3
    print("Mining block 3...")
    my_chain.add_block(Block(3, "", "Transaksi C -> A: 3 koin"))

    # Validasi blockchain
    print("\nBlockchain Status:")
    print(f"Valid: {my_chain.is_chain_valid()}")
    
    # Tampilkan isi blockchain
    print("\nBlockchain Contents:")
    for block in my_chain.chain:
        print(f"Block #{block.index}: {block.data}")
        print(f"  Hash: {block.hash}")
        print(f"  Previous: {block.previous_hash}")
        print(f"  Nonce: {block.nonce}\n")

    # Simpan ke file
    my_chain.save_to_file()

    # Testing load dari file
    print("\nTesting Load from File:")
    new_chain = Blockchain()
    if new_chain.load_from_file():
        print(f"Loaded {len(new_chain.chain)} blocks")
        print(f"Valid: {new_chain.is_chain_valid()}")

---

## 6. Hasil dan Pembahasan
1.Hasil Uji
Hasil pengujian menunjukkan bahwa program TinyChain berhasil melakukan mining tiga blok menggunakan mekanisme Proof of Work sesuai tingkat kesulitan yang ditentukan. Setiap blok tervalidasi dengan baik, keterkaitan antarblok tetap terjaga, dan blockchain dinyatakan valid. Proses penyimpanan ke file JSON serta pemuatan kembali blockchain juga berjalan lancar tanpa mengganggu integritas data.
Kesesuaian Hasil dengan Ekspektasi

2.Hasil yang diperoleh sudah sesuai dengan ekspektasi.
Setiap blok berhasil di-mine menggunakan mekanisme Proof of Work dengan hash yang memenuhi tingkat kesulitan. Blockchain tervalidasi dengan baik, menunjukkan bahwa keterkaitan antarblok dan integritas data terjaga. Selain itu, proses penyimpanan dan pemuatan blockchain dari file JSON berjalan tanpa merusak struktur data.

3.Error dan Solusinya
Selama pengujian, tidak ditemukan error pada eksekusi program. Namun, potensi error dapat terjadi jika file blockchain.json tidak ditemukan saat proses load. Hal ini sudah ditangani menggunakan exception handling (try-except) sehingga program tidak berhenti dan tetap berjalan dengan aman. Solusi yang diterapkan sudah tepat untuk menjaga kestabilan program.
Hasil eksekusi program Caesar Cipher:

![Hasil Eksekusi](screenshots/output.png)
![Hasil Input](screenshots/input.png)
![Hasil Output](screenshots/output.png)
)

---

## 7. Jawaban Pertanyaan
(Jawab pertanyaan diskusi yang diberikan pada modul.  
- Pertanyaan 1: Mengapa fungsi hash sangat penting dalam blockchain?
Fungsi hash sangat penting karena digunakan untuk menghubungkan setiap blok dengan blok sebelumnya. Hash menjamin integritas data, karena perubahan kecil pada isi blok akan menghasilkan hash yang berbeda, sehingga manipulasi data dapat langsung terdeteksi. 
- Pertanyaan 2: Bagaimana Proof of Work mencegah double spending?
Proof of Work mencegah double spending dengan mewajibkan penambang menyelesaikan perhitungan yang sulit untuk menambahkan blok baru. Transaksi yang sudah tercatat dalam blok dan tervalidasi tidak bisa digunakan kembali tanpa mengulang proses mining, yang membutuhkan waktu dan sumber daya besar.
- Pertanyaan 3:Apa kelemahan PoW dalam hal efisiensi energi?
Kelemahan utama PoW adalah konsumsi energi yang sangat tinggi karena proses mining membutuhkan perhitungan komputasi terus-menerus. Hal ini membuat PoW kurang efisien dan berdampak pada biaya operasional serta lingkungan.  
)
---

## 8. Kesimpulan
Program ini mengimplementasikan blockchain sederhana menggunakan Python. Class Block merepresentasikan satu blok yang berisi index, hash blok sebelumnya, data transaksi, timestamp, nonce, dan hash. Hash dihitung menggunakan algoritma SHA-256, sedangkan proses Proof of Work dilakukan pada method mine_block() dengan mencari nonce hingga hash memenuhi jumlah leading zero sesuai tingkat kesulitan (difficulty).

Class Blockchain mengelola rantai blok, dimulai dari genesis block. Setiap blok baru ditambahkan melalui proses mining agar valid. Fungsi is_chain_valid() digunakan untuk memeriksa integritas blockchain dengan mengecek kecocokan hash dan keterkaitan antarblok. Blockchain juga dapat disimpan ke file JSON dan dimuat kembali, sehingga data bersifat persisten.

Pada bagian main program, dilakukan mining tiga blok dengan data transaksi berbeda, lalu blockchain divalidasi dan ditampilkan isinya. Hasilnya menunjukkan bahwa mekanisme Proof of Work berhasil menjaga keutuhan data dan mencegah perubahan blok tanpa melakukan mining ulang.
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
