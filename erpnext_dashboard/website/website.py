'''
'''
import frappe

def update_website_context(context):
	context.update({"web_include_css": []})
