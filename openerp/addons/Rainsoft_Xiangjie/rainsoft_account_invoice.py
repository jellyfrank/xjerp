# -*- coding: utf-8 -*-

from openerp.osv import fields, osv
import openerp.addons.decimal_precision as dp    

class rainsoft_account_invoice(osv.osv):
    _name='account.invoice'
    _inherit = 'account.invoice'
    
    _columns={	
            'p_comment':fields.related('partner_id','comment',type='text',relation='res.partner',string='p_comment'),
      }

rainsoft_account_invoice()

class rainsoft_account_invoice_line(osv.osv):
		_name="account.invoice.line"
		_inherit="account.invoice.line"
		
		def _get_average_price(self,cr,uid,ids,fields,args,context=None):
				res={}
				if not context.has_key('period'):
						for i_id in ids:
								res[i_id]={
												'average_price':0.0,
												'cost_amount':0.0,
												}
						return res
					
				period = context['period']
				for i_id in ids:
					invoice = self.browse(cr,uid,i_id)
					#check if the product is phantom type
					boms_id = self.pool.get('mrp.bom').search(cr,uid,[('product_id','=',invoice.product_id.id),('type','=','phantom')],context=context)
					if len(boms_id):
							boms = self.pool.get('mrp.bom').browse(cr,uid,boms_id[0],context=context)
							a_price = 0.0
							for bom in boms.bom_lines:
									bom_lines = self.pool.get('rainsoft.account.carryover.line').search(cr,uid,[('product_id','=',bom.product_id.id),('period_id','=',period)],context=context)
									line = self.pool.get('rainsoft.account.carryover.line').browse(cr,uid,bom_lines[0],context=context)
									a_price +=line.average_price * bom.product_qty
							res[i_id]={'average_price':a_price,'cost_amount':a_price*invoice.quantity,}
					else:
							line_ids = self.pool.get('rainsoft.account.carryover.line').search(cr,uid,[('product_id','=',invoice.product_id.id),('period_id','=',period)],context=context)
							if len(line_ids):
									line = self.pool.get('rainsoft.account.carryover.line').browse(cr,uid,line_ids[0],context=context)
									res[i_id]={'average_price':line.average_price,'cost_amount':line.average_price*invoice.quantity,}
				return res
		
		_columns={
            'date':fields.related('invoice_id','date_invoice',type='date',string='Date'),
			'state':fields.related('invoice_id','state',type='char',string='State'),
			'average_price':fields.function(_get_average_price,multi="sums",string='Average Price',digits_compute=dp.get_precision('Account')),
			'cost_amount':fields.function(_get_average_price,multi="sums",string="Cost Amount",digits_compute=dp.get_precision('Account')),
            }

rainsoft_account_invoice_line()

   
