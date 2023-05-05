------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------- BASE DE DONNEES MYSQL---------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

-- Oups je viens de me rendre compte que je me suis trompée j'ai inversé prenom et nom pour chaque étudiant, no panic, pour modifier des enregistrements, on peut utiliser la requête SQL suivante :

UPDATE etudiants SET nom='Spaghetti', prenom='Betty' WHERE nom='Betty' AND prenom='Spaghetti';
UPDATE etudiants SET nom='Steak', prenom='Chuck' WHERE nom='Chuck' AND prenom='Steak';
UPDATE etudiants SET nom='Doe', prenom='John' WHERE nom='John' AND prenom='Doe';
UPDATE etudiants SET nom='Barnes', prenom='Binkie' WHERE nom='Binkie' AND prenom='Barnes';
UPDATE etudiants SET nom='Dupuis', prenom='Gertrude' WHERE nom='Gertrude' AND prenom='Dupuis';

-- J'effectue une verification suite à mes grosses bêtises, juste pour voir dans l'ordre d'id, on peut utiliser la requête SQL suivante :

mysql> SELECT * FROM etudiants ORDER BY id;
+----+-----------+----------+-----+---------------------------------+
| id | nom       | prenom   | age | email                           |
+----+-----------+----------+-----+---------------------------------+
|  1 | Spaghetti | Betty    |  23 | betty.Spaghetti@laplateforme.io |
|  2 | Steak     | Chuck    |  45 | chuck.steak@laplateforme.io     |
|  3 | Doe       | John     |  18 | john.doe@laplateforme.io        |
|  4 | Barnes    | Binkie   |  16 | binkie.barnes@laplateforme.io   |
|  5 | Dupuis    | Gertrude |  20 | gertrude.dupuis@laplateforme.io |
+----+-----------+----------+-----+---------------------------------+
5 rows in set (0,00 sec)

-- Ouf, bêtises réparées :)

-- Pour ajouter à a table “etudiants” un élève nommé Martin Dupuis, âgé de 18 ans avec une adresse mail martin.dupuis@laplateforme.io, on peut utiliser la requête SQL suivante :

INSERT INTO etudiants (nom, prenom, age, email) VALUES ('Dupuis', 'Martin', 18, 'martin.dupuis@laplateforme.io');

-- Verification :

mysql> SELECT * FROM etudiants ORDER BY id;
+----+-----------+----------+-----+---------------------------------+
| id | nom       | prenom   | age | email                           |
+----+-----------+----------+-----+---------------------------------+
|  1 | Spaghetti | Betty    |  23 | betty.Spaghetti@laplateforme.io |
|  2 | Steak     | Chuck    |  45 | chuck.steak@laplateforme.io     |
|  3 | Doe       | John     |  18 | john.doe@laplateforme.io        |
|  4 | Barnes    | Binkie   |  16 | binkie.barnes@laplateforme.io   |
|  5 | Dupuis    | Gertrude |  20 | gertrude.dupuis@laplateforme.io |
|  6 | Dupuis    | Martin   |  18 | martin.dupuis@laplateforme.io   |
+----+-----------+----------+-----+---------------------------------+
6 rows in set (0,00 sec)


-- Vu que notre table "etudiants" ne contient pas d'informations sur la famille, il n'est pas possible de récupérer les membres d'une même famille avec une simple requête SQL sur cette table.
-- Pour cela on va devoir tout d'abord ajouter une colonne "famille" à ma table "etudiants" et y saisir les informations sur la famille de chaque étudiant :

ALTER TABLE etudiants ADD COLUMN famille VARCHAR(255);
UPDATE etudiants SET famille = 'Dupuis' WHERE nom = 'Dupuis';
UPDATE etudiants SET famille = 'Barnes' WHERE nom = 'Barnes';
UPDATE etudiants SET famille = 'Steak' WHERE nom = 'Steak';
UPDATE etudiants SET famille = 'Spaghetti' WHERE nom = 'Spaghetti';
UPDATE etudiants SET famille = 'Doe' WHERE nom = 'Doe';

-- Affiche : 

mysql> ALTER TABLE etudiants ADD COLUMN famille VARCHAR(255);
Query OK, 0 rows affected (0,04 sec)
Records: 0  Duplicates: 0  Warnings: 0

mysql> UPDATE etudiants SET famille = 'Dupuis' WHERE nom = 'Dupuis';
Query OK, 2 rows affected (0,00 sec)
Rows matched: 2  Changed: 2  Warnings: 0

mysql> UPDATE etudiants SET famille = 'Barnes' WHERE nom = 'Barnes';
Query OK, 1 row affected (0,00 sec)
Rows matched: 1  Changed: 1  Warnings: 0

mysql> UPDATE etudiants SET famille = 'Steak' WHERE nom = 'Steak';
Query OK, 1 row affected (0,00 sec)
Rows matched: 1  Changed: 1  Warnings: 0

mysql> UPDATE etudiants SET famille = 'Spaghetti' WHERE nom = 'Spaghetti';
Query OK, 1 row affected (0,00 sec)
Rows matched: 1  Changed: 1  Warnings: 0

mysql> UPDATE etudiants SET famille = 'Doe' WHERE nom = 'Doe';
Query OK, 1 row affected (0,01 sec)
Rows matched: 1  Changed: 1  Warnings: 0

-- Verification visuelle :

mysql> SELECT * FROM etudiants ORDER BY id;
+----+-----------+----------+-----+---------------------------------+-----------+
| id | nom       | prenom   | age | email                           | famille   |
+----+-----------+----------+-----+---------------------------------+-----------+
|  1 | Spaghetti | Betty    |  23 | betty.Spaghetti@laplateforme.io | Spaghetti |
|  2 | Steak     | Chuck    |  45 | chuck.steak@laplateforme.io     | Steak     |
|  3 | Doe       | John     |  18 | john.doe@laplateforme.io        | Doe       |
|  4 | Barnes    | Binkie   |  16 | binkie.barnes@laplateforme.io   | Barnes    |
|  5 | Dupuis    | Gertrude |  20 | gertrude.dupuis@laplateforme.io | Dupuis    |
|  6 | Dupuis    | Martin   |  18 | martin.dupuis@laplateforme.io   | Dupuis    |
+----+-----------+----------+-----+---------------------------------+-----------+
6 rows in set (0,00 sec)

-- Pour récupérer les infos des membres d’une même famille (ex pour la famille Dupuis) :

            SELECT * FROM etudiants WHERE famille='Dupuis';

-- Affiche : 

mysql> SELECT * FROM etudiants WHERE famille='Dupuis';
+----+--------+----------+-----+---------------------------------+---------+
| id | nom    | prenom   | age | email                           | famille |
+----+--------+----------+-----+---------------------------------+---------+
|  5 | Dupuis | Gertrude |  20 | gertrude.dupuis@laplateforme.io | Dupuis  |
|  6 | Dupuis | Martin   |  18 | martin.dupuis@laplateforme.io   | Dupuis  |
+----+--------+----------+-----+---------------------------------+---------+
2 rows in set (0,00 sec)

