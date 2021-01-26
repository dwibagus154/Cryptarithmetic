import time

# buka file

file_cryp = open("cryp3.txt", "r")

# baca isi file
cryp = file_cryp.readlines()

# mengetahui jumlah baris
# ###########
jumlahBaris = len(cryp)
# print(jumlahBaris)
# menghitung jumlah huruf
listHuruf = []
# print(len(listHuruf))
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
                # print(len(baris))
                # print(baris[0])
                # print(baris[4])

# jika list huruf belum 10 items, tambahkan karakter bebas
jumlahHurufAwal = len(listHuruf)
while(len(listHuruf) < 10):
    listHuruf.insert(0, "*")

# print huruf terakhir di pojok kanan bawwah
print(cryp[len(cryp)-1][len(cryp[len(cryp)-1])-2])
#########
# print(len(cryp[len(cryp)-1])-1)
print(listHuruf)


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


# print nilai hasil
print(ujiCrypHasil(cryp, listHuruf, 1, 2, 3, 4, 5, 6, 1, 2, 3, 5))


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


# print tanya
print(ujiCrypTanya(cryp, listHuruf, 1, 2, 3, 4, 5, 6, 1, 2, 3, 5))


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


print(isUnik([25, 25, 3, 4, 5, 6, 7], 6))


def isAwalZero(cryp, listHuruf, a, b, c, d, e, f, g, h, i, j):
    isZero = False
    for k in range(len(cryp) - 2):
        l = 0
        # jika awalnya spasi
        while cryp[k][l] == ' ':
            l += 1
        # print(l)
        # print(cryp[k][l])
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


# apakah ada yang diwali dengan nol
print(isAwalZero(cryp, listHuruf, 1, 2, 3, 4, 5, 0, 5, 8, 9, 0))

percobaan = 0

