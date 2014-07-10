# -*- coding: utf-8 -*-
##############################################################################
# Sj City name for OpenERP
# Copyright (C) 2014 Jinan Shangjie Technology CO.,LTD. (<http://www.jnshangjie.com/>).
##############################################################################

from openerp.osv import fields, osv

try:
    from openerp import SUPERUSER_ID
except ImportError:
    SUPERUSER_ID = SUPERUSER_ID


class sj_city(osv.Model):
    _name = "sj.city"
    _description = "sj.city"

    _columns = {
        'name': fields.char(u'地市名称', size=20, required=True, help=u"地市名称"),
        'code': fields.char(u'行政区号', size=4, required=True, help=u"行政区号"),
    }
sj_city()

class sj_county(osv.Model):
    _name = "sj.county"
    _description = "sj.county"

    _columns = {
        'name': fields.char(u'区县名称', size=20, required=True, help=u"区县名称"),
        'code': fields.char(u'行政区号', size=6, required=True, help=u"行政区号"),
        'city_id': fields.many2one('sj.city', u'所属地市', required=True),
    }
    _defaults = {
        'city_id': lambda obj, cr, uid, context: context.get('city_id', ''),
    }
sj_county()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: