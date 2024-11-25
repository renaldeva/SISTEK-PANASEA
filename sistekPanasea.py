import pandas as pd
import os
from datetime import datetime
from tabulate import tabulate

ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "12345678"

# Define file paths for the CSV files
APOTEKER_FILE = 'apoteker.csv'
PASIEN_FILE = 'pasien.csv'
OBAT_FILE = 'data_obat.csv'

def load_data(file_path):
    """Load data from a CSV file into a DataFrame."""
    if os.path.exists(file_path):
        return pd.read_csv(file_path).to_dict(orient='records')
    return []

def save_data(file_path, data):
    """Save the data to a CSV file."""
    df = pd.DataFrame(data)
    df.to_csv(file_path, index=False)

def tampilan_judul():
    print('''
    +=================================================================================+
    ||  ___  ___  ___  _____  ___  _  __    ___   _    _  _    _    ___  ___    _    ||
    || / __|| _ |/ __||_   _|| __|| |/ /   | _ \ /_\  | \| |  /_\  / __|| __|  /_\   ||
    || \__ \ | | \__ \  | | || _| | ' <    |  _// _ \ | .` | / _ \ \__ \| _|  / _ \  ||
    || |___/|___||___/  |_| ||___||_|\_\   |_| /_/ \_\|_|\_|/_/ \_\|___/|___|/_/ \_\ ||
    ||                                                                               ||      
    +=================================================================================+                                                                  
    ''')

def tampilan_menu():
    print("\n=== Menu Utama ===")
    print(tabulate([
        ["1", "Kelola Data Apoteker"],
        ["2", "Kelola Data Pasien"],
        ["3", "Kelola Data Obat"],
        ["4", "Kelola Pemesanan Obat"],
        ["5", "Kelola Stock Obat"],
        ["6", "Keluar"]
    ], headers=["No", "Menu"], tablefmt="grid"))

def tampilan_menu_apoteker():
    print("\n=== Menu Kelola Data Apoteker ===")
    print(tabulate([
        ["1", "Tambah Apoteker"],
        ["2", "Hapus Apoteker"],
        ["3", "Tampilkan Daftar Apoteker"],
        ["4", "Kembali ke Menu Utama"]
    ], headers=["No", "Submenu"], tablefmt="grid"))

def tampilan_menu_pasien():
    print("\n=== Menu Kelola Data Pasien ===")
    print(tabulate([
        ["1", "Tambah Pasien"],
        ["2", "Hapus Pasien"],
        ["3", "Tampilkan Daftar Pasien"],
        ["4", "Kembali ke Menu Utama"]
    ], headers=["No", "Submenu"], tablefmt="grid"))

def tampilan_menu_obat():
    print("\n=== Menu Kelola Data Obat ===")
    print(tabulate([
        ["1", "Tambah Obat"],
        ["2", "Hapus Obat"],
        ["3", "Tampilkan Daftar Obat"],
        ["4", "Filter Tanggal Kadaluarsa"],
        ["5", "Kembali ke Menu Utama"]
    ], headers=["No", "Submenu"], tablefmt="grid"))

def filter_tanggal_kadaluarsa():
    print("=== Filter Tanggal Kadaluarsa ===")
    tanggal_filter = input("Masukkan tanggal filter (YYYY-MM-DD): ")
    
    # Load data obat from CSV
    data_obat = load_data(OBAT_FILE)

    try:
        # Mengonversi string tanggal ke objek datetime
        filter_date = datetime.strptime(tanggal_filter, "%Y-%m-%d")
        
        # Mencari obat yang kadaluarsa sebelum tanggal filter
        filtered_obat = [obat for obat in data_obat if datetime.strptime(obat["Tanggal Kadaluarsa"], "%Y-%m-%d") < filter_date]
        
        if filtered_obat:
            print("\nObat yang kadaluarsa sebelum", tanggal_filter, ":")
            print(tabulate(filtered_obat, headers="keys", tablefmt="grid"))
        else:
            print("Tidak ada obat yang kadaluarsa sebelum", tanggal_filter)
    except ValueError:
        print("Format tanggal salah! Harap masukkan dalam format YYYY-MM-DD.")

