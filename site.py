#!/usr/local/bin/python3.7
import cherrypy
import os

class MonSiteWeb(object):
    def __init__(self):
        self.qs=Questions()
        self.photos=Photos()
        self.music=Music()
        self.publis=Publis()
        self.code=Code()
        self.nv=NonViolence()
        self.meta=Meta()
#les pages peuvent etre des objets ou des méthodes de l'objet principal
    def index(self):
        return '''
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN">
<HTML>
<TITLE>The ꘏꘏�꘏꘏ website</TITLE>
<HEAD>The ꘏꘏�꘏꘏ website</HEAD>
<BODY>
<br>
<ul>
<li><a href=/qs>questions (im)pertinentes</a></li>
<li><a href=/photos>photos</a></li>
<li><a href=/music>music</a></li>
<li><a href=/publis>publis</a></li>
<li><a href=/nv>non-violence</a></li>
<li><a href=/code>code python</a></li>
<li><a href=/meta>metapolitique</a></li>
</ul>
contact : aurel.pere [at] gmail.com
</BODY>
</HTML>
    '''
    index.exposed=True

class Questions(object):
    def __init__(self):
        self.nom="page des questions"
    def index(self):
        return '''
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN">
<HTML>
<TITLE>The ꘏꘏�꘏꘏ website - la page des questions</TITLE>
<HEAD>The ꘏꘏�꘏꘏ website - la page des questions</HEAD>
<BODY>
<br><br><br>
Cette page est la page des questions.<br><br>
<a href="/fichiers/gnd.pdf">GreenNewDeal</a><br>
<br><br><br>
[<a href="/">Retour</a>]
</BODY>
</HTML>
    '''
    index.exposed =True


class Code(object):
    def __init__(self):
        self.nom="page de code python"
    def index(self):
        return '''
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN">
<HTML>
<TITLE>The ꘏꘏�꘏꘏ website - la page des questions</TITLE>
<HEAD>The ꘏꘏�꘏꘏ website - la page des questions</HEAD>
<BODY>
<br><br><br>
Cette page est la page de dev de code python.<br><br>
Pour l'instant elle ne concerne qu'un programme développé pour le <a href="https://www.cnnr.fr">cnnr</a><br>
Le depot du code est disponible sur <a href="https://framagit.org/kr1p/planif-ecologique-openstreetmap">framagit</a><br><br>

<a href="/fichiers/classPlanning.py">fichier ClassPlanning.py</a><br>
<br><br>
<a href="/fichiers/v0_a.py">fichier v0_a.py</a><br>
<br><br>

Ce programme a été initialement développé pour le cnnr (www.cnnr.fr). Il est conçu en python pour utiliser les données d'openstreetmap et d'ocsge afin de faire des calculs sur le où et combien on peut développer la planification écologique<br><br>

Il permet de :<br><br>
1. calculer un "score" de proximité à des services de mobilité pour chaque logement<br><br>
2. calibrer le nombre de services à construire pour que tous les logements puissent y accéder en moins de 20 minutes (12,5 km en voiture, 5 km en vélo, 1,5 km à pied)<br><br>
3. calculer si chaque logement a un jardin (modifier le fichier des logements avec un index) dans l'optique de savoir où et combien de logements peuvent accueillir une installation géothermique individuelle <br><br>
4. calculer le nombre de stations services disposant d'un espace naturel ou agricole de 12ha à moins d'un kilometre (modifier le fichier des stations services avec un index) dans l'optique de savoir où et combien de stations services peuvent etre converties en stations energies renouvelables.<br><br>

Il pourra nottament interesser des chercheurs en géomatique ou en écologie appliquée pour mettre en oeuvre une planification écologique.<br><br>

Les fichiers osm.pbf doivent être placés dans le repertoire "home/KIT" (~/KIT) et les fichiers .shp ocsge dans des répertoires adhoc dans "home" également (MiPy, LR, Corse, Pays, et OCS_GE_1-1_2017_SHP_RGAF09UTM20_D972_2019-07-24 pour la martinique)<br><br>

Il fonctionne sous linux et il est nécessaire d'installer postegresql, osm2pgsql, ogr2ogr. La distribution OsGeo de linux est bien adaptée car préconfigurée pour cet usage.<br><br>

Les fonctions utilisées sont disponible dans ClassPlanning.py et le "wrapping" pas à pas dans un module tkinter est disponible dans v0_a.py. La base de données utilisée dans le "wrapping" avec tkinter se nomme 'gis'.<br><br>

Pour le calcul 2, il est nécessaire de définir une "bounding box" (bbox) du territoire/de l'espace considéré en coordonnées epsg 4326. Les bbox ne sont pas définies dans le wrapper tkinter et il est nécessaire de modifier le fichier de façon adéquate.<br><br>

Toute contribution est la bienvenue, notamment pour tester le programme sur des territoires et pour une partie "rendering"(représentation graphique) qui n'est pas encore développée.<br><br>


<br><br>
[<a href="/">Retour</a>]
</BODY>
</HTML>
    '''
    index.exposed =True

