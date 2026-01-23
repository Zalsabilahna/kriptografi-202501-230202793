# Laporan Praktikum Kriptografi
Minggu ke-: X  
Topik: [Public Key Infrastructure (PKI & Certificate Authority]  
Nama: [zalsabilah nur aeni]  
NIM: [230202793]  
Kelas: [5 IKKA]  

---

## 1. Tujuan
Setelah mengikuti praktikum ini, mahasiswa diharapkan mampu:
1.Membuat sertifikat digital sederhana.
2.Menjelaskan peran Certificate Authority (CA) dalam sistem PKI.
3.Mengevaluasi fungsi PKI dalam komunikasi aman (contoh: HTTPS, TLS).

## 2. Dasar Teori
Public Key Infrastructure (PKI) adalah sistem yang digunakan untuk menjaga keamanan komunikasi digital dengan memanfaatkan sepasang kunci, yaitu public key dan private key. Public key digunakan untuk enkripsi atau verifikasi, sedangkan private key digunakan untuk dekripsi atau membuat tanda tangan digital. PKI membantu memastikan data yang dikirim aman, tidak diubah, dan berasal dari pihak yang benar.

Certificate Authority (CA) adalah pihak tepercaya yang bertugas menerbitkan dan mengelola sertifikat digital dalam sistem PKI. Sertifikat digital berfungsi sebagai bukti identitas pemilik public key. CA menandatangani sertifikat tersebut agar dapat dipercaya oleh pengguna lain. Dengan adanya CA, pengguna dapat yakin bahwa komunikasi digital dilakukan dengan pihak yang sah dan aman.

## 3. Alat dan Bahan
(- Python 3.x  
- Visual Studio Code / editor lain  
- Git dan akun GitHub  
- Library tambahan (misalnya pycryptodome, jika diperlukan)  )

---

## 4. Langkah Percobaan
1.Membuat folder struktur praktikum/week10-pki/src/ dan screenshots/.
2.Install library cryptography dengan perintah pip install cryptography.
3.Mengimplementasikan class PKICertificate dalam file src/pki_cert.py.
4.Implementasi method create_self_signed_certificate() untuk membuat sertifikat.
5.Implementasi method save_certificate() untuk menyimpan sertifikat ke file PEM.
6.Implementasi method save_private_key() untuk menyimpan private key.
7.Implementasi method get_certificate_info() untuk menampilkan informasi sertifikat.
8Implementasi method verify_certificate() untuk memverifikasi signature.
9.Menjalankan program dengan perintah python pki_cert.py.
10.Mengambil screenshot hasil eksekusi program.
## 5. Source Code
from cryptography import x509
from cryptography.x509.oid import NameOID
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from datetime import datetime, timedelta, timezone


class PKICertificate:
    def __init__(self, key_size=2048):
        """
        Inisialisasi PKI Certificate dengan generate key pair
        """
        self.key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=key_size
        )
        self.certificate = None
    
    def create_signed_certificate(
        self,
        country="",
        organization="",
        common_name="",
        validity_days=365
    ):
        """
        Membuat self-signed certificate
        """
        # Subject dan Issuer sama (self-signed)
        subject = issuer = x509.Name([
            x509.NameAttribute(NameOID.COUNTRY_NAME, country),
            x509.NameAttribute(NameOID.ORGANIZATION_NAME, organization),
            x509.NameAttribute(NameOID.COMMON_NAME, common_name),
        ])
        
        # Buat certificate
        self.certificate = (
            x509.CertificateBuilder()
            .subject_name(subject)
            .issuer_name(issuer)
            .public_key(self.key.public_key())
            .serial_number(x509.random_serial_number())
            .not_valid_before(datetime.now(timezone.utc))
            .not_valid_after(datetime.now(timezone.utc) + timedelta(days=validity_days))
            .add_extension(
                x509.SubjectAlternativeName([
                    x509.DNSName(common_name),
                ]),
                critical=False,
            )
            .sign(self.key, hashes.SHA256())
        )
        
        return self.certificate
    
    def save_certificate(self, filename="cert.pem"):
        """
        Simpan certificate ke file PEM
        """
        if self.certificate is None:
            raise ValueError("Certificate belum dibuat. Jalankan create_signed_certificate() terlebih dahulu.")
        
        with open(filename, "wb") as f:
            f.write(self.certificate.public_bytes(serialization.Encoding.PEM))
        
        print(f"✓ Sertifikat berhasil disimpan: {filename}")
    
    def save_private_key(self, filename="private_key.pem", password=None):
        """
        Simpan private key ke file PEM
        """
        encryption = serialization.NoEncryption()
        if password:
            encryption = serialization.BestAvailableEncryption(password.encode())
        
        with open(filename, "wb") as f:
            f.write(self.key.private_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PrivateFormat.PKCS8,
                encryption_algorithm=encryption
            ))
        
        print(f"✓ Private key berhasil disimpan: {filename}")
    
    def get_certificate_info(self):
        """
        Tampilkan informasi certificate
        """
        if self.certificate is None:
            return "Certificate belum dibuat"
        
        info = {
            "Subject": self.certificate.subject.rfc4514_string(),
            "Issuer": self.certificate.issuer.rfc4514_string(),
            "Serial Number": self.certificate.serial_number,
            "Not Valid Before": self.certificate.not_valid_before_utc,
            "Not Valid After": self.certificate.not_valid_after_utc,
            "Signature Algorithm": self.certificate.signature_algorithm_oid._name,
        }
        
        return info
    
    def verify_certificate(self):
        """
        Verifikasi certificate dengan public key
        """
        if self.certificate is None:
            return False
        
        try:
            public_key = self.key.public_key()
            public_key.verify(
                self.certificate.signature,
                self.certificate.tbs_certificate_bytes,
                padding.PKCS1v15(),
                algorithm=self.certificate.signature_hash_algorithm
            )
            return True
        except Exception as e:
            print(f"Verifikasi gagal: {e}")
            return False


