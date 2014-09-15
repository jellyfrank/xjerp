# -*- coding:utf-8 -*-
from openerp.osv import osv,fields
from openerp.tools.translate import _
import xlrd,base64

class rainsoft_product_import(osv.osv):
    _name='rainsoft.product.import'
    
    _columns={
            'file':fields.binary('xls file'),
            }

    def btn_import(self,cr,uid,ids,context=None):
        for wiz in self.browse(cr,uid,ids):
            if not wiz.file:continue

            excel = xlrd.open_workbook(file_contents=base64.decodestring(wiz.file))
            sheets = excel.sheets()
            for sh in sheets:
               # if sh.name==u"青岛工厂" or sh.name==u'哈尔滨工厂' or sh.name==u'济南工厂':
                    lines=[]
                    pro_id=0
                    for row in range(1,sh.nrows):
                        if sh.cell(row,1).value or sh.cell(row,17).value:
                            print sh.cell(row,1).value,sh.cell(row,17).value
                            if sh.cell(row,0).value:
                                cates = sh.cell(row,0).value.split('/')
                                cate=cates[len(cates)-1]
                                parent_cate = cates[len(cates)-2]
                                parent_cate_ids = self.pool.get('product.category').search(cr,uid,[('name','=',parent_cate)],context=context)
                                print parent_cate_ids
                                for parent_cate_id in parent_cate_ids:
                                    cate_ids = self.pool.get('product.category').search(cr,uid,[('name','=',cate),('parent_id','=',parent_cate_id)],context=context)
                                    print cate,parent_cate_id 
                                    print cate_ids
                                    if len(cate_ids):
                                        break

                            print cate_ids
                            if len(cate_ids):
                                goods_no = sh.cell(row,1).value
                                name = sh.cell(row,2).value
                                print name
                                if sh.cell(row,3).value=="Y":
                                    can_sale = True
                                else:
                                    can_sale = False

                                if sh.cell(row,4).value=="Y":
                                    can_purchase = True
                                else:
                                    can_purchase = False

                                stard_price = sh.cell(row,5).value
                                
                                if sh.cell(row,6).value==u"库存商品":
                                    product_type="product"
                                elif sh.cell(row,6).value==u"消耗品":
                                    product_type="consu"
                                else:
                                    product_type="service"
                                    
                                pro_uoms = self.pool.get('product.uom').search(cr,uid,[('name','=',sh.cell(row,7).value)],context=context)
                                print sh.cell(row,7).value
                                if not len(pro_uoms):
                                    raise osv.except_osv(_('Error!'),_('unit '+sh.cell(row,7).value+" doesn't exist"))
                                if sh.cell(row,8).value==u'按订单生产':
                                    product_method='make_to_order'
                                else:
                                    product_method='make_to_stock'

                                if sh.cell(row,9).value==u'购买':
                                    supplier_method='buy'
                                else:
                                    supplier_method='produce'

                                if sh.cell(row,10).value==u'标准价格':
                                    cost_method='standard'
                                else:
                                    cost_method='average'

                                #cost price
                                if sh.cell(row,11).value:
                                    cost_price = sh.cell(row,11).value
                                else:
                                    cost_price = 0.0
                                #prdocut manager

                                #follow produce
                                if sh.cell(row,13).value=="Y":
                                    follow_produce = True
                                else:
                                    follow_produce = False

                                #follow in stock
                                if sh.cell(row,14).value=="Y":
                                    follow_stock = True
                                else:
                                    follow_stock = False

                                #keep period
                                if sh.cell(row,15).value:
                                    keep_period = sh.cell(row,15).value

				#stock check
                                if sh.cell(row,16).value==u'实时':
                                    valuation='real_time'
                                else:
                                    valuation='manual_periodic'

                                #seller_ids
                                if sh.cell(row,17).value:
                                    suppliers = self.pool.get('res.partner').search(cr,uid,[('ref','=',sh.cell(row,17).value)],context=context)
                                    if len(suppliers):
                                        seller_id =suppliers[0]

                                min_count = sh.cell(row,18).value

                                send_period = sh.cell(row,19).value


                                line={
                                    'name':name,
                                    'categ_id':cate_ids[0],
                                    'sale_ok':can_sale,
                                    'purchase_ok':can_purchase,
                                    'list_price':stard_price,
                                    'type':product_type,
                                    'uom_id':pro_uoms[0],
                                    'uom_po_id':pro_uoms[0],
                                    'default_code':goods_no,
                                    'procure_method':product_method,
                                    'supply_method':supplier_method,
                                    'cost_method':cost_method,
                                    'standard_price':cost_price,
                                    'track_production':follow_produce,
                                    'track_incoming':follow_stock,
                                    'valuation':valuation,
                                    'warranty':keep_period,
                                    }

                                pro_id = self.pool.get('product.product').create(cr,uid,line,context=context)
                                if pro_id and sh.cell(row,17).value:
                                    supplierinfo={
                                            'product_id':pro_id,
                                            'name':seller_id,
                                            'min_qty':min_count or 0,
                                            'delay':send_period or 0,
                                            }
                                    self.pool.get('product.supplierinfo').create(cr,uid,supplierinfo,context=context)
                                cate_ids=[]
                            else:
                                #seller_ids
                                if sh.cell(row,17).value:
                                    suppliers = self.pool.get('res.partner').search(cr,uid,[('ref','=',sh.cell(row,17).value)],context=context)
                                    if len(suppliers):
                                        seller_id =suppliers[0]

                                #
                                if sh.cell(row,18).value:
                                    min_count = sh.cell(row,18).value

                                if sh.cell(row,19).value:
                                    send_period = sh.cell(row,19).value
                                if pro_id and sh.cell(row,17).value:
                                    supplierinfo={
                                            'product_id':pro_id,
                                            'name':seller_id,
                                            'min_qty':min_count or 0,
                                            'delay':send_period or 0,
                                            }
                                    self.pool.get('product.supplierinfo').create(cr,uid,supplierinfo,context=context)





rainsoft_product_import()