class Photos(object):
    def __init__(self):
        self.nom="page des photos"
    def index(self):
        return '''
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN">
<HTML>
<TITLE>The ꘏꘏�꘏꘏ website - la page des photos</TITLE>
<HEAD>The ꘏꘏�꘏꘏ website - la page des photos</HEAD>
<BODY>
<br><br><br>
Cette page est la page des photos.<br><br>
<CENTER><TABLE width=95% border=0>
<TR><TD width=34%><a href="/fichiers/selection/1.JPG"><img src="/fichiers/selection/thumb.1.JPG" alt="Art1" width="200" height=auto></a></TD>
<TD width=33%><a href="/fichiers/selection/2.JPG"><img src="/fichiers/selection/thumb.2.JPG" alt="Art1" width="200" height=auto></a></TD>
<TD width=34%><a href="/fichiers/selection/3.JPG"><img src="/fichiers/selection/thumb.3.JPG" alt="Art1" width="200" height=auto></a></TD></TR>
<TR><TD width=34%><a href="/fichiers/selection/3b.JPG"><img src="/fichiers/selection/thumb.3b.JPG" alt="Art1" width="200" height=auto></a></TD>
<TD width=33%><a href="/fichiers/selection/3c.JPG"><img src="/fichiers/selection/thumb.3c.JPG" alt="Art1" width="200" height=auto></a></TD>
<TD width=34%><a href="/fichiers/selection/3d.JPG"><img src="/fichiers/selection/thumb.3d.JPG" alt="Art1" width="200" height=auto></a></TD></TR>
<TR><TD width=34%><a href="/fichiers/selection/4.JPG"><img src="/fichiers/selection/thumb.4.JPG" alt="Art1" width="200" height=auto></a></TD>
<TD width=33%><a href="/fichiers/selection/5.JPG"><img src="/fichiers/selection/thumb.5.JPG" alt="Art1" width="200" height=auto></a></TD>
<TD width=34%><a href="/fichiers/selection/6.JPG"><img src="/fichiers/selection/thumb.6.JPG" alt="Art1" width="200" height=auto></a></TD></TR>
<TR><TD width=34%><a href="/fichiers/selection/7.JPG"><img src="/fichiers/selection/thumb.7.JPG" alt="Art1" width="200" height=auto></a></TD>
<TD width=33%><a href="/fichiers/selection/8.JPG"><img src="/fichiers/selection/thumb.8.JPG" alt="Art1" width="200" height=auto></a></TD>
<TD width=34%><a href="/fichiers/selection/9.JPG"><img src="/fichiers/selection/thumb.9.JPG" alt="Art1" width="200" height=auto></a></TD></TR>
<TR><TD width=34%><a href="/fichiers/selection/10.JPG"><img src="/fichiers/selection/thumb.10.JPG" alt="Art1" width="200" height=auto></a></TD>
<TD width=33%><a href="/fichiers/selection/11.JPG"><img src="/fichiers/selection/thumb.11.JPG" alt="Art1" width="200" height=auto></a></TD>
<TD width=34%><a href="/fichiers/selection/12.JPG"><img src="/fichiers/selection/thumb.12.JPG" alt="Art1" width="200" height=auto></a></TD></TR>
<TR><TD width=34%><a href="/fichiers/selection/13.JPG"><img src="/fichiers/selection/thumb.13.JPG" alt="Art1" width="200" height=auto></a></TD>
<TD width=33%><a href="/fichiers/selection/14.JPG"><img src="/fichiers/selection/thumb.14.JPG" alt="Art1" width="200" height=auto></a></TD>
<TD width=34%><a href="/fichiers/selection/15.JPG"><img src="/fichiers/selection/thumb.15.JPG" alt="Art1" width="200" height=auto></a></TD></TR>
<TR><TD width=34%><a href="/fichiers/selection/16.JPG"><img src="/fichiers/selection/thumb.16.JPG" alt="Art1" width="200" height=auto></a></TD>
<TD width=33%><a href="/fichiers/selection/17.JPG"><img src="/fichiers/selection/thumb.17.JPG" alt="Art1" width="200" height=auto></a></TD>
<TD width=34%><a href="/fichiers/selection/18.JPG"><img src="/fichiers/selection/thumb.18.JPG" alt="Art1" width="200" height=auto></a></TD></TR>
<TR><TD width=34%><a href="/fichiers/selection/19b.JPG"><img src="/fichiers/selection/thumb.19b.JPG" alt="Art1" width="200" height=auto></a></TD>
<TD width=33%><a href="/fichiers/selection/20.JPG"><img src="/fichiers/selection/thumb.20.JPG" alt="Art1" width="200" height=auto></a></TD>
<TD width=34%><a href="/fichiers/selection/21.JPG"><img src="/fichiers/selection/thumb.21.JPG" alt="Art1" width="200" height=auto></a></TD></TR>
<TR><TD width=34%><a href="/fichiers/selection/22.JPG"><img src="/fichiers/selection/thumb.22.JPG" alt="Art1" width="200" height=auto></a></TD>
<TD width=33%><a href="/fichiers/selection/23.JPG"><img src="/fichiers/selection/thumb.23.JPG" alt="Art1" width="200" height=auto></a></TD>
<TD width=34%><a href="/fichiers/selection/24.JPG"><img src="/fichiers/selection/thumb.24.JPG" alt="Art1" width="200" height=auto></a></TD></TR>
<TR><TD width=34%><a href="/fichiers/selection/25.JPG"><img src="/fichiers/selection/thumb.25.JPG" alt="Art1" width="200" height=auto></a></TD>
<TD width=33%><a href="/fichiers/selection/26.JPG"><img src="/fichiers/selection/thumb.26.JPG" alt="Art1" width="200" height=auto></a></TD>
<TD width=34%><a href="/fichiers/selection/27.JPG"><img src="/fichiers/selection/thumb.27.JPG" alt="Art1" width="200" height=auto></a></TD></TR>

</TABLE></CENTER>
<br><br><br>
[<a href="/">Retour</a>]
</BODY>
</HTML>
    '''
    index.exposed =True

