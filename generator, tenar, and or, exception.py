
import random as rd

lis = [rd.randint(1,100) for b in range(10)]

liskv = [rd.randint(1,100)**2  for b in range (10)]

b='jfor'
print(b.startswith('a'))
print('+' if '' else '-')   # приведение к типу bool
print([] or '' or 0)   # так работает оператор or

a=10
b=5
try:
    c=a+b
except:
    print('Nelzya')
else:
    print('mozhno'+f' {c}')
finally:
    print ('poschitaly')
    
    
raise ZeroDivisionError ('‘ahah’')  # вручную создали ошибку