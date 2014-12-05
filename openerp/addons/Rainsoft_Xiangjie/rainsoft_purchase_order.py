#-*- coding:utf-8 -*-

from openerp.osv import osv,fields
from openerp.tools.translate import _
import datetime
import time

class rainsoft_purchase_order(osv.osv):
    _name='purchase.order'
    _inherit='purchase.order'
    
    def _get_client(self,cr,uid,ids,name,args,context=None):
        res={}
        for id in ids:
            purchase_order = self.browse(cr,uid,id)
            if purchase_order.origin:
                origin = purchase_order.origin.split(' ')[0]
            else:
                origin = ' '
            sale_order_id = self.pool.get('sale.order').search(cr,uid,[('name','=',origin)],context=context)
            partner_id = self.pool.get('sale.order').read(cr,uid,sale_order_id,['partner_id'],context=context)
            if partner_id:
                res[id]=partner_id[0]['partner_id'][0]
            else:
                res[id]=[]
        return res

    def _search_client(self,cr,uid,obj,name,args,context=None):
        res=[]
        ids = obj.search(cr,uid,[])
        for v in obj.browse(cr,uid,ids):
            if v.client:
                if args[0][2] in v.client.name:
                    res.append(v.id)
        return [('id','in',res)]

    def _get_sale_order_comment(self,cr,uid,ids,name,args,context=None):
        res={}
        sale_object = self.pool.get('sale.order')  
        for id in ids:
            purchase_order = self.browse(cr,uid,id,context=context)
            sale_order_ids = sale_object.search(cr,uid,[('name','=',purchase_order.origin)],context=context)
            sale_orders = sale_object.browse(cr,uid,sale_order_ids,context=context)
            if len(sale_orders):
                res[id]=sale_orders[0].note
        return res


    _columns={
        'client':fields.function(_get_client,fnct_search=_search_client,type='many2one',obj='res.partner',method=True,string='Client'),
        'pay_type':fields.related('partner_id','property_supplier_payment_term',type="many2one",relation='account.payment.term',string='Pay Type'),
        's_comment':fields.function(_get_sale_order_comment,'Sale Note',type="text"),

    }

    def onchange_partner_id(self, cr, uid, ids, partner_id,context=None):
			partner = self.pool.get('res.partner')
			if not partner_id:
					return {'value': {
						'fiscal_position': False,
						'payment_term_id': False,
						}}
			supplier_address = partner.address_get(cr, uid, [partner_id], ['default'])
			supplier = partner.browse(cr, uid, partner_id)

			#Read contract from module account.analytic.account
			contracts = self.pool.get('account.analytic.account').search(cr,uid,[('partner_id','=',partner_id)],context=context)
			if len(contracts):
					contract = self.pool.get('account.analytic.account').browse(cr,uid,contracts[0],context=context)
					if datetime.datetime.strptime(contract.date,"%Y-%m-%d")<datetime.datetime.now():
							return{'warning':{'title':'错误','message':'供应商合同已过期'},'value':{'partner_id':''}}
					if datetime.datetime.strptime(contract.date,'%Y-%m-%d')-datetime.datetime.now()<datetime.timedelta(days=45):
							raise osv.except_osv(_('Tip'),_('该供应商合同期限将于45天内到期！'))
			return {'value': {
					'pricelist_id': supplier.property_product_pricelist_purchase.id,
					'fiscal_position': supplier.property_account_position and supplier.property_account_position.id or False,
					'payment_term_id': supplier.property_supplier_payment_term.id or False,
            }}

    def send_sms(self,cr,uid,ids,context=None):
	  purchase_order = self.browse(cr,uid,ids[0])
	  mod_obj=self.pool.get('ir.model.data')
	  form_res=mod_obj.get_object_reference(cr,uid,'Rainsoft_Xiangjie','rainsoft_sms_form_view')
	  form_id = form_res and form_res[1] or False
	  value =  {
		  'name':_('Send Text Message'),
		  'view_mode': 'form',
		  'view_id': form_id,
		  'views': [(form_id,'form')],
		  'view_type': 'form',		    
		  'res_model': 'rainsoft.sms', # object name
		  'type': 'ir.actions.act_window',
		  'target': 'new', # if you want to open the form in new tab,
		  }
	  return value
rainsoft_purchase_order()
