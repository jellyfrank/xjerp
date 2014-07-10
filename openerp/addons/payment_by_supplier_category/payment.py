# coding: utf-8

from osv import orm, fields

class AccountVoucher(orm.Model):
    _inherit = 'account.voucher'

    _columns = {
            'product_categ_id': fields.related('partner_id',
                'product_categ_id', type='many2one', store=True,
                relation='product.category', string=u'供货类型')
            }

