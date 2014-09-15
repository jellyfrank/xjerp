# -*- coding:utf-8 -*-

from openerp.osv import osv,fields
from xml.etree import ElementTree
import httplib,urllib

class rainsoft_sms(osv.osv):
    _name='rainsoft.sms'   
	  
    _columns={
	'partner_id':fields.many2one('res.partner',string='partner'),
        'mobile':fields.char('Mobile'),
        'content':fields.text('Contents'),
        'status':fields.char('Status'),
        'message':fields.char('Message'),
        'template_id':fields.many2one('rainsoft.sms.template',string='template'),
    }    
    
    def _get_mobile(self,cr,uid,context=None):
	mobile=''
	if context.get('active_id'):
	    if context.get('active_model')=="sale.order":
		mobile = self.pool.get(context.get('active_model')).browse(cr,uid,context.get('active_id'),context=context).partner_id.mobile
	    if context.get('active_model')=="purchase.order":
		mobile = self.pool.get(context.get('active_model')).browse(cr,uid,context.get('active_id'),context=context).client.mobile
            if context.get('active_model')=='stock.picking.out':
                mobile = self.pool.get(context.get('active_model')).browse(cr,uid,context.get('active_id')).partner_id.mobile
	return mobile
	  
    def _get_partner(self,cr,uid,context=None):
	client_id=''
	if context.get('active_model')=='sale.order':
	    active_model =context.get('active_model')
	    client_id = self.pool.get(active_model).browse(cr,uid,context.get('active_id'),context=context).partner_id.id
	if context.get('active_model')=='purchase.order':
	    active_model =context.get('active_model')
	    client_id = self.pool.get(active_model).browse(cr,uid,context.get('active_id'),context=context).client.id
        if context.get('active_model')=='stock.picking.out':
	    active_model =context.get('active_model')
            client_id = self.pool.get(active_model).browse(cr,uid,context.get('active_id'),context=context).partner_id.id
	return client_id
    
    _defaults={
	'mobile':_get_mobile,
	'partner_id':_get_partner,
      }
    
    def on_change_template(self,cr,uid,ids,template_id,context=None):
	res={}	
	if template_id and context.get('active_model'):	
	    if context.get('active_model')=='sale.order':
		partner_name = self.pool.get(context.get('active_model')).browse(cr,uid,context.get('active_id')).partner_id.name
	    if context.get('active_model')=='purchase.order':
		client = self.pool.get(context.get('active_model')).browse(cr,uid,context.get('active_id')).client
		partner_name = client.name
	    if context.get('active_model')=='stock.picking.out':
		partner_name = self.pool.get(context.get('active_model')).browse(cr,uid,context.get('active_id')).partner_id.name
	    template = self.pool.get('rainsoft.sms.template').browse(cr,uid,template_id,context=context)
	    content=template.content.replace('{partner}',partner_name)
	    val={
	      'content':content
	      }
	    res["value"]=val
	return res

    def send_sms(self,cr,uid,ids,context=None):
        if context==None:
            context={}

        message = self.pool.get('rainsoft.sms').browse(cr,uid,ids[0],context=context)
        rs_send_service = self.pool.get('rainsoft.sendsms')
        res = rs_send_service.send(cr,uid,ids,message.mobile,message.content,context=context)
        val={
	    'status':res['status'],
	    'message':res['message'],
	  }
	return self.pool.get('rainsoft.sms').write(cr,uid,message.id,val,context=context)
     
        
rainsoft_sms()

class rainsoft_sms_template(osv.osv):
    _name='rainsoft.sms.template'
    
    _columns={
	'name':fields.char('Name'),
	'content':fields.text('Context'),
      }
    
rainsoft_sms_template()

        

