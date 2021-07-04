
n=int(input())
tabla={}


for i in range (n):
    tur=input().split(';')
    if tur[0] not in tabla:
        tabla[tur[0]]=[1,0,0,0,0]
    else:
        tabla[tur[0]][0]+=1
    if tur[2] not in tabla:
        tabla[tur[2]]=[1,0,0,0,0]
    else:
        tabla[tur[2]][0]+=1
    if int(tur[1]) > int(tur[3]):
        tabla[tur[0]][1]+=1
        tabla[tur[0]][4]+=3
        tabla[tur[2]][3]+=1
    elif int(tur[1]) == int(tur[3]):
        tabla[tur[0]][2]+=1
        tabla[tur[0]][4]+=1
        tabla[tur[2]][2]+=1
        tabla[tur[2]][4]+=1
    else:
        tabla[tur[2]][1]+=1
        tabla[tur[2]][4]+=3
        tabla[tur[0]][3]+=1
for elem in tabla:
    print(elem+':', end='')
    for k in range (5):
        print(tabla[elem][k], end=' ')
    print('')
        