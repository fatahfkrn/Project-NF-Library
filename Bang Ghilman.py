import random, string
from os import read, system
from time import sleep

def menu():
      print(
    """\n***** SELAMAT DATANG DI NF LIBRARY *****
      MENU:
      [1] Tambah Anggota Baru
      [2] Tambah Buku Baru
      [3] Pinjam Buku
      [4] Kembalikan Buku
      [5] Lihat Data Peminjaman
      [6] Keluar""")
def clear():
      print("\nEnter back to MENU")
      a = input()
      _ = system('cls')
def readBuku():         # Function untuk mengakses file buku
      dataBuku = []
      f = open('File Buku.txt')
      for each_line in f:
            dataBuku.append(each_line.strip())
      f.close()
      return dataBuku
def cek_buku(kd_buku):        # Function untuk mengecek kode buku
      for i in readBuku():
            if i[:6] == kd_buku:
                  return True
      return False
def nambahBuku(kode,judul,penulis, stok):       # Function untuk menambahkan data ke file buku
      myfile = open("File Buku.txt", 'a+')
      myfile.write(kode +", "+judul+", "+penulis+", "+stok+"\n")
      myfile.close()
def readAnggota():            # Function untuk mengakses file anggota
      dataAnggota = []
      f = open('File Anggota.txt')
      for each_line in f:
            dataAnggota.append(each_line.strip())
      f.close()
      return dataAnggota
def cek_anggota(kd_anggota):        # Function untuk mengecek kode anggota
      for i in readAnggota():
            if i[:6] == kd_anggota:
                  return True
      return False
def daftarAnggota(kode, nama, status):          # Function untuk menambahkan data ke file anggota
      myfile = open("File Anggota.txt", 'a+')
      myfile.write(kode +", "+nama+", "+status+"\n")
      myfile.close()
def cek_stok(kd_buku):        # Function untuk mengecek stock di file buku, 
      dataBuku = readBuku()
      for i in range (len(dataBuku)):
            if dataBuku [i][:6] == kd_buku:
                  dataBuku[i] = dataBuku[i].split(", ")# Mengubah string menjadi list
                  if int(dataBuku[i][-1]) > 0:        # jika stok dikurang 1 hasilnya lebih dari 0, maka kembalikan nilai dari (stok dikurang 1)
                        return True
      return False
def kurangStok(kd_buku):            # Function untuk mengurangi stok buku
      dataBuku = readBuku()
      for i in range(len(dataBuku)): #Ini adalah perulangan 
            if dataBuku[i][:6] == kd_buku: # Mengecek buku ada atau tidak di dalam file 
                  dataBuku[i] = dataBuku[i].split(", ") #Ini untuk mengubah jadi list (ngambil stok)
                  dataBuku[i][-1] = str(int(dataBuku[i][-1]) - 1)# Ngubah stok 
                  dataBuku[i] = ", ".join(dataBuku[i])#Ngembaliin menjadi str
      myfile = open('File Buku.txt', 'w+')
      for i in dataBuku:
            myfile.write(i+"\n")
      myfile.close()
def nambahStok(kd_buku):
      dataBuku = readBuku()
      for i in range(len(dataBuku)): #Ini adalah perulangan 
            if dataBuku[i][:6] == kd_buku: # Mengecek buku ada atau tidak di dalam file 
                  dataBuku[i] = dataBuku[i].split(", ") #Ini untuk mengubah jadi list (ngambil stok)
                  dataBuku[i][-1] = str(int(dataBuku[i][-1]) + 1)# Ngubah stok 
                  dataBuku[i] = ", ".join(dataBuku[i])#Ngembaliin menjadi str
      myfile = open('File Buku.txt', 'w+')
      for i in dataBuku:
            myfile.write(i+"\n")
      myfile.close()
def readPinjamBuku():                # Function untuk mengakses file peminjaman
      a_list = []
      myfile = open("File Peminjaman.txt")
      for line in myfile:
            a_list.append(line.strip())
      return a_list
def pinjamBuku(kd_buku,kd_anggota):                   # Function untuk mengecek ada gk kode anggota yang di input didalam file peminjaman
      dataPinjam = readPinjamBuku()
      ada = 0
      for i in range(len(dataPinjam)): #Ini adalah perulangan 
            if dataPinjam[i][:6] == kd_buku:
                  dataPinjam[i] = dataPinjam[i]+", "+kd_anggota
                  ada = 1
      if ada == 1:
            f = open('File Peminjaman.txt',"w+")
            for i in dataPinjam:
                  f.write(i+"\n")
            f.close()
      else:
            f = open('File Peminjaman.txt',"a+")
            f.write(kd_buku+", "+kd_anggota+"\n")
            f.close()
def cek_statusAngggota(kd_anggota):                   # Function untuk mengecek status keanggotaan
      dataAnggota = readAnggota()
      for i in range(len(dataAnggota)):
            if dataAnggota[i][:6] == kd_anggota:
                  if dataAnggota[i][-1] == "1":
                        return True
                  else:
                        return False
def anggota_pinjam(kd_buku,kd_anggota):         # Function untuk mengecek ada berapa kode anggota di kode buku
      dataPinjam = readPinjamBuku()
      for i in range(len(dataPinjam)):
            if dataPinjam[i][:6] == kd_buku:
                  dataPinjam[i] = dataPinjam[i].split(", ") #Ini untuk mengubah jadi list 
                  if dataPinjam[i].count(kd_anggota) == 1:
                        return True
                  else:
                        return False
