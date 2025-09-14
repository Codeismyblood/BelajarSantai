inputKata = input("Input : ")
splitString = list(inputKata)
#print(splitString)
firstWord=""
secondWord =""
container = []
container2 = []
for i in range(len(splitString)):
    print(splitString)
    data1 = splitString[i]
    print(f"{data1} : ini data1")
    firstWord = str(data1)
    print(f"{firstWord} : ini firstWord")
    container.append(data1)
    convertContainer = ''.join(container)
#print(convertContainer)
#print(type(convertContainer))
for j in range(len(splitString)-1,-1,-1):
    data2 = splitString[j]
    print(f"ini data 2 : {data2}")
    secondWord = str(data2)
    container2.append(data2)
    convertContainer2 = ''.join(container2)
#print(convertContainer2)
#print(type(convertContainer2))
if convertContainer == convertContainer2:
    print(f"{convertContainer}|{convertContainer2} : palindrome")
else:
    print(f"{convertContainer}|{convertContainer2} : Not Palindrome")