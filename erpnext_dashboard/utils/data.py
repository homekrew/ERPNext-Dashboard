'''
'''

import frappe
from dateutil import relativedelta
from frappe.utils import getdate
from six import string_types

def get_date_diff(start_date, end_date, frequency="months"):

	diff = 0
	if(frequency not in ["days", "months", "years"]):
		frappe.throw(_("Frequency should be in days or month or years"))

	if not(start_date or end_date):
		return  diff
	
	if isinstance(start_date, string_types):
		start_date = getdate(start_date)
	
	if isinstance(end_date, string_types):
		end_date = getdate(end_date)
	
	diff = relativedelta.relativedelta(start_date, end_date)
	return getattr(diff, frequency)

