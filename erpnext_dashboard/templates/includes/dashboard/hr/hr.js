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
			this.get_employees_by_year(filters);
			this.get_work_locations(filters);
			this.get_employee_age_group(filters);
			this.get_employee_work_anniversary(filters);
			this.get_new_joinee(filters);
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
							"chart_type": "doughnut",
							"height": "300"
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
							$(res.message[i]).appendTo($wrapper);
						}
					}
				}
			})
		},
		get_birthday_list: function(filters){
			var me = this;
			$(".birthday-list").empty();
			frappe.call({
				"method": "erpnext_dashboard.www.hr.get_birthday_list",
				"args": filters,
				"callback": function(res){
					if(res && res.message){
						var $wrapper = $(".birthday-list");
						for(var i=0;i<res.message.length; i++){
							$(res.message[i]).appendTo($wrapper);
						}
							
					}
				}
			})	
		},
		get_leave_applications: function(filters){
			var me = this;
			$(".leave-applications").empty();
			frappe.call({
				"method": "erpnext_dashboard.www.hr.get_leave_applications",
				"args": filters,
				"callback": function(res){
					if(res && res.message){
						var $wrapper = $(".leave-applications");
						for(var i=0;i<res.message.length; i++){
							$(res.message[i]).appendTo($wrapper);
						}	
					}
				}
			})
		},
		get_employees_by_year: function(filters){
			if(this.employees_by_year){
				this.employees_by_year.distroy()
			}
			frappe.call({
				"method": "erpnext_dashboard.www.hr.get_employees_by_year",
				"args": filters,
				"callback": function(res){
					if(res && res.message){
						console.log(res.message);
						var args = {
							"data": res.message,
							"data_field": "total",
							"label_field": "year",
							"parent": $(".employees-by-year"),
							"chart_type": "bar",
							"height": "130"
						};
						this.employees_by_years = new erpnext_dashboard.dashboard.BarChart(args);
						this.employees_by_years.render_data();
					}
				}
			});
		},
		get_work_locations: function(filters){
			if(this.work_locations){
				this.work_locations.distroy()
			}
			frappe.call({
				"method": "erpnext_dashboard.www.hr.get_work_locations",
				"args": filters,
				"callback": function(res){
					if(res && res.message){
						console.log(res.message);
						var args = {
							"data": res.message,
							"data_field": "total",
							"label_field": "work_location",
							"parent": $(".work-locations"),
							"chart_type": "pie",
							"height": "130",
						
						};
						this.work_locations = new erpnext_dashboard.dashboard.DoughnutChart(args);
						this.work_locations.render_data();
					}
				}
			});

		},
		get_employee_age_group: function(filters){
			if(this.age_group){
				this.age_group.distroy()
			}
			frappe.call({
				"method": "erpnext_dashboard.www.hr.get_employee_age_group",
				"args": filters,
				"callback": function(res){
					if(res && res.message){
						console.log(res.message);
						var args = {
							"data": res.message,
							"data_field": "total",
							"label_field": "age_group",
							"parent": $(".age-group"),
							"chart_type": "bar",
							"height": "300",
						
						};
						this.age_group = new erpnext_dashboard.dashboard.BarChart(args);
						this.age_group.render_data();
					}
				}
			});
			
		},
		get_employee_work_anniversary: function(filters){
			var me = this;
			$(".employee-work-anniversary").empty();
			frappe.call({
				"method": "erpnext_dashboard.www.hr.get_employee_work_anniversary",
				"args": filters,
				"callback": function(res){
					if(res && res.message){
						var $wrapper = $(".employee-work-anniversary");
						for(var i=0;i<res.message.length; i++){
							$(res.message[i]).appendTo($wrapper);
						}	
					}
				}
			})
		},
		get_new_joinee: function(filters){
			var me = this;
			$(".new-joinee").empty();
			frappe.call({
				"method": "erpnext_dashboard.www.hr.get_new_joinee",
				"args": filters,
				"callback": function(res){
					if(res && res.message){
						var $wrapper = $(".new-joinee");
						for(var i=0;i<res.message.length; i++){
							$(res.message[i]).appendTo($wrapper);
						}	
					}
				}
			})
		},
	});
	var dashboard = new erpnext_dashboard.dashboard.HRDashboard({"filters_fields": erpnext_dashboard.filters});	
	dashboard.init_dashboard();
})
