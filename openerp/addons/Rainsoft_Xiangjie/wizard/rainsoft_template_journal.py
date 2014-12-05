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

class rainsoft_template_journal(osv.Model):
    _name='rainsoft.template.journal'

    def btn_create(self,cr,uid,ids,context=None):
        if context is None:
            context = {}
        move_ids = context.get(('active_ids'),[])
        stock_moves = self.pool.get('stock.move').browse(cr,uid,move_ids,context=context)
        for stock_move in stock_moves:
            if stock_move.origin.startswith('SO'):
                sale_order_id = self.pool.get('sale.order').search(cr,uid,[('name','=',stock_move.origin)],context=context)
                sale_order = self.pool.get('sale.order').browse(cr,uid,sale_order_id[0],context=context)
                account_move_ids = self.pool.get('account.move').search(cr,uid,[('ref','=',stock_move.origin)],context=context)
                account_moves = self.pool.get('account.move').browse(cr,uid,account_move_ids,context=context)
                for account_move in account_moves:
                    context.update({'journal_id':account_move.journal_id.id,'period_id':account_move.period_id.id})
                    name =  stock_move.product_id.name_get()[0][1]
                    self.pool.get('account.move.line').create(cr,uid,{
                        'move_id':account_move.id,
                        'name':name,
                        'partner_id':sale_order.partner_id.id,
                        'debit':stock_move.product_id.standard_price*stock_move.product_qty,
                        'credit':0.0,
                        'account_id':stock_move.product_id.categ_id.property_account_expense_categ.id,
                        },context=context)
                    self.pool.get('account.move.line').create(cr,uid,{
                        'move_id':account_move.id,
                        'name':name,
                        'partner_id':sale_order.partner_id.id,
                        'debit':0.0,
                        'credit':stock_move.product_id.standard_price*stock_move.product_qty,
                        'account_id':stock_move.product_id.categ_id.property_stock_account_output_categ.id,
                        },context=context)
