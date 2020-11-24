#Se citeste un sir de caractere care reprezinta un CNP
#sa se verifice corectitudinea lui: numarul de caractere sa fie =13
#si toate caracterele sa fie cifre
import sys
a=str(input('Dati CNPul = '))
t=True
if (len(a)==13):
    for i in a:
        if ((ord(i)<=57) and (ord(i)>=48)):
            t=True
        else:
            t=False
else:
    print('Eroare')    
    sys.exit()   
if t==True:
    print('CNPul este corect')  
else:
    print('CNPul nu este corect')   