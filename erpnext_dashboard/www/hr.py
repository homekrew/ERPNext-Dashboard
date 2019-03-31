'''
'''
import frappe
from frappe import _, msgprint, throw
from frappe.utils import nowdate, nowtime, cint, flt
import json

no_cache=True

def get_context(context):
	
	filters = json.dumps(get_filters())
	print(filters)
	context.update({"filters": filters})
	

def get_filters():
	return[
			{
			"fieldname": "company",
			"fieldtype": "Select",
			"label": _("Company"),
			"class": "company",
			"options": [val.name for val in frappe.db.get_list("Company")]
		}	
	]

def get_company_condition(company, alias):
	cond = ""
	if company:
		cond += " and {0} = '{1}'".format(alias, company)
	return cond


@frappe.whitelist()
def get_employee_by_departments(company):
	return frappe.db.sql("""SELECT e.department, count(e.name) as total, d.color as color 
		from
			`tabEmployee` e inner join `tabDepartment` d 
		on 
			e.department=d.name where e.status='Active' %s 
		group by
			e.department """%(get_company_condition(company, "e.company")), as_dict=True)

@frappe.whitelist()
def get_absent_and_present(company):
	return frappe.db.sql("""SELECT a.status, e.employee_name, image, e.name, a.attendance_date 
		from 
			`tabAttendance` a inner join `tabEmployee` e on a.employee=e.name	
		where 
			a.docstatus=1 and a.attendance_date='%s'  %s 
		order by 
			status """%(nowdate(), get_company_condition(company, "a.company")), as_dict=True)


@frappe.whitelist()
def get_birthday_list(company):
	print(company)

@frappe.whitelist()
def get_leave_applications(company):
	print(company)

