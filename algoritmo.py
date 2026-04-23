myArray = (1, 3, 2, 0, 7, 8, 1, 3, 0, 6, 7, 0)

lista_temporal = []

for n in myArray:
    if n != 0:
        lista_temporal.append(n)
    else:
        lista_temporal.sort()
        
        for num in lista_temporal:
            print(num, end="")
        
        print(" ", end="")
        lista_temporal = []