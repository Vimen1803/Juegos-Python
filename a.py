varx = 0
while varx < 10:
    with open("ejer/log.txt", "a") as f:
            var1 = int(input("Ingresa un numero "))
            f.write(str(var1))
            if var1 % 2:
                f.write(" impar \n")
                varx = varx + 1
            else:
                f.write(" par \n")
                varx = varx + 1
        