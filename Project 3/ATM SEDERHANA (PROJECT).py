print("##                    PROJECT 1 PEMROGRAMAN DASAR SEMESTER 2 TAHUN AJARAN 2024-2025                  ##")
print("## SELAMAT DATANG DI PROGRAM ATM SEDERHANA BERBASIS CONSOLE (TEXT) BAHASA PEMROGRAMAN BAHASA PYTHON: ##")
print("##                                            KELAS X TEL 9                                          ##")

print("=" * 50)  
print("Masukkan data".center(50))  # Mengarahkan pengguna untuk memasukkan data
print("=" * 50) 
input ("\nNama Lengkap        : ") 
input ("Nomor Absen         : ") 
input ("Kelas               : ") 
input ("Hari/TTL            : ") 
print("Guru Mata Pelajaran : Apdaniel Alamsyah. S.KOM\n") 

# fungsi login
def login():
    attempt = 0  # Inisialisasi percobaan login
    max_attempt = 3  # Maksimal percobaan login yang diperbolehkan
    username = "p"  # Username default 
    password = "p"  # Password default 

    print("=" * 50)  
    print("Silahkan login untuk melanjutkan".center(50))  # Menampilkan pesan login
    print("=" * 50) 

    # Loop untuk melakukan percobaan login
    while attempt < max_attempt:
        USERNAME = input("\nMasukkan username : ")  # Input username
        PASSWORD = input("Masukkan password : ")  # Input password

        if USERNAME == username and PASSWORD == password:  # Cek kecocokan username dan password
            print("-" * 50)
            print ("Login Berhasil".center(50))  # Menampilkan pesan login berhasil
            print("-" * 50)
            return True  # Login berhasil
        else:
            attempt += 1  # Tambah percobaan
            if attempt < max_attempt:
                print (f"\nUsername dan Password salah anda memiliki {max_attempt - attempt} kesempatan ")
                print ("-" * 54)  # Menampilkan informasi sisa kesempatan
            else:
                print ("\nLogin Gagal, Program akan ditutup")  # Jika login gagal setelah 3 kali percobaan
                return False  # Login gagal

# Program ATM Sederhana
def atm_sederhana():
    saldo = 250000  # Saldo awal
    pin = "4321"    # PIN default
    kesempatan = 3  # Batas kesalahan memasukkan PIN

    print("\n" + "=" * 50)
    print("Selamat Datang di ATM Sederhana".center (50))  # Menampilkan pesan selamat datang
    print("=" * 50)

    # Verifikasi PIN
    while kesempatan > 0:  # Loop sampai kesempatan memasukkan PIN habis
        PIN = input("\nMasukkan PIN Anda: ")  # Input PIN
        if PIN == pin:  # Jika PIN cocok
            print("-" * 50)
            print("PIN berhasil diverifikasi.".center(50))  # Menampilkan pesan PIN berhasil
            print("-" * 50)
            break  # Keluar dari loop
        else:
            kesempatan -= 1  # Kurangi kesempatan jika PIN salah
            print(f"\nPIN kamu salah, Kesempatan tersisa: {kesempatan}")  # Menampilkan sisa kesempatan
            print("-" * 50)
    else:
        print("Anda telah salah memasukkan PIN 3 kali. Kartu anda diblokir.")  # Jika gagal 3 kali
        return  # Keluar dari fungsi ATM

    # Menu ATM
    while True:
        print("\n" + "=" * 50)
        print("ATM SEDERHANA".center(50))
        print("-" * 50)
        print("1. Cek Saldo")  # Pilihan untuk cek saldo
        print("2. Tarik Tunai")  # Pilihan untuk tarik tunai
        print("3. Setor Tunai")  # Pilihan untuk setor tunai
        print("4. Keluar")  # Pilihan untuk keluar

        pilihan = input("Silahkan pilih Option (1-4) : ")  # Input pilihan

        # Validasi input pilihan (harus antara 1-4)
        if pilihan == "1" or pilihan == "2" or pilihan == "3" or pilihan == "4":
            pilihan = int(pilihan)  # Mengubah input ke integer
        else:
            print("Pilihan tidak valid. Silahkan pilih Option (1-4)")  # Jika input salah
            continue  # Kembali ke awal loop

        # PILIHAN PERTAMA (Cek Saldo)
        if pilihan == 1:
            print(f"\nSaldo kamu saat ini Rp {saldo}")  # Menampilkan saldo

        # PILIHAN KEDUA (Tarik Saldo)
        elif pilihan == 2: 
            tarik = input("Berapa saldo yang ingin kamu tarik : Rp ")  # Input jumlah tarik tunai

            if tarik.isdigit():  # Memeriksa apakah input berupa angka
                tarik = int(tarik)  # Mengonversi input ke integer
            else:
                print("Input tidak valid, Silahkan coba kembali")  # Jika input tidak valid
                continue

            if tarik <= saldo:  # Cek apakah saldo cukup
                saldo -= tarik  # Mengurangi saldo sesuai dengan jumlah tarik
                print("-" * 50)
                print(f"Kamu berhasil menarik saldo sebesar RP {tarik},\ndan Sisa saldo kamu sekarang Rp {saldo}")  # Menampilkan hasil tarik
            else:
                print("Maaf saldo Kamu tidak cukup , Silahkan coba kembali !!!")  # Jika saldo tidak cukup

        # PILIHAN KETIGA (Setor Tunai)
        elif pilihan == 3:
            setor = input("Berapa nominal yang ingin kamu setor : Rp ")  # Input jumlah setor tunai

            if setor.isdigit():  # Memeriksa apakah input berupa angka
                 setor = int(setor)  # Mengonversi input ke integer
            else:
                 print("Input tidak valid, Silahkan coba kembali")  # Jika input tidak valid
                 continue

            if setor > 0:  # Cek apakah setor lebih dari 0
                saldo += setor  # Menambah saldo
                print("-" * 50)
                print(f"Kamu berhasil setor uang sebesar RP {setor},\ndan Sisa saldo kamu sekarang Rp {saldo}")  # Menampilkan hasil setor

        # PILIHAN KEEMPAT (Keluar)
        elif pilihan == 4:  
            print("-" * 50)
            print("Terima kasih sudah menggunakan program atm sederhana kami".center (50))  # Pesan keluar
            print("-" * 50)
            break  # Keluar dari loop ATM

        else:
            print("Pilihan tidak valid, silahkan coba kembali")  # Jika pilihan tidak valid

# Jalankan program
if login():  # Jika login berhasil
    atm_sederhana()  # Jalankan program ATM
