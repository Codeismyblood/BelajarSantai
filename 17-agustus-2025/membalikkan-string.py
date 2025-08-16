# Cara Pertama
# inputKalimat = input("Masukkan kalimat : ")
# convertInputKalimat = inputKalimat[::-1]
# print("Hasil kalimat yang di balik :", convertInputKalimat)

# Cara Kedua
inputKalimat = 'Logic'
convertInputKalimat = list(inputKalimat)
print(type(convertInputKalimat))
print(convertInputKalimat)
for i in range(len(inputKalimat)-1, -1, -1):
    print(inputKalimat[i])
