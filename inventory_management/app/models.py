from app import db

class Article:
    def __init__(self, nom, description, quantite):
        self.nom = nom
        self.description = description
        self.quantite = quantite

    @classmethod
    def get_all(cls):
        articles = []
        for article in db.articles.find():
            articles.append(cls(article['nom'], article['description'], article['quantite']))
        return articles

    @classmethod
    def get_by_id(cls, article_id):
        article = db.articles.find_one({'_id': article_id})
        if article:
            return cls(article['nom'], article['description'], article['quantite'])
        else:
            return None

    @classmethod
    def create(cls, nom, description, quantite):
        db.articles.insert_one({
            'nom': nom,
            'description': description,
            'quantite': quantite
        })

    @classmethod
    def update(cls, article_id, nom, description, quantite):
        db.articles.update_one({'_id': article_id}, {'$set': {
            'nom': nom,
            'description': description,
            'quantite': quantite
        }})

    @classmethod
    def delete(cls, article_id):
        db.articles.delete_one({'_id': article_id})

