chuslo = int(input("Enter 5-digit number: "))
perwe = chuslo // 10000
druge = chuslo // 1000 % 10
tretie = chuslo // 100 % 10
chetverte = chuslo // 10 % 10
piate = chuslo % 10
resultat = str(piate) + str(chetverte) + str(tretie) + str(druge) + str(perwe)
print (resultat)