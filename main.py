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

choix = int(input("1: consommation / 2: énergies / 3: échanges / 4 taux de Co2:"))

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


def interpolate(value, base):
    value = max(0, min(value, base))
    factor = value / base
    return factor


def get_x_from_date(date):
    year, month, day = map(int, date.split('-'))
    maxd = 30
    if month in {1, 3, 5, 7, 8, 10, 12}:
        maxd = 31
    return year + (interpolate(month, 12)) + (interpolate(day, maxd) * 0.1)

# fonction qui retourne True si la liste contiens un élément vide.
def has_empty(liste):
    return any(value == '' or value is None for value in liste)


y_dic = {}
x = []
y = []
p = 0
for data in donnees:
    if has_empty(data):
        continue
    x.append(mdates.datestr2num(data[2]))
    for i in indexs:
        if i not in y_dic:
            y_dic[i] = [(int(data[i]))]
        else:
            y_dic.get(i).append(int(data[i]))

# configuration du graphique et affichage.
plt.figure(figsize=(18, 10))
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=30))
plt.gcf().autofmt_xdate()
for val in y_dic.values():
    plt.plot(x, val, linewidth=0.5)
plt.title(titre)
plt.xlabel('Mois')
plt.ylabel('Utilisation')
plt.legend(label_nom)
frame = plt.gca()
plt.show()
