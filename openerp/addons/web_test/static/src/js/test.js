/*
 *OpenERP Web Development Test
 *Author: Kevin Kong
 * 
 **/
openerp.web_test = function(instance){
  
    var _t = instance.web._t,
	_lt = instance.web._lt;
    var QWeb = instance.web.qweb;
    var ikey,cssclass = '';
    
    instance.web.form.FieldChar.include({
	init:function(view,node){
	    this._super(view,node);
	    if(typeof node.attrs.check_mobile!="undefined"){
	      data = node.attrs.check_mobile.split('"');
	      ikey = data[1];
	      cssclass=data[3];
	    }
	}
    });
    
    instance.web.FormView.include({
	get_fields_values:function(){
	    var values = {};
	    var ids = this.get_selected_ids();
	    values["id"] = ids.length > 0 ? ids[0] : false;
	    _.each(this.fields, function(value_, key) {
		values[key] = value_.get_value();
	    });
	    
	    
	    var self = this;	    
	    //if there's already custorm css ,remove it.
	    var custorm_data = self.$el.find('.'+cssclass);
	    custorm_data.each(function(){
		console.log($(this).text())
		$(this).removeClass().addClass('oe_form_char_content');
		console.log($(this));
	    });
	    
	    var datas  = self.$el.find('.oe_form_char_content');
	    datas.each(function(){
		//console.log($(this).text());
		if($(this).text()==ikey){
		    $(this).addClass(cssclass);
		}
	    });
	    return values;
	}
    });
};