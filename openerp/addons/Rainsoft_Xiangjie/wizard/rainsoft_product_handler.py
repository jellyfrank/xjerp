#-*- coding:utf-8 -*-
##############################################################################
#
#    OpenERP, Designed For QingDao Xiangjie Company
#    Powered By Rainsoft(QingDao) Author:Kevin Kong 2014 (kfx2007@163.com)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
from openerp.osv import osv,fields
from openerp.tools.translate import _

class rainsoft_product_handler(osv.Model):
    _name='rainsoft.product.handler'

    _columns={
            'cost_method':fields.selection((('standard',u'标准'),('average',u'平均')),'Cost Method'),
            'valuation':fields.selection((('manual_periodic',u'手动'),('real_time',u'实时')),'Inventory Valuation'),
            }
    def btn_update(self,cr,uid,ids,context=None):
        if context==None:
            context={}
        products = self.pool.get('product.product').browse(cr,uid,context.get(('active_ids'),[]),context=context)
        for product in products:
            product.write({'cost_method':context.get(('cost_method'),'standard'),'valuation':context.get(('valuation'),'manual_periodic')})
