##########################################################################################################################################################################################################
########################################################################################### SQL et PYTHON ################################################################################################
##########################################################################################################################################################################################################

# À l’aide du SQL et python, développer un programme permettant la gestion d’un zoo

# Chaque animal possède un identifiant qui l’identifie de façon unique, un nom , une race, l’id du type de cage, une date de naissance et un pays d’origine.
# Une cage peut contenir un ou plusieurs animaux, mais peu être aussi vide. Chaque cage a un identifiant unique, une superficie et une capacité maximum.
'''
myslq -u root -p
monarque

CREATE DATABASE Zoo;
Query OK, 1 row affected (0,02 sec)

USE Zoo;
CREATE TABLE animal (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nom VARCHAR(50),
    race VARCHAR(50),
    id_cage INT,
    date_naissance DATE,
    pays_origine VARCHAR(50)
);
Query OK, 0 rows affected (0,04 sec)

CREATE TABLE cage (
    id INT PRIMARY KEY AUTO_INCREMENT,
    superficie FLOAT,
    capacite_max INT
);
Query OK, 0 rows affected (0,02 sec)

DESCRIBE animal;

+----------------+-------------+------+-----+---------+----------------+
| Field          | Type        | Null | Key | Default | Extra          |
+----------------+-------------+------+-----+---------+----------------+
| id             | int         | NO   | PRI | NULL    | auto_increment |
| nom            | varchar(50) | YES  |     | NULL    |                |
| race           | varchar(50) | YES  |     | NULL    |                |
| id_cage        | int         | YES  |     | NULL    |                |
| date_naissance | date        | YES  |     | NULL    |                |
| pays_origine   | varchar(50) | YES  |     | NULL    |                |
+----------------+-------------+------+-----+---------+----------------+
6 rows in set (0,01 sec)

DESCRIBE cage;

+--------------+-------+------+-----+---------+----------------+
| Field        | Type  | Null | Key | Default | Extra          |
+--------------+-------+------+-----+---------+----------------+
| id           | int   | NO   | PRI | NULL    | auto_increment |
| superficie   | float | YES  |     | NULL    |                |
| capacite_max | int   | YES  |     | NULL    |                |
+--------------+-------+------+-----+---------+----------------+
3 rows in set (0,00 sec)'''


'''
"id" est le nom de la première colonne. Nous avons défini cette colonne comme étant un entier (INT) et la clé primaire (PRIMARY KEY) de la table. De plus, nous avons défini la colonne pour s'auto-incrémenter (AUTO_INCREMENT), ce qui signifie que chaque fois que nous ajoutons une nouvelle ligne à la table, la valeur de cette colonne sera incrémentée automatiquement.
"nom" est le nom de la deuxième colonne. Nous avons défini cette colonne comme étant une chaîne de caractères (VARCHAR) avec une longueur maximale de 50 caractères.
"race" est le nom de la troisième colonne. Nous avons défini cette colonne comme étant une chaîne de caractères (VARCHAR) avec une longueur maximale de 50 caractères.
"cage_id" est le nom de la quatrième colonne. Nous avons défini cette colonne comme étant un entier (INT) qui représente l'identifiant de la cage dans laquelle l'animal est hébergé.
"date_naissance" est le nom de la cinquième colonne. Nous avons défini cette colonne comme étant une date (DATE) qui représente la date de naissance de l'animal.
"pays_origine" est le nom de la sixième colonne. Nous avons défini cette colonne comme étant une chaîne de caractères (VARCHAR) avec une longueur maximale de 50 caractères. Cette colonne représente le pays d'origine de l'animal.
")" indique la fin de la liste de colonnes pour cette table.
En somme, cette commande SQL crée une nouvelle table nommée "animal" avec six colonnes: "id", "nom", "race", "cage_id", "date_naissance" et "pays_origine". La colonne "id" est la clé primaire de la table et s'auto-incrémente. Les autres colonnes contiennent des informations sur chaque animal, telles que leur nom, leur race, leur date de naissance et leur pays d'origine.
'''

