------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------- BASE DE DONNEES MYSQL---------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

-- Pour compter le nombre d’étudiants mineurs présent en base de données, on peut utiliser la requête SQL suivante :

            SELECT COUNT(*) FROM etudiants WHERE age < 18;

-- Affiche :

mysql> SELECT COUNT(*) FROM etudiants WHERE age < 18;
+----------+
| COUNT(*) |
+----------+
|        1 |
+----------+
1 row in set (0,00 sec)