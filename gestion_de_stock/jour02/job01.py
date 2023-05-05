##########################################################################################################################################################################################################
########################################################################################### SQL et PYTHON ################################################################################################
##########################################################################################################################################################################################################

# Le module "mysql-connector-python" permet d'établir une connexion avec une base de données MySQL à partir d'un programme Python. 

# Pour l'utiliser, il faut d'abord l'installer en exécutant la commande suivante dans mon terminal ou invite de commandes :

#                                               pip install mysql-connector-python

# Pour se connecter à ma base de données MySQL depuis un programme Python, on peut utiliser le code suivant :

import mysql.connector

# Créer une connexion à la base de données
connexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="monarque",
    database="LaPlateforme"
)

# Créer un curseur pour exécuter les requêtes
curseur = connexion.cursor()

# Exécuter une requête SQL pour récupérer des données
requete = "SELECT * FROM etudiants"
curseur.execute(requete)
resultats = curseur.fetchall()

# Afficher les résultats
for resultat in resultats:
    print(resultat)

# Fermer le curseur et la connexion
curseur.close()
connexion.close()

# Affiche : 

(1, 'Spaghetti', 'Betty', 20, 'betty.Spaghetti@laplateforme.io', 'Spaghetti')
(2, 'Steak', 'Chuck', 45, 'chuck.steak@laplateforme.io', 'Steak')
(4, 'Barnes', 'Binkie', 16, 'binkie.barnes@laplateforme.io', 'Barnes')
(5, 'Dupuis', 'Gertrude', 20, 'gertrude.dupuis@laplateforme.io', 'Dupuis')
(6, 'Dupuis', 'Martin', 18, 'martin.dupuis@laplateforme.io', 'Dupuis')