'''CREATE TABLE animal (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nom VARCHAR(50),
    race VARCHAR(50),
    cage_id INT,
    date_naissance DATE,
    pays_origine VARCHAR(50),
    FOREIGN KEY (cage_id) REFERENCES cage(id)
);

# Pour supprimer un animal, vous pouvez utiliser la commande DELETE FROM suivie d'une condition spécifiant l'animal que vous souhaitez supprimer.
DELETE FROM animal
WHERE id = 2;

# Pour modifier les caractéristiques d'un animal existant, vous pouvez utiliser la commande UPDATE suivie des valeurs que vous souhaitez 
# modifier et d'une condition spécifiant l'animal que vous souhaitez modifier.
UPDATE animal
SET nom = 'Rex', race = 'Labrador'
WHERE id = 1;

SELECT animal.id, animal.nom, animal.race, animal.id_cage, animal.date_naissance, animal.pays_origine, cage.superficie, cage.capacite_max
FROM animal
INNER JOIN cage ON animal.id_cage = cage.id;

Empty set (0,00 sec)

# Pour permettre au directeur du zoo d'ajouter, supprimer ou modifier des animaux ou des cages il faut créer une classe qui permet d’effectuer différentes opérations (CRUD) 
# sur la table animal, ça veut dire pouvoir : Créer une nouvelle entrée (Create), Lire une ou plusieurs entrées (Read), Mettre à jour une ou plusieurs entrées (Update) ou Supprimer une ou plusieurs entrées (Delete)


        
import mysql.connector

class Animal:
    def __init__(self):
        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="monarque",
            database="Zoo"
        )
        self.cursor = self.db.cursor()
        
    def create(self, nom, race, id_cage, date_naissance, pays_origine):
        sql = "INSERT INTO animal (nom, race, id_cage, date_naissance, pays_origine) VALUES (%s, %s, %s, %s, %s)"
        values = (nom, race, id_cage, date_naissance, pays_origine)
        self.cursor.execute(sql, values)
        self.db.commit()
        print(self.cursor.rowcount, "animal ajouté.")
        
    def read_all(self):
        sql = "SELECT * FROM animal"
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        for row in result:
            print(row)
            
    def update(self, id, nom=None, race=None, id_cage=None, date_naissance=None, pays_origine=None):
        sql = "UPDATE animal SET "
        values = []
        if nom:
            sql += "nom=%s, "
            values.append(nom)
        if race:
            sql += "race=%s, "
            values.append(race)
        if id_cage:
            sql += "id_cage=%s, "
            values.append(id_cage)
        if date_naissance:
            sql += "date_naissance=%s, "
            values.append(date_naissance)
        if pays_origine:
            sql += "pays_origine=%s, "
            values.append(pays_origine)
        sql = sql[:-2] + " WHERE id=%s"
        values.append(id)
        self.cursor.execute(sql, tuple(values))
        self.db.commit()
        print(self.cursor.rowcount, "animal modifié.")
        
    def delete(self, id):
        sql = "DELETE FROM animal WHERE id=%s"
        values = (id,)
        self.cursor.execute(sql, values)
        self.db.commit()
        print(self.cursor.rowcount, "animal supprimé.")
        
# Création d'une instance de la classe animal :
animaux = Animal()

# Ajout d'un nouvel animal :
animaux.create("Otis","Ornithorynque", 1, "2016-08-08", "Sénégal")
animaux.create("Tootsi","Tapir", 1, "2014-05-01", "Malaisie")
animaux.create("Luna","Puma", 2, "2012-12-05", "Sénégal")
animaux.create("Falcon","Faucon", 3, "2018-06-12", "Georgie")

# Récupération et affichage de tous les animaux du zoo :
animaux.read_all()

# Mise à jour de l'animal avec l'identifiant 2
#animaux.update()

# Suppression de l'animal avec l'identifiant 3
#animaux.delete(3)

mysql> SELECT animal.id_cage, cage.id
    -> FROM animal
    -> LEFT JOIN cage ON animal.id_cage = cage.id
    -> WHERE cage.id IS NULL;
Empty set (0,00 sec)

# Sur terminal j'insere mes données animaux :
INSERT INTO animal (nom, race, id_cage, date_naissance, pays_origine) VALUES 
("Otis","Ornithorynque", 1, "2016-08-08", "Sénégal"),
("Tootsi","Tapir", 1, "2014-05-01", "Malaisie"),
("Luna","Puma", 2, "2012-12-05", "Sénégal"),
("Falcon","Faucon", 3, "2018-06-12", "Georgie");

Query OK, 4 rows affected (0,01 sec)
Records: 4  Duplicates: 0  Warnings: 0

SELECT * FROM animal ORDER BY id;

+----+--------+---------------+---------+----------------+--------------+
| id | nom    | race          | id_cage | date_naissance | pays_origine |
+----+--------+---------------+---------+----------------+--------------+
|  1 | Otis   | Ornithorynque |       1 | 2016-08-08     | Sénégal      |
|  2 | Tootsi | Tapir         |       1 | 2014-05-01     | Malaisie     |
|  3 | Luna   | Puma          |       2 | 2012-12-05     | Sénégal      |
|  4 | Falcon | Faucon        |       3 | 2018-06-12     | Georgie      |
+----+--------+---------------+---------+----------------+--------------+
4 rows in set (0,01 sec)

# Sur terminal j'insere des données cage :

INSERT INTO cage (superficie, capacite_max)
VALUES (30.5, 5),
       (15.2, 1),
       (8.5, 2);

Query OK, 3 rows affected (0,01 sec)
Records: 3  Duplicates: 0  Warnings: 0

mysql> SELECT * FROM cage ORDER BY id;
+----+------------+--------------+
| id | superficie | capacite_max |
+----+------------+--------------+
|  1 |       30.5 |            5 |
|  2 |       15.2 |            1 |
|  3 |        8.5 |            2 |
+----+------------+--------------+
3 rows in set (0,00 sec)

# Pour joindre mes deux tables :

SELECT animal.id, animal.nom, animal.race, cage.id, cage.superficie, cage.capacite_max
FROM animal
JOIN cage ON animal.id_cage = cage.id;

# Affiche : 
+----+--------+---------------+----+------------+--------------+
| id | nom    | race          | id | superficie | capacite_max |
+----+--------+---------------+----+------------+--------------+
|  1 | Otis   | Ornithorynque |  1 |       30.5 |            5 |
|  2 | Tootsi | Tapir         |  1 |       30.5 |            5 |
|  3 | Luna   | Puma          |  2 |       15.2 |            1 |
|  4 | Falcon | Faucon        |  3 |        8.5 |            2 |
+----+--------+---------------+----+------------+--------------+
4 rows in set (0,00 sec)

import mysql.connector

# Se connecter à la base de données
mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="mydatabase"
)

# Créer un curseur pour exécuter les requêtes SQL
mycursor = mydb.cursor()

# Fonction pour ajouter une nouvelle cage
def ajouter_cage():
    superficie = input("Entrez la superficie de la cage : ")
    capacite_max = input("Entrez la capacité maximale de la cage : ")
    sql = "INSERT INTO cage (superficie, capacite_max) VALUES (%s, %s)"
    val = (superficie, capacite_max)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "cage ajoutée.")

# Fonction pour ajouter un nouvel animal
def ajouter_animal():
    nom = input("Entrez le nom de l'animal : ")
    race = input("Entrez la race de l'animal : ")
    cage_id = input("Entrez l'ID de la cage : ")
    date_naissance = input("Entrez la date de naissance de l'animal (format : AAAA-MM-JJ) : ")
    pays_origine = input("Entrez le pays d'origine de l'animal : ")
    sql = "INSERT INTO animal (nom, race, cage_id, date_naissance, pays_origine) VALUES (%s, %s, %s, %s, %s)"
    val
'''

