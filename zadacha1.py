#1 - Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
#N = 20 -> [2,5]
#N = 30 -> [2, 3, 5]

def getListMult(numN):
    list = []
    listMult = [list.append(i) for i in range(1, numN+1) if numN % i == 0]
    return list

def primeNum(numN):
    primeList = []
    for i in range(2, numN):
        while numN % i == 0:
            numN /= i
            primeList.append(i)
    return primeList

numN = int(input("Введите натуральное число: "))
list1 = getListMult(numN)
list2 = primeNum(numN)
print(f'Простые множители числа {numN} :{list2}')

def primfacs(n):
   i = 2
   primfac = []
   while i * i <= n:
       while n % i == 0:
           primfac.append(i)
           n = n / i
       i = i + 1
   if n > 1:
       primfac.append(n)
   return primfac