# for a in range(9, 10):
#     for b in range(9, 10):
#         for c in range(9, 10):
#             for d in range(9, 10):
#                 for e in range(9, 10):
#                     for f in range(9, 10):
#                         for g in range(1, 2):
#                             for h in range(2, 3):
#                                 for i in range(3, 10):
#                                     for j in range(10):
#                                         print(ujiCrypHasil(cryp, listHuruf,
#                                                            a, b, c, d, e, f, g, h, i, j))
#                                         print(ujiCrypHasil(cryp, listHuruf, a, b, c, d, e, f, g, h, i, j) == ujiCrypTanya(
#                                             cryp, listHuruf, a, b, c, d, e, f, g, h, i, j))
#                                         if ujiCrypHasil(cryp, listHuruf, a, b, c, d, e, f, g, h, i, j) == ujiCrypTanya(cryp, listHuruf, a, b, c, d, e, f, g, h, i, j):
#                                             print('selesai')
#                                             break
#                                             if not isAwalZero(cryp, listHuruf, a, b, c, d, e, f, g, h, i, j):
#                                                 if jumlahHurufAwal == 10:
#                                                     if isUnik([a, b, c, d, e, f, g, h, i, j]):
#                                                         break
#                                                 elif jumlahHurufAwal == 9:
#                                                     if isUnik([b, c, d, e, f, g, h, i, j]):
#                                                         break
#                                                 elif jumlahHurufAwal == 8:
#                                                     if isUnik([c, d, e, f, g, h, i, j]):
#                                                         break
#                                                 elif jumlahHurufAwal == 7:
#                                                     if isUnik([d, e, f, g, h, i, j]):
#                                                         break
#                                                 elif jumlahHurufAwal == 6:
#                                                     if isUnik([e, f, g, h, i, j]):
#                                                         break
#                                                 elif jumlahHurufAwal == 5:
#                                                     if isUnik([f, g, h, i, j]):
#                                                         break
#                                                 elif jumlahHurufAwal == 4:
#                                                     if isUnik([g, h, i, j]):
#                                                         break
#                                                 elif jumlahHurufAwal == 3:
#                                                     if isUnik([h, i, j]):
#                                                         break
#                                                 else:
#                                                     if isUnik([i, j]):
#                                                         break
#                                         percobaan += 1
# print(a)
# print(percobaan)
print(isUnik([0, 1, 9, 5, 6, 7, 2, 0, 8], jumlahHurufAwal))
a = 2
ketemu = False
awal = time.time()
while a < 10 and not ketemu:
    b = 9
    if not isUnik([a, b], jumlahHurufAwal):
        b += 1
    print("b=")
    print(b)
    while b < 10 and not ketemu:
        c = 7
        if not isUnik([a, b], jumlahHurufAwal):
            b += 1
        while c < 10 and not ketemu:
            d = 8
            if not isUnik([a, b, c], jumlahHurufAwal):
                c += 1
            print("c=")
            print(c)
            while d < 10 and not ketemu:
                e = 6
                if not isUnik([a, b, c, d], jumlahHurufAwal):
                    d += 1
                print("d=")
                print(d)
                while e < 10 and not ketemu:
                    f = 0
                    if not isUnik([a, b, c, d, e], jumlahHurufAwal):
                        e += 1
                    print("e=")
                    print(e)
                    while f < 10 and not ketemu:
                        g = 0
                        if not isUnik([a, b, c, d, e, f], jumlahHurufAwal):
                            f += 1
                        # print("f=")
                        # print(f)
                        while g < 10 and not ketemu:
                            h = 0
                            if not isUnik([a, b, c, d, e, f, g], jumlahHurufAwal):
                                g += 1
                                # print("g=")
                                # print(g)
                            while h < 10 and not ketemu:
                                i = 0
                                if not isUnik([a, b, c, d, e, f, g, h], jumlahHurufAwal):
                                    h += 1
                                # print("h=")
                                # print(h)
                                while i < 10 and not ketemu:
                                    j = 0
                                    if not isUnik([a, b, c, d, e, f, g, h, i], jumlahHurufAwal):
                                        i += 1
                                    # print("i=")
                                    # print(i)
                                    while j < 10 and not ketemu:
                                        if not isUnik([a, b, c, d, e, f, g, h, i, j], jumlahHurufAwal):
                                            j += 1
                                        # print("j=")
                                        # print(j)
                                        # print(ujiCrypHasil(cryp, listHuruf,
                                        #                    a, b, c, d, e, f, g, h, i, j))
                                        # print(ujiCrypHasil(cryp, listHuruf, a, b, c, d, e, f, g, h, i, j) == ujiCrypTanya(
                                        #     cryp, listHuruf, a, b, c, d, e, f, g, h, i, j))
                                        if ujiCrypHasil(cryp, listHuruf, a, b, c, d, e, f, g, h, i, j) == ujiCrypTanya(cryp, listHuruf, a, b, c, d, e, f, g, h, i, j):
                                            print("tahap1")
                                            if not isAwalZero(cryp, listHuruf, a, b, c, d, e, f, g, h, i, j):
                                                print("tahap2")
                                                if jumlahHurufAwal == 10:
                                                    if isUnik([a, b, c, d, e, f, g, h, i, j], jumlahHurufAwal):
                                                        ketemu = True
                                                elif jumlahHurufAwal == 9:
                                                    if isUnik([b, c, d, e, f, g, h, i, j], jumlahHurufAwal):
                                                        ketemu = True
                                                elif jumlahHurufAwal == 8:
                                                    ketemu = True
                                                elif jumlahHurufAwal == 7:
                                                    if isUnik([d, e, f, g, h, i, j], jumlahHurufAwal):
                                                        ketemu = True
                                                elif jumlahHurufAwal == 6:
                                                    if isUnik([e, f, g, h, i, j], jumlahHurufAwal):
                                                        ketemu = True
                                                elif jumlahHurufAwal == 5:
                                                    if isUnik([f, g, h, i, j], jumlahHurufAwal):
                                                        ketemu = True
                                                elif jumlahHurufAwal == 4:
                                                    if isUnik([g, h, i, j], jumlahHurufAwal):
                                                        ketemu = True
                                                elif jumlahHurufAwal == 3:
                                                    if isUnik([h, i, j], jumlahHurufAwal):
                                                        ketemu = True
                                                else:
                                                    if isUnik([i, j], jumlahBaris):
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
                print('c=')
                print(c)
        if not ketemu:
            b += 1
            print(b)
        print(ketemu)
    if not ketemu:
        a += 1
akhir = time.time()
print(percobaan)
print(b)
print([a, b, c, d, e, f, g, h, i, j])
print(listHuruf)
print(akhir-awal)
print(listHuruf[5])
print(f)
abjad = f
# nulis file
f = open("jawaban.txt", "w")
f.write("solusi\n")
jawaban = [[" " for j in range((2*len(cryp[len(cryp)-1]) + 1) + 8)]
           for i in range(len(cryp))]
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
print(jawaban)
for i in range(len(jawaban)):
    for j in range(len(jawaban[0])):
        f.write(str(jawaban[i][j]))
    f.write("\n")
f.close()


# tutup file
file_cryp.close()
