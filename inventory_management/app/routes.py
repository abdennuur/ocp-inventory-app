from app import app
from flask import render_template

# Home route
@app.route('/')
def index():
    return render_template('index.html')

# Route to display articles
@app.route('/articles')
def articles():
    articles = [
        {'nom': 'Article 1', 'description': 'Description 1', 'quantite': 10},
        {'nom': 'Article 2', 'description': 'Description 2', 'quantite': 20},
    ]
    return render_template('articles.html', articles=articles)

# Route to display commandes
@app.route('/commandes')
def commandes():
    commandes = [
        {'id': 1, 'description': 'Commande 1', 'date': '2024-04-24'},
        {'id': 2, 'description': 'Commande 2', 'date': '2024-04-25'},
    ]
    return render_template('commandes.html', commandes=commandes)

# Route to display inventaire
@app.route('/inventaire')
def inventaire():
    inventaire = [
        {'id': 1, 'nom': 'Inventaire 1', 'quantite': 100},
        {'id': 2, 'nom': 'Inventaire 2', 'quantite': 200},
    ]
    return render_template('inventaire.html', inventaire=inventaire)

# Route to display login form
@app.route('/login')
def login():
    return render_template('login.html')

