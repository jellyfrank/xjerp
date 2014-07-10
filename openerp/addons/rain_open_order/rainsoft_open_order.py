# -*- coding: utf-8 -*-

from openerp.tools.translate import _
from openerp.osv import fields, osv
import openerp.addons.decimal_precision as dp


class rainsoft_open_order(osv.osv):
    _name = "rainsoft.open.order"

    _columns = {
        'from_date': fields.date(u'开始时间'),
        'to_date': fields.date(u'结束时间'),
        'preight_product_id': fields.many2one('product.product', u'运费产品'),
    }

    def action_query(self, cr, uid, ids, context=None):
        if context is None:
            context = {}

        from_date = self.browse(cr, uid, ids[0]).from_date
        to_date = self.browse(cr, uid, ids[0]).to_date
        preight_product_id = self.browse(cr, uid, ids[0]).preight_product_id.id

        # 筛选所有店铺
        # partners = self.pool.get('res.partner').search(cr, uid, [], context=context)

        #清空表
        rainsoft_open_orders = self.pool.get('rainsoft.open.order.line').search(cr, uid, [], context=context)
        self.unlink(cr, uid, rainsoft_open_orders)
        #获取这段时间的 客户
        sale_orders = self.pool.get('sale.order').search(cr, uid, [('date_confirm', '>=', from_date),
                                                                   ('date_confirm', '<', to_date),
                                                                ('state', '=', 'done'), ],
                                                         context=context)
        for sale_order in sale_orders:
            obj_order = self.pool.get('sale.order').browse(cr, uid, sale_order, context=context)
            if len(self.pool.get('rainsoft.open.order.line').search(cr, uid,
                                                                    [('partner_id', '=', obj_order.partner_id.id)],
                                                                    context=context)) == 0:
                self.pool.get('rainsoft.open.order.line').create(cr, uid, {'partner_id': obj_order.partner_id.id},
                                                                 context=context)

        return {
            'name': u'开业订单一览表' + '(' + from_date + u'到' + to_date + ')',
            'view_type': 'form',
            'view_mode': 'tree, form',
            'res_model': 'rainsoft.open.order.line',
            'type': 'ir.actions.act_window',
            'context': {
                'from_date': from_date,
                'to_date': to_date,
                'preight_product_id': preight_product_id,
            },
            'limit': 10000,
        }


rainsoft_open_order()


class rainsoft_open_order_line(osv.osv):
    """
        开业订单栏目表
    """
    _name = 'rainsoft.open.order.line'

    def _amount_all(self, cr, uid, ids, field_name, arg, context=None):
        res = {}
        if context.has_key('from_date') and context.has_key('to_date'):
            from_date = context['from_date']
            to_date = context['to_date']
            preight_product_id = context['preight_product_id']

            lines = self.browse(cr, uid, ids)

            for line in lines:
                res[line.id] = {
                    'order_amount': 0.0,
                    'cost_amount': 0.0,
                    'preight_amount': 0.0,
                    'profit': 0.0
                }
                sale_orders = self.pool.get('sale.order').search(cr, uid, [('partner_id', '=', line.partner_id.id),
                                                                           ('date_confirm', '>=', from_date),
                                                                           ('date_confirm', '<', to_date),
                                                                            ('state', '=', 'done'), ],
                                                                 context=context)
                if len(sale_orders) > 0:
                    for order in sale_orders:
                        obj_order = self.pool.get('sale.order').browse(cr, uid, order, context=context)
                        for order_line in obj_order.order_line:
                            if obj_order.amount_total > 0.0:
                                # 订单金额 只在 amount_total > 0 时计算。小于0时，可能是运费或者其他费用
                                res[line.id]['order_amount'] += obj_order.amount_total
                                # 成本，只计算 amount_total > 0 ，
                                res[line.id]['cost_amount'] += order_line.purchase_price * order_line.product_uom_qty
                            # 运费 (营业运输费,只有在运费产品中才会统计,取绝对值）
                            if order_line.product_id.id == preight_product_id:
                                res[line.id]['preight_amount'] += abs(obj_order.amount_total)

                    res[line.id]['profit'] = res[line.id]['order_amount'] - res[line.id]['cost_amount'] - res[line.id]['preight_amount']

        return res



    _columns = {
        'partner_id': fields.many2one('res.partner', 'Customer'),
        'brand': fields.related('partner_id', 'brand', type='many2one', relation='rainsoft.brand', string='brand', store=True),
        # store=True 为了 搜索分组 否则不允许分组
        #'brand': fields.related('partner_id', 'country_id', type='many2one', relation='res.country', string='brand', store=True),
        'state_id': fields.related('partner_id', 'state_id', type='many2one', relation='res.country.state',store=True,
                                   string='State'),
        'order_amount': fields.function(_amount_all, multi='sums', digits_compute=dp.get_precision('Account'),
                                        method=True, type='float',
                                        string='Order Amount'),
        'cost_amount': fields.function(_amount_all, multi='sums', digits_compute=dp.get_precision('Account'),
                                       method=True, type='float',
                                       string='Cost Amount'),
        'preight_amount': fields.function(_amount_all, multi='sums', digits_compute=dp.get_precision('Account'),
                                          method=True, type='float',
                                          string='Preight  Amount'),
        'profit': fields.function(_amount_all, multi='sums', digits_compute=dp.get_precision('Account'),
                                  method=True, type='float',
                                  string='Preight  Amount'),
    }


rainsoft_open_order_line()