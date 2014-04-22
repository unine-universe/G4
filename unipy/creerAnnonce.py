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
        if 'type' in kwargs and 'choix' in kwargs and 'faculte' in kwargs and 'nomannonce' in kwargs:
            db = openDB()
            cursor = db.cursor()
            cursor.execute("INSERT INTO annonce VALUES(NULL, type, faculte, choix, nomannonce)", (kwargs['type'], kwargs['faculte'], kwargs['choix'], kwargs['nomannonce'],))
            # Enregistrer les insertions.
            db.commit()
            if cursor.rowcount == 1:
                return '<h1>Annonce enregistrée</h1><p><a href="/compte">Aller sur mon compte</a></p>'
            else:
                return '<h1>Erreur d\'enregistrement!</h1>'
            cursor.close()
            db.close()
        else:
            return '<h1>Il manque des paramètres!</h1>'