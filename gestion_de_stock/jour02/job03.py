##########################################################################################################################################################################################################
########################################################################################### SQL et PYTHON ################################################################################################
##########################################################################################################################################################################################################

# Pour ajouter les données suivantes à la table “etage” :

INSERT INTO etage (nom, numero, superficie)
VALUES ('RDC', 0, 500),
       ('R+1', 1, 500);
       
# Affiche : Query OK, 2 rows affected (0,02 sec)
#           Records: 2  Duplicates: 0  Warnings: 0

mysql> SELECT * FROM etage;
+----+------+--------+------------+
| id | nom  | numero | superficie |
+----+------+--------+------------+
|  1 | RDC  |      0 |        500 |
|  2 | R+1  |      1 |        500 |
+----+------+--------+------------+
2 rows in set (0,00 sec)

# Pour ajouter les données suivantes à la table “salles” :

INSERT INTO salles (nom, id_etage, capacite)
VALUES
('Lounge', 1, 100),
('Studio Son', 1, 5),
('Broadcasting', 2, 50),
('Bocal Peda', 2, 4),
('Coworking', 2, 80),
('Studio Video', 2, 5);

# Affiche : Query OK, 6 rows affected (0,01 sec)
#           Records: 6  Duplicates: 0  Warnings: 0

mysql> SELECT * FROM salles;
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
6 rows in set (0,00 sec)

# Pour exporter ma base de donnée, je peux utiliser la commande suivante dans mon terminal MySQL :

mysqldump -u root -p -h localhost laPlateforme > /Users/brady/Desktop/export_entreprise.sql

# Copier bureau en tant que nom de chemin : /Users/brady/Desktop

# Affiche pour la table etage :

mysql> SHOW COLUMNS FROM etage;
+------------+--------------+------+-----+---------+----------------+
| Field      | Type         | Null | Key | Default | Extra          |
+------------+--------------+------+-----+---------+----------------+
| id         | int          | NO   | PRI | NULL    | auto_increment |
| nom        | varchar(255) | YES  |     | NULL    |                |
| numero     | int          | YES  |     | NULL    |                |
| superficie | int          | YES  |     | NULL    |                |
+------------+--------------+------+-----+---------+----------------+
4 rows in set (0,00 sec)

# Affiche pour la table salles :

mysql> SHOW COLUMNS FROM salles;
+----------+--------------+------+-----+---------+----------------+
| Field    | Type         | Null | Key | Default | Extra          |
+----------+--------------+------+-----+---------+----------------+
| id       | int          | NO   | PRI | NULL    | auto_increment |
| nom      | varchar(255) | YES  |     | NULL    |                |
| id_etage | int          | YES  |     | NULL    |                |
| capacite | int          | YES  |     | NULL    |                |
+----------+--------------+------+-----+---------+----------------+
4 rows in set (0,00 sec)