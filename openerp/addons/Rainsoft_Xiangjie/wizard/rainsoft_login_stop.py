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

class rainsoft_login_stop(osv.Model):
    _name='rainsoft.login.stop'

    _columns={
            'active':fields.boolean('Active'),
            }

    def btn_stop(self,cr,uid,ids,context=None):
        if context ==None:
            context={}
        users = self.pool.get('res.users').browse(cr,uid,context.get(('active_ids'),[]),context=context)
        for user in users:
            user.write({'active':context.get(('active'),False)})
