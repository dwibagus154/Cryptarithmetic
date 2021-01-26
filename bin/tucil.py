# Nama = Kadek Dwi Bagus Ananta Udayana
# NIM = 13519057
# KELAS = K2

import time

# buka file

file_cryp = open("./test/test5.txt", "r")

# baca isi file
cryp = file_cryp.readlines()

# ########################### MEMASUKKAN SEMUA HURUF KE DALAM LIST #############################################
# mengetahui jumlah baris
jumlahBaris = len(cryp)
# menghitung jumlah huruf
listHuruf = []

for baris in cryp:
    for i in range(len(baris)):
        # cek apakah item nya adalah spasi atau - atau +
        if not baris[i] == '-' and not baris[i] == ' ' and not baris[i] == '+' and not baris[i] == '\n':
            # cek apakah list nya masih kosong
            if len(listHuruf) == 0:
                listHuruf.append(baris[i])
            else:
                # cek apakah sudah ada di dalam list atau belum
                tidakAda = True
                for j in range(len(listHuruf)):
                    if baris[i] == listHuruf[j]:
                        tidakAda = False

                if tidakAda:
                    listHuruf.append(baris[i])


# jika list huruf belum 10 items, tambahkan karakter bebas
jumlahHurufAwal = len(listHuruf)
while(len(listHuruf) < 10):
    listHuruf.insert(0, "*")

# ########################################################################################################

# ########################### FUNGSI MENCARI HASIL PEJUMLAHAN #############################################


def ujiCrypHasil(cryp, listHuruf, a, b, c, d, e, f, g, h, i, j):
    hasil = 0
    idxHasil = len(cryp[len(cryp)-1])-1
    # jika diakhiri dengan spasi
    satuan = 0
    while cryp[len(cryp)-1][idxHasil] == ' ' or cryp[len(cryp)-1][idxHasil] == '\n':
        idxHasil -= 1
    # print(idxHasil)
    for l in range(idxHasil, -1,  -1):
        for m in range(len(listHuruf)):
            if cryp[len(cryp)-1][l] == listHuruf[m]:
                pangkat = 10**satuan
                if m == 0:
                    hasil += (a*pangkat)
                elif m == 1:
                    hasil += (b*pangkat)
                elif m == 2:
                    hasil += (c*pangkat)
                elif m == 3:
                    hasil += (d*pangkat)
                elif m == 4:
                    hasil += (e*pangkat)
                elif m == 5:
                    hasil += (f*pangkat)
                elif m == 6:
                    hasil += (g*pangkat)
                elif m == 7:
                    hasil += (h*pangkat)
                elif m == 8:
                    hasil += (i*pangkat)
                else:
                    hasil += (j*pangkat)
                satuan += 1
    return hasil
# ########################################################################################################

# ########################### FUNGSI MENCARI JUMLAH PARAMETER YANG DIJUMLAHKAN ############################


def ujiCrypTanya(cryp, listHuruf, a, b, c, d, e, f, g, h, i, j):
    tanya = 0
    for k in range(len(cryp) - 2):
        # print(k)
        idxTanya = len(cryp[k])-2
        # jika diakhiri dengan spasi
        satuan = 0
        while cryp[k][idxTanya] == ' ' or cryp[k][idxTanya] == '+':
            idxTanya -= 1
        # print(idxTanya)
        for l in range(idxTanya, -1,  -1):
            for m in range(len(listHuruf)):
                if cryp[k][l] == listHuruf[m]:
                    pangkat = 10**satuan
                    if m == 0:
                        tanya += (a*pangkat)
                    elif m == 1:
                        tanya += (b*pangkat)
                    elif m == 2:
                        tanya += (c*pangkat)
                    elif m == 3:
                        tanya += (d*pangkat)
                    elif m == 4:
                        tanya += (e*pangkat)
                    elif m == 5:
                        tanya += (f*pangkat)
                    elif m == 6:
                        tanya += (g*pangkat)
                    elif m == 7:
                        tanya += (h*pangkat)
                    elif m == 8:
                        tanya += (i*pangkat)
                    else:
                        tanya += (j*pangkat)
                    satuan += 1
    return tanya
# ########################################################################################################

# #####################################   FUNGSI APAKAH SEBUAH LIST UNIK    ##################################


