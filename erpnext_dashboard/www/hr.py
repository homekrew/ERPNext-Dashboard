'''
'''
import frappe
from frappe import _, msgprint, throw
from frappe.utils import nowdate, nowtime, getdate, cint, flt, add_to_date
import json
from erpnext_dashboard.utils import update_random_colors, get_date_diff

no_cache=True

def get_context(context):
	
	filters = json.dumps(get_filters())
	context.update({"filters": filters})
	

def get_filters():
	return[
			{
			"fieldname": "company",
			"fieldtype": "Select",
			"label": _("Company"),
			"class": "company",
			"options": [""]+[val.name for val in frappe.db.get_list("Company")]
		}	
	]

def get_company_condition(company, alias):
	cond = ""
	if company:
		cond += " and {0} = '{1}'".format(alias, company)
	return cond


'''
	GET employee by deparments
'''
@frappe.whitelist()
def get_employee_by_departments(company):
	return update_random_colors(frappe.db.sql("""SELECT e.department, count(e.name) as total, d.color as color 
		from
			`tabEmployee` e inner join `tabDepartment` d 
		on 
			e.department=d.name where e.status='Active' %s 
		group by
			e.department """%(get_company_condition(company, "e.company")), as_dict=True))



'''
	GET list of employees who're absent today
'''
@frappe.whitelist()
def get_absent_and_present(company):
	results = frappe.db.sql("""SELECT e.employee_name as title, image, e.name, a.attendance_date  as sub_title,
			"work_off" as status
		from 
			`tabAttendance` a inner join `tabEmployee` e on a.employee=e.name	
		where 
			a.docstatus=1 and a.attendance_date='%s'  %s 
		order by 
			status limit 4"""%(nowdate(), get_company_condition(company, "a.company")), as_dict=True)

	template = frappe.get_template("templates/includes/dashboard/hr/html/list.html")
	data = []
	for res in results:
		data.append(template.render(res))
	return data


'''
	GET birthday list for all the employee for today's date
'''
@frappe.whitelist()
def get_birthday_list(company):
	results = frappe.db.sql(""" select e.employee_name as title, e.date_of_birth as sub_title, e.image, "event" as status
				from `tabEmployee` e
			
			where 
				e.status='Active' and month(e.date_of_birth)='%s' and day(e.date_of_birth)='%s' 
				%s """%(getdate(nowdate()).month, getdate(nowdate()).day,
					get_company_condition(company, "e.company")), as_dict=True)

	template = frappe.get_template("templates/includes/dashboard/hr/html/list.html")
	data = []
	for res in results:
		data.append(template.render(res))
	return data



'''
	GET last four pending leave applications
'''
@frappe.whitelist()
def get_leave_applications(company):
	
	leaves = frappe.db.sql("""SELECT l.name, l.employee_name, concat_ws(" - ", l.from_date, l.to_date) as date, 
			e.image, l.status, l.leave_type, l.leave_approver, l.description, e.designation,
			total_leave_days
		from 
			`tabLeave Application`  l inner join `tabEmployee` e on l.employee=e.name
		where 
			l.docstatus=0 and l.status not in ('Approved', 'Rejected') and l.from_date >= '%s' %s 
		order by
			l.total_leave_days DESC limit 4""" %(
			nowdate(), get_company_condition(company, "l.company")), as_dict=True)

	data = []
	template  = frappe.get_template("templates/includes/dashboard/hr/html/leave_application.html")
	for leave in leaves:
		data.append(template.render(leave))
	return data


'''
	GET no's of employees joined in past years
'''
@frappe.whitelist()
def get_employees_by_year(company):
	
	return update_random_colors(frappe.db.sql(""" select YEAR(e.date_of_joining) as year, count(e.name) as total 
		from 
			`tabEmployee`  e 
		where 
			status='Active' %s
		group by
			YEAR(e.date_of_joining)
		"""%(get_company_condition(company, "e.company")), as_dict=True))


'''
	GET no's of employees working in different locations
'''
@frappe.whitelist()
def get_work_locations(company):
	return update_random_colors(frappe.db.sql(""" select work_location, count(name) as total from `tabEmployee`
			where 
				status='Active' %s 
			group by
				work_location """%(get_company_condition(company, "company")), as_dict=True))


'''
	GET no's of employees for different age group
'''
@frappe.whitelist()
def get_employee_age_group(company):
	
	results = frappe.db.sql(""" select date_of_joining, date_of_birth from `tabEmployee`
		where
			status='Active' %s """%(get_company_condition(company, "company")), as_dict=True)

	data = [{"15-25":0},{"26-35": 0},{"36-50": 0},{"50+": 0}]

	now = nowdate()
	for res in results:
		diff = abs(get_date_diff(res.date_of_birth, now, "years"))
		if(diff >= 15 and diff <= 25):
			data[0]["15-25"] += 1
		elif(diff >= 26 and diff <= 35):
			data[1]["26-35"] += 1
		elif (diff >= 36 and diff <= 50):
			data[2]["36-50"] += 1
		elif (diff >= 51):
			data[3]["50+"] += 1
	results = []
	for item in data:
		for key, val in item.items():
			results.append({"age_group": key, "total": val})

	return update_random_colors(results)



'''
	Work anniversary for the employees
'''
@frappe.whitelist()
def get_employee_work_anniversary(company):
	
	now = getdate(nowdate())
	results = frappe.db.sql(""" select employee_name as title, designation as sub_title, image from `tabEmployee`
		where
			status = 'Active' and DAY(date_of_joining) = '%s' and 
			MONTH(date_of_joining) ='%s' and DATEDIFF('%s', date_of_joining) >= 365 %s 
		
		"""%(now.day, now.month, now, get_company_condition(company, "company")), as_dict=True)

	template = frappe.get_template("templates/includes/dashboard/hr/html/list.html")
	data = []
	for res in results:
		res.update({"status":""})
		data.append(template.render(res))
	return data


'''
	GET new joiners since last three months to today
'''
@frappe.whitelist()
def get_new_joinee(company):
	
	now = getdate(nowdate())
	after = add_to_date(now, months=-3)
	results = frappe.db.sql(""" select employee_name as title, date_of_joining as sub_title, image from `tabEmployee`
			where
			status = 'Active' and date_of_joining BETWEEN '%s' and '%s' 
			%s """%(after, now, get_company_condition(company, "company")), as_dict=True)
	
	template = frappe.get_template("templates/includes/dashboard/hr/html/list.html")
	data = []
	for res in results:
		res.update({"status":""})
		data.append(template.render(res))
	return data