class Music(object):
    def __init__(self):
        self.nom="page de creation musicale"
    def index(self):
        return '''
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN">
<HTML>
<TITLE>The ꘏꘏�꘏꘏ website - la page musique</TITLE>
<HEAD>The ꘏꘏�꘏꘏ website - la page musique</HEAD>
<BODY>
<br><br><br>
vous trouverez un extrait de bidouillages musical ici : <a href=/fichiers/medley.mp3>medley</a>
<br><br><br>
[<a href="/">Retour</a>]
</BODY>
</HTML>
    '''
    index.exposed=True

class Publis(object):
    def __init__(self):
        self.nom="page des publis"
    def index(self):
        return '''
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN">
<HTML>
<TITLE>The ꘏꘏�꘏꘏ website - la page des publis</TITLE>
<HEAD>The ꘏꘏�꘏꘏ website - la page des publis</HEAD>
<BODY>
<br><br><br>
Cette page est la page des publis.<br><br>

Vous y trouverez des documents publiés dont je suis l'auteur.<br><br>
2010 : <a href="/fichiers/2011/apere_cete_phtv_aqui_1.pdf">potentiel photovoltaique aquitaine</a><br>
2010 : <a href="/fichiers/2011/apere_cete_phtv_limou_1.pdf">potentiel photovoltaique limousin</a><br>
2011 : <a href="/fichiers/2011/apere_cete_phtv_aqui_2.pdf">prospective aquitaine photovoltaique 2020</a> (notez qu'on se trouve entre le scenario "median" et "de transition" fin 2019 avec environ 1800 MW installés cf stats <a href="https://www.statistiques.developpement-durable.gouv.fr/tableau-de-bord-solaire-photovoltaique-quatrieme-trimestre-2019">ici</a>)<br>
2011 : <a href="/fichiers/2011/apere_cete_phtv_limou_2.pdf">prospective limousin photovoltaique 2020"</a> (notez qu'on est à environ 85% du scenario de transition fin 2019 avec environ 250MW installés cf stats <a href="https://www.statistiques.developpement-durable.gouv.fr/tableau-de-bord-solaire-photovoltaique-quatrieme-trimestre-2019">ici</a>)<br> 
2011 : <a href="/fichiers/2011/EC_Synthese_CUB.pdf">synthese des politique energie climat de 6 agglomerations</a> (exemple sur la CUB)<br>
2012 : <a href="/fichiers/2012/cete_apere_loyers_aquitaine.pdf">etude des loyers prives en aquitaine</a><br>
2012 : <a href="/fichiers/2012/apere_synthese_loyers_pc.pdf">etude des loyers prives en poitou charentes</a><br>
2012 : <a href="/fichiers/2012/apere_synthese_loyers_17.pdf">synthese des loyers prives en charente maritime</a> (avec une data visualisation interessante)<br>
2013 : <a href="/fichiers/2013/CETE_cout_logement.pdf">cout du logement en gironde</a> (methode avec donnees locales sans pre-modele)<br>
2013 : <a href="/fichiers/2013/diag_epci79_NordOuest_vfinale.pdf">diagnostic de tous les epci des deux-sevres</a> (exemple sur l'epci nord ouest)<br>
2014 : publication quae psdr (envoyée fin 2014, publiée en 2015/2016) <a href="https://www.cairn.info/partenariats-pour-le-developpement-territorial--9782759224081-page-125.htm">Didier Labat, Aurélien Péré. "Méthode d’analyse des outils de politique forestière et de planification foncière.". Dans Partenariats pour le développement territorial, pages 125 à 148,2015</a><br>
2015 : <a href="/fichiers/2015/apere_dtectv_fet.pdf">facture energetique territoriale</a><br><br>

A partir de 2015 la plupart de mes propositions n'ont pas été publiées, ou pas en mon nom. <br><br>

2016 : <a href="/fichiers/2016/script_habitat&activite_vacant.sql">script sql pour identifier les logements et batiments vacants dans le fichier majic</a> (je vous laisse deviner combien de lignes prend la commande sql permettant d'identifier tous les logements vides depuis plusieurs années au 1er janvier dans toute la France). Vous pouvez aussi calculer ceci en nombre de frappes clavier et clics de souris.
<br>

2016 : <a href="/fichiers/2016/apere_dterso_zoneactivite_07.03.16.pdf">creation epfe aquitaine - contribution au diagnostic foncier des zones d'activites</a><br>

2017 : <a href="/fichiers/2017/memoire_enr_APERE_31.08.17.pdf">memoire m2 sur les enr  : Quels critères pour une transition écologique « conviviale » ?</a><br>

2019 : <a href="/fichiers/2019/APERE_ADEME_CCTP éolien_09.06.19.pdf">cahier des charges pour une etude sur l'impact de l'eolien sur les prix fonciers et immobiliers</a>(non retenu par le cedip)<br>

2019 : <a href="/fichiers/2019/apere_inforsid_confiance_ntic.pdf">Proposition Inforsid transmise à M. Colletis : "Quelles sont les « nouvelles couches de contraintes » plus ou moins institutionnalisées que les
NTIC apportent et comment cela influence ou interfère avec les différents échelons de démocratie ?"</a> (non retenue par le cedip) <br>

2019 : <a href="/fichiers/2019/apere_note_FOAD_velo_cedip.pdf">proposition de formation à distance velo pour le ministere de l'ecologie</a>(non retenue par le cedip)<br>

2019 : <a href="/fichiers/2019/apere_veille_cedip.pdf">veille logicielle pour le cedip</a>(retenue par le cedip)<br>

2019 : <a href="/fichiers/2019/apere_plu_mtp_noteverdanson.pdf">contribution citoyenne aux enjeux d'innondation du plu à montepellier - verdanson</a><br><br>

2020 : <a href="/fichiers/Harrassment_journal.pdf">contribution à un outil anti harcellement version papier (creative commons)</a>
<br><br>
   
<br><br>
[<a href="/">Retour</a>]
</BODY>
</HTML>
    '''
    index.exposed =True

