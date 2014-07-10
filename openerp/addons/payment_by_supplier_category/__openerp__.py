# -*- coding: utf-8 -*-
##############################################################################
#
#    Payment by supplier category
#    Copyright (C) 2013-2014 Shine IT (http://www.openerp.cn)
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


{
    'name': 'Payment by supplier category',
    'version': '0.1',
    'category': 'Account',
    'description': """
        Payment by supplier category
....""",
    'author': 'Shine IT',
    'website': 'http://openerp.cn',
    'depends': ['account'],
    'data': [
        'partner_view.xml',
        'payment_view.xml',
    ],
    'demo': [],
    'test':[],
    'installable': True,
    'images': [],
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
