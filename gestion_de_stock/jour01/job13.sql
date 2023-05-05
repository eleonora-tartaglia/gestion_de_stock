------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------- BASE DE DONNEES MYSQL---------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

-- Pour récupérer les élèves dont l’age est compris entre 18 et 25 ans, on peut utiliser la requête SQL suivante :

            SELECT * FROM etudiants WHERE age BETWEEN 18 AND 25;

-- Affiche :

mysql> SELECT * FROM etudiants WHERE age BETWEEN 18 AND 25;
+----+-----------+----------+-----+---------------------------------+-----------+
| id | nom       | prenom   | age | email                           | famille   |
+----+-----------+----------+-----+---------------------------------+-----------+
|  1 | Spaghetti | Betty    |  23 | betty.Spaghetti@laplateforme.io | Spaghetti |
|  3 | Doe       | John     |  18 | john.doe@laplateforme.io        | Doe       |
|  5 | Dupuis    | Gertrude |  20 | gertrude.dupuis@laplateforme.io | Dupuis    |
|  6 | Dupuis    | Martin   |  18 | martin.dupuis@laplateforme.io   | Dupuis    |
+----+-----------+----------+-----+---------------------------------+-----------+
4 rows in set (0,00 sec)

-- En plus .... pour voir le plus petit et le plus grand âge dans la table : 

            SELECT MIN(age), MAX(age) FROM etudiants;

-- Affiche :

mysql> SELECT MIN(age), MAX(age) FROM etudiants;
+----------+----------+
| MIN(age) | MAX(age) |
+----------+----------+
|       16 |       45 |
+----------+----------+
1 row in set (0,00 sec)