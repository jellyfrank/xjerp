#-*- coding:utf-8 -*-
import logging
from openerp.tools.translate import _
from openerp.osv import fields,osv,orm
from rainsoft_message import message


_logger = logging.getLogger(__name__)


class rainsoft_product(osv.osv):
	_name="product.product"
	_inherit="product.product"


	def _get_total_price(self,cr,uid,ids,name,args,context=None):
	    res={}
	    products = self.browse(cr,uid,ids)
	    for product in products:
		total = product.lst_price * product.qty_available
		res[product.id]=total
	    return res


	_description="add constraints"
	_columns={
	    'total':fields.function(_get_total_price,type="float",string="Total"),
        'loc_rack':fields.many2one('rainsoft.rack',string="Rack"),
	}
	_sql_constraints=[
			('rainsoft_product_default_code','unique(default_code)','default_code must be unique'),
			('rainsoft_product_name','unique(name_template)','there is one product which has the same name.'),
			]

	def copy(self,cr,uid,id,default=None,context=None):
		if context is None:
			context={}
		if not default:
			default={}

		context_wo_lang=context.copy()
		context_wo_lang.pop('lang',None)
		product=self.read(cr,uid,id,['name','default_code'],context=context_wo_lang)
		default = default.copy()
		default.update(name=_("%s (copy)") % (product['name']))
       
		if context.get('variant',False):
			fiedls=['product_tmpl_id','active','variants','price_marign','price_extral']
			data=self.read(cr,uid,id,fields=fields,context=context)
			for f in fields:
				if f in default:
					data[f]=default[f]
			data['product_tmpl_id']=data.get('product_tmpl_id',False)\
					and data['product_tmpl_id'][0]
			del data['id']
			return self.create(cr,uid,data)
		else:
			default.update(default_code=product['default_code']+'0')
			result = super(rainsoft_product,self).copy(cr,uid,id,default=default,context=context)
			return result
		      
	def create(self,cr,uid,values,context=None):
		if values.has_key("default_code"):
		    for x in list(values['default_code']):
			if not x.isdigit():
			    raise osv.except_osv(u'输入错误!',message.get_joke())
		return super(rainsoft_product,self).create(cr,uid,values,context=context)
	
	def write(self,cr,uid,ids,values,context=None):
		if values.has_key("default_code"):
		    for x in list(values['default_code']):
			if not x.isdigit():
			    raise osv.except_osv(u'输入错误!',message.get_joke())
		return super(rainsoft_product,self).write(cr,uid,ids,values,context=context)
		

rainsoft_product()


class rainsoft_catetory(osv.Model):
		_inherit="product.category"

		def name_search(self,cr,user,name='',args=None,operator="ilike",context=None,limit=100):
				res = []
				#import pudb
				#pudb.set_trace()
				limit = limit or 100
				if name:
						res_ids = self.search(cr,user,[('name','=',name)],limit=limit,context=context)
						new_limit = limit - len(res_ids)
						if new_limit:
								ids = self.search(cr,user,[('name',operator,name)],limit=new_limit,context=context)
								res_ids = list(set(res_ids+ids))
						new_limit = limit - len(res_ids)
						if new_limit:
								self.get_children_category(cr,user,res_ids,res,limit=new_limit,context=context)
								res = list(set(res))
								return self.name_get(cr,user,res,context=context)
				return super(rainsoft_catetory,self).name_search(cr,user,name=name,args=args,operator=operator,context=context,limit=limit)

		def get_children_category(self,cr,uid,ids,res,limit=100,context=None):
				for x_id in ids:
						children_ids =  self.search(cr,uid,[('parent_id','=',x_id)],limit=limit,context=context)
						new_limit = limit - len(children_ids)
						if new_limit:
								self.get_children_category(cr,uid,children_ids,res,new_limit,context=context)
						res.append(x_id)
