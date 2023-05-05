##########################################################################################################################################################################################################
########################################################################################### SQL et PYTHON ################################################################################################
##########################################################################################################################################################################################################
'''
# On va créer une new base de données : 

CREATE DATABASE IF NOT EXISTS Entreprise;
# Affiche : Query OK, 1 row affected (0,01 sec)

USE Entreprise;
# Affiche : Database changed

CREATE TABLE IF NOT EXISTS employes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nom VARCHAR(255),
    prenom VARCHAR(255),
    salaire DECIMAL(10,2),
    id_service INT
);
# Affiche : Query OK, 0 rows affected (0,02 sec)

# Pour insérer des employées dans la table “employes” :

INSERT INTO employes (nom, prenom, salaire, id_service) VALUES 
('Christie', 'Agatha', 2500.50, 1),
('Eyre', 'Jane', 3000.75, 2),
('Poirot', 'Hercule', 2000.00, 3),
('Lieven', 'Thomas', 3500.00, 1);

# Affiche : Query OK, 4 rows affected (0,01 sec) Records: 4  Duplicates: 0  Warnings: 0

# Verification :

mysql> SELECT * FROM employes ORDER BY id;
+----+----------+---------+---------+------------+
| id | nom      | prenom  | salaire | id_service |
+----+----------+---------+---------+------------+
|  1 | Christie | Agatha  | 2500.50 |          1 |
|  2 | Eyre     | Jane    | 3000.75 |          2 |
|  3 | Poirot   | Hercule | 2000.00 |          3 |
|  4 | Lieven   | Thomas  | 3500.00 |          1 |
+----+----------+---------+---------+------------+
4 rows in set (0,00 sec)

# Pour récupérer tous les employées dont le salaire est supérieur à 3 000 € :

SELECT * FROM employes WHERE salaire > 3000;

# Affiche : 

mysql> SELECT * FROM employes WHERE salaire > 3000;
+----+--------+--------+---------+------------+
| id | nom    | prenom | salaire | id_service |
+----+--------+--------+---------+------------+
|  2 | Eyre   | Jane   | 3000.75 |          2 |
|  4 | Lieven | Thomas | 3500.00 |          1 |
+----+--------+--------+---------+------------+
2 rows in set (0,00 sec)

# Pour creer une table “services” contenant les champs suivants :
# - id, int, primary key, auto-incrémente
# - nom, varchar

CREATE TABLE services (
  id INT PRIMARY KEY AUTO_INCREMENT,
  nom VARCHAR(255)
);

# Affiche :

Query OK, 0 rows affected (0,02 sec)

# Pour inserer des services à ma table employés :

INSERT INTO services (nom) VALUES ('Marketing');
INSERT INTO services (nom) VALUES ('Vente');
INSERT INTO services (nom) VALUES ('Finance');

# Affiche :

mysql> INSERT INTO services (nom) VALUES ('Marketing');
Query OK, 1 row affected (0,00 sec)

mysql> INSERT INTO services (nom) VALUES ('Vente');
Query OK, 1 row affected (0,00 sec)

mysql> INSERT INTO services (nom) VALUES ('Finance');
Query OK, 1 row affected (0,01 sec)

# Verification :
SELECT * FROM services ORDER BY id;

# Affiche :
+----+-----------+
| id | nom       |
+----+-----------+
|  1 | Marketing |
|  2 | Vente     |
|  3 | Finance   |
+----+-----------+
3 rows in set (0,00 sec)

# Pour récupérer tous les employés et leur service respectif, il faut utiliser la clause JOIN 
# joint les tables "employes" et "services" en fonction de l'identifiant de service (id_service) :

SELECT e.*, s.nom AS service_nom 
FROM employes e
JOIN services s ON e.id_service = s.id;

# Affiche :
+----+----------+---------+---------+------------+-------------+
| id | nom      | prenom  | salaire | id_service | service_nom |
+----+----------+---------+---------+------------+-------------+
|  1 | Christie | Agatha  | 2500.50 |          1 | Marketing   |
|  2 | Eyre     | Jane    | 3000.75 |          2 | Vente       |
|  3 | Poirot   | Hercule | 2000.00 |          3 | Finance     |
|  4 | Lieven   | Thomas  | 3500.00 |          1 | Marketing   |
+----+----------+---------+---------+------------+-------------+
4 rows in set (0,00 sec)

# Pour créer une classe qui permet d’effectuer différentes opérations (CRUD) sur la table salariée, ça veut dire pouvoir :
    # Créer une nouvelle entrée (Create)
    # Lire une ou plusieurs entrées (Read)
    # Mettre à jour une ou plusieurs entrées (Update)
    # Supprimer une ou plusieurs entrées (Delete)
'''

# Permet d'importer le module pour se connecter à une base de données MySQL à partir de Python :
import mysql.connector

# Déclare une classe Python nommée Salaries. Cette classe permettra de réaliser les différentes opérations CRUD sur la table des salariés
class Salaries:
    
# Définit la méthode __init__, qui est le constructeur de la classe : exécutée automatiquement lorsqu'une instance de la classe est créée
    def __init__(self):
        
# Crée une connexion à la base de données MySQL à l'aide du module mysql.connector. Les informations de connexion sont spécifiées dans les arguments de la méthode connect().
        self.db = mysql.connector.connect(
            host="localhost",   # Cet argument spécifie l'adresse de l'hôte sur lequel la base de données est hébergée. Ici la base de données est hébergée localement sur la machine.
            user="root",    # Cet argument spécifie le nom d'utilisateur à utiliser pour se connecter à la base de données.
            password="monarque",    # Cet argument spécifie le mot de passe associé à l'utilisateur spécifié précédemment.
            database="Entreprise"   # Cet argument spécifie le nom de la base de données à laquelle se connecter.
        )
        self.cursor = self.db.cursor()  # Crée un curseur MySQL à partir de la connexion à la base de données. Le curseur est utilisé pour exécuter des requêtes sur la base de données.
        
# Permet d'ajouter un nouvel employé à la table employes en utilisant les paramètres nom, prenom, salaire et id_service.
    def create(self, nom, prenom, salaire, id_service):
        
# La variable sql contient la chaîne de caractères SQL avec des paramètres (%s) qui seront remplacés par les valeurs des variables correspondantes.
        sql = "INSERT INTO employes (nom, prenom, salaire, id_service) VALUES (%s, %s, %s, %s)"
        values = (nom, prenom, salaire, id_service) # on crée un tuple values contenant les valeurs des variables nom, prenom, salaire et id_service.
        self.cursor.execute(sql, values) # permet d'envoyer la requête SQL avec les paramètres à la base de données.
        self.db.commit() # permet de valider les changements dans la base de données
        print(self.cursor.rowcount, "employé ajouté.") # affiche ensuite le nombre de lignes modifiées (généralement 1 si l'insertion a réussi)

    def read(self):
        self.cursor.execute("SELECT * FROM employes")
        result = self.cursor.fetchall()
        for row in result:
            print(row)

    def update(self, id, salaire):
        sql = "UPDATE employes SET salaire = %s WHERE id = %s"
        values = (salaire, id)
        self.cursor.execute(sql, values)
        self.db.commit()
        print(self.cursor.rowcount, "employé(s) mis à jour.")

    def delete(self, id):
        sql = "DELETE FROM employes WHERE id = %s"
        values = (id,)
        self.cursor.execute(sql, values)
        self.db.commit()
        print(self.cursor.rowcount, "employé(s) supprimé(s).")

# Création d'une instance de la classe Salaries
salaries = Salaries()

# Ajout d'un nouvel employé
salaries.create("Dupont", "Jean", 2500, 1)

# Récupération et affichage de tous les employés
salaries.read()

# Mise à jour du salaire de l'employé avec l'identifiant 2
salaries.update(2, 3500)

# Suppression de l'employé avec l'identifiant 3
salaries.delete(3)

# Affiche : 
1 employé ajouté.
(1, 'Christie', 'Agatha', Decimal('2500.50'), 1)
(2, 'Eyre', 'Jane', Decimal('3000.75'), 2)
(3, 'Poirot', 'Hercule', Decimal('2000.00'), 3)
(4, 'Lieven', 'Thomas', Decimal('3500.00'), 1)
(5, 'Dupont', 'Jean', Decimal('2500.00'), 1)
1 employé(s) mis à jour.
1 employé(s) supprimé(s).

