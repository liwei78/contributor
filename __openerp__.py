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

{
    "name" : "Distributor",
    "version" : "1.0",
    'category': '',
    "description" : "add a attribute `distributor_id` to res.partner",
    "author" : "liwei",
    "website" : "http://railser.cn",
    "depends" : ["base"],
    "init_xml" : [],
    "update_xml" : ["distributor_view.xml"],
    "installable" : True,
    "active" : False
}
