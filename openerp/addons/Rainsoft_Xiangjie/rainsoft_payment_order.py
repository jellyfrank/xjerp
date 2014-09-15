#coding:utf-8

from openerp.osv import osv,fields

class rainsoft_payment_order(osv.Model):
    _inherit='payment.order'

    _columns={
            'partner_id':fields.many2one('res.partner',string='Partner',domain=[('supplier','=',True)]),
            }
