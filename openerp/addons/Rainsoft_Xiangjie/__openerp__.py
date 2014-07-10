#-*- coding:utf-8 -*-
##############################################################################
#
#    OpenERP, Designed For QingDao Xiangjie Company
#    Powered By Rainsoft(QingDao) Author:Kevin Kong 2014 (kfx2007@163.com)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
		"name":u"青岛香界贸易有限公司专用模块",
		"version":"1.0",
		"description":u"""
青岛香界贸易有限公司专用模块
================================================================
该模块为青岛香界商贸有限公司专用模块，由雨水软件根据香界商贸有限公司特定的业务需求量身定做。
改模块包括的业务功能主要有：

* 联系人添加一些自定义字段，如QQ等
* 添加对合作伙伴的唯一性限制
* 添加短信平台接口，提供在特定业务处给客户发短信的功能
* 销售模块添加按营建模板导入功能
* 销售订单确认时添加验证客户的预付款及信用额度验证
* 合作伙伴的联系地址更改为更符合中国国情的排列方式，并详细到县级
* 报价单添加预付款金额和信用额度的限制
* 仓库添加销售和送货对比单
* 仓库添加货架管理功能，并在盘点时提供按货架过滤
* 仓库内部调拨自动加载选中的仓库内的产品
* 若干其他视图及页面功能的优化
* 部分也面去掉创建并编辑功能

更多详情及参见使用说明或联系雨水软件事业部。
------------------------
版权 雨水软件 2014
作者：Kevin Kong
		  """,
		"author":"rainsoft",
		"website":"http://www.qdrainsoft.com",
		"depends":["base","product","purchase","sale","stock","crm"],
		"update_xml":["rainsoft_partner_view.xml","rainsoft_product_view.xml","rainsoft_sale_view.xml","rainsoft_product_model_view.xml","rainsoft_myproduct_view.xml","rainsoft_internal_move_view.xml","rainsoft_sms_view.xml","rainsoft_city_view.xml","rainsoft_stock_picking_out_view.xml","rainsoft_crm_lead_view.xml","rainsoft_purchase_order_view.xml","rainsoft_fill_inventory_view.xml","rainsoft_stock_picking_in_view.xml","rainsoft_rack_view.xml","rainsoft_sale_out_order_view.xml","report/rainsoft_saleout_report.xml","res_config_view.xml","rainsoft_workflow.xml","rainsoft_account_stock_view.xml","security/rainsoft_security.xml","rainsoft_stock_inventory_view.xml","rainsoft_partner_forbidden_view.xml","rainsoft_account_invoice_view.xml","rainsoft_brand_view.xml","rainsoft_account_voucher_view.xml","rainsoft_stock_view.xml","rainsoft_stock_invoice_onshipping_view.xml","rainsoft_sale_stock_view.xml","rainsoft_account_report_partner_balance_view.xml","rainsoft_account_report_partner_ledger_view.xml"],
		"js":['static/src/js/test.js'],
		"installable":True,
		"category":"Generic Modules/Others"
}