import mysql.connector

# Se connecter à la base de données
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="monarque",
  database="Zoo"
)

# Créer un curseur pour exécuter les requêtes SQL
mycursor = mydb.cursor()

# Fonction pour ajouter une nouvelle cage
def ajouter_cage():
    superficie = input("Entrez la superficie de la cage : ")
    capacite_max = input("Entrez la capacité maximale de la cage : ")
    sql = "INSERT INTO cage (superficie, capacite_max) VALUES (%s, %s)"
    val = (superficie, capacite_max)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "cage ajoutée.")

def ajouter_animal():
  nom = input("Nom de l'animal : ")
  race = input("Race de l'animal : ")
  date_naissance = input("Date de naissance (AAAA-MM-JJ) : ")
  pays_origine = input("Pays d'origine : ")
  
  # affichage de toutes les cages disponibles
  cursor.execute("SELECT id, superficie, capacite_max FROM cage")
  cages = cursor.fetchall()
  print("Cages disponibles :")
  for cage in cages:
    print(f"{cage[0]} - Superficie : {cage[1]}, Capacité maximum : {cage[2]}")
    
  cage_id = input("ID de la cage : ")
  
  # insertion de l'animal dans la base de données
  sql = "INSERT INTO animal (nom, race, id_cage, date_naissance, pays_origine) VALUES (%s, %s, %s, %s, %s)"
  values = (nom, race, cage_id, date_naissance, pays_origine)
  cursor.execute(sql, values)
  db.commit()
  
  print("Animal ajouté avec succès !")

