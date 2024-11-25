import pandas as pd
import os
from datetime import datetime
from tabulate import tabulate

ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "12345678"


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
        ["1", "Buat Pemesanan"],
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

                    # Simpan data apoteker ke dalam dictionary atau database
                    apoteker_data = {
                        "nama": nama_apoteker,
                        "alamat": alamat_apoteker,
                        "no_telepon": no_telepon_apoteker
                    }

                    # Tambahkan data apoteker ke dalam list atau database
                    apoteker_list = []  # atau database apoteker
                    apoteker_list.append(apoteker_data)

                    print("Apoteker berhasil ditambahkan!")
                    print("Data Apoteker:")
                    print("Nama:", nama_apoteker)
                    print("Alamat:", alamat_apoteker)
                    print("No Telepon:", no_telepon_apoteker)
                elif sub_pilihan == '2':
                    print("Menghapus Apoteker...")
                    # Logika untuk menghapus apoteker
                    nama_apoteker = input("Masukkan nama apoteker yang akan dihapus: ")
                    apoteker_found = False

                    for apoteker in apoteker_list:  # atau database apoteker
                        if apoteker["nama"] == nama_apoteker:
                            apoteker_found = True
                            apoteker_list.remove(apoteker)  # atau hapus data apoteker dari database
                            print("Apoteker berhasil dihapus!")
                            break

                    if not apoteker_found:
                        print("Apoteker tidak ditemukan.")
                elif sub_pilihan == '3':
                    print("Menampilkan Daftar Apoteker...")
                    if not apoteker_list:  # Check if the list is empty
                        print("Tidak ada apoteker yang terdaftar.")
                    else:
                        print("Daftar Apoteker:")
                        for apoteker in apoteker_list:  # Loop through the list of pharmacists
                            print("Nama:", apoteker["nama"])
                            print("Alamat:", apoteker["alamat"])
                            print("No Telepon:", apoteker["no_telepon"])
                            print("-------------------------")  # Separator for better readability
                elif sub_pilihan == '4':
                    break  # Kembali ke menu utama
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

                    # Simpan data pasien ke dalam dictionary atau database
                    pasien_data = {
                        "nama": nama_pasien,
                        "alamat": alamat_pasien,
                        "no_telepon": no_telepon_pasien,
                        "umur": umur_pasien
                    }

                    # Tambahkan data pasien ke dalam list atau database
                    pasien_list = []  # atau database pasien
                    pasien_list.append(pasien_data)

                    print("Pasien berhasil ditambahkan!")
                    print("Data Pasien:")
                    print("Nama:", nama_pasien)
                    print("Alamat:", alamat_pasien)
                    print("No Telepon:", no_telepon_pasien)
                    print("Umur:", umur_pasien)
                elif sub_pilihan == '2':
                    print("Menghapus Pasien...")
                    # Logika untuk menghapus pasien
                    nama_pasien = input("Masukkan nama pasien yang akan dihapus: ")
                    pasien_found = False

                    for pasien in pasien_list:  # Loop through the list of patients
                        if pasien["nama"] == nama_pasien:
                            pasien_found = True
                            pasien_list.remove(pasien)  # Remove the patient from the list
                            print("Pasien berhasil dihapus!")
                            break

                    if not pasien_found:
                        print("Pasien tidak ditemukan.")
                elif sub_pilihan == '3':
                    print("Menampilkan Daftar Pasien...")
                    if not pasien_list:  # Check if the list is empty
                        print("Tidak ada pasien yang terdaftar.")
                    else:
                        print("Daftar Pasien:")
                        for pasien in pasien_list:  # Loop through the list of patients
                            print("Nama:", pasien["nama"])
                            print("Alamat:", pasien["alamat"])
                            print("No Telepon:", pasien["no_telepon"])
                            print("Umur:", pasien["umur"])
                            print("-------------------------")  # Separator for better readability
                elif sub_pilihan == '4':
                    break  # Kembali ke menu utama
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
                    tanggal_kadaluarsa = input("Masukkan tanggal kadaluarsa (DD-MM-YYYY): ")

                    # Simpan data obat ke dalam dictionary atau database   
                    obat_data = {
                        "nama": nama_obat,
                        "dosis": dosis_obat,
                        "jumlah": jumlah_obat,
                        "tanggal_kadaluarsa": tanggal_kadaluarsa
                    }

                    # Tambahkan data obat ke dalam list atau database
                    obat_list = []  # Inisialisasi list obat di luar blok ini
                    obat_list.append(obat_data)
                    print("Obat berhasil ditambahkan!")
                    print("Data Obat:")
                    print("Nama:", nama_obat)
                    print("Dosis:", dosis_obat)
                    print("Jumlah:", jumlah_obat)
                    print("Tanggal Kadaluarsa:", tanggal_kadaluarsa)
                elif sub_pilihan == '2':
                    print("Menghapus Obat...")
                    # Logika untuk menghapus obat
                    nama_obat = input("Masukkan nama obat yang akan dihapus: ")
                    obat_found = False

                    for obat in obat_list:  # Loop through the list of medications
                        if obat["nama"] == nama_obat:
                            obat_found = True
                            obat_list.remove(obat)  # Remove the medication from the list
                            print("Obat berhasil dihapus!")
                            break

                    if not obat_found:
                        print("Obat tidak ditemukan.")
                elif sub_pilihan == '3':
                    print("Menampilkan Daftar Obat...")
                    if not obat_list:  # Check if the list is empty
                        print("Tidak ada obat yang terdaftar.")
                    else:
                        print("Daftar Obat:")
                        for obat in obat_list:  # Loop through the list of medications
                            print(tabulate([
                            print("Nama Obat:", obat["nama"]),
                            print("Dosis:", obat["dosis"]),
                            print("Jumlah:", obat["jumlah"]),
                            print("Tanggal Kadaluarsa:", obat["tanggal_kadaluarsa"])
                            ], headers=["Nama", "Dosis", "Jumlah", "Tanggal Kadaluarsa"], tablefmt="grid"))
                            print("-------------------------")  # Separator for better readability
                elif sub_pilihan == '4':
                    filter_tanggal_kadaluarsa()
                elif sub_pilihan == '5':
                    break  # Kembali ke menu utama
                else:
                    print("Pilihan tidak valid! Silakan coba lagi.")

        elif pilihan == '4':
            while True:
                tampilan_menu_pemesanan()
                sub_pilihan = input("Pilih submenu (1-3): ")
                if sub_pilihan == '1':
                    pemesanan = buat_pemesanan()
                    print("Pemesanan berhasil dibuat.")
                elif sub_pilihan == '2':
                    if 'pemesanan' in locals():
                        cetak_struk(pemesanan)
                    else:
                        print("Belum ada pemesanan yang dibuat.")
                elif sub_pilihan == '3':
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
                    obat_found = False

                    for obat in obat_list:  # Loop through the list of medications
                        if obat["nama"].lower() == nama_obat.lower():  # Case-insensitive comparison
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
                    obat_found = False

                    for obat in obat_list:  # Loop through the list of medications
                        if obat["nama"].lower() == nama_obat.lower():  # Case-insensitive comparison
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