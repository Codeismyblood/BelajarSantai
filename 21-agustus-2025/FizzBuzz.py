inputAngka = int(input("Masukkan FizzBuzz : "))
print(inputAngka)
print(type(inputAngka))
for i in range(1,inputAngka+1):
    if i % 3 == 0 and i % 5 == 0:
        print(f"FizzBuzz : {i}")
    elif i % 3 == 0:
        print(f"Fizz : {i}")
    elif i % 5 == 0:
        print(f"Buzz : {i}")
    else:
        print(i)