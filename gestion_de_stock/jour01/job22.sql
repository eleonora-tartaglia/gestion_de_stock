------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------- BASE DE DONNEES MYSQL---------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

-- Pour récupérer les informations de l’étudiant le plus jeune, on peut utiliser la requête SQL suivante :

            SELECT * FROM etudiants WHERE age = (SELECT MIN(age) FROM etudiants);

-- Affiche :

mysql> SELECT * FROM etudiants WHERE age = (SELECT MIN(age) FROM etudiants);
+----+--------+--------+-----+-------------------------------+---------+
| id | nom    | prenom | age | email                         | famille |
+----+--------+--------+-----+-------------------------------+---------+
|  4 | Barnes | Binkie |  16 | binkie.barnes@laplateforme.io | Barnes  |
+----+--------+--------+-----+-------------------------------+---------+
1 row in set (0,00 sec)