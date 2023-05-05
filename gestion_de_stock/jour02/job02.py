##########################################################################################################################################################################################################
########################################################################################### SQL et PYTHON ################################################################################################
##########################################################################################################################################################################################################

# Une fois qu'on a récupéré les données depuis la base de données dans mon programme Python, on peut les utiliser pour effectuer des calculs ou pour les enregistrer dans un fichier :

# Pour rentrer dans la base de donnée crée hier : La Plateforme, 

#       USE LaPlateforme;

# On peut enfin crée des tables appartenants à la base de donnée concernée

CREATE TABLE etage (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nom VARCHAR(255),
    numero INT,
    superficie INT
);

# Affiche : Query OK, 0 rows affected (0,05 sec)

#       CREATE TABLE salles

CREATE TABLE salles (
  id INT PRIMARY KEY AUTO_INCREMENT,
  nom VARCHAR(255),
  id_etage INT,
  capacite INT
);

# Affiche : Query OK, 0 rows affected (0,02 sec)