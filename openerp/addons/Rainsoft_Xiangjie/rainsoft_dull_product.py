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
from datetime import date,datetime
from dateutil.relativedelta import relativedelta

class rainsoft_dull_product(osv.Model):
    _name='rainsoft.dull.product'

    _columns={
            'month':fields.integer('Month')
            }

    def btn_analyse(self,cr,uid,ids,context=None):
        if context==None:
            context={}
        _month =date.today()+relativedelta(months=-context.get(('month'),0))
        move_ids = self.pool.get('stock.move').search(cr,uid,[('create_date','>=',str(_month))],context=context)
        product_ids =list(set([x.product_id.id for x in self.pool.get('stock.move').browse(cr,uid,move_ids,context=context) if x]))
        
        dull_pid = self.pool.get('product.product').search(cr,uid,[('id','not in',product_ids)],context=context)

        return {
                    'name':str(context.get('month'))+u'月内呆滞物品报表',
                    'res_model':'product.product',
                    'view_mode':'tree,form',
                    'view_type':'form',
                    'type':'ir.actions.act_window',
                    'domain':[('id','in',dull_pid)],
                }
