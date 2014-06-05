# -*- coding: utf-8 -*-
##############################################################################
#
#    Copyright (C) 2014 myatthu (<myatthu@myatthu-K43SJ>)
#    All Rights Reserved
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published
#    by the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
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
    'name': "Sale Types",
    'version': '1.0',
    'category': 'Sale Management',
    'description': """
			Ability to use cash sale and credit sale.
		""",
    'author': 'myatthu <myatthu@myatthu-K43SJ>',
    'website': '',
    'license': 'AGPL-3',
    "depends" : ['base','sale','account','sale_discountline'],
    "data" : ['sale_type_view.xml',],
    "demo" : [],
    "test" :[],
    "active": False,
    "installable": True
}