def supprimer_animal():
  animal_id = input("ID de l'animal à supprimer : ")
  
  # suppression de l'animal dans la base de données
  sql = "DELETE FROM animal WHERE id = %s"
  values = (animal_id,)
  cursor.execute(sql, values)
  db.commit()
  
  print("Animal supprimé avec succès !")

def modifier_animal():
  animal_id = input("ID de l'animal à modifier : ")
  
  # récupération de l'animal dans la base de données
  sql = "SELECT nom, race, id_cage, date_naissance, pays_origine FROM animal WHERE id = %s"
  values = (animal_id,)
  cursor.execute(sql, values)
  animal = cursor.fetchone()
  
  # affichage des informations de l'animal
  print(f"Nom : {animal[0]}")
  print(f"Race : {animal[1]}")
  print(f"ID de la cage : {animal[2]}")
  print(f"Date de naissance : {animal[3]}")
  print(f"Pays d'origine : {animal[4]}")
  
  # saisie des nouvelles informations
  nom = input("Nouveau nom (laissez vide si inchangé) : ")
  if nom == "":
    nom = animal[0]
  race = input("Nouvelle race (laissez vide si inchangée) : ")
  if race == "":
    race = animal[1]
  date_naissance = input("Nouvelle date de naissance (AAAA-MM-JJ) (laissez vide si inchangée) : ")
  if date_naissance == "":
    date_naissance = animal[4]
  pays_origine = input("Nouveau pays d'origine (laissez vide si inchangé) : ")
  if pays_origine == "":
    pays_origine = animal[5]

  # construction de la requête SQL
  sql = "UPDATE animal SET nom = %s, race = %s, id_cage = %s, date_naissance = %s, pays_origine = %s WHERE id = %s"
  values = (nom, race, id_cage, date_naissance, pays_origine, id)
  cursor.execute(sql, values)
  connection.commit()

  print("Animal modifié avec succès!")

animaux = Animal()

# Ajout d'un nouvel employé
animaux.create("Dupont", "Jean", 2500, 1)

# Récupération et affichage de tous les employés
animaux.read()

# Suppression de l'employé avec l'identifiant 3
animaux.delete(3)
