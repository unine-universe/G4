'''
Created on Apr 6, 2014

@author: hmuriel
'''
from jinja2.environment import Environment
from jinja2.loaders import FileSystemLoader
from unipy.db import openDB

class CreerAnnonce(object):
    env = None
    
    def __init__(self):
        # Référence au dossier HTML
        self.env = Environment(loader=FileSystemLoader('html'))
    
    def creer(self):
        # Charger et compléter le template HTML
        return self.env.get_template('CreerAnnonce.html').render()
    
    def save(self, **kwargs):
        print(kwargs)
        if 'type' in kwargs and 'category' in kwargs and'faculty' in kwargs and 'title' in kwargs:
            db = openDB()
            cursor = db.cursor()
            cursor.execute("INSERT INTO annonce VALUES(NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", 
                           (kwargs['type'], kwargs['publisher'], kwargs['category'],kwargs['faculty'], kwargs['title'], '', '', '', '', '', '', '', '', '', '' ,''))
            # Enregistrer les insertions.
            db.commit()
            if cursor.rowcount == 1:
                return self.env.get_template('CreerAnnonce.html').render(msg = "Annonce enregistrée !")
                #TODO : bouton aller sur mon compte --> <a href="/compte">Aller sur mon compte</a></p>'
            else:
                #TODO : afficher le msg à la fin
                return self.env.get_template('CreerAnnonce.html').render(msg = "Erreur d'enregistrement !")
            cursor.close()
            db.close()
        else:
            return self.env.get_template('CreerAnnonce.html').render(msg = "Il manque des paramètres... Réessayez")