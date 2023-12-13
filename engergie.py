import csv
from matplotlib import pyplot as plt


#Ouverture du fichier RTE_2020.csv
RTE_2020=[]
with open('RTE_2020.csv',newline='') as csvfile: 
    reader=csv.reader(csvfile,delimiter=',')
    for row in reader:
        RTE_2020.append(row)


#La première et la dernière sont inutiles
del RTE_2020[0]
del RTE_2020[-1]

#Création de "Liste_consommation_total" qui fait la production total de chacune des énergies
Liste_consommation_total=[0,0,0,0,0,0,0,0,0]
booll=True
for i in range (7,16,1) :
    for element in RTE_2020 :
        if booll==True :
            Liste_consommation_total[-7+i] =  int(Liste_consommation_total[-7+i])+ int(element[i])
        booll = not booll

#La colonne "pompage" comsommde de l'énergie donc on l'enlève car on ne veut pas
del Liste_consommation_total[7]

#On crée "total" qui fait le total de la production. Il sera utilise pour faire les pourcentages servant dans un camambert
total = 0
for element in Liste_consommation_total :
    total = total + element
total = total #Pruduction total
total_pourcent= total/100 #Pruduction total modifié servant pour transformer chaque colonne dans "Liste_consommation_total" en pourcentage

#Transformation "Liste_consommation_total" en pourcentage pour chaque colonne
Liste_consommation_total_pourcentage = [0,0,0,0,0,0,0,0]
for i in range(len(Liste_consommation_total)):
    Liste_consommation_total_pourcentage[i] = Liste_consommation_total[i]/total_pourcent
    

#print(Liste_consommation_total)
#print(total)
#print(total_10)
#print(Liste_consommation_total_pourcentage)



#--------------------------------------------------------------------------------
#Graphe camambert pour la production total
labels = "Fioul","Charbon","Gaz","Nucleaire","Eolien","Solaire","Hydraulique","Bioenergies"
fig, ax = plt.subplots()
ax.pie(Liste_consommation_total_pourcentage, labels=labels,autopct='%1.1f%%')
plt.title("Part de production")
texte_2 = "Prudction total " + str(total)  + " MW"
#plt.legend(Liste_consommation_total)
plt.figtext(.8, .8, texte_2)
#plt.show()
#--------------------------------------------------------------------------------
#creation d'une liste des total de vente d'energie à chaque pays voisins
Liste_vente_total=[0,0,0,0,0]
for i in range (18,23,1) :
    for element in RTE_2020 :
        if booll==True :
            if int(element[i]) < 0 :
                Liste_vente_total[-18+i] =  int(Liste_vente_total[-18+i])+ int(element[i])
        booll = not booll

#creation d'une liste des total de achat d'energie à chaque pays voisins 
Liste_achat_total=[0,0,0,0,0]
for i in range (18,23,1) :
    for element in RTE_2020 :
        if booll==True :
            if int(element[i]) > 0 :
                Liste_achat_total[-18+i] =  int(Liste_achat_total[-18+i])+ int(element[i])
        booll = not booll

#vente total d'energie
total_ech = 0
for element in Liste_vente_total :
    total_ech = total_ech + element
total_ech = total_ech/100

#achat total d'energie
total_ech_achat = 0
for element in Liste_achat_total :
    total_ech_achat = total_ech_achat + element
total_ech_achat = total_ech_achat/100

#Liste des total de vente d'energie en pourcentage
Liste_ech_pourcentage = [0,0,0,0,0]
for i in range(len(Liste_vente_total)):
    Liste_ech_pourcentage[i] = Liste_vente_total[i]/total_ech

#Liste des total de achat d'energie en pourcentage
Liste_ech_pourcentage_achat = [0,0,0,0,0]
for i in range(len(Liste_achat_total)):
    Liste_ech_pourcentage_achat[i] = Liste_achat_total[i]/total_ech_achat


#print(Liste_vente_total)
#print(Liste_achat_total)
#print(Liste_ech_pourcentage)
#print(Liste_ech_pourcentage_achat)
#print(total_ech)
#print(total_ech_achat)

#camambert de la part vente d'energie par pays voisin
labels_pays = "Angletter","Espagne","Italie","Suisse","allemagne_belge"
fig, ax = plt.subplots()
ax.pie(Liste_ech_pourcentage, labels=labels_pays,autopct='%1.1f%%')
plt.title("Part de vente par pays")
texte_2 = "Vente total " + str(total_ech)  + " MW"
plt.figtext(.8, .8, texte_2)
#plt.legend(Liste_vente_total)
#plt.show()

#camambert de la part d'achat d'energie par pays voisin
labels_pays = "Angletter","Espagne","Italie","Suisse","allemagne_belge"
fig, ax = plt.subplots()
ax.pie(Liste_ech_pourcentage_achat, labels=labels_pays,autopct='%1.1f%%')
plt.title("Part d'achat par pays") 
texte_3 = "Achat total " + str(total_ech_achat)  + " MW"
plt.figtext(.8, .8, texte_3)
#plt.legend(Liste_achat_total)
plt.show()