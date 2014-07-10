# coding: utf-8
from osv import orm, fields

class Partner(orm.Model):
    _inherit = 'res.partner'

    _columns = {
            'product_categ_id': fields.many2one('product.category',
                u'供货类型'),
            }

