'''
Created on Apr 6, 2014

@author: hmuriel
'''
import cherrypy
import os
from unipy.accueil import Annonces
from unipy.compte import Compte
from unipy.creerAnnonce import CreerAnnonce

# Paramètres pour cherrypy, pas besoin de les modifier.
cherrypy.config.update({
    # 'environment': 'production',
    'server.socket_host': '127.0.0.1',
    'server.socket_port': 8080,
    'log.error_file': 'site.log',
    'log.screen': True,
    'tools.sessions.on': True
})

# Racine de l'application
root_path = os.path.dirname(__file__)
# Controlleurs
accueil = Annonces()
compte = Compte()
creerannonce = CreerAnnonce()

# Gestionnaire des chemins d'accès (p. ex. /annonces/new)
d = cherrypy.dispatch.RoutesDispatcher()
# d.connect('NOM POUR LE CHEMIN',    'CHEMIN depuis la racine',    'OBJECT'                , 'METHODE')
d.connect('accueil'                , '/'                            , controller=accueil, action='accueil')
d.connect('mon-compte'             , '/compte'                      , controller=compte, action='index')
d.connect('mes-annonces'           , '/compte/annonces'             , controller=compte, action='annonces')
d.connect('mes-annonces-enligne'   , '/compte/annonces/enligne'       , controller=compte, action='annoncesEnLigne')
d.connect('mes-annonces-archives'  , '/compte/annonces/archives'    , controller=compte, action='annoncesArchives')
d.connect('mes-favoris'            , '/compte/favoris'              , controller=compte, action='favoris')
d.connect('mes-favoris-annonces'   , '/compte/favoris/annonces'     , controller=compte, action='favorisAnnonces')
d.connect('mes-favoris-recherche'  , '/compte/favoris/recherche'    , controller=compte, action='favorisRecherche')
d.connect('creer-annonce'          , '/creer-annonce'               , controller=creerannonce, action='creer')

# Configuration pour l'application
conf = {
        # Gestionnaire des chemins d'accès et la racine des dossiers.
        '/' : {'request.dispatch' : d, 'tools.staticdir.root':root_path},
        # Publication du dossier des images 
        '/img':{'tools.staticdir.on' : True, 'tools.staticdir.dir' :'img'},
        # Publication du dossier CSS
        '/css':{'tools.staticdir.on' : True, 'tools.staticdir.dir' :'css'},
        # Publication du dossier JS
        '/js':{'tools.staticdir.on' : True, 'tools.staticdir.dir' :'js'}
        }
# Démarrage du serveur cherrypy
cherrypy.quickstart(accueil, '/', conf)