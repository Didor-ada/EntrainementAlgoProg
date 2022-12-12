import random

# for i in range(10):
#     print(random.randint(0,5))

# for i in range(10):
#     print(random.randint(1,6))


#### TD 3 : Booléens et conditionnelles
# 1) Pour commencer
def valeurAbsolue(x):
    if x < 0:
        return -x
    else:
        return x
print(valeurAbsolue(-123))

def estEntre0et2Pi(x):
    if x <= 6.18 and x > 0:
        return "oui"
    else:
        return None
print(estEntre0et2Pi(6.18)) 

def lePlusGrandDesDeux(x,y):
    if x > y:
        return x
    if y > x:
        return y
print(lePlusGrandDesDeux(18,5))

def lePlusGrandDesTrois(x,y,z):
    if x > y and x > z:
        return x
    if y > x and y > z:
        return y
    if z > x and z > y:
        return z
print(lePlusGrandDesTrois(4,15,19))
print("################SUITE###################")
# 2) Facture de vin

def facture1(v, pu):
    facture = pu * v
    majoration = facture * 1.10
    return majoration
print(facture1(6,10))

def facture2(v, pu):
    facture = pu * v
    majoration = facture * 1.10
    if facture < 100:
        return majoration
    else:
        return facture
print(facture2(6,10))
print(facture2(12,10))

def facture3(v, pu):
    facture = pu * v
    majoration = facture * 1.10
    if facture // 10 <= 2:
        return facture + 2
    else:
        return majoration
print(facture3(1,21))
print("################SUITE###################")
# 3) Divisibilité
def estPair(n):
    if n % 2 == 0:
        return True
    else:
        return False
print(estPair(16))

def estBissextile(annee):
    if annee // 400:
        return True
    if annee // 4 and (annee % 100 !=0):
        return True
    if annee == 2020 and annee == 2000:
        return True
    if annee == 2019 and annee == 1900:
        return False

def nbJoursDansMois(mois, annee):
    janvier = 1
    fevrier = 2
    mars = 3
    avril = 4
    mai = 5
    juin = 6
    juillet = 7
    aout = 8
    septembre = 9
    octobre = 10
    novembre = 11
    decembre = 12
    moisTrenteUn = [janvier, mars, mai, juillet, aout, octobre, decembre]
    moisTrente = [avril, juin, septembre, novembre]
    moisTrenteUn = 31
    moisTrente = 30
    fevrierNonBissextile = 28
    fevrierBissextile = 29
    if mois == moisTrente:
        return "Ce mois possède 31 jours à l'année : " + annee
    elif mois == moisTrenteUn:
        return "Ce mois possède 30 jours à l'année :" + annee
    if estBissextile(annee) == True:
        return fevrierBissextile
    else:
        return fevrierNonBissextile
print("################SUITE###################")
# 4) Tirage au sort
seuil = 0.10
if random.random() < seuil:
    print("pile")
else:
    print("face")

ligne = ""
chance = 0.80
for i in range(40):
    if random.random() < chance:
        ligne = ligne + "*"
    else:
        ligne = ligne + "O"
    print(ligne)
print("################SUITE###################")
# 5) Les boucles while
# for i in range(9):
#     print(2*i)

i=0
while i <= 9:
    print(i*2)
    i+=1

def deuxSommePaire():
    nombre1 = random.randint(1,6)
    nombre2 = random.randint(1,6)
    if (nombre1 + nombre2) % 2 == 0:
        return nombre1, nombre2
    else:
        return "Le résultat de l'addition de " + str(nombre1) + " et de " + str(nombre2) + " n'est pas pair!"
print(deuxSommePaire()) 
print("################SUITE###################")
# 6) Pour aller plus loin : Les nombres premiers
def estPremier(n):
    for i in range(2, n):
        if (n%i) == 0:
            return False
    return True
print(estPremier(15))

def nombresPremiers(n):
    if estPremier(n) == True:
        for i in range(2, n):
            if i<n:
                print(i)
    else:
        return False

print(nombresPremiers(15))
print("################SUITE###################")
print("################SUITE###################")
#### TD4 : Tuples et Listes
# 1) Les n-uplets(tuples)
def intensite(c):
    intens = (c[0] + c[1] + c[2]) / 3
    return intens
print(intensite((255,0,0)))

def sombre(c):
    division = (c[0]/2, c[1]/2, c[2]/2)
    return division
print(sombre((120, 258,75)))

def somme(c1, c2):
    sommeC1C2 = ((c1[0]+c2[0]), (c1[1]+c2[1]), (c2[2]+c2[2]))
    return sommeC1C2
print(somme((150,135,100),(200, 230, 15)))

# 2) Listes : lecture simple et modification en place
lst = [2, 5, 6, 3, 10, 15]
lst2 = []
for i in range(len(lst)):
    lst2.append(lst[i]*2)
print(lst2)

def doubler(liste):
    lst = []
    for i in range(len(liste)):
        lst.append(liste[i]*2)
    return lst
print(doubler([2,4,6,8,10,12,15]))

def strToIntLst(lstToInt):
    for i in range(len(lstToInt)):
        lstToInt[int(i)]
    return lstToInt
print(strToIntLst(["12", "1", "5", "22"]))