class NonViolence(object):
    def __init__(self):
        self.nom="page non violence"
    def index(self):
        return '''
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN">
<HTML>
<TITLE>The ꘏꘏�꘏꘏ website - la page non violence</TITLE>
<HEAD>The ꘏꘏�꘏꘏ website - la page non violence</HEAD>
<BODY>
<br><br><br>
Cette page est la page non violence.<br>
Vous y trouverez des ressources intéressantes et quelques exemples d'actions auxquelles j'ai participé.
<br><br><br>
liste de 198 types d'actions non violentes : <a href="https://nonviolence.fr/IMG/pdf/Fiche_198_actions.pdf">ici </a><br><br>
ressources réunions : <a href="/fichiers/reunions.pdf">ici</a><br><br>
ressources bizi sur les actions non violentes : <a href="/fichiers/repertoire.pdf"> ici </a><br><br><br>
passerelle avec goulotte vélo réalisée à montpellier : <img src="/fichiers/passerellevelo.png"></img><br><br>
piste vélo : <a href="https://www.youtube.com/watch?v=iSHADaRB2hE">video réalisée à Montpellier</a><br><br>
lien vers xr (extinction rebellion) : <a href="https://https://rebellion.global">ici</a> <br><br>
lien vers anv cop21 : <a href="https://anv-cop21.org">ici</a><br><br>
<br><br><br>
[<a href="/">Retour</a>]
</BODY>
</HTML>
    '''
    index.exposed =True