def tampilan_menu_pemesanan():
    print("\n=== Menu Kelola Pemesanan Obat ===")
    print(tabulate([
        ["1" , "Buat Pemesanan"],
        ["2", "Kembali ke Menu Utama"]
    ], headers=["No", "Submenu"], tablefmt="grid"))

def buat_pemesanan():
    print("=== Buat Pemesanan ===")
    # Logika untuk membuat pemesanan
    nama_obat = input("Masukkan nama obat: ")
    jumlah = input("Masukkan jumlah obat: ")
    harga = float(input("Masukkan harga obat: "))
    
    # Simulasi data pemesanan
    pemesanan = {
        "Nama Obat": nama_obat,
        "Jumlah": jumlah,
        "Harga": harga,
        "Total": harga * int(jumlah),
        "Tanggal": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    
    cetak_struk(pemesanan)

def cetak_struk(pemesanan):
    print("\n=== Struk Pemesanan ===")
    print(tabulate([[
        pemesanan["Nama Obat"],
        pemesanan["Jumlah"],
        pemesanan["Harga"],
        pemesanan["Total"],
        pemesanan["Tanggal"]
    ]], headers=["Nama Obat", "Jumlah", "Harga", "Total", "Tanggal"], tablefmt="grid"))

def tampilan_menu_stock():
    print("\n=== Menu Kelola Stock Obat ===")
    print(tabulate([
        ["1", "Cek Stock Obat"],
        ["2", "Cek Tanggal Kadaluarsa"],
        ["3", "Kembali ke Menu Utama"]
    ], headers=["No", "Submenu"], tablefmt="grid"))

def login_admin():
    print("=== Login Admin ===")
    username = input("Masukan Username: ")
    password = input("Masukan Password: ")

    if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
        print("Login Berhasil")
        return True
    else:
        print("Login gagal! Username atau password salah.")
        return False

# Proses login
if login_admin():
    tampilan_judul()
    print("Selamat datang di sistem!")
    while True:
        tampilan_menu()
        pilihan = input("Pilih menu (1-6): ")
        
        if pilihan == '1':
            while True:
                tampilan_menu_apoteker()
                sub_pilihan = input("Pilih submenu (1-4): ")
                if sub_pilihan == '1':
                    print("Menambah Apoteker...")
                    # Logika untuk menambah apoteker
                    nama_apoteker = input("Masukkan nama apoteker: ")
                    alamat_apoteker = input("Masukkan alamat apoteker: ")
                    no_telepon_apoteker = input("Masukkan no telepon apoteker: ")

                    # Simpan data apoteker ke dalam dictionary
                    apoteker_data = {
                        "nama": nama_apoteker,
                        "alamat": alamat_apoteker,
                        "no_telepon": no_telepon_apoteker
                    }

                    # Load existing apoteker data and append new data
                    apoteker_list = load_data(APOTEKER_FILE)
                    apoteker_list.append(apoteker_data)
                    save_data(APOTEKER_FILE, apoteker_list)

                    print("Apoteker berhasil ditambahkan!")
                elif sub_pilihan == '2':
                    print("Menghapus Apoteker...")
                    # Logika untuk menghapus apoteker
                    nama_apoteker = input("Masukkan nama apoteker yang akan dihapus: ")
                    apoteker_list = load_data(APOTEKER_FILE)
                    apoteker_found = False

                    for apoteker in apoteker_list:
                        if apoteker["nama"] == nama_apoteker:
                            apoteker_found = True
                            apoteker_list.remove(apoteker)
                            save_data(APOTEKER_FILE, apoteker_list)
                            print("Apoteker berhasil dihapus!")
                            break

                    if not apoteker_found:
                        print("Apoteker tidak ditemukan.")
                elif sub_pilihan == '3':
                    print("Menampilkan Daftar Apoteker...")
                    apoteker_list = load_data(APOTEKER_FILE)
                    if not apoteker_list:
                        print("Tidak ada apoteker yang terdaftar.")
                    else:
                        print("Daftar Apoteker:")
                        for apoteker in apoteker_list:
                            print("Nama:", apoteker["nama"])
                            print("Alamat:", apoteker["alamat"])
                            print("No Telepon:", apoteker["no_telepon"])
                            print("-------------------------")
                elif sub_pilihan == '4':
                    break
                else:
                    print("Pilihan tidak valid! Silakan coba lagi.")
        
        elif pilihan == '2':
            while True:
                tampilan_menu_pasien()
                sub_pilihan = input("Pilih submenu (1-4): ")
                if sub_pilihan == '1':
                    print("Menambah Pasien...")
                    # Logika untuk menambah pasien
                    nama_pasien = input("Masukkan nama pasien: ")
                    alamat_pasien = input("Masukkan alamat pasien: ")
                    no_telepon_pasien = input("Masukkan no telepon pasien: ")
                    umur_pasien = input("Masukkan umur pasien: ")

                    # Simpan data pasien ke dalam dictionary
                    pasien_data = {
                        "nama": nama_pasien,
                        "alamat": alamat_pasien,
                        "no_telepon": no_telepon_pasien,
                        "umur": umur_pasien
                    }

                    # Load existing pasien data and append new data
                    pasien_list = load_data(PASIEN_FILE)
                    pasien_list.append(pasien_data)
                    save_data(PASIEN_FILE, pasien_list)

                    print("Pasien berhasil ditambahkan!")
                elif sub_pilihan == '2':
                    print("Menghapus Pasien...")
                    # Logika untuk menghapus pasien
                    nama_pasien = input("Masukkan nama pasien yang akan dihapus: ")
                    pasien_list = load_data(PASIEN_FILE)
                    pasien_found = False

                    for pasien in pasien_list:
                        if pasien["nama"] == nama_pasien:
                            pasien_found = True
                            pasien_list.remove(pasien)
                            save_data(PASIEN_FILE, pasien_list)
                            print("Pasien berhasil dihapus!")
                            break

                    if not pasien_found:
                        print("Pasien tidak ditemukan.")
                elif sub_pilihan == '3':
                    print("Menampilkan Daftar Pasien...")
                    pasien_list = load_data(PASIEN_FILE)
                    if not pasien_list:
                        print("Tidak ada pasien yang terdaftar.")
                    else:
                        print("Daftar Pasien:")
                        for pasien in pasien_list:
                            print("Nama:", pasien["nama"])
                            print("Alamat:", pasien["alamat"])
                            print("No Telepon:", pasien["no_telepon"])
                            print("Umur:", pasien["umur"])
                            print("-------------------------")
                elif sub_pilihan == '4':
                    break
                else:
                    print("Pilihan tidak valid! Silakan coba lagi.")

        elif pilihan == '3':
            while True:
                tampilan_menu_obat()
                sub_pilihan = input("Pilih submenu (1-5): ")
                if sub_pilihan == '1':
                    print("Menambah Obat...")
                    # Logika untuk menambah obat
                    nama_obat = input("Masukkan nama obat: ")
                    dosis_obat = input("Masukkan dosis obat: ")
                    jumlah_obat = input("Masukkan jumlah obat: ")
                    tanggal_kadaluarsa = input("Masukkan tanggal kadaluarsa (YYYY-MM-DD): ")

                    # Simpan data obat ke dalam dictionary
                    obat_data = {
                        "nama": nama_obat,
                        "dosis": dosis_obat,
                        "jumlah": jumlah_obat,
                        "tanggal_kadaluarsa": tanggal_kadaluarsa
                    }

                    # Load existing obat data and append new data
                    obat_list = load_data(OBAT_FILE)
                    obat_list.append(obat_data)
                    save_data(OBAT_FILE, obat_list)

                    print("Obat berhasil ditambahkan!")
                elif sub_pilihan == '2':
                    print("Menghapus Obat...")
                    # Logika untuk menghapus obat
                    nama_obat = input("Masukkan nama obat yang akan dihapus: ")
                    obat_list = load_data(OBAT_FILE)
                    obat_found = False

                    for obat in obat_list:
                        if obat["nama"] == nama_obat:
                            obat_found = True
                            obat_list.remove(obat)
                            save_data(OBAT_FILE, obat_list)
                            print("Obat berhasil dihapus!")
                            break

                    if not obat_found:
                        print("Obat tidak ditemukan.")
                elif sub_pilihan == '3':
                    print("Menampilkan Daftar Obat...")
                    obat_list = load_data(OBAT_FILE)
                    if not obat_list:
                        print("Tidak ada obat yang terdaftar.")
                    else:
                        print("Daftar Obat:")
                        # Create a list of lists for tabulate
                        obat_table = [[obat["nama"], obat["dosis"], obat["jumlah"], obat["tanggal_kadaluarsa"]] for obat in obat_list]
                        print(tabulate(obat_table, headers=["Nama Obat", "Dosis", "Jumlah", "Tanggal Kadaluarsa"], tablefmt="grid"))
                elif sub_pilihan == '4':
                    filter_tanggal_kadaluarsa 
                
                elif sub_pilihan == '5':
                    break  # Kembali ke menu utama
                else:
                    print("Pilihan tidak valid! Silakan coba lagi.")

        elif pilihan == '4':
            while True:
                tampilan_menu_pemesanan()
                sub_pilihan = input("Pilih submenu (1-2): ")
                if sub_pilihan == '1':
                    buat_pemesanan()
                elif sub_pilihan == '2':
                    # Logic to display the last order receipt can be added here
                    print("Fitur ini belum diimplementasikan.")
                elif sub_pilihan == '2':
                    break  # Kembali ke menu utama
                else:
                    print("Pilihan tidak valid! Silakan coba lagi.")

        elif pilihan == '5':
            while True:
                tampilan_menu_stock()
                sub_pilihan = input("Pilih submenu (1-3): ")
                if sub_pilihan == '1':
                    print("Cek Stock Obat...")
                    nama_obat = input("Masukkan nama obat yang ingin dicek: ")
                    obat_list = load_data(OBAT_FILE)
                    obat_found = False

                    for obat in obat_list:
                        if obat["nama"].lower() == nama_obat.lower():
                            obat_found = True
                            print("Detail Obat:")
                            print("Nama Obat:", obat["nama"])
                            print("Dosis:", obat["dosis"])
                            print("Jumlah Tersedia:", obat["jumlah"])
                            print("Tanggal Kadaluarsa:", obat["tanggal_kadaluarsa"])
                            break

                    if not obat_found:
                        print("Obat tidak ditemukan.")
                elif sub_pilihan == '2':
                    print("Cek Tanggal Kadaluarsa...")
                    nama_obat = input("Masukkan nama obat yang ingin dicek: ")
                    obat_list = load_data(OBAT_FILE)
                    obat_found = False

                    for obat in obat_list:
                        if obat["nama"].lower() == nama_obat.lower():
                            obat_found = True
                            print("Detail Obat:")
                            print("Nama Obat:", obat["nama"])
                            print("Tanggal Kadaluarsa:", obat["tanggal_kadaluarsa"])
                            break

                    if not obat_found:
                        print("Obat tidak ditemukan.")
                elif sub_pilihan == '3':
                    break  # Kembali ke menu utama
                else:
                    print("Pilihan tidak valid! Silakan coba lagi.")

        elif pilihan == '6':
            print("Keluar dari sistem")
            break
        else:
            print("Pilihan tidak valid! Silakan coba lagi.")
else:
    print("Akses ditolak.")