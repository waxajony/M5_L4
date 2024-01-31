def kerakli_pul_soni(tangalar, S):
    gnom_tangalari = sum(tangalar)  # Gnomlarning umumiy tangalari miqdori
    kerakli_pul = max(0, S - gnom_tangalari)  # Sovg'a narxini to'lash uchun qancha pul kerakligini topamiz
    return kerakli_pul

with open('INPUT.txt', 'r') as file:
    tangalar = list(map(int, file.readline().split()))  
    S = int(file.readline())  
# Natijani topish
natija = kerakli_pul_soni(tangalar, S)

# OUTPUT.TXT fayliga natijani yozish
with open('OUTPUT.txt', 'w') as file:
    file.write(str(natija))
