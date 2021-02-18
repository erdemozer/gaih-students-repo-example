import random

print ("1-100 arası rastgele asal sayılardan oluşan 3x3 bir matris ")
sayi1, sayi2 = 1, 100
primeList = []
matris = [[0 for x in range(3)] for y in range(3)]

#asal sayılardan oluşan dizi
for sayi in range(sayi1,sayi2 + 1):
   if sayi > 1:
       for i in range(2,sayi):
           if (sayi % i) == 0:
               break
       else:
        primeList.append(sayi)

#asal sayılardan oluşan dizi içinden 3x3 matris oluşturma
for j in range(3):
    for k in range (3):
        matris[j][k] = random.choice(primeList)

print(matris)

"""
for m in range(3):
    print(matris[m])
"""
