##########################################################################################################################################################################################################
########################################################################################### SQL et PYTHON ################################################################################################
##########################################################################################################################################################################################################

# Pour ecrire un programme qui récupère tous les noms et les capacités de la table “salles” et afficher le résultat en console :

import mysql.connector

# Connection à la base de données

cnx = mysql.connector.connect(user='root', password='monarque',
                              host='localhost',
                              database='LaPlateforme')
cursor = cnx.cursor()

# Exécutez la requête pour récupérer les noms et les capacités de la table "salles"

query = ("SELECT nom, capacite FROM salles")
cursor.execute(query)

# Parcourez les résultats et affichez-les en console

for (nom, capacite) in cursor:
    print("Nom de la salle : {}, Capacité : {}".format(nom, capacite))

# Fermez la connexion et le curseur

cursor.close()
cnx.close()

# Affiche : 

Nom de la salle : Lounge, Capacité : 100
Nom de la salle : Studio Son, Capacité : 5
Nom de la salle : Broadcasting, Capacité : 50
Nom de la salle : Bocal Peda, Capacité : 4
Nom de la salle : Coworking, Capacité : 80
Nom de la salle : Studio Video, Capacité : 5