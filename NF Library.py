import random, string
def fitur1():
      
      #Tampilan fitur 1
      print("\n*** PENDAFTARAN ANGGOTA BARU ***\n")
      nama = input("Masukkan Nama: ")
      tipeAnggota = input("Apakah merupakan karyawan NF Group? (Y/T): ")
      if tipeAnggota == "Y" or tipeAnggota == "y":
            tipeAnggota = "1"
      else:
            tipeAnggota = "2"
      kode = "LIB" + ''.join(random.choice(string.digits) for _ in range(3))
      print("Pendaftaran anggota dengan kode", kode, "atas nama", nama, "berhasil.")
      
      #Menambahkan data ke file anggota
      myFile = open('File Anggota.txt', 'a+')
      myFile.write(kode + ', ' + nama + ', ' + tipeAnggota + '\n')
      myFile.close()

def fitur2():

      #Tampilan Fitur 2      
      print("\n*** PENAMBAHAN BUKU BARU ***\n")
      judul = input("Judul: ")
      penulis = input("Penulis: ")
      stok = input("Stok: ")
      penulis = penulis.split() 
      penulis = ''.join(penulis)
      kode = penulis[:3].upper() + ''.join(random.choice(string.digits) for _ in range(3))
      print("Penambahan buku baru dengan kode " + kode+" dan judul "+judul+" berhasil.")
      
      #Menambahkan data ke file buku
      myFile = open('File Buku.txt')
      myFile.write(kode + ', ' + judul + ', ' + penulis + ', ' + stok + '\n')
      myFile.close()

def fitur3():
      print("\n*** PEMINJAMAN BUKU***\n")

      kd_buku = input("Kode buku: ")

      #Akses File Buku
      dataBuku = []
      f = open('File Buku.txt')
      for each_line in f:
            dataBuku.append(each_line.strip())
      f.close()

      #Akses Kode Buku
      kodeBuku = False
      for i in dataBuku:
            if i[:6] == kd_buku:
                  kodeBuku = True


      #Mengecek apakah inputan kode buku ada didalam file buku
      if kodeBuku :           #jika benar
            kd_anggota = input("Kode anggota: ")
            
            #Akses File Anggota
            dataAnggota = []
            f = open('File Anggota.txt')
            for each_line in f:
                  dataAnggota.append(each_line.strip())
            f.close()

            #Akses Kode Anggota
            kodeAnggota = False
            for i in dataAnggota:
                  if i[:6] == kd_anggota:
                        kodeAnggota = True
            #Mengecek apakah kode anggota ada didalam file anggota
            if kodeAnggota:           #jika ada
                  
                  #Cek Stock
                  stock = False
                  for i in range (len(dataBuku)):
                        if dataBuku [i][:6] == kd_buku:
                              dataBuku[i] = dataBuku[i].split(", ")# Mengubah string menjadi list
                              if int(dataBuku[i][-1]) > 0:
                                    stock = True
                              dataBuku[i] = ', '.join(dataBuku[i])#Ngembaliin menjadi str
                              

                  #Mengecek apakah stock buku ada atau tidak
                  if stock:         #jika ada

                        #Akses file peminjaman 
                        listPinjam= []
                        myfile = open("File Peminjaman.txt")
                        for line in myfile:
                              listPinjam.append(line.strip())
                        myfile.close()

                        #Mengecek stock buku dari kode buku
                        ada = 0
                        for i in range(len(listPinjam)): #Ini adalah perulangan 
                              if listPinjam[i][:6] == kd_buku:
                                    listPinjam[i] = listPinjam[i]+", "+kd_anggota
                                    ada = 1
                        if ada == 1:      #jika ada
                              f = open('File Peminjaman.txt',"w+")
                              for i in listPinjam:
                                    f.write(i+"\n")
                              f.close()
                        else:
                              f = open('File Peminjaman.txt',"a+")
                              f.write(kd_buku+", "+kd_anggota+"\n")
                              f.close()
                              
                        #mengecek buku dan mengubah stock buku
                        for i in range(len(dataBuku)): #Ini adalah perulangan 
                              if dataBuku[i][:6] == kd_buku: # Mengecek buku ada atau tidak di dalam file 
                                    dataBuku[i] = dataBuku[i].split(", ") #Ini untuk mengubah jadi list (ngambil stok)
                                    dataBuku[i][-1] = str(int(dataBuku[i][-1]) - 1)# Ngubah stok 
                                    dataBuku[i] = ', '.join(dataBuku[i])#Ngembaliin menjadi str

                                    #mengganti data kedalam file buku
                        myfile = open('File Buku.txt', 'w+')
                        for i in dataBuku:
                              myfile.write(i+"\n")
                        myfile.close()

                        #Menampilkan hasil peminjaman
                        print("Peminjaman buku "+kd_buku + " oleh "+kd_anggota+" berhasil.")

                  else:       #jika salah, tampilkan
                        print("Stok buku kosong. Peminjaman gagal.")
            else:             #jika salah, tampilkan
                  print("Kode anggota tidak terdaftar. Peminjaman gagal.\n")
      else:                   #jika salah, tampilkan
            print("Kode buku tidak ditemukan. Peminjaman gagal.\n")

