# -*- coding: utf-8 -*-

from openerp.osv import osv
from openerp.osv import fields
import time


class inscription_establishment(osv.osv):
    """ Scolar establishment """
    _name = 'inscription.establishment'
    _description = 'Scolar Establishment'
    _columns = {
    'logo': fields.binary('Logo'),
    'name': fields.char('Nom', size=100, required=True),
    'description': fields.text('Description'),
    'address': fields.text('Addresse'),
    'universitys' : fields.one2many('inscription.university', 'establishment', 'Universite'),
    }
    
    def name_get(self, cr, uid, ids, context={}):
        if not len(ids):
            return []
        res=[]
        for u in self.browse(cr, uid, ids,context=context):
            res.append((u.id, u.name))
        return res

inscription_establishment()


class inscription_university(osv.osv):
    """ University """
    _name = 'inscription.university'
    _description = 'University'
    _table = 'inscription_university'
    _columns = {
    'logo': fields.binary('Logo'),
    'abbreviation': fields.char('Abbreviation', size=10, required=True),
    'name': fields.char('Nom', size=100, required=True),
    'description': fields.text('Description'),
    'website': fields.char('site web', size=100),
    'address': fields.text('Addresse'),
    'establishment' : fields.many2one('inscription.establishment', 'Etablissement'),
    'degrees' : fields.one2many('inscription.degree', 'university', 'Diplome'),
    }
    
    def name_get(self, cr, uid, ids, context={}):
        if not len(ids):
            return []
        res=[]
        for u in self.browse(cr, uid, ids,context=context):
            res.append((u.id, u.abbreviation + ', ' + u.name))
        return res
    
inscription_university()


class inscription_degree(osv.osv):
    """ Degree """
    _name = 'inscription.degree'
    _description = 'Degree'
    _columns = {
    'name': fields.char('Name', size=100, required=True),
    'description': fields.text('Description'),
    'university' : fields.many2one('inscription.university', 'Universite'),
    'specialities' : fields.one2many('inscription.speciality', 'degree', 'Specialities'),
    }
    
    def name_get(self, cr, uid, ids, context={}):
        if not len(ids):
            return []
        res=[]
        for u in self.browse(cr, uid, ids,context=context):
            res.append((u.id, u.university.abbreviation + ': ' + u.name))
        return res

inscription_degree()

class inscription_speciality(osv.osv):
    """ Degree speciality """
    _name = 'inscription.speciality'
    _description = 'speciality'
    _columns = {
    'name': fields.char('Name', size=100, required=True),
    'description': fields.text('Description'),
    'degree' : fields.many2one('inscription.degree', 'Degree'),
    'reformes' : fields.one2many('inscription.reforme', 'speciality', 'Reformes'),
    'inscriptions' : fields.one2many('inscription.inscription', 'speciality', 'Inscriptions'),
    }
    
    def name_get(self, cr, uid, ids, context={}):
        if not len(ids):
            return []
        res=[]
        for u in self.browse(cr, uid, ids,context=context):
            res.append((u.id, u.name + '(' + u.degree.name + ')'))
        return res

inscription_speciality()


class inscription_reforme(osv.osv):
    """ reforme """
    _name = 'inscription.reforme'
    _description = 'reforme'
    _columns = {
    'name': fields.char('Nom', size=100, required=True),
    'description': fields.text('Description'),
    'apply_date': fields.date('appliquer au date'),
    'confirmation': fields.selection((('Oui', 'Confirmie'), ('Non', 'Non confirmie')), 'Status'),
    'application': fields.selection((('Oui', 'Applicater'), ('Non', 'Non Applicater')), 'Application'),
    'speciality' : fields.many2one('inscription.speciality', 'Degree speciality'),
    'modules': fields.many2many('inscription.module', 'inscription_module_reforme_rel',
                    'reforme_id', 'module_id', string="Modules"),
    }

inscription_reforme()


class inscription_module(osv.osv):
    """ Module class """
    _name = 'inscription.module'
    _description = 'Module class'
    _columns = {
    'id': fields.char('Identifier', size=10, required=True),
    'designation': fields.char('Designation', size=100, required=True),
    'coefficient': fields.float('Coefficient', required=True),
    'hours_number': fields.integer('Nombre d\'heurs'),
    'description': fields.text('Description'),
    'conformity' : fields.many2one('inscription.module', 'Conforme'),
    'reformes': fields.many2many('inscription.reforme', 'inscription_module_reforme_rel', 
                        'module_id', 'reforme_id', string="Reformes"),
    'teaching_units': fields.many2many('inscription.teaching_unit', 'inscription_module_teaching_unit_rel', 
                        'module_id', 'teaching_unit_id', string="Teaching Units"),
    'credits': fields.one2many('notes.credit', 'module', 'Credits'),
    }

inscription_module()


class inscription_teaching_unit(osv.osv):
    """ Teaching Unit """
    _name = 'inscription.teaching_unit'
    _description = 'teaching_unit'
    _columns = {
    'designation': fields.char('Designation', size=100, required=True),
    'coefficient': fields.float('Coefficient', required=True),
    'hours_number': fields.integer('Nombre d\'heurs'),
    'description': fields.text('Description'),
    'modules': fields.many2many('inscription.module', 'inscription_module_teaching_unit_rel', 
                        'teaching_unit_id', 'module_id', string="Modules"),
    'exams' : fields.one2many('notes.exam', 'teaching_unit', 'Exams'),
    }

inscription_teaching_unit()


class inscription_inscription(osv.osv):
    """ inscription class """
    _name = 'inscription.inscription'
    _description = 'Inscription class'
    _columns = {
    'student' : fields.many2one('user.student', 'Etudiant'),
    'speciality' : fields.many2one('inscription.speciality', 'Study Speciality'),
    'study_year': fields.many2one('util.study_year', 'annee scolaire'),
    'confirmation': fields.selection((('Oui', 'Confirmie'), ('Non', 'Non confirmie')), 'Status'),
    }

inscription_inscription()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: