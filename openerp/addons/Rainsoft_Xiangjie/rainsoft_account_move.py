#coding:utf-8

from openerp.osv import osv,fields

class rainsoft_account_move(osv.Model):
    _name="account.move"
    _inherit=['account.move','mail.thread',]
