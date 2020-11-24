#De la tastatura se citeste un sir de caractere.
#elaborati un brogram care va determina a)nr de majuscule din sir
#b)numarul de cifre din sir
#c)numarul de caractere specifice din sir
st=str(input('Dati sirul de caractere= '))
import string
sm=0
smic=0
sp=0
special_chars=string.punctuation

for i in st:
    if i in string.ascii_uppercase:
        sm=sm+1
    elif ((ord(i)<=57) and (ord(i)>=48)):
        smic=smic+1
    if i in special_chars:
        sp=sp+1
print('Numarul de litere mari este = ',sm)
print('Numarul de cifre este = ',smic)
print('Numarul de caractere speciale este = ',sp)

