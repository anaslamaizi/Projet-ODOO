# -*- coding: utf-8 -*-

from openerp.osv import osv
from openerp.osv import fields
import time


class util_country(osv.osv):
    """ Country """
    _name = 'util.country'
    _description = 'Country'
    _rec_name = 'name'
    _columns = {
    'country_flag': fields.binary('Drapeau pays'),
    'name': fields.char('Nom de pays', size=100, required=True),
    'towns': fields.one2many('util.town', 'country', 'Towns')
    }
    
    def name_get(self, cr, uid, ids, context={}):
        if not len(ids):
            return []
        res=[]
        for u in self.browse(cr, uid, ids,context=context):
            res.append((u.id, u.name))
        return res
        
util_country()

class util_town(osv.osv):
    """ Town of different country"""
    _name = 'util.town'
    _description = 'Town'
    #_rec_name = 'name'
    _columns = {
    'name': fields.char('Nom', size=100, required=True),
    'country': fields.many2one('util.country', 'ville', required=True),
    }
    
    def name_get(self, cr, uid, ids, context={}):
        if not len(ids):
            return []
        res=[]
        for u in self.browse(cr, uid, ids,context=context):
            res.append((u.id, u.name + ', ' + u.country.name ))
        return res
        
util_town()

class util_study_year(osv.osv):
    """ Study year """
    _name = 'util.study_year'
    _description = 'Study year'
    _columns = {
    'study_year': fields.char('L\'année scolaire', size=100, required=True)
    }
    
    def name_get(self, cr, uid, ids, context={}):
        if not len(ids):
            return []
        res=[]
        for u in self.browse(cr, uid, ids,context=context):
            res.append((u.id, u.study_year))
        return res
        
util_study_year()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: