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
import datetime

class rainsoft_supplier_contract(osv.Model):
		_inherit='account.analytic.account'

		_columns={
						'contract_type':fields.selection([('temp',u'临时合同'),('long',u'长期合同')],'Contract Type',required=True),
						}

		def run_check(self,cr,uid,ids,context=None):
				ids = self.search(cr,uid,[]);
				contracts = self.browse(cr,uid,ids);
				for contract in contracts:
                                    if contract.state in ('open','pending') and contract.date:
                                        if datetime.datetime.strptime(contract.date,'%Y-%m-%d')-datetime.datetime.now()<datetime.timedelta(days=20):
                                            contract.write({'state':'pending'});
                                        else:
                                            contract.write({'state':'open'});
