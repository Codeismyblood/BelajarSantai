inputNumber = int(input("Masukkan Baris Bintang : "))
def printStarLine(inputNumber: int) -> None:
    for i in range(1,inputNumber+1):
        for j in range(i):
            print("*", end="")
        #bintangsetaradenganindex-0 di looping j dan setara dengan element 1 pada looping i(ini kondisi ketika iterasi di mulai)
        print()
printStarLine(inputNumber)
