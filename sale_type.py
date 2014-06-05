from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
import time
from openerp import pooler
from openerp.osv import fields, osv
from openerp.tools.translate import _
from openerp.tools import DEFAULT_SERVER_DATE_FORMAT, DEFAULT_SERVER_DATETIME_FORMAT, DATETIME_FORMATS_MAP, float_compare
import openerp.addons.decimal_precision as dp
from openerp import netsvc
import logging
_logger=logging.getLogger(__name__)

class sale_order(osv.osv):
	TYPE=([
		('cash','Cash Sale'),
		('credit','Credit Sale'),
	])	
	
	_name='sale.order'
	_inherit='sale.order'
	_columns={
		'sale_type':fields.selection(TYPE,'Sale Types',help='Intends for different types of sale',required=True),
	
	}
sale_order()

class account_invoice(osv.osv):
	TYPE=([
		('cash','Cash Sale'),
		('credit','Credit Sale'),
	])	
	
	_name='account.invoice'
	_inherit='account.invoice'
	_columns={
		'sale_type':fields.selection(TYPE,'Sale Types',help='Intends for different types of sale',required=True),
	
	}
account_invoice()
