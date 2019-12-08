# title : Program Gaji Karyawan
# Author : faqih yugo susilo
# description :  prosedural
print('''
===============================================
            Program Gaji Karyawan
===============================================
    1. Direktur Utama 10jt
    2. Manajer Pabrik 8jt
    3. Manajer Pemasaran 7jt
===============================================
''')
inp = int(input("Masukkan jabatan sesuai angka : "))
if (inp is 1):
    gp = 10000000
elif (inp is 2):
    gp = 8000000
elif (inp is 3):
    gp = 7000000
else:
    gp = "Salah, masukkan sesuai jabatan"
print("===============================================")
bln = input("Masukkan bulan : ")
thn = int(input("Masukkan tahun : "))
nik = int(input("Masukkan nik : "))
nm = input("Masukkan nama : ")
alm = input("Masukkan alamat : ")
hd = int(input('Masukkan jumlah kehadiran : '))
thd = int(input('Masukkan jumlah ketidakhadiran : '))
an = int(input("Masukkan jumlah anak : "))

pph = 0.05 * gp
ansu = 500000
trans = 750000
hdr = 50000
pjk = 0.05
thdr = 30000

if (an <= 0):
    ank = 0
elif (an >= 3):
    ank = 500000
else:
    ank = 750000

tolhdr = hd * hdr
tolthdr = thd * thdr
tp = (gp + ank + ansu + trans + tolhdr)
tpa = (tolthdr + pph)
tolp = (tp - tpa)

print("\n\n")
print("===============================================")
print("=============+++++++++++++++++++++=============")
print("                   Rincian                     ")
print("-----------------------------------------------")
print('''
        NIK Karyawan       :''', nik, '''
        Nama Karyawan      :''', nm, '''
        Gaji Karyawan      : Rp.''', gp, '''
        Tunjangan Anak     : Rp.''', ank, '''
        Asuransi Kesehatan : Rp.''', ansu, '''
        Uang Transport     : Rp.''', trans, '''
        Jumlah Absen Masuk :''', hd, '''* 50000/hari
''')
print("-----------------------------------------------")
print("     Total Pendapatan   : Rp.", tp, "          ")
print("-----------------------------------------------")
print('\n')
print("=============+++++++++++++++++++++=============")
print("                   Potongan                    ")
print("-----------------------------------------------")
print('''
        Jumlah Alfa  :''', thd, ''' * 30.000/hari
        PPh Pasal 21 : Rp.''', pph, '''
''')
print("-----------------------------------------------")
print("     Total Potongan   : Rp.", tpa, "           ")
print("-----------------------------------------------")
print("====+++++++++++++++++++++++++++++++++++========")
print("     Total gaji karyawan : Rp.", tolp, "       ")
print("===============================================")
print("\n\n")
print('''
                    PT. BIZANTECH ULTIMATUM
                One Stop Busniness and IT Solution
    Jl. cempaka blok M No.70 Perum Pondok Betung,Tangerang Selatan
            website https://bizantech.co.id, Telp (021) 782821
    ================================================================

                                    Rician Gaji
     |------------------------------------------------------------------|
     | Nama    | Gaji       | Pendapatan   | Potongan    | Total Gaji   |
     |------------------------------------------------------------------|
     |''', nm, ''' | Rp.''', gp, ''' | RP.''', tp, ''' | Rp.''', tpa, '''| RP.''', tolp, '''|        
     |------------------------------------------------------------------|

                                                                ''', bln, thn, '''



                                                                ''', nm, '''

''')
