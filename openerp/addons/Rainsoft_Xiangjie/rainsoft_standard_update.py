#coding:utf-8

from openerp.osv import osv,fields
from openerp.tools.translate import _
import xlrd,base64

class rainsoft_standard_update(osv.Model):
    _name="rainsoft.standard.update"

    _columns={
            'data':fields.binary('File')
            }

    def btn_import(self,cr,uid,ids,context=None):
        for wiz in self.browse(cr,uid,ids):
            if not wiz.data:continue
        excel = xlrd.open_workbook(file_contents=base64.decodestring(wiz.data))
        sheets = excel.sheets()
        for sh in sheets:
            for row in range(2,sh.nrows):
                product_No = str(sh.cell(row,0).value).split('.')[0]
                print product_No
                product_id = self.pool.get('product.product').search(cr,uid,[('default_code','=',product_No)],context=context)
                products = self.pool.get('product.product').browse(cr,uid,product_id,context=context)
                for product in products:
						product.write({'standard_price':sh.cell(row,8).value})
                                                print sh.cell(row,8).value
                


        
