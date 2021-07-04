n=int(input())
nach=n
a=0
prob=[[0 for j in range(n)] for i in range(n)]
numb=1
while n>0:
    for i in range(n):
        prob[a][i+a]=numb
        numb+=1
    n-=1
    for i in range(n):
        prob[i+1+a][nach-1-a]=numb
        numb+=1
    for i in range(n):
        prob[nach-1-a][n-i-1+a]=numb
        numb+=1
    n-=1     
    for i in range(n):
        prob[n-i+a][a]=numb
        numb+=1
    a+=1
for i in range(nach):
    for j in range (nach):
        if prob[i][j]//10<1:
            print (prob[i][j], end='  ')
        else:
            print (prob[i][j], end=' ')
    print('') 