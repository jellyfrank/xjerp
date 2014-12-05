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

class rainsoft_partner_update_credit(osv.Model):
    _name="rainsoft.partner.update.credit"

    _columns={
            'credit':fields.float('Credit',size=10),
            }
    
    def btn_update(self,cr,uid,ids,context=None):
        if context==None:
            context={}
        partners = self.pool.get('res.partner').browse(cr,uid,context.get(('active_ids'),[]),context=context)
        for partner in partners:
            partner.write({'credit_limit':context.get(('credit'),0)})
