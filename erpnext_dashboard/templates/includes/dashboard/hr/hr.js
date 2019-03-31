/*
	Developer Navdeep
	Email navdeep@blox.ae
*/

frappe.ready(function(){
	erpnext_dashboard.dashboard.HRDashboard = erpnext_dashboard.dashboard.BaseDashboard.extend({
		init: function(args){
			this._super(args);
			$.extend(this, args);
		},
		refresh: function(){
			this._super();
			const filters = this.filters.values;
			this.get_employee_by_departments(filters);
			this.get_absent_and_present(filters);
			this.get_birthday_list(filters);
			this.get_leave_applications(filters);
		},
		get_employee_by_departments: function(filters){
			var me = this;
			if(this.employee_by_departments){
				this.employee_by_departments.destroy();
			}
			frappe.call({
				"method": "erpnext_dashboard.www.hr.get_employee_by_departments",
				"args": filters,
				"callback": function(res){
					if(res && res.message){
						var args = {
							"data": res.message,
							"data_field": "total",
							"label_field": "department",
							"parent": $(".emp-by-departments"),
							"chart_type": "doughnut"
						};

						this.employee_by_departments = new erpnext_dashboard.dashboard.DoughnutChart(args);
						this.employee_by_departments.render_data();
					}
				}
			})
		},
		get_absent_and_present: function(filters){
			var me = this;
			$(".present-and-absent").empty();
			frappe.call({
				"method": "erpnext_dashboard.www.hr.get_absent_and_present",
				"args": filters,
				"callback": function(res){
					if(res && res.message){
						var $wrapper = $(".present-and-absent");
						for(var i=0;i<res.message.length; i++){
							var f = res.message[i];
							var $li = $("<li>").attr("class", "collection-item avatar").appendTo($wrapper);
							$("<img/>").attr("src", f.image||"").attr("class", "circle").appendTo($li);
							$("<p>").attr("class", "font-weight-600").text(f.employee_name).appendTo($li);
							$("<p>").attr("class", "medium-small").text(f.attendance_date).appendTo($li);

						}
					}
				}
			})
		},
		get_birthday_list: function(filters){
			var me = this;
			frappe.call({
				"method": "erpnext_dashboard.www.hr.get_birthday_list",
				"args": filters,
				"callback": function(res){
					console.log(res);
				}
			})	},
		get_leave_applications: function(filters){
			var me = this;
			frappe.call({
				"method": "erpnext_dashboard.www.hr.get_leave_applications",
				"args": filters,
				"callback": function(res){
					console.log(res);
				}
			})}
	});
	var dashboard = new erpnext_dashboard.dashboard.HRDashboard({"filters_fields": erpnext_dashboard.filters});	
	dashboard.init_dashboard();
});
