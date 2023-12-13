import csv

import matplotlib.dates as mdates
from matplotlib import pyplot as plt


# fonction pour charger les fichiers.
def load_data(file_path, delim):
    with open(file_path, 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile, delimiter=delim)
        temp = [[cell.replace(" ", "").strip() for cell in row] for row in reader]
    del temp[0]
    del temp[-1]
    return temp


# charge les données CSV dans les variables.
donnees = load_data('RTE_2020.csv', ',')

choix = int(input("1: consommation / 2: énergies / 3: échanges / 4 taux de Co2: "))

titre = ""
label_nom = []
indexs = []

if choix == 1:
    titre = "Graphique de la consommation d'énergie en 2020."
    label_nom = ['Consommation', 'Prevision J-1', 'Prevision']
    indexs = [4, 5, 6]
elif choix == 2:
    titre = "Graphique de l'utilisation des énergies en 2020."
    label_nom = ['Fioul', 'Charbon', 'Gaz', 'Nucleaire', 'Eolien', 'Solaire', 'Hydraulique', 'Bioenergies']
    indexs = [7, 8, 9, 10, 11, 12, 13, 15]
elif choix == 3:
    titre = "Graphique des échanges des énergies en 2020."
    label_nom = ['Ech. physiques', 'Ech. comm. Angleterre', 'Ech. comm. Espagne', 'Ech. comm. Italie',
                 'Ech. comm. Suisse', 'Ech. comm. Allemagne-Belgique']
    indexs = [16, 18, 19, 20, 21, 22]
elif choix == 4:
    titre = "Graphique du taux de carbone en 2020."
    label_nom = ['Taux de Co2']
    indexs = [17]
else:
    raise ValueError("Cet index ne fait pas partie de la liste donnée.")


# fonction qui retourne True si la liste contiens un élément vide.
def has_empty(liste):
    return any(value == '' or value is None for value in liste)


y_dic = {}
cam_dic = {}
x = []
for data in donnees:
    if has_empty(data):
        continue

    x.append(mdates.datestr2num(data[2]))

    for i in indexs:
        y_dic.setdefault(i, []).append(int(data[i]))
        cam_dic[i] = cam_dic.get(i, 0) + int(data[i])

values = list(cam_dic.values())
total = sum(values)
pourcentages = [val / total for val in values]

# Configuration du graphique et affichage du line plot.
fig, ax = plt.subplots(figsize=(18, 10))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
ax.xaxis.set_major_locator(mdates.DayLocator(interval=30))
fig.autofmt_xdate()

for val in y_dic.values():
    ax.plot(x, val, linewidth=0.5)

ax.set_title(titre)
ax.set_xlabel('Mois')
ax.set_ylabel('Utilisation')
ax.legend(label_nom)

# Afficher le premier graphique
plt.show()

# Create a new figure for the pie chart
fig_pie, ax_pie = plt.subplots(figsize=(10, 8))

# Plot the pie chart
ax_pie.pie(pourcentages, labels=label_nom, autopct='%1.1f%%')
ax_pie.set_title("Part de production")
plt.legend(loc='upper right', bbox_to_anchor=(1.3, 1.15))
# Afficher le deuxieme graphique
plt.show()
