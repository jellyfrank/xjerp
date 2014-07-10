# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
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

import time
from report import report_sxw

class guarantee_route(report_sxw.rml_parse):      #解析类
    def __init__(self, cr, uid, name, context=None):
        super(guarantee_route, self).__init__(cr, uid, name, context=context)
        self.localcontext.update({
            'time': time,
            'helloworld':self.helloworld,
        })
        
    def helloworld(self):
	    return 'Hello World!!'

    def get_selection_item(obj, field, value=None):
        try:
            if isinstance(obj, report_sxw.browse_record_list):
                obj = obj[0]
            if isinstance(obj, (str,unicode)):
                model = obj
                field_val = value
            else:
                model = obj._table_name
                field_val = getattr(obj, field)
            if kind=='item':
                if field_val:
                    return dict(self.pool.get(model) \
                    .fields_get(self.cr, self.uid, allfields=[field], context=self.context)\
                    [field]['selection'])[field_val]
            elif kind=='items':
                return self.pool.get(model) \
                .fields_get(self.cr, self.uid, allfields=[field], context=self.context)\
                [field]['selection']
            return ''
        except Exception:
            return ''
        return get_selection_item


report_sxw.report_sxw('report.credit.sj.guarantee.route', 'credit.sj.guarantee.route',
                      'credit_sj_guarantee_route/credit_sj_guarantee_route_report.rml', parser=guarantee_route, header="external")

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: