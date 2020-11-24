#de la tastatura se citesc
#patru cuvinte fiecare cuvant fiind citit
#intro singura variabila,un cuvant va fi format din minim 3 caractere
#elaborati un program care va forma un cuvant nou in felul urmator:
#din primul cuvant va adauga primele 2 caractere
#din al doilea cuvant va adauga primul caracter
#se vor adauga primele trei caractere din cuvantul al treilea
#se vor adauga len(al patrulea cuvant)/2 caractere
#la ecran se vor afisa cuvintele citite cat si cel format
a=str(input('Dati primul cuvant = '))
b=str(input('Dati al doilea cuvant = '))
c=str(input('Dati al treilea cuvant = '))
d=str(input('Dati al patrulea cuvant = '))
a1=a[:2]
b1=b[:1]
c1=c[:3]
len1=((len(d))//2)
len2=len1
d1=d[:len2]
if ((len(a)<3) or (len(b)<3) or (len(c)<3) or (len(d)<3)):
    print('Eroare')
else:
    print('Primul cuvant este = ',a)
    print('Al doilea cuvant este = ',b)
    print('Al treilea cuvant este = ',c)
    print('Al patrulea cuvant este = ',d)
    cuvant=a1+b1+c1+d1
    print('Cuvantul format este = ',cuvant)
