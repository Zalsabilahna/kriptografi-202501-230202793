# Laporan Praktikum Kriptografi
Minggu ke-: X  
Topik: [Serangan Kriptografi]  
Nama: [zalsabilah nur aeni]  
NIM: [230202793]  
Kelas: [5 IKKA]  

---

## 1. Tujuan
1.Mengidentifikasi jenis serangan pada sistem informasi nyata.
2.Mengevaluasi kelemahan algoritma kriptografi yang digunakan.
3.Memberikan rekomendasi algoritma kriptografi yang sesuai untuk perbaikan keamanan.

---

## 2. Dasar Teori
Serangan kriptografi adalah upaya untuk melemahkan atau menembus sistem keamanan kriptografi dengan tujuan memperoleh informasi rahasia, memalsukan data, atau merusak keutuhan sistem. Serangan ini dapat menargetkan algoritma kriptografi, implementasi sistem, maupun perilaku pengguna. Secara umum, serangan kriptografi muncul karena kelemahan pada desain algoritma, kesalahan implementasi, atau penggunaan kunci yang tidak aman.

Beberapa jenis serangan kriptografi yang umum antara lain brute force attack, yaitu mencoba semua kemungkinan kunci hingga menemukan yang benar, dan cryptanalysis, yaitu menganalisis pola matematika pada algoritma untuk menemukan kelemahan. Selain itu, terdapat juga serangan seperti man-in-the-middle, side-channel attack, dan replay attack. Pemahaman teori dasar serangan kriptografi penting agar sistem keamanan dapat dirancang dengan lebih kuat dan mampu meminimalkan risiko kebocoran data.

## 3. Alat dan Bahan
Python 3.11 atau lebih baru
Visual Studio Code / editor lain
Git dan akun GitHub
Library: hashlib, bcrypt, argon2-cffi
Tools analisis: John the Ripper (optional, untuk demo)


## 4. Langkah Percobaan
1.Membuat file caesar_cipher.py di folder praktikum/week2-cryptosystem/src/.
2.Menyalin kode program Caesar Cipher sesuai panduan praktikum ke dalam file tersebut.
3.Menyimpan file dan membuka terminal pada direktori project.
4.Menjalankan program menggunakan perintah python caesar_cipher.py.
5.Mengamati hasil enkripsi dan dekripsi yang ditampilkan oleh program.


## 5. Source Code
import hashlib
import time
from typing import List, Tuple

def sha1_hash(password: str) -> str:
    """
    Simulasi hashing LinkedIn (SHA-1 tanpa salt)
    """
    return hashlib.sha1(password.encode()).hexdigest()

def load_common_passwords(filename: str = "common_passwords.txt") -> List[str]:
    """
    Load common passwords untuk dictionary attack
    """
    # Simulasi common passwords (dalam real attack, gunakan rockyou.txt)
    common_passwords = [
        "password", "123456", "123456789", "password123",
        "linkedin", "welcome", "qwerty", "abc123",
        "monkey", "1234567890", "princess", "letmein",
        "dragon", "iloveyou", "sunshine", "master",
        "admin", "login", "solo", "trustno1"
    ]
    return common_passwords

def dictionary_attack(target_hashes: List[str], 
                     dictionary: List[str]) -> Tuple[dict, int, float]:
    """
    Simulasi dictionary attack terhadap LinkedIn hashes
    
    Returns:
        (cracked_passwords, total_attempts, time_elapsed)
    """
    cracked = {}
    attempts = 0
    start_time = time.time()
    
    for password in dictionary:
        hash_value = sha1_hash(password)
        attempts += 1
        
        if hash_value in target_hashes:
            cracked[hash_value] = password
            print(f"Cracked: {password} → {hash_value}")
    
    elapsed = time.time() - start_time
    return cracked, attempts, elapsed

def brute_force_numeric(target_hashes: List[str], 
                       max_length: int = 6) -> Tuple[dict, int, float]:
    """
    Simulasi brute force untuk numeric passwords
    """
    cracked = {}
    attempts = 0
    start_time = time.time()
    
    # Brute force 6-digit numbers (000000-999999)
    for num in range(10 ** max_length):
        password = str(num).zfill(max_length)
        hash_value = sha1_hash(password)
        attempts += 1
        
        if hash_value in target_hashes:
            cracked[hash_value] = password
            print(f"Cracked: {password} → {hash_value}")
        
        # Progress indicator
        if attempts % 100000 == 0:
            print(f"Progress: {attempts:,} attempts")
    
    elapsed = time.time() - start_time
    return cracked, attempts, elapsed

def analyze_hash_distribution(hashes: List[str]) -> dict:
    """
    Analisis distribusi hash untuk identifikasi password umum
    """
    distribution = {}
    for hash_value in hashes:
        distribution[hash_value] = distribution.get(hash_value, 0) + 1
    
    # Sort by frequency
    sorted_dist = sorted(distribution.items(), key=lambda x: x[1], reverse=True)
    return dict(sorted_dist)

# Simulasi LinkedIn Breach
if __name__ == "__main__":
    print("=" * 70)
    print("SIMULASI LINKEDIN PASSWORD BREACH (2012)")
    print("=" * 70)
    
    # Simulasi LinkedIn database (sample hashes)
    print("\n[1] Generating simulated LinkedIn hashes...")
    linkedin_passwords = [
        "password", "123456", "linkedin", "password123",
        "welcome", "123456", "password", "admin",
        "123456789", "qwerty", "password", "login"
    ]
    
    linkedin_hashes = [sha1_hash(pwd) for pwd in linkedin_passwords]
    
    print(f"Total hashes in database: {len(linkedin_hashes)}")
    print(f"Unique hashes: {len(set(linkedin_hashes))}")
    
    # Analisis distribusi
    print("\n[2] Analyzing hash distribution...")
    distribution = analyze_hash_distribution(linkedin_hashes)
    
    print("\nTop 5 most common hashes:")
    for i, (hash_val, count) in enumerate(list(distribution.items())[:5], 1):
        print(f"  {i}. {hash_val[:16]}... (appears {count} times)")
    
    # Dictionary attack
    print("\n[3] Launching dictionary attack...")
    common_passwords = load_common_passwords()
    cracked_dict, dict_attempts, dict_time = dictionary_attack(
        linkedin_hashes, common_passwords
    )
    
    print(f"\nDictionary Attack Results:")
    print(f"  Passwords cracked: {len(cracked_dict)}")
    print(f"  Total attempts: {dict_attempts:,}")
    print(f"  Time elapsed: {dict_time:.4f} seconds")
    print(f"  Speed: {dict_attempts/dict_time:,.0f} hashes/second")
    
    # Brute force numeric
    print("\n[4] Launching brute force (numeric 6-digit)...")
    print("(This will try 1,000,000 combinations)")
    
    user_input = input("Continue? (y/n): ")
    if user_input.lower() == 'y':
        cracked_brute, brute_attempts, brute_time = brute_force_numeric(
            linkedin_hashes, max_length=6
        )
        
        print(f"\nBrute Force Results:")
        print(f"  Passwords cracked: {len(cracked_brute)}")
        print(f"  Total attempts: {brute_attempts:,}")
        print(f"  Time elapsed: {brute_time:.4f} seconds")
        print(f"  Speed: {brute_attempts/brute_time:,.0f} hashes/second")
    
    # Summary
    print("\n" + "=" * 70)
    print("ATTACK SUMMARY")
    print("=" * 70)
    
    total_cracked = len(set(list(cracked_dict.keys())))
    total_hashes = len(set(linkedin_hashes))
    crack_rate = (total_cracked / total_hashes) * 100
    
    print(f"Total unique hashes: {total_hashes}")
    print(f"Successfully cracked: {total_cracked} ({crack_rate:.1f}%)")
    print(f"\nCracked passwords:")
    for hash_val, password in cracked_dict.items():
        count = distribution.get(hash_val, 0)
        print(f"  {password:15} → affects {count} accounts")
    
    print("\n" + "=" * 70)
    print("VULNERABILITY ANALYSIS")
    print("=" * 70)
    
    print("\nIdentified Weaknesses:")
    print("  1. SHA-1 hashing (fast, designed for speed)")
    print("  2. No salt (identical passwords = identical hashes)")
    print("  3. No key stretching (single iteration)")
    print("  4. Weak password policy (common passwords allowed)")
    
    print("\nReal-world Impact:")
    print("  - With modern GPU: 10 billion SHA-1/second")
    print("  - Dictionary of 1 billion passwords: < 1 second")
    print("  - 8-character brute force: minutes to hours")
    print("  - Rainbow tables: instant lookup")
)