def isUnik(ls, jumlahHurufAwal):
    unik = True
    k = 0
    ls1 = []
    if jumlahHurufAwal == 10:
        ls1 = ls
    elif jumlahHurufAwal == 9:
        for i in range(1, len(ls)):
            ls1.append(ls[i])
    elif jumlahHurufAwal == 8:
        for i in range(2, len(ls)):
            ls1.append(ls[i])
    elif jumlahHurufAwal == 7:
        for i in range(3, len(ls)):
            ls1.append(ls[i])
    elif jumlahHurufAwal == 6:
        for i in range(4, len(ls)):
            ls1.append(ls[i])
    elif jumlahHurufAwal == 5:
        for i in range(5, len(ls)):
            ls1.append(ls[i])
    elif jumlahHurufAwal == 4:
        for i in range(6, len(ls)):
            ls1.append(ls[i])
    elif jumlahHurufAwal == 3:
        for i in range(7, len(ls)):
            ls1.append(ls[i])
    else:
        for i in range(8, len(ls)):
            ls1.append(ls[i])

    while unik and k < len(ls1):
        for j in range(len(ls1)):
            if k != j:
                if ls1[k] == ls1[j]:
                    unik = False
        k += 1
    return unik

# ########################################################################################################


# ##########################    FUNGSI APAKAH PADA SOAL DIAWALI ANGKA 0     ##############################
def isAwalZero(cryp, listHuruf, a, b, c, d, e, f, g, h, i, j):
    isZero = False
    for k in range(len(cryp)):
        if k == len(cryp) - 2:
            k += 1
        l = 0
        # jika awalnya spasi
        while cryp[k][l] == ' ':
            l += 1
        for m in range(len(listHuruf)):
            if cryp[k][l] == listHuruf[m]:
                if m == 0:
                    if a == 0:
                        isZero = True
                elif m == 1:
                    if b == 0:
                        isZero = True
                elif m == 2:
                    if c == 0:
                        isZero = True
                elif m == 3:
                    if d == 0:
                        isZero = True
                elif m == 4:
                    if e == 0:
                        isZero = True
                elif m == 5:
                    if f == 0:
                        isZero = True
                elif m == 6:
                    if g == 0:
                        isZero = True
                elif m == 7:
                    if h == 0:
                        isZero = True
                elif m == 8:
                    if i == 0:
                        isZero = True
                else:
                    if j == 0:
                        isZero = True
    return isZero

# ########################################################################################################

# ################################  APAKAH LIST KURANG DARI 10#######################################


def lessThenTen(list):
    less = True
    for i in range(len(list)):
        if list[i] > 9:
            less = False
    return less
# ########################################################################################################


# ##################################    MAIN PROGRAM        #############################################
# JUMLAH PERCOBAAN DIDEFINISIKAN VAR percobaan
percobaan = 0
a = 0
ketemu = False
awal = time.time()
while a < 10 and not ketemu:
    b = 0
    while b < 10 and not ketemu:
        c = 0
        while not isUnik([a, b], jumlahHurufAwal):
            b += 1
        while c < 10 and not ketemu:
            d = 0
            while not isUnik([a, b, c], jumlahHurufAwal):
                c += 1
            while d < 10 and not ketemu:
                e = 0
                while not isUnik([a, b, c, d], jumlahHurufAwal):
                    d += 1
                while e < 10 and not ketemu:
                    f = 0
                    while not isUnik([a, b, c, d, e], jumlahHurufAwal):
                        e += 1
                    while f < 10 and not ketemu:
                        g = 0
                        while not isUnik([a, b, c, d, e, f], jumlahHurufAwal):
                            f += 1
                        while g < 10 and not ketemu:
                            h = 0
                            while not isUnik([a, b, c, d, e, f, g], jumlahHurufAwal):
                                g += 1
                            while h < 10 and not ketemu:
                                i = 0
                                while not isUnik([a, b, c, d, e, f, g, h], jumlahHurufAwal):
                                    h += 1
                                while i < 10 and not ketemu:
                                    j = 0
                                    while not isUnik([a, b, c, d, e, f, g, h, i], jumlahHurufAwal):
                                        i += 1
                                    while j < 10 and not ketemu:
                                        while not isUnik([a, b, c, d, e, f, g, h, i, j], jumlahHurufAwal):
                                            j += 1
                                        if lessThenTen([a, b, c, d, e, f, g, h, i, j]):
                                            if ujiCrypHasil(cryp, listHuruf, a, b, c, d, e, f, g, h, i, j) == ujiCrypTanya(cryp, listHuruf, a, b, c, d, e, f, g, h, i, j):
                                                if not isAwalZero(cryp, listHuruf, a, b, c, d, e, f, g, h, i, j):
                                                    if jumlahHurufAwal == 10:
                                                        ketemu = True
                                                    elif jumlahHurufAwal == 9:
                                                        ketemu = True
                                                    elif jumlahHurufAwal == 8:
                                                        ketemu = True
                                                    elif jumlahHurufAwal == 7:
                                                        ketemu = True
                                                    elif jumlahHurufAwal == 6:
                                                        ketemu = True
                                                    elif jumlahHurufAwal == 5:
                                                        ketemu = True
                                                    elif jumlahHurufAwal == 4:
                                                        ketemu = True
                                                    elif jumlahHurufAwal == 3:
                                                        ketemu = True
                                                    else:
                                                        ketemu = True
                                        percobaan += 1
                                        if not ketemu:
                                            j += 1
                                    if not ketemu:
                                        i += 1
                                if not ketemu:
                                    h += 1
                            if not ketemu:
                                g += 1
                        if not ketemu:
                            f += 1
                    if not ketemu:
                        e += 1
                if not ketemu:
                    d += 1
            if not ketemu:
                c += 1
        if not ketemu:
            b += 1
    if not ketemu:
        a += 1
