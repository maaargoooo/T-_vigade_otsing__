from random import *
def arvud_loendis():
    """Andmete sisestamine, funktsioonide kutsumine ja vastuste kuvamine
    """
    s=[]
    print("Данные:")
    n=abs(int(input("Сколько целых чисел генерируем в список? => ")))
    mini=int(input("Введите минимальное число диапазона => "))
    maxi=int(input("Введите максимальное число диапазона => "))
    if mini>=maxi: #mini=100, maxi=5 -> mini=5, maxi=100
        mini,maxi=vahetus(mini,maxi)
    s=generaator(n,s,mini,maxi)
    print()
    print("Результаты:")
    print("Полученный список от",mini,"до",maxi,s)
    s.sort()
    print("Отсортированный список",s)
    pos=[]
    neg=[]
    null=[]
    pos,neg,null=jagamine(s,pos,neg,null)
    print("Список положительных элементов",pos)
    print("Список отрицательных элементов",neg)
    print("Список нулевых элементов",null)
    kesk=keskmine(pos,n)
    lisamine(s,kesk)
    print("Среднее положительных:",kesk)
    kesk=keskmine(neg,n)
    lisamine(s,kesk)
    print("Среднее отрицательных:",kesk)
    print("Добавляем средние в изначальный массив:")
    print(s)

def vahetus(a:int,b:int)->int:
    """Kui min on maxi suurem, vahetame need ära
     : param int a: minimaalne arv on suurem kui max
     : param int b: maksimaalne arv väiksem kui min
     : rtype: int, int
    """
    abi=a
    a=b
    b=abi
    return a,b

def generaator(n:int,loend:list,a:int,b:int):
    """Juhuslike numbrite lisamine loendisse
     : param int n: genereeritud numbrite arv
     : param list loend: loend numbritega
     : param int a: min väärtus
     : param int b: max väärtus
     : rtype list:
    """
    for i in range (n):
        loend.append(randint(a,b))
    

def jagamine(loend:list,p:list,n:list,nol:list):
    """Lisage muutuja erinevatesse loenditesse, kui tingimused on täidetud
     : param list loend: loend numbritega
     : param list p: nullist suuremate numbritega loend
     : param list n: loend nullist väiksemate arvudega
     : param list nol: loend nullväärtustega
     : rtype list:
    """
    for el in loend:
         if el>0:
             p.append(el)
         elif el<0:
             n.append(el)
         else:
             nol.append(el)

def keskmine(loend,n):
    """Keskmise arvutamine loendist
     : param list loend: loend numbritega
     : rtype float:
    """
    n=len(loend)
    if n==0:
        kesk=0
    else:
        sum=0
        for i in loend:
            sum+=i
            kesk=round(sum/n,2)
    return kesk

def lisamine(loend,el):
    """Lisa loendisse keskmine ja sorteeri
     : param list loend: loend numbritega
     : param float el: keskmised
     : rtype list:
    """
    loend.append(el)
    loend.sort()
    return loend


