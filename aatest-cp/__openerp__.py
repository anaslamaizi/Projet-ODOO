{
'name': 'Gestion des filiere final final',
'version': '0.1',
'category': 'Education',
'summary': 'Gestion d\'etudiants, profs, inscriptions, examens...',
'description': """
Ce module a ete cree par anas lamaizi ENT espace numerique de travail.
=======================================================================================

Ce module a ete cree par anas lamaizi ENT espace numerique de travail
contien:

* gestion dutilisateur(version : 0.1)
* Inscription dans universaite+etablisement (version : 0.1)
* gestion des examens (version : 0.1)

Version : 0.1

Author : Anas lamaizi""",
'author': 'Anas lamaizi',
'depends': ['mail'],
'data': [
    'user/user_view.xml',
    'inscription/inscription_view.xml',
    'notes/notes_view.xml',
    'util/util_view.xml','stage/stage_view.xml',
],
'update_xml': [
    'user/user_view.xml',
    'inscription/inscription_view.xml',
    'notes/notes_view.xml',
    'util/util_view.xml','stage/stage_view.xml',
],
'demo': [
    'inscription/establishment_demo.xml',
    'inscription/university_demo.xml',
],
'installable': True,
'images': [],
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
