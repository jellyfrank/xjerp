# -*- coding:utf-8 -*-

from openerp.osv import osv,fields
from openerp.tools.translate import _
from openerp import netsvc
import openerp.addons.decimal_precision as dp

class rainsoft_picking(osv.Model):
    _name="stock.picking"
    _inherit="stock.picking"
    
    def _get_note(self,cr,uid,ids,fields,args,context=None):
        res={}
        for id in ids:
            origin = self.browse(cr,uid,id).origin
            sale_order_ids = self.pool.get('sale.order').search(cr,uid,[('name','=',origin)],context=context)
            sale_orders = self.pool.get('sale.order').browse(cr,uid,sale_order_ids,context=context)
            if len(sale_orders):
                res[id]=sale_orders[0].note
        return res
    
    _columns={
                    'deliver_state':fields.selection([('delivering',u'在途'),('delivered',u'已收货')],'Delivery State',select=True),
                    'out_type':fields.selection([('sale','Sale'),('proxy','Proxy'),],'Out Type',select=True),
                    's_note':fields.function(_get_note,string='Note',type='char'),
                    }




class rainsoft_picking_out(osv.osv):
		_name='stock.picking.out'
		_inherit='stock.picking.out'

                def _get_note(self,cr,uid,ids,fields,args,context=None):
                    res={}
                    for id in ids:
                        origin = self.browse(cr,uid,id).origin
                        sale_order_ids = self.pool.get('sale.order').search(cr,uid,[('name','=',origin)],context=context)
                        sale_orders = self.pool.get('sale.order').browse(cr,uid,sale_order_ids,context=context)
                        if len(sale_orders):
                            res[id]=sale_orders[0].note
                    return res

		
		_columns={
				'deliver_state':fields.selection([('delivering',u'在途'),('delivered',u'已收货')],'Delivery State',select=True),
                                'out_type':fields.selection([('sale','Sale'),('proxy','Proxy'),],'Out Type',select=True),
                                's_note':fields.function(_get_note,'Note',type='char'),
				}

		_defaults={
						'deliver_state':'delivering',
						}
		
		def send_sms(self,cr,uid,ids,context=None):
				mod_obj=self.pool.get('ir.model.data')
				form_res=mod_obj.get_object_reference(cr,uid,'Rainsoft_Xiangjie','rainsoft_sms_form_view')
				form_id = form_res and form_res[1] or False
				value ={
					   'name':_('Send Text Message'),
					   'view_mode': 'form',
					   'view_id': False,
					   'views': [(form_id,'form')],
					   'view_type': 'form',            
					   'res_model': 'rainsoft.sms', # object name
					   'type': 'ir.actions.act_window',
					   'target': 'new', # if you want to open the form in new tab
					   }
					
				return value
                def write(self,cr,uid,ids,values,context=None):
                    return super(rainsoft_picking_out,self).write(cr,uid,ids,values,context=context)
			  
rainsoft_picking_out()

class rainsoft_stock_move(osv.osv):
    _name="stock.move"
    _inherit="stock.move"
    
    def onchange_quantity(self, cr, uid, ids, product_id, product_qty,
                          product_uom, product_uos):
        """ On change of product quantity finds UoM and UoS quantities
        @param product_id: Product id
        @param product_qty: Changed Quantity of product
        @param product_uom: Unit of measure of product
        @param product_uos: Unit of sale of product
        @return: Dictionary of values
        """
        result = {
                  'product_uos_qty': 0.00
          }
        warning = {}

        if (not product_id) or (product_qty <=0.0):
            result['product_qty'] = 0.0
            return {'value': result}

        product_obj = self.pool.get('product.product')
        uos_coeff = product_obj.read(cr, uid, product_id, ['uos_coeff'])
        
        # Warn if the quantity was decreased 
        if ids:
            for move in self.read(cr, uid, ids, ['product_qty']):
		print product_qty,move['product_qty']
                if product_qty < move['product_qty']:
                    warning.update({
                       'title': _('Information'),
                       'message': _("By changing this quantity here, you accept the "
                                "new quantity as complete: OpenERP will not "
                                "automatically generate a back order.") })
		if product_qty > move['product_qty']:
		    product_qty = move['product_qty']
		    result['product_qty']=product_qty
                break

        if product_uos and product_uom and (product_uom != product_uos):
            result['product_uos_qty'] = product_qty * uos_coeff['uos_coeff']
        else:
            result['product_uos_qty'] = product_qty

        return {'value': result, 'warning': warning}
rainsoft_stock_move()
