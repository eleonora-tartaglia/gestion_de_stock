------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------- BASE DE DONNEES MYSQL---------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

-- Pour trier les ages des étudiants par ordre croissant, on peut utiliser la requête SQL suivante :

            SELECT * FROM etudiants ORDER BY age ASC;

-- Affiche :

mysql> SELECT * FROM etudiants ORDER BY age ASC;
+----+----------+-----------+-----+---------------------------------+
| id | nom      | prenom    | age | email                           |
+----+----------+-----------+-----+---------------------------------+
|  4 | Binkie   | Barnes    |  16 | binkie.barnes@laplateforme.io   |
|  3 | John     | Doe       |  18 | john.doe@laplateforme.io        |
|  5 | Gertrude | Dupuis    |  20 | gertrude.dupuis@laplateforme.io |
|  1 | Betty    | Spaghetti |  23 | betty.Spaghetti@laplateforme.io |
|  2 | Chuck    | Steak     |  45 | chuck.steak@laplateforme.io     |
+----+----------+-----------+-----+---------------------------------+
5 rows in set (0,00 sec)