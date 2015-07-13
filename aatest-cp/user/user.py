from openerp.osv import osv
from openerp.osv import fields
import time
from openerp import pooler, tools

class user_person(osv.osv):
    """ classe parent de  tout les utilisateurs """
    _name = 'user.person'
    _description = 'Parent class of all users'
    _columns = {
    'picture': fields.binary("Photo"),
    'cin_passport': fields.char('CIN/Apogee', size=100, required=True),
    'first_name': fields.char('Prenom', size=100, required=True),
    'last_name': fields.char('Nom', size=100, required=True),
    'address': fields.text('Addresse'),
    'town': fields.many2one('util.town', 'Ville', required=True),
    'email': fields.char('Email Adress', size=100),
    'phone': fields.integer('Numero de telephone'),
    'birthday': fields.date('date de naissance'),
    'user_groups' : fields.many2one('res.groups', 'Groupes d\'utilisateurs associes'),
    }
  
    def name_get(self, cr, uid, ids, context={}):
        if not len(ids):
            return []
        res=[]
        for u in self.browse(cr, uid, ids,context=context):
            res.append((u.id, u.cin_passport + ', ' + u.first_name + ' ' + u.last_name))
        return res
        
user_person()


class user_parent(osv.osv):
    """ The student parent or tutor """
    _name = 'user.parent'
    _description = 'Student parent or tutor'
    _inherit = 'user.person'
    _columns = {
        'students' : fields.one2many('user.student', 'parent', 'Etudiant'),
    }
user_parent()


class user_teacher(osv.osv):
    """ Teacher """
    _name = 'user.teacher'
    _description = 'teacher'
    _inherit = 'user.person'
    _columns = {
    'contract': fields.integer('Numero dinscription', required=True)
    }
user_teacher()


class user_student(osv.osv):
    """ Student """
    _name = 'user.student'
    _description = 'student'
    _inherit = 'user.person'
    _columns = {
    'inscription_number': fields.char('Numero dinscription', size=100, required=True),
    'parent' : fields.many2one('user.parent', 'Parent/Chef de departements'),
    'inscriptions' : fields.one2many('inscription.inscription', 'student', 'Inscriptions'),
    'credits': fields.one2many('notes.credit', 'Etudiant', 'Credit'),
    'evaluation': fields.one2many('notes.evaluation', 'Etudiant', 'Evaluation'),
    }
user_student()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: