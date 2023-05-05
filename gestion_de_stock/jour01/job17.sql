------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------- BASE DE DONNEES MYSQL---------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

-- Suite à une erreur de saisie, l’age de Betty Spaghetti n’est pas correct. 

-- Afin de modifier l’age de Betty de 23 ans a 20 ans, on peut utiliser la requête SQL suivante :

            UPDATE etudiants SET age = 20 WHERE nom = 'Spaghetti' AND prenom = 'Betty';

-- Affiche :

mysql> UPDATE etudiants SET age = 20 WHERE nom = 'Spaghetti' AND prenom = 'Betty';
Query OK, 1 row affected (0,01 sec)
Rows matched: 1  Changed: 1  Warnings: 0

-- Verification : Pour afficher le résultat pour l'étudiante nommé "Betty Spaghetti", on peut utiliser la requête SQL suivante :

            SELECT * FROM etudiants WHERE nom='Spaghetti' AND prenom='Betty';

-- Affiche :

mysql> SELECT * FROM etudiants WHERE nom='Spaghetti' AND prenom='Betty';
+----+-----------+--------+-----+---------------------------------+-----------+
| id | nom       | prenom | age | email                           | famille   |
+----+-----------+--------+-----+---------------------------------+-----------+
|  1 | Spaghetti | Betty  |  20 | betty.Spaghetti@laplateforme.io | Spaghetti |
+----+-----------+--------+-----+---------------------------------+-----------+
1 row in set (0,00 sec)