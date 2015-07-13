# -*- coding: utf-8 -*-

from openerp.osv import osv
from openerp.osv import fields
import time


class  stage_tache(osv.osv):
    """ stage_tache """
    _name = 'stage.tache'
    _description = 'stage_tache'
    _columns = {
    'type': fields.char('Type', size=100, required=True),
    }

stage_tache()

class  stage_type(osv.osv):
    """ stage_type """
    _name = 'stage.type'
    _description = 'stage_type'
    _columns = {
    'type': fields.char('Type', size=100, required=True),
    }

stage_type()

class  stage_statut(osv.osv):
    """ stage_statut """
    _name = 'stage.statut'
    _description = 'stage_statut'
    _columns = {
    'type': fields.char('Status', size=100, required=True),
    }

stage_statut()

class  stage_stage(osv.osv):
    """ stage_stage"""
    _name = 'stage.stage'
    _description = 'stage_stage'
    _columns = {
    'sujet': fields.char('sujet', size=100, required=True),
	'date_debut': fields.date('Date Début', required=True),
	'date_fin': fields.date('Date Fin', required=True),
    }

stage_stage()