---

## 6. Hasil dan Pembahasan
1.hasil uji
Hasil pengujian menunjukkan bahwa serangan dictionary attack berhasil memecahkan beberapa password dengan sangat cepat karena menggunakan daftar password umum dan hashing SHA-1 tanpa salt. Hash yang sama muncul berulang kali menandakan banyak pengguna memakai password identik, sehingga tingkat keberhasilan serangan cukup tinggi. Sementara itu, brute force numeric mampu memecahkan password berbentuk angka, tetapi membutuhkan waktu dan percobaan jauh lebih banyak. Secara keseluruhan, hasil uji sesuai ekspektasi dan membuktikan bahwa penggunaan hash lemah tanpa salt sangat rentan terhadap serangan kriptografi.
2.Kesesuaian Hasil dengan Ekspektasi
Hasil yang diperoleh sudah sesuai dengan ekspektasi. Password yang menggunakan kata umum seperti password, 123456, dan admin berhasil di-crack dengan cepat melalui dictionary attack. Hal ini membuktikan bahwa penggunaan SHA-1 tanpa salt dan tanpa key stretching sangat rentan terhadap serangan kriptografi, seperti yang terjadi pada kasus kebocoran data LinkedIn.
3.Error dan Solusinya
Selama pengujian tidak ditemukan error pada program. Namun, brute force numeric membutuhkan waktu komputasi lebih lama dan meminta konfirmasi pengguna sebelum dijalankan. Hal ini merupakan mekanisme pengamanan agar program tidak berjalan terlalu lama. Solusinya adalah membatasi panjang password atau menghentikan brute force jika tidak diperlukan.
Hasil eksekusi program Caesar Cipher:

![Hasil Eksekusi](screenshots/output.png)
![Hasil Input](screenshots/input.png)
![Hasil Output](screenshots/output.png)
)

---

## 7. Jawaban Pertanyaan
(Jawab pertanyaan diskusi yang diberikan pada modul.  
- Pertanyaan 1: Mengapa banyak sistem lama masih rentan terhadap brute force atau dictionary attack?
Banyak sistem lama masih rentan karena menggunakan algoritma hash lama yang cepat (seperti MD5 atau SHA-1), tidak menerapkan salt, dan tidak memiliki key stretching. Selain itu, kebijakan password pada sistem lama biasanya lemah (password pendek dan umum) serta tidak ada pembatasan percobaan login, sehingga brute force dan dictionary attack bisa dilakukan dengan mudah dan cepat.
- Pertanyaan 2: Apa bedanya kelemahan algoritma dengan kelemahan implementasi?
Kelemahan algoritma terjadi ketika metode kriptografi itu sendiri sudah tidak aman secara teori atau praktis, misalnya SHA-1 yang sudah rawan collision. Sedangkan kelemahan implementasi terjadi karena kesalahan penerapan, seperti tidak menggunakan salt, konfigurasi yang salah, manajemen kunci yang buruk, atau penggunaan algoritma yang benar tetapi dengan parameter keamanan yang lemah.
- Pertanyaan 3:Bagaimana organisasi dapat memastikan sistem kriptografi mereka tetap aman di masa depan?
Organisasi dapat menjaga keamanan dengan rutin memperbarui algoritma dan standar kriptografi, menggunakan password hashing modern (bcrypt, scrypt, atau Argon2), menerapkan salt dan key stretching, serta melakukan audit dan pengujian keamanan secara berkala. Selain itu, mengikuti rekomendasi komunitas keamanan dan memantau perkembangan ancaman baru sangat penting agar sistem tetap aman dalam jangka panjang. 
)
---

## 8. Kesimpulan
Berdasarkan hasil pengujian, program berhasil mensimulasikan serangan dictionary attack dan brute force terhadap hash SHA-1 tanpa salt, di mana beberapa password umum dapat dipecahkan dengan cepat, sesuai dengan ekspektasi teori kriptografi. Hasil uji menunjukkan bahwa sistem lama dengan algoritma hash cepat dan kebijakan password lemah sangat rentan terhadap serangan. Tidak ditemukan error berarti saat eksekusi; jika terjadi kendala, umumnya berasal dari input pengguna atau keterbatasan waktu eksekusi brute force, yang dapat diatasi dengan membatasi panjang password atau jumlah percobaan.

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
