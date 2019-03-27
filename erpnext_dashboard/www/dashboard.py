'''
'''
import frappe

no_cache=True
def get_context(context):
	
	context.update({"background": ""})
	setting = frappe.get_doc("Dashboard Setting", "Dashboard Setting")
	if "theme" in context:
		context['theme']["background_image"] =  None

	context.update({"setting": setting.as_dict()})
