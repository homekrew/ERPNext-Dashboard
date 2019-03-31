/*
	Developer Navdeep
	Email navdeep@blox.ae
*/

frappe.provide("erpnext_dashboard.dashboard");

erpnext_dashboard.dashboard.BaseDashboard = Class.extend({

	init: function(args){
		$.extend(this, args);
	},
	init_dashboard: function(){
		var me = this;
		this.make();
		this.make_filters();
	},
	make: function(){
		this.fields = [];
	},
	make_filters: function(){
		if(!this.filters_fields){
			return false;
		}
		var args = {
			"parent": $(".filters"),
			"filters_fields": this.filters_fields,
			"dashboard": this,
		};
		this.filters = new erpnext_dashboard.dashboard.Filters(args);
		this.refresh();
	},
	refresh: function(){
		// Backward compatibility
		// please write the same function in custom controller in custom dashboard file
	},
});

erpnext_dashboard.dashboard.Filters = Class.extend({

	init: function(args){
		$.extend(this, args);
		this.make();
	},
	make: function(){
		this.fields = {};
		this.values = {};
		this.make_filters();
	},
	make_filters: function(){
		
		var me  = this;
		for(var i=0; i<me.filters_fields.length; i++){
			var f = me.filters_fields[i];
			if(f.fieldtype == "Select"){
				this.fields[f.fieldname] = this.make_select_field(f);	
				this.init_handler(this.fields[f.fieldname], f);
			}
			else if(f.fieldtype == "Date"){
				this.fields[f.fieldname] = this.make_date_field(f);
				this.init_handler(this.fields[f.fieldname], f);
			}
		}
	},
	make_select_field: function(field){
		var $wrapper = $("<div class='input-field col s12'></div>").appendTo(this.parent);
		var $select = $("<select class="+field.fieldname+ "></select>").appendTo($wrapper);
		for(var i=0;i<field.options.length;i++){
			var option = field.options[i];
			$select.append($("<option>").attr("value", option).text(option));
		}
		$select.formSelect();
		return $select

	},
	make_date_field: function(field){
		var $wrapper = $("<div class='input-field col s12'></div>").appendTo(this.parent);
		var $date = $("<input>").appendTo($wrapper);
		$date.attr("class", "datepicker "+field.fieldname)
		$date.attr("type", "text");
		$date.datepicker();
		return $date
	},
	init_handler: function(f, field){

		var me = this;
		f.attr("data-fieldname", field.fieldname);
		this.values[field.fieldname] = f.val();
		f.on("change", function(event){
			event.preventDefault();
			me.values[$(this).attr("data-fieldname")] = $(this).val();
			me.dashboard.refresh();
		});	
	},
});

erpnext_dashboard.dashboard.DoughnutChart = Class.extend({

	init: function(args){
		$.extend(this, args);
		this.make_wrapper();
	},
	make_wrapper: function(args){
		this.parent.empty();
		this.wrapper_id = cstr(Math.random()).split(".")[1];
		this.$wrapper = $("<canvas style='width:500px; height:500px;'></canvas>").appendTo(this.parent);
		this.$wrapper.attr("id", this.wrapper_id);	

	},
	get_default_options: function(){
		return	{
			responsive: true,
			legend: {
				position: this.position || 'top',
			},
			title: {
				display: true,
				text: this.title || '',
			},
			animation: {
				animateScale: true,
				animateRotate: true
			}
		}
	},
	get_default_params: function(){

		return {
			"type": this.chart_type,
			"data":{
				"datasets":[],
				"labels": [],
			}
			
		}
	},
	render_data: function(){
		var params = this.get_default_params();
		params.options = this.get_default_options();

		var data = {
			"data": [],
			"backgroundColor": [],
			"label": "",
		};
		var me = this;
		for(var i=0;i<this.data.length; i++){
			var ele = this.data[i];
			data.data.push(ele[this.data_field]);
			params.data.labels.push(ele[this.label_field]);
			data.backgroundColor.push(ele.color);
		}
		params.data.datasets.push(data);
		console.log(params);
		ele = document.getElementById(this.wrapper_id).getContext('2d');
		this.chart = new Chart(ele, params);
	},
	destroy: function(){
		this.chart.destroy();
	}
})