abjad = f
# ########################################################################################################

# # ##########################  NULIS FILE      #########################################################
f = open("./test/jawaban.txt", "w")
jawaban = [[" " for s in range((2*len(cryp[len(cryp)-1]) + 1) + 8)]
           for t in range(len(cryp))]
for q in range(len(cryp)):
    for r in range(len(cryp[len(cryp)-1])):
        if cryp[q][r] == listHuruf[0]:
            jawaban[q][r + 5 + len(cryp[len(cryp)-1])] = a
            jawaban[q][r] = listHuruf[0]
        elif cryp[q][r] == listHuruf[1]:
            jawaban[q][r + 5 + len(cryp[len(cryp)-1])] = b
            jawaban[q][r] = listHuruf[1]
        elif cryp[q][r] == listHuruf[2]:
            jawaban[q][r + 5 + len(cryp[len(cryp)-1])] = c
            jawaban[q][r] = listHuruf[2]
        elif cryp[q][r] == listHuruf[3]:
            jawaban[q][r + 5 + len(cryp[len(cryp)-1])] = d
            jawaban[q][r] = listHuruf[3]
        elif cryp[q][r] == listHuruf[4]:
            jawaban[q][r + 5 + len(cryp[len(cryp)-1])] = e
            jawaban[q][r] = listHuruf[4]
        elif cryp[q][r] == listHuruf[5]:
            jawaban[q][r + 5 + len(cryp[len(cryp)-1])] = abjad
            jawaban[q][r] = listHuruf[5]
        elif cryp[q][r] == listHuruf[6]:
            jawaban[q][r + 5 + len(cryp[len(cryp)-1])] = g
            jawaban[q][r] = listHuruf[6]
        elif cryp[q][r] == listHuruf[7]:
            jawaban[q][r + 5 + len(cryp[len(cryp)-1])] = h
            jawaban[q][r] = listHuruf[7]
        elif cryp[q][r] == listHuruf[8]:
            jawaban[q][r + 5 + len(cryp[len(cryp)-1])] = i
            jawaban[q][r] = listHuruf[8]
        elif cryp[q][r] == listHuruf[9]:
            jawaban[q][r + 5 + len(cryp[len(cryp)-1])] = j
            jawaban[q][r] = listHuruf[9]
        elif cryp[q][r] == "+":
            jawaban[q][r + 5 + len(cryp[len(cryp)-1])] = "+"
            jawaban[q][r] = "+"
        elif cryp[q][r] == "-":
            jawaban[q][r + 5 + len(cryp[len(cryp)-1])] = "-"
            jawaban[q][r] = "-"
        else:
            jawaban[q][r + 5 + len(cryp[len(cryp)-1])] = " "
            jawaban[q][r] = " "
# f.writelines(teks_list)
if ketemu:
    for i in range(len(jawaban)):
        for j in range(len(jawaban[0])):
            f.write(str(jawaban[i][j]))
        f.write("\n")
else:
    f.write("Tidak Ada Solusi\n")

akhir = time.time()
waktu = round((akhir - awal), 4)

# print waktu
f.write("\nWaktu: ")
if waktu > 3600:
    jam = waktu // 3600
    temp = round((waktu % 3600), 4)
    if temp > 60:
        menit = temp//60
        detik = round((temp % 60), 4)
    else:
        menit = 0
        detik = temp
else:
    jam = 0
    if waktu > 60:
        menit = waktu // 60
        detik = round((waktu % 60), 4)
    else:
        menit = 0
        detik = waktu
f.write(str(jam))
f.write(" jam, ")
f.write(str(menit))
f.write(" menit, ")
f.write(str(detik))
f.write(" detik.")
f.write("\n\nJumlah Percobaan : ")
f.write(str(percobaan))

f.close()
# ########################################################################################################

# tutup file
file_cryp.close()