if __name__ == "__main__":
    print("=" * 60)
    print("PKI Certificate Generator - UPB Kriptografi")
    print("=" * 60)
    
    # Buat instance PKI Certificate
    pki = PKICertificate(key_size=2048)
    
    # Buat self-signed certificate
    print("\n[1] Membuat self-signed certificate...")
    cert = pki.create_signed_certificate(
        country="ID",
        organization="UPB Kriptografi",
        common_name="kudostack.com",
        validity_days=360
    )
    print("✓ Certificate berhasil dibuat")
    
    # Simpan certificate dan private key
    print("\n[2] Menyimpan certificate dan private key...")
    pki.save_certificate("./praktikum/week10-pki/assets/cert.pem")
    pki.save_private_key("./praktikum/week10-pki/assets/private_key.pem")
    
    # Tampilkan informasi certificate
    print("\n[3] Informasi Certificate:")
    print("-" * 60)
    cert_info = pki.get_certificate_info()
    for key, value in cert_info.items():
        print(f"{key:20}: {value}")
    
    # Verifikasi certificate
    print("\n[4] Verifikasi Certificate:")
    print("-" * 60)
    is_valid = pki.verify_certificate()
    if is_valid:
        print("✓ Certificate VALID - Signature terverifikasi")
    else:
        print("✗ Certificate INVALID - Signature tidak valid")
    

---

## 6. Hasil dan Pembahasan
rogram ini mensimulasikan konsep dasar Public Key Infrastructure (PKI) dengan membuat self-signed certificate menggunakan library cryptography pada Python. Proses dimulai dari pembuatan key pair RSA yang menjadi fondasi keamanan dalam PKI. Public key dimasukkan ke dalam sertifikat, sedangkan private key digunakan untuk menandatangani sertifikat tersebut.
Karena sertifikat bersifat self-signed, maka entitas yang membuat sertifikat juga bertindak sebagai Certificate Authority (CA). Hal ini umum digunakan dalam lingkungan pembelajaran, pengujian, atau sistem internal, namun tidak direkomendasikan untuk produksi karena tidak divalidasi oleh CA resmi.
Hasil verifikasi yang berhasil membuktikan bahwa integritas dan keaslian sertifikat terjaga, karena tanda tangan digital cocok dengan data sertifikat dan public key yang digunakan. Dengan demikian, program ini telah berhasil menerapkan konsep dasar PKI, mulai dari pembuatan sertifikat hingga proses verifikasi tanda tangan digital.
Hasil eksekusi program Caesar Cipher:

![Hasil Eksekusi](screenshots/output.png)
![Hasil Input](screenshots/input.png)
![Hasil Output](screenshots/output.png)
)

---

## 7. Jawaban Pertanyaan
(Jawab pertanyaan diskusi yang diberikan pada modul.  
- Pertanyaan 1: Bagaimana browser memverifikasi sertifikat HTTPS?
Saat pengguna membuka website HTTPS, browser akan memeriksa sertifikat digital yang dikirim oleh server. Browser mengecek apakah sertifikat tersebut diterbitkan oleh Certificate Authority (CA) tepercaya yang sudah ada di dalam trust store browser, apakah masa berlakunya masih aktif, dan apakah nama domain sesuai dengan sertifikat. Jika semua valid, browser akan mempercayai koneksi dan membuat koneksi terenkripsi menggunakan SSL/TLS.
- Pertanyaan 2: Apa yang terjadi jika CA palsu menerbitkan sertifikat?
Jika CA palsu berhasil menerbitkan sertifikat, maka penyerang dapat menyamar sebagai website asli dan melakukan serangan seperti Man-in-the-Middle (MitM). Akibatnya, data pengguna seperti username, password, atau informasi kartu kredit dapat dicuri. Namun, browser modern biasanya akan menolak sertifikat dari CA yang tidak tepercaya dan menampilkan peringatan keamanan kepada pengguna.
- Pertanyaan 3:Mengapa PKI penting dalam komunikasi aman (misalnya transaksi online)?
PKI sangat penting karena memastikan bahwa komunikasi dilakukan dengan pihak yang sah dan data yang dikirim terenkripsi serta tidak diubah. Dalam transaksi online, PKI melindungi informasi sensitif seperti data pribadi dan pembayaran, serta mencegah pemalsuan identitas. Tanpa PKI, keamanan dan kepercayaan dalam komunikasi digital tidak dapat terjamin.
)
---

## 8. Kesimpulan
Public Key Infrastructure (PKI) berhasil dilakukan melalui pembuatan sertifikat digital self-signed menggunakan algoritma RSA dan hash SHA-256. Program mampu menghasilkan pasangan kunci, membuat sertifikat digital, menyimpan sertifikat dan private key, serta menampilkan informasi sertifikat dengan benar.
Proses verifikasi sertifikat menunjukkan hasil valid, yang menandakan bahwa tanda tangan digital dapat diverifikasi menggunakan public key yang sesuai. Hal ini membuktikan bahwa mekanisme dasar PKI, seperti keaslian, integritas data, dan kepercayaan terhadap sertifikat, telah berjalan dengan baik meskipun sertifikat masih bersifat self-signed dan digunakan untuk tujuan pembelajaran.

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
