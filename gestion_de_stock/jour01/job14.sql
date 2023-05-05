------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------- BASE DE DONNEES MYSQL---------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

-- Pour récupérer les élèves dont l’age est compris entre 18 et 25 ans et en les triant par ordre croissant, on peut utiliser la requête SQL suivante :

SELECT * FROM etudiants 
WHERE age BETWEEN 18 AND 25 
ORDER BY age ASC;

-- Affiche :

+----+-----------+----------+-----+---------------------------------+-----------+
| id | nom       | prenom   | age | email                           | famille   |
+----+-----------+----------+-----+---------------------------------+-----------+
|  3 | Doe       | John     |  18 | john.doe@laplateforme.io        | Doe       |
|  6 | Dupuis    | Martin   |  18 | martin.dupuis@laplateforme.io   | Dupuis    |
|  5 | Dupuis    | Gertrude |  20 | gertrude.dupuis@laplateforme.io | Dupuis    |
|  1 | Spaghetti | Betty    |  23 | betty.Spaghetti@laplateforme.io | Spaghetti |
+----+-----------+----------+-----+---------------------------------+-----------+
4 rows in set (0,01 sec)