def fitur4():
      print("\n*** PENGEMBALIAN BUKU ***\n")

      kd_buku = input("Kode buku: ")

      #Akses File Peminjaman
      dataPinjam = []
      f = open('File Peminjaman.txt')
      for each_line in f:
            dataPinjam.append(each_line.strip())
      f.close()
      #Akses Kode Buku
      kodeBuku = False
      for i in dataPinjam:
            if i[:6] == kd_buku:
                  kodeBuku = True
      #Mengecek apakah kode anggota yang diinput ada di file peminjaman
      if kodeBuku:            #
            kd_anggota = input("Kode anggota: ")
            
            #mengakses file buku
            dataBuku = []
            f = open('File Buku.txt')
            for each_line in f:
                  dataBuku.append(each_line.strip())
            f.close()
            
            #mengakses stok buku untuk menambahkan stok
            for i in range(len(dataBuku)): #Ini adalah perulangan 
                  if dataBuku[i][:6] == kd_buku: # Mengecek buku ada atau tidak di dalam file 
                        dataBuku[i] = dataBuku[i].split(", ") #Ini untuk mengubah jadi list (ngambil stok)
                        dataBuku[i][-1] = str(int(dataBuku[i][-1]) + 1)# Ngubah stok 
                        dataBuku[i] = ', '.join(dataBuku[i])#Ngembaliin menjadi str

            #memperbarui stock buku yang ada di file buku
            myfile = open('File Buku.txt', 'w+')
            for i in dataBuku:
                  myfile.write(i+"\n")
            myfile.close()

            for i in range (len(dataPinjam)):
                  if dataPinjam[i][:6] == kd_buku:
                        dataPinjam[i] = dataPinjam[i].split(", ")
                        if dataPinjam[i].count(kd_anggota) != 0:
                              dataPinjam[i].remove(kd_anggota)

                              if (len(dataPinjam[i])) == 1:
                                    del dataPinjam[i]
                              else:
                                    dataPinjam[i]= ", ".join(dataPinjam[i])
                              myfile = open('File Peminjaman.txt', 'w+')
                              for i in dataPinjam:
                                    myfile.write(i+"\n")
                              myfile.close()
                              
                              #mengecek apakah kode anggota ada difile peminjaman
                              if True:                      #jika ada
                                    denda = int(input("Keterlambatan pengembalian (dalam hari, 0 jika tidak terlambat): "))
                                    #mengakses file data anggota
                                    dataAnggota = []
                                    f = open('File Anggota.txt')
                                    for each_line in f:
                                          dataAnggota.append(each_line.strip())
                                    f.close()
                                    #mengecek status dari anggota
                                    status = False
                                    for i in range(len(dataAnggota)):
                                          if dataAnggota[i][:6] == kd_anggota:
                                                if dataAnggota[i][-1] == "1":
                                                      status = True
                                    if status:         ##jika kode anggota mempunyai status sebagai anggota
                                          denda = 1000 * denda
                                    else:                         #jika bukan merupakan anggota
                                          denda = 2500 * denda

                                    # menampilkan hasil dari keterlambatan pengembalian
                                    print("Total denda =", denda)
                                    print("Silakan membayar denda keterlambatan di kasir.")
                        else:
                              print("Kode anggota tidak ada")
      else:
            print("Kode buku salah")

def fitur5():
      # ubah data text -> list (temp) -> dict (dataBuku)
      # Data buku
      temp = []  #variabel wadah list
      dataBuku = {}  #variabel wadah dict
      
      # akses file buku
      myfile = open("File Buku.txt")
      for line in myfile:
            temp = line.split(", ") #Mengubah menjadi multiple list
            
            dataBuku[temp[0]] = [temp[1],temp[2],str(int(temp[3]))] #Mengubah multi list menjadi dict

      # Data Anggota
      temp = []  #variabel wadah list
      dataAnggota = {}  #variabel wadah dict
      
      # akses file anggota
      myfile = open("File Anggota.txt")
      for line in myfile:
            temp = line.split(", ") #Mengubah menjadi multiple list
            dataAnggota[temp[0]] = [temp[1],str(int(temp[2]))] #Mengubah multi list menjadi dict

            
      # Data Pinjam
      temp = []
      dataPinjam = {}
      myfile = open("File Peminjaman.txt")
      for line in myfile:
            temp = line.strip().split(", ") #Mengubah menjadi multiple list
            dataPinjam[temp[0]] = temp[1:] #Mengubah multi list menjadi dict

      
      #kita nampilin value dataBuku dimana keysnya adalah kode buku yang ada didalam dataPinjam
      print("*** \nDAFTAR PEMINJAMAN BUKU ***\n")

      for i in dataPinjam.keys():
            nomer = 0
            print("Judul : "+dataBuku[i][0])
            print("Penulis : "+dataBuku[i][1])
            print("Daftar Pinjam:")
            for j in dataPinjam[i]:
                  nomer +=1
                  print(str(nomer)+". "+str(dataAnggota[j][0])+("(*)" if dataAnggota[j][1] == "1" else ""))
                  print()

print(
      """
    ***** SELAMAT DATANG DI NF LIBRARY *****
      MENU:
      [1] Tambah Anggota Baru
      [2] Tambah Buku Baru
      [3] Pinjam Buku
      [4] Kembalikan Buku
      [5] Lihat Data Peminjaman
      [6] Keluar""")
while True:
      pilih = input("\nMasukkan menu pilihan Anda: ")
      # Fitur 1
      if pilih == "1":
            fitur1()

      # Fitur 2
      elif pilih == "2":
            fitur2()

      # Fitur 3
      elif pilih == "3":
            fitur3()
      # Fitur 4
      elif pilih == "4":
            fitur4()
      # Fitur 5
      elif pilih == "5":
            fitur5()
      # Mengakhiri program/perulangan while
      elif pilih == "6":
            print("Terima kasih atas kunjungan Anda...")
            break
      #Ketika masukkan tidak sesuai
      else:
            print("Pilihan Anda salah. Ulangi.")