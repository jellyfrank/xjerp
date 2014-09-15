#coding:utf-8

from openerp.osv import osv,fields

class rainsoft_stock_return(osv.Model):
		_inherit='stock.return.picking'

		_defaults={
						'invoice_state': '2binvoiced',
						}
