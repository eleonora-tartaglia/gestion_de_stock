------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------- BASE DE DONNEES MYSQL---------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

-- John Doe ne fait plus partie des étudiants, supprimer le de la base de données. Pour cela, on peut utiliser la requête SQL suivante :

            DELETE FROM etudiants WHERE nom='Doe' AND prenom='John';

-- Affiche :

mysql> DELETE FROM etudiants WHERE nom='Doe' AND prenom='John';
Query OK, 1 row affected (0,01 sec)

-- Verification :

mysql> SELECT * FROM etudiants ORDER BY id;
+----+-----------+----------+-----+---------------------------------+-----------+
| id | nom       | prenom   | age | email                           | famille   |
+----+-----------+----------+-----+---------------------------------+-----------+
|  1 | Spaghetti | Betty    |  20 | betty.Spaghetti@laplateforme.io | Spaghetti |
|  2 | Steak     | Chuck    |  45 | chuck.steak@laplateforme.io     | Steak     |
|  4 | Barnes    | Binkie   |  16 | binkie.barnes@laplateforme.io   | Barnes    |
|  5 | Dupuis    | Gertrude |  20 | gertrude.dupuis@laplateforme.io | Dupuis    |
|  6 | Dupuis    | Martin   |  18 | martin.dupuis@laplateforme.io   | Dupuis    |
+----+-----------+----------+-----+---------------------------------+-----------+
5 rows in set (0,00 sec)