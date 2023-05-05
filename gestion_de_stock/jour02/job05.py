##########################################################################################################################################################################################################
########################################################################################### SQL et PYTHON ################################################################################################
##########################################################################################################################################################################################################

# Affiche ma table etage :
'''
mysql> SELECT * FROM etage;
+----+------+--------+------------+
| id | nom  | numero | superficie |
+----+------+--------+------------+
|  1 | RDC  |      0 |        500 |
|  2 | R+1  |      1 |        500 |
+----+------+--------+------------+
2 rows in set (0,00 sec)'''

# Pour calculer la superficie de l’ensemble des étages et afficher “La superficie de La Plateforme est de X m2”, X étant le résultat de la requête :

#            SELECT SUM(superficie) as total_superficie FROM etage;

# Affiche : 

'''mysql> SELECT SUM(superficie) as total_superficie FROM etage;
+------------------+
| total_superficie |
+------------------+
|             1000 |
+------------------+
1 row in set (0,00 sec)'''

# Pour afficher dans le terminal : 

import mysql.connector

# Se connecter à la base de données
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="monarque",
  database="LaPlateforme"
)

# Exécuter la requête
mycursor = mydb.cursor()
mycursor.execute("SELECT SUM(superficie) as total_superficie FROM etage")

# Récupérer le résultat et l'afficher
result = mycursor.fetchone()[0]
print(f"La superficie de La Plateforme est de {result} m2")

# Fermer la connexion
mycursor.close()
mydb.close()

# Affiche :

# La superficie de La Plateforme est de 1000 m2