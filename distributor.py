# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2009 Tiny SPRL (<http://tiny.be>).
#
#    This program id designed for OG
#    It's add a attribute to res.partner with distributor_id
#    written by liwei
#    hi@liwei.me
#
##############################################################################

from osv import fields,osv

class custom_distributor(osv.osv):
    _name = 'res.partner'
    _inherit = 'res.partner'
    _columns = {
        'distributor_id': fields.char('Distributor',size=64, help="Distributor ID of Partner."),
    }
    _defaults = {
        'distributor_id': lambda *a: 0,
    }
custom_distributor()