def remove_anggota(kd_buku,kd_anggota):         # Function untuk menghapus kode anggota
      dataPinjam = readPinjamBuku()
      for i in range(len(dataPinjam)):
            if dataPinjam[i][:6] == kd_buku: # Mengecek buku ada atau tidak di dalam file 
                  dataPinjam[i] = dataPinjam[i].split(", ") #Ini untuk mengubah jadi list 
                  dataPinjam[i].remove(kd_anggota)
                  if len(dataPinjam[i]) == 1 :
                        del dataPinjam[i]
                  else:
                        dataPinjam[i] = ", ".join(dataPinjam[i])#Ngembaliin menjadi str
      myfile = open('File Peminjaman.txt', 'w+')
      for i in dataPinjam:
            myfile.write(i+"\n")
      myfile.close()
def viewPinjam():
      dataPinjam  = readPinjamBuku()
      dataBuku    = readBuku()
      dataAnggota = readAnggota()
      dataBukuD   = {}
      dataAnggotaD = {}

      for i in range(len(dataBuku)):
            dataBuku[i] = dataBuku[i].split(", ") #Ini untuk mengubah jadi list 
            dataBukuD[dataBuku[i][0]] = dataBuku[i][1:]

      for i in range(len(dataAnggota)):
            dataAnggota[i] = dataAnggota[i].split(", ") #Ini untuk mengubah jadi list 
            dataAnggotaD[dataAnggota[i][0]] = dataAnggota[i][1:]

      for i in range(len(dataPinjam)):
            dataPinjam[i] = dataPinjam[i].split(", ") #Ini untuk mengubah jadi list 

      print("\n*** DAFTAR PEMINJAMAN BUKU ***\n")

      for i in range(len(dataPinjam)):
            print("Judul: "+dataBukuD[dataPinjam[i][0]][0])
            print("Penulis: "+dataBukuD[dataPinjam[i][0]][1])
            for j in range(len(dataPinjam[i][1:])):
                  if dataAnggotaD[dataPinjam[i][j+1]][1] == "1":
                        print(str(j+1)+". "+dataAnggotaD[dataPinjam[i][j+1]][0]+"(*)")            
                  else:
                        print(str(j+1)+". "+dataAnggotaD[dataPinjam[i][j+1]][0])            
            print()

# Kode ini untuk menampilkan menu & fitur
menu()

while True:
      pilih = input("\nMasukkan menu pilihan Anda: ")
      
      # Fitur 1
      if pilih == "1":
            #Tampilan fitur 1
            print("\n*** PENDAFTARAN ANGGOTA BARU ***\n")
            nama = input("Masukkan Nama: ")
            tipeAnggota = input("Apakah merupakan karyawan NF Group? (Y/T): ")
            kode = "LIB" + ''.join(random.choice(string.digits) for _ in range(3))
            tipeAnggota = "1" if tipeAnggota == "Y" else  "2"
            daftarAnggota(kode, nama, tipeAnggota)
            print("Pendaftaran anggota dengan kode", kode, "atas nama", nama, "berhasil.")

      # Fitur 2
      elif pilih == "2":
            #Tampilan Fitur 2      
            print("\n*** PENAMBAHAN BUKU BARU ***\n")
            judul = input("Judul: ")
            penulis = input("Penulis: ")
            penulis = penulis.split() 
            penulis = ''.join(penulis)
            stok = input("Stok: ")
            kode = penulis[:3].upper() + ''.join(random.choice(string.digits) for _ in range(3))
            nambahBuku(kode, judul, penulis, stok)
            print("Penambahan buku baru dengan kode " + kode+" dan judul "+judul+" berhasil.")

      # Fitur 3
      elif pilih == "3":
            print("\n*** PEMINJAMAN BUKU ***\n")
            kd_buku = input("Kode buku: ")
            if cek_buku(kd_buku):
                  kd_anggota = input("Kode anggota: ")
                  if cek_anggota(kd_anggota):
                        if cek_stok(kd_buku):
                              pinjamBuku(kd_buku,kd_anggota)
                              kurangStok(kd_buku)
                              print("Peminjaman buku "+kd_buku+" oleh "+kd_anggota+" berhasil.")
                        else:
                              print("Stok buku kosong. Peminjaman gagal.")
                  else:
                        print("Kode anggota tidak terdaftar. Peminjaman gagal.\n")
            else:
                  print("Kode buku tidak ditemukan. Peminjaman gagal.\n")

      # Fitur 4
      elif pilih == "4":
            print("*** PENGEMBALIAN BUKU ***\n")
            kd_buku = input("Kode buku: ")
            if cek_buku(kd_buku):
                  kd_anggota = input("Kode anggota: ")
                  nambahStok(kd_buku)
                  if anggota_pinjam(kd_buku,kd_anggota):
                        denda = int(input("Keterlambatan pengembalian (dalam hari, 0 jika tidak terlambat): "))
                        if cek_statusAngggota(kd_anggota):
                              denda = 1000 * denda
                        else:
                              denda = 2500 * denda
                        print("\nTotal denda =",denda)
                        print("Silakan membayar denda keterlambatan di kasir.")
                        remove_anggota(kd_buku,kd_anggota)
                        print("Pengembalian buku "+kd_buku+" oleh "+kd_anggota+" berhasil.")
                  else:
                        print("Kode anggota tidak terdaftar sebagai peminjam buku tersebut. Pengembalian buku gagal.\n")
            else:
                  print("Kode buku salah. Pengembalian buku gagal.")

      # Fitur 5
      elif pilih == "5":
            viewPinjam()
      
      # Jika Selesai
      elif pilih == "6":
            print("Terima kasih atas kunjungan Anda...")
            break
      else:
            print("Pilihan Anda salah. Ulangi.")
      clear()
      menu()