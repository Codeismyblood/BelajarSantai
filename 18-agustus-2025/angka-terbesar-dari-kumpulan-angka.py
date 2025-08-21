#inputAngka1 = int(input("Input Angka - 1 : "))
#inputAngka2 = int(input("Input Angka - 2 : "))
#inputAngka3 = int(input("Input Angka - 3 : "))

#if inputAngka3 > inputAngka2 and inputAngka3 > inputAngka1:
#    print("Angka Terbesar Adalah : " , inputAngka3)
#    print("Kode ini yang di eksekusi")
#elif inputAngka2 > inputAngka1:
#    print("Angka Terbesar Adalah : " , inputAngka2)
#elif inputAngka1 > inputAngka2:
#    print("Angka Terbesar Adalah : " , inputAngka1)

input = [10,25,7,100,50]
max = 0
for i in input:
    #print(i)
    if i > max:
        max = i
print("Nilai terbesar : " , max)
