------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------- BASE DE DONNEES MYSQL---------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

-- Pour compter le nombre d’étudiants présent en base de données, on peut utiliser la requête SQL suivante :

            SELECT COUNT(*) FROM etudiants;

-- Affiche :

mysql> SELECT COUNT(*) FROM etudiants;
+----------+
| COUNT(*) |
+----------+
|        5 |
+----------+
1 row in set (0,00 sec)