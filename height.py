
from numpy import zeros

sum=zeros((12,2))
with open ('dataset_3380_5.txt', 'r') as f1:
    for stri in f1:
        stri=stri.split()
        sum[int(stri[0])-1,[1]]+=int(stri[2])
        sum[int(stri[0])-1,[0]]+=1

for l in range(12):
    if sum[[l],[0]]==0:
        print (str(l+1)+': -')
    else:
        print(str(l+1)+str(sum[[l],[1]]/sum[[l],[0]]))



"""
from numpy import zeros

sum=zeros((12,2))
with open ('dataset_3380_5.txt', 'r') as f1:
    for stri in f1:
        stri=stri.split()
        sum[int(stri[0])-1,[1]]+=int(stri[2])
        sum[int(stri[0])-1,[0]]+=1

for l in range(12):
    if sum[[l],[0]]==0:
        print (str(l+1)+': -')
    else:
        print(str(l+1)+str(sum[[l],[1]]/sum[[l],[0]]))


# со словарем

rost={}
sum=[[]]
with open ('dataset_3380_5.txt', 'r') as f1:
    for stri in f1:
        stri=stri.split()
        if stri[0] not in rost:
            rost[stri[0]]=[int(stri[2])]
        else:
            rost[stri[0]]+=[int(stri[2])]

av_rost={}

for k in rost:
    sum=0
    for top in range(len(rost[k])):
        sum+=int(rost[k][top])
    av_rost[k]=sum/len(rost[k])
    
p=['1','2','3','4','5','6','7','8','9','10','11']

for l in p:
    if l not in av_rost.keys():
        print (p, end='')
        print (': -')
    else:
        print(l, end = ' ')
        print(av_rost[l])
"""
