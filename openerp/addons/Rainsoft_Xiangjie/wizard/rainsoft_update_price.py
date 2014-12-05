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

class rainsoft_update_price(osv.Model):
    _name='rainsoft.update.price'

    _columns={
            'period':fields.many2one('account.period',string='Period')
            }

    def btn_update(self,cr,uid,ids,context=None):
        if context is None:
            context={}
        period = context.get(('period'),False)
        carryovers = self.pool.get('rainsoft.account.carryover').search(cr,uid,[('period','=',period)],context=None)
        products = self.pool.get('product.product').browse(cr,uid,context.get(('active_ids'),[]),context=None)
        for product in products:
            c_lines = self.pool.get('rainsoft.account.carryover.line').search(cr,uid,[('carryover_id','=',carryovers[0]),('product_id','=',product.id)])
            line = self.pool.get('rainsoft.account.carryover.line').browse(cr,uid,c_lines[0],context=context)
            product.write({'standard_price':line.average_price})
            


    
