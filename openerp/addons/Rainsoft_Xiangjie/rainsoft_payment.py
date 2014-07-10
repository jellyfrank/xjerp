#-*- coding:utf-8 -*-

from openerp.osv import osv,fields

class rainsoft_payment(osv.osv):
    _name="payment.line"
    _inherit="payment.line"

    _order="partner_id"
rainsoft_payment()
