##########################################################################################################################################################################################################
########################################################################################### SQL et PYTHON ################################################################################################
##########################################################################################################################################################################################################

# Affiche ma table salles :

'''mysql> SELECT * FROM salles;
+----+--------------+----------+----------+
| id | nom          | id_etage | capacite |
+----+--------------+----------+----------+
|  1 | Lounge       |        1 |      100 |
|  2 | Studio Son   |        1 |        5 |
|  3 | Broadcasting |        2 |       50 |
|  4 | Bocal Peda   |        2 |        4 |
|  5 | Coworking    |        2 |       80 |
|  6 | Studio Video |        2 |        5 |
+----+--------------+----------+----------+
6 rows in set (0,00 sec)'''

# Pour calculer la somme des capacités des salles, on utilise la fonction :

#            SELECT SUM(capacite) AS total_capacite_salles FROM salles;


# Affiche : 

'''mysql> SELECT SUM(capacite) AS total_capacite_salles FROM salles;
+-----------------------+
| total_capacite_salles |
+-----------------------+
|                   244 |
+-----------------------+
1 row in set (0,00 sec)'''

# Pour afficher dans le terminal :

import mysql.connector

# Connexion à la base de données
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="monarque",
  database="LaPlateforme"
)

# Création d'un curseur pour exécuter les requêtes SQL
mycursor = mydb.cursor()

# Exécution de la requête SQL
mycursor.execute("SELECT SUM(capacite) FROM salles")

# Récupération du résultat
resultat = mycursor.fetchone()[0]

# Affichage du résultat
print("La somme des capacités des salles est de", resultat)

# Affiche :

# La somme des capacités des salles est de 244