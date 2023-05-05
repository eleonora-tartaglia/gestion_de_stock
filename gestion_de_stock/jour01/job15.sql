------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------- BASE DE DONNEES MYSQL---------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

-- Pour trier les élèves par leurs noms et par ordre alphabétique, on peut utiliser la requête SQL suivante :

            SELECT * FROM etudiants ORDER BY nom ASC;

-- Affiche :

mysql> SELECT * FROM etudiants ORDER BY nom ASC;
+----+-----------+----------+-----+---------------------------------+-----------+
| id | nom       | prenom   | age | email                           | famille   |
+----+-----------+----------+-----+---------------------------------+-----------+
|  4 | Barnes    | Binkie   |  16 | binkie.barnes@laplateforme.io   | Barnes    |
|  3 | Doe       | John     |  18 | john.doe@laplateforme.io        | Doe       |
|  5 | Dupuis    | Gertrude |  20 | gertrude.dupuis@laplateforme.io | Dupuis    |
|  6 | Dupuis    | Martin   |  18 | martin.dupuis@laplateforme.io   | Dupuis    |
|  1 | Spaghetti | Betty    |  23 | betty.Spaghetti@laplateforme.io | Spaghetti |
|  2 | Steak     | Chuck    |  45 | chuck.steak@laplateforme.io     | Steak     |
+----+-----------+----------+-----+---------------------------------+-----------+
6 rows in set (0,00 sec)