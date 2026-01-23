# ====== Operasi Aritmetika Modular ======
def mod_add(a, b, n): 
    return (a + b) % n

def mod_sub(a, b, n): 
    return (a - b) % n

def mod_mul(a, b, n): 
    return (a * b) % n

def mod_exp(base, exp, n): 
    return pow(base, exp, n)  # eksponensiasi modular cepat


# ====== GCD dan Extended GCD ======
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def egcd(a, b):
    if a == 0:
        return b, 0, 1
    g, x1, y1 = egcd(b % a, a)
    return g, y1 - (b // a) * x1, x1

def modinv(a, n):
    g, x, _ = egcd(a, n)
    if g != 1:
        return None
    return x % n


# ====== Logaritma Diskrit (Brute Force) ======
def discrete_log(a, b, n):
    for x in range(n):
        if pow(a, x, n) == b:
            return x
    return None


# ====== PROGRAM UTAMA ======
def main():
    print("=== PROGRAM ARITMETIKA MODULAR & KRIPTOGRAFI DASAR ===")
    print("1. Penjumlahan Modular")
    print("2. Pengurangan Modular")
    print("3. Perkalian Modular")
    print("4. Eksponensiasi Modular")
    print("5. GCD (Pembagi Bersama Terbesar)")
    print("6. Invers Modular")
    print("7. Logaritma Diskrit (Brute Force)")
    print("0. Keluar")
    
    while True:
        try:
            pilihan = int(input("\nPilih menu (0-7): "))
        except ValueError:
            print("Masukkan angka yang valid!")
            continue

        if pilihan == 0:
            print("Terima kasih! Program selesai.")
            break

        # Input sesuai kebutuhan tiap operasi
        if pilihan in [1, 2, 3]:
            a = int(input("Masukkan a: "))
            b = int(input("Masukkan b: "))
            n = int(input("Masukkan modulus n: "))
            if pilihan == 1:
                print(f"Hasil (a + b) mod n = {mod_add(a, b, n)}")
            elif pilihan == 2:
                print(f"Hasil (a - b) mod n = {mod_sub(a, b, n)}")
            else:
                print(f"Hasil (a * b) mod n = {mod_mul(a, b, n)}")

        elif pilihan == 4:
            base = int(input("Masukkan basis: "))
            exp = int(input("Masukkan eksponen: "))
            n = int(input("Masukkan modulus n: "))
            print(f"Hasil (base^exp) mod n = {mod_exp(base, exp, n)}")

        elif pilihan == 5:
            a = int(input("Masukkan a: "))
            b = int(input("Masukkan b: "))
            print(f"GCD(a, b) = {gcd(a, b)}")

        elif pilihan == 6:
            a = int(input("Masukkan a: "))
            n = int(input("Masukkan modulus n: "))
            inv = modinv(a, n)
            if inv is None:
                print("Invers tidak ada (a dan n tidak relatif prima)")
            else:
                print(f"Invers dari {a} mod {n} = {inv}")

        elif pilihan == 7:
            a = int(input("Masukkan a: "))
            b = int(input("Masukkan b: "))
            n = int(input("Masukkan modulus n: "))
            x = discrete_log(a, b, n)
            if x is not None:
                print(f"Nilai x sehingga {a}^x ≡ {b} (mod {n}) adalah x = {x}")
            else:
                print("Tidak ditemukan solusi untuk x dalam rentang 0 hingga n-1.")

        else:
            print("Pilihan tidak valid! Silakan pilih antara 0-7.")

# Jalankan program
if __name__ == "__main__":
    main()
