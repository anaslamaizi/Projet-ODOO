# -*- coding: utf-8 -*-

from openerp.osv import osv
from openerp.osv import fields
import time


class notes_evaluation(osv.osv):
    """ Evaluation """
    _name = 'notes.evaluation'
    _description = 'Student evaluation'
    _columns = {
    'note': fields.float('Note', required=True),
    'session': fields.selection((('P', 'premiere session'), ('D', 'deuxieme session')), 'Session', required=True),
    'exam': fields.many2one('notes.exam', 'Exam'),
    'student': fields.many2one('user.student', 'Etudiants'),
    }


notes_evaluation()


class notes_exam(osv.osv):
    """ Exam """
    _name = 'notes.exam'
    _description = 'Exam'
    _columns = {
    'document': fields.binary('Document examen'),
    'date': fields.date('Date'),
    'session': fields.selection((('P', 'premiere session'), ('D', 'deuxieme session')), 'Session', required=True),
    'teaching_unit': fields.many2one('inscription.teaching_unit', 'Nom de Prof'),
    'exam_category': fields.many2one('notes.exam_category', 'categorie'),
    }


notes_exam()


class notes_exam_category(osv.osv):
    """ Exam category"""
    _name = 'notes.exam_category'
    _description = 'Exam category'
    _columns = {
    'designation': fields.char('Designation', size=100, required=True),
    'exams': fields.one2many('notes.exam', 'exam_category', 'Exams'),
    }


notes_exam_category()


class notes_credit(osv.osv):
    """ Student credit """
    _name = 'notes.credit'
    _description = 'Student credit'
    _columns = {
    'student': fields.many2one('user.student', 'Etudiants'),
    'module': fields.many2one('inscription.module', 'Module'),
    'credit': fields.float('Credit'),
    'status': fields.selection((('v', 'Valider'), ('NV', 'Non valider')), 'Status'),
    }


notes_evaluation()


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: