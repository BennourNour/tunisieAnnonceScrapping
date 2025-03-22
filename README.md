# tunisieAnnonceScrapping
Ce projet est une API Flask permettant de récupérer et de scraper des annonces immobilières en Tunisie, avec des endpoints pour accéder aux données collectées et lancer des sessions de scraping
### Prérequis
Avant d'exécuter cette application, vous devez avoir installé les outils suivants sur votre machine :
- [Python 3.x](https://www.python.org/downloads/) (si vous ne l'avez pas déjà installé)
- [PostgreSQL](https://www.postgresql.org/download/) (si vous prévoyez d'utiliser la fonctionnalité d'enregistrement dans PostgreSQL)
### Configuration

1. **Base de données PostgreSQL** :
   - Créez une base de données PostgreSQL appelée `tunisie_annonce`.
   - Configurez les paramètres de connexion dans le fichier `scraper.py` pour correspondre à votre installation de PostgreSQL.

## Installation et Exécution
1. Clonez ce dépôt sur votre machine locale :
    git clone https://github.com/BennourNour/tunisieAnnonceScrapping.git
    cd projet-tunisie-annonce
2. Installez les dépendances nécessaires :
    pip install -r requirements.txt
### Exécution de l'application

1. Lancez l'application Flask en exécutant le fichier `app.py` :
    python api/app.py

2. L'application sera accessible à l'adresse suivante :
    http://127.0.0.1:5000/

## Fonctionnalités

- **GET /annonces** : Retourne toutes les annonces collectées sous forme de JSON.
- **POST /scrape** : Lance une session de scraping pour récupérer de nouvelles annonces.
  
