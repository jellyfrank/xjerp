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

class rainsoft_vouchers(osv.Model):
		_name='rainsoft.vouchers'

		def view_init(self,cr,uid,field_list,context=None):
				if context is None:
						context={}
				record_id = context and context.get('active_id',False)
				print record_id


		def btn_post(self,cr,uid,ids,context=None):
				move_obj = self.pool.get('account.move')

				for move_id in move_obj.browse(cr,uid,context.get(('active_ids'),[]),context=context):
						if move_id.state !='draft':
								raise osv.except_osv(_('Warning!'),"You can't post a posted journal item!")
				move_obj.button_validate(cr,uid,context.get(('active_ids'),[]),context=context)
				
