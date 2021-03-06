# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "erpnext_dashboard"
app_title = "Erpnext Dashboard"
app_publisher = "SGH"
app_description = "Analytical dashboard for ERPNext"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "navdeepghai1@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
#app_include_css = [
#	"/assets/css/dashboard-min.css"
#]
#app_include_js = [
#	"/assets/js/dashboard.min.js"
#]

#web_include_css = [
#	"/assets/css/web-dashboard.min.css"
#]

#web_include_js = [
#	"/assets/js/web-dashboard.min.js"
#]

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"
update_website_context = "erpnext_dashboard.website.website.update_website_context"
# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "erpnext_dashboard.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "erpnext_dashboard.install.before_install"
# after_install = "erpnext_dashboard.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "erpnext_dashboard.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"erpnext_dashboard.tasks.all"
# 	],
# 	"daily": [
# 		"erpnext_dashboard.tasks.daily"
# 	],
# 	"hourly": [
# 		"erpnext_dashboard.tasks.hourly"
# 	],
# 	"weekly": [
# 		"erpnext_dashboard.tasks.weekly"
# 	]
# 	"monthly": [
# 		"erpnext_dashboard.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "erpnext_dashboard.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "erpnext_dashboard.event.get_events"
# }