class Meta(object):
    def __init__(self):
        self.nom="page meta politique"
    def index(self):
        return '''
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN">
<HTML>
<TITLE>The ꘏꘏�꘏꘏ website - la page metapolitique</TITLE>
<HEAD>The ꘏꘏�꘏꘏ website - la page metapolitique</HEAD>
<BODY>
<br><br><br>
Cette page est la page metapolitique.<br>
Vous y trouverez des ressources intéressantes sur des questions politiques.
<br><br><br>
#rh&harcellement : <a href="/fichiers/Harrassment_journal.pdf">une contribution</a> d'outil pour lutter contre le harcellement au travail,<br><br>
#velo,<br><br>
#budget&sankey : un exemple d'utilisation de schémas de sankey pour visualiser des budgets publics:<br><br><a href="/fichiers/sankey_madrid_2009.gif">
<img src="/fichiers/thumb_sankey.gif"></a>
<br><br>l'exemple <a href="https://fr.wikipedia.org/wiki/Audrey_Tang">d'audrey tang</a> à taïwan avec vg0v<br><br>
#enr,<br><br>
#climat,<br><br>
#donnéeshistorisées,<br><br>
#chiffre&structure,<br><br>
#psychologiecoll&effetsurveillance<br><br>
<br><br><br>
[<a href="/">Retour</a>]
</BODY>
</HTML>
    '''
    index.exposed =True

site=MonSiteWeb()
cherrypy.config.update({'environment': 'production',
    'log.screen': True,
    'log.error_file':'/home/kr1p/webapps/cherrypy/logerrors',                        
    'tools.encode.encoding':'Utf-8',
    'tools.staticdir.root':'/home/kr1p/webapps/cherrypy',
    #'tools.sessions.on' = True,
    #'tools.sessions.secure'=True,
    #'tools.sessions.storage_type': "File",
    #'tools.sessions.storage_path': '/home/kr1p/webapps/cherrypy/sessions',
    #'tools.sessions.httponly=True,
    #'tools.sessions.timeout'=10,
    'server.socket_host': '127.0.0.1',
    'server.socket_port': 25638})
conf={'/fichiers':{'tools.staticdir.on':True,'tools.staticdir.dir':'fichiers'}}
cherrypy.quickstart(site,config=conf)



