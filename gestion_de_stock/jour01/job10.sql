------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------- BASE DE DONNEES MYSQL---------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

-- Pour trier les ages des étudiants par ordre decroissant, on peut utiliser la requête SQL suivante :

            SELECT * FROM etudiants ORDER BY age DESC;

-- Affiche :

mysql> SELECT * FROM etudiants ORDER BY age DESC;
+----+----------+-----------+-----+---------------------------------+
| id | nom      | prenom    | age | email                           |
+----+----------+-----------+-----+---------------------------------+
|  2 | Chuck    | Steak     |  45 | chuck.steak@laplateforme.io     |
|  1 | Betty    | Spaghetti |  23 | betty.Spaghetti@laplateforme.io |
|  5 | Gertrude | Dupuis    |  20 | gertrude.dupuis@laplateforme.io |
|  3 | John     | Doe       |  18 | john.doe@laplateforme.io        |
|  4 | Binkie   | Barnes    |  16 | binkie.barnes@laplateforme.io   |
+----+----------+-----------+-----+---------------------------------+
5 rows in set (0,00 sec)