# -*- coding: utf-8 -*-
##############################################################################
# Guarantee Request name for OpenERP
# Copyright (C) 2014 Jinan Shangjie Technology CO.,LTD. (<http://www.jnshangjie.com/>).
##############################################################################

from datetime import datetime
from dateutil.relativedelta import relativedelta
from openerp.osv import fields, osv
import openerp.addons.decimal_precision as dp
import time
from openerp.tools.translate import _
import datetime
import simplejson

try:
    from openerp import SUPERUSER_ID
except ImportError:
    SUPERUSER_ID = SUPERUSER_ID


class credit_sj_guarantee_application(osv.Model):
    _name = "credit.sj.guarantee.application"
    _description = "credit.sj.guarantee.applicationt"
    _order = 'route_line desc, name desc'

    _columns = {
        'name': fields.char(u'核保编号', size=12, readonly=True, required=True),
        'company_name': fields.char(u'经营单位名称', size=64, required=True),
        'customer_city': fields.many2one('sj.city', u'客户地市'),
        'customer_property': fields.selection([('nationalized', u'国有'),
                                               ('private', u'民营'), ],
                                              u'客户性质', ),
        'submit_time': fields.datetime(u'提交时间', readonly=True),
        'main_manager': fields.many2one('res.users', u'主办客户经理', required=True),
        'main_phone': fields.char(u'主办客户经理手机', size=20, required=True),
        'assist_manager': fields.many2one('res.users', u'协办客户经理', required=True),
        'assist_phone': fields.char(u'协办客户经理手机', size=20, required=True),
        'operator_manager': fields.many2one('res.users', u'核保经办客户经理'),
        'operator_phone': fields.char(u'核保经办客户经理手机', size=20),
        'credit_customer_name': fields.char(u'授信客户名称', size=20, required=True),
        'customer_credit_rating': fields.char(u'客户信用评级', size=20),
        'credit_approval_date': fields.date(u'授信批复日期', required=True),
        'approval_no': fields.char(u'批复号', size=20, required=True),
        'line_of_credit': fields.float(u'授信额度', required=True),
        'credit_business_type': fields.selection([('loan', u'贷款'),
                                                  ('guarantee', u'担保'),
                                                  ('pledge', u'质押'),
                                                  ('hypothecate', u'抵押'), ],
                                                 u'授信业务种类', required=True),
        'credit_money': fields.float(u'本笔授信额度'),
        'credit_scale_start_date': fields.date(u'授信规模起始日期', required=True),
        'plan_guarantee_date': fields.date(u'计划核保日期', required=True),
        'plan_lend_date': fields.date(u'计划放款日期', required=True),
        'guarantor1_name': fields.char(u'担保人1名称', size=20, required=True),
        'guarantor1_guarantee_amount': fields.float(u'担保金额'),
        'guarantor1_city': fields.many2one('sj.city', u'地市', required=True),
        'guarantor1_county': fields.many2one('sj.county', u'区县', required=True),
        'address': fields.char(u'具体地址', size=128, required=True),
        'guarantor1_guarantee_way': fields.selection([('hypothecate', u'抵押'),
                                                      ('assure', u'保证'),
                                                      ('pledge', u'质押'),
                                                      ('natural_guarantee', u'自然人担保'),
                                                      ('other', u'其他'), ],
                                                     u'担保方式', required=True),
        'guarantor1_guaranty': fields.char(u'抵制物名称', size=128),
        'guarantor2_name': fields.char(u'担保人2名称', size=20),
        'guarantor2_guarantee_amount': fields.float(u'担保金额'),
        'guarantor2_city': fields.many2one('sj.city', u'地市'),
        'guarantor2_county': fields.many2one('sj.county', u'区县'),
        'guarantor2_guarantee_way': fields.selection([('hypothecate', u'抵押'),
                                                      ('assure', u'保证'),
                                                      ('pledge', u'质押'),
                                                      ('natural_guarantee', u'自然人担保'),
                                                      ('other', u'其他'), ],
                                                     u'担保方式', ),
        'guarantor2_guaranty': fields.char(u'抵制物名称', size=128),
        'guarantor3_name': fields.char(u'担保人3名称', size=20),
        'guarantor3_guarantee_amount': fields.float(u'担保金额'),
        'guarantor3_city': fields.many2one('sj.city', u'地市'),
        'guarantor3_county': fields.many2one('sj.county', u'区县'),
        'guarantor3_guarantee_way': fields.selection([('hypothecate', u'抵押'),
                                                      ('assure', u'保证'),
                                                      ('pledge', u'质押'),
                                                      ('natural_guarantee', u'自然人担保'),
                                                      ('other', u'其他'), ],
                                                     u'担保方式', ),
        'guarantor3_guaranty': fields.char(u'抵制物名称', size=128),
        'guarantor4_name': fields.char(u'担保人4名称', size=20),
        'guarantor4_guarantee_amount': fields.float(u'担保金额'),
        'guarantor4_city': fields.many2one('sj.city', u'地市'),
        'guarantor4_county': fields.many2one('sj.county', u'区县'),
        'guarantor4_guarantee_way': fields.selection([('hypothecate', u'抵押'),
                                                      ('assure', u'保证'),
                                                      ('pledge', u'质押'),
                                                      ('natural_guarantee', u'自然人担保'),
                                                      ('other', u'其他'), ],
                                                     u'担保方式', ),
        'guarantor4_guaranty': fields.char(u'抵制物名称', size=128),
        'guarantor5_name': fields.char(u'担保人5名称', size=20),
        'guarantor5_guarantee_amount': fields.float(u'担保金额'),
        'guarantor5_city': fields.many2one('sj.city', u'地市'),
        'guarantor5_county': fields.many2one('sj.county', u'区县'),
        'guarantor5_guarantee_way': fields.selection([('hypothecate', u'抵押'),
                                                      ('assure', u'保证'),
                                                      ('pledge', u'质押'),
                                                      ('natural_guarantee', u'自然人担保'),
                                                      ('other', u'其他'), ],
                                                     u'担保方式', ),
        'guarantor5_guaranty': fields.char(u'抵制物名称', size=128),
        'credit_approval_filename': fields.char(u'上传授信批复文件名', invisible='1'),
        'credit_approval': fields.binary(u'上传授信批复', required=True),
        'credit_report_filename': fields.char(u'上传授信调查报告文件名', invisible='1'),
        'credit_report': fields.binary(u'上传授信调查报告', required=True),
        'guarantee_user': fields.many2one('res.users', u'核保专员', readonly=True),
        'guarantee_result': fields.selection([(u'成功', u'成功'),
                                              (u'失败', u'失败'), ],
                                             u'核保结果', ),
        'state': fields.selection([('draft', u'草稿'),
                                   ('submit', u'已提交'),
                                   ('wait_officer', u'待分配专员'),
                                   ('get_office', u'已分配专员'),
                                   ('done', u'审核完成'),
                                   ('return', u'退回'), ],
                                  u'审核状态', ),
        'guarantee_result_note': fields.text(u'核保备注'),
        'note': fields.text(u'备注（填写）', required=True),
        'route_line': fields.many2one('credit.sj.guarantee.route', u'路线'),
        'destination': fields.related("route_line", "destination", type="char", string=u"目的地", readonly=True, ),
    }

    _defaults = {
        'name': lambda obj, cr, uid, context: '/',
        'state': lambda *a: 'draft',
        'main_manager': lambda self, cr, uid, context: uid,
    }

    def btn_review(self, cr, uid, ids, context=None):
        """
            提交审核按钮，改变状态及提交时间
        """
        state = 'submit'
        submit_time = time.strftime("%Y-%m-%d %H:%M:%S")
        self.write(cr, uid, ids, {'state': state, 'submit_time': submit_time}, context=context)
        return True

    def calculate_route(self, cr, uid, context=None):
        """
            计算并生成路线
        """
        # 查询出所有满足条件的核保单
        route_dic = {}   # 存放的路线信息字典 { (目的地，计划核保日期，授信规模起始日期，路线编号) : {核保申请单id:[id],计数num:数量} }
        # 查询状态是 '已提交'(review) 的核保申请单信息
        ids = self.search(cr, uid, [('state', '=', 'submit')], context=context)
        all_requisitions = self.browse(cr, uid, ids)
        # 获取系统设定参数（核保路线中申请单的上限）
        request_number = self.pool.get('ir.config_parameter').get_param(cr, uid,
                                                                        'credit_sj_guarantee_application.auto_line')
        int_number = int(request_number)
        # 组织核保路线字典
        route_id = ''
        for res in all_requisitions:
            destination = res.guarantor1_city.name + res.guarantor1_county.name
            if (destination, res.plan_guarantee_date, res.credit_scale_start_date, route_id) not in route_dic:
                route_id = self.pool.get('ir.sequence').get(cr, uid,
                                                            'credit.sj.guarantee.route')  # 生成路线编号，例：201405190007
                county_code = res.guarantor1_county.code   # 地市区号
                route_id = route_id[0:8] + county_code + route_id[8:]
                # 结构：{ (目的地，计划核保日期，授信规模起始日期，路线编号) : {核保申请单id:[id],计数num:数量} }
                route_dic[(destination, res.plan_guarantee_date, res.credit_scale_start_date, route_id)] = {
                    'ids': [res.id], 'num': 1}
            else:
                # 获取核保路线中的核保申请单个数
                number = route_dic[(destination, res.plan_guarantee_date, res.credit_scale_start_date, route_id)].get(
                    'num')
                # 路线中申请单个数等于上限个数时，重新生成一条路线
                if number == int_number:
                    route_id = self.pool.get('ir.sequence').get(cr, uid, 'credit.sj.guarantee.route')
                    county_code = res.guarantor1_county.code
                    route_id = route_id[0:8] + county_code + route_id[8:]
                    route_dic[(destination, res.plan_guarantee_date, res.credit_scale_start_date, route_id)] = {
                        'ids': [res.id], 'num': 1}
                else:
                    # 追加核保申请单id
                    route_dic[(destination, res.plan_guarantee_date, res.credit_scale_start_date, route_id)][
                        'ids'].append(res.id)
                    # 更新核保申请单个数
                    route_dic[(destination, res.plan_guarantee_date, res.credit_scale_start_date, route_id)][
                        'num'] = number + 1
        creat_route(self, cr, uid, ids, route_dic)
        return True

    def create(self, cr, uid, vals, context=None):
        """
            核保编号自动生成、校验计划放款日期必须大于计划核保日期
        """
        if vals.get('name', '/') == '/':
            vals['name'] = self.pool.get('ir.sequence').get(cr, uid, 'credit.sj.guarantee.application') or '/'
            vals['name'] = vals['name'].replace('/', '')
        plan_guarantee_date = vals.get('plan_guarantee_date')
        plan_lend_date = vals.get('plan_lend_date')
        if plan_guarantee_date and plan_lend_date and plan_guarantee_date > plan_lend_date:
            raise osv.except_osv(_(u'提醒'), _(u'计划放款日期必须大于计划核保日期！'))
        return super(credit_sj_guarantee_application, self).create(cr, uid, vals, context=context)

    def write(self, cr, uid, ids, vals, context=None):
        instructors = self.browse(cr, uid, ids)
        for obj in instructors:
            plan_guarantee_date = vals.get('plan_guarantee_date', '') if vals.get('plan_guarantee_date','') else obj.plan_guarantee_date
            plan_lend_date = vals.get('plan_lend_date', '') if vals.get('plan_lend_date', '') else obj.plan_lend_date
        if plan_guarantee_date and plan_lend_date and plan_guarantee_date > plan_lend_date:
            raise osv.except_osv(_(u'提醒'), _(u'计划放款日期必须大于计划核保日期！'))
        result = super(credit_sj_guarantee_application, self).write(cr, uid, ids, vals, context=context)
        return result


    def unlink(self, cr, uid, ids, context=None):
        """
            删除时校验核保单状态
        """
        rec = self.read(cr, uid, ids, ['state'], context=context)
        for lst in rec:
            state = lst.get('state')
            if state not in ('draft', 'return'):
                raise osv.except_osv(_(u'提醒'), _(u'只能删除草稿或退回的核保单！'))
        return super(credit_sj_guarantee_application, self).unlink(cr, uid, ids, context)


    def btn_done(self, cr, uid, ids, context=None):
        """
            提交完成
            校验核保结果是否为空，核保结果为失败时校验核保备注不为空
        """
        # 校验核保结果不为空
        for rec in self.browse(cr, uid, ids, context=context):
            if not rec.guarantee_result:
                raise osv.except_osv(_(u'提醒'), _(u'核保结果不能为空'))
            elif rec.guarantee_result == u'失败' and not rec.guarantee_result_note:
                raise osv.except_osv(_(u'提醒'), _(u'核保备注不能为空'))
                # 查询核保单所对应的路线id
        rec = self.read(cr, uid, ids, ['route_line'], context=context)
        route_id = rec[0].get('route_line')[0]
        # 从路线对象池中取出对象
        route_model = self.pool.get('credit.sj.guarantee.route')
        # 通过路线id查询出此路线信息
        route_information = route_model.read(cr, uid, [route_id],
                                             ['guarante_total_number', 'guarante_complete_number'],
                                             context=context)
        guarante_total_number = route_information[0].get('guarante_total_number')
        guarante_complete_number = route_information[0].get('guarante_complete_number')
        # 需要更新路线的字典
        route_dic = {}
        # 计数
        guarante_complete_number += 1
        route_dic['guarante_complete_number'] = guarante_complete_number
        # 修改此核保路线状态
        if guarante_complete_number == guarante_total_number:
            route_dic['state'] = 'done'
        route_model.write(cr, uid, [route_id], route_dic, context=context)
        # 修改核保单状态
        self.write(cr, uid, ids, {'state': 'done'}, context=context)
        return True


    def onchange_city_county(self, cr, uid, ids, guarantor1_city, county, context=None):
        """
            地市、区县联动
        """
        res = {}
        if guarantor1_city:
            res[county] = ''
        return {'value': res}


    def btn_return(self, cr, uid, ids, context=None):
        """
            退回申请单
        """
        # 查询核保单所对应的所有的路线id
        rec = self.read(cr, uid, ids, ['route_line','state'], context=context)
        #判断核保单状态
        request_state=rec[0].get("state")
        if request_state=='get_office':
            route_id = rec[0].get('route_line')[0]
            # 从路线对象池中取出所有对象
            route_model = self.pool.get('credit.sj.guarantee.route')
            # 通过路线id查询出路线信息（每条路线对应的核保单数量）
            route_information = route_model.read(cr, uid, [route_id],
                                                 ['guarante_total_number', 'guarante_complete_number'],
                                                 context=context)
            guarante_total_number = route_information[0].get('guarante_total_number')
            guarante_complete_number = route_information[0].get('guarante_complete_number')
            # 需要更新路线的字典
            route_dic = {}
            #判断路线下面的核保单数是不是最后一条。
            if guarante_total_number == 1:
                # 是最后一条，则删除此条路线
                route_model.write(cr, uid, [route_id], {'guarante_total_number': 0}, context=context)
                route_model.unlink(cr, uid, [route_id])
            else:
                # 不是最后一条，则此条路线下面的核保单数减去1
                guarante_total_number -= 1
                route_dic['guarante_total_number'] = guarante_total_number
                if guarante_complete_number == guarante_total_number:
                    route_dic['state'] = 'done'
                route_model.write(cr, uid, [route_id], route_dic, context=context)
                # 修改状态
            state = 'return'
            self.write(cr, uid, ids,
                       {'state': state, 'guarantee_user': False, 'guarantee_result': False, 'guarantee_result_note': False,
                        'route_line': False},
                       context=context)
            # 指定跳转action
            form_ids = self.pool.get('ir.model.data').search(cr, uid, [('model', '=', 'ir.ui.view'),
                                                                       ('name', '=', 'view_form_credit_sj_guar_appl')],
                                                             context=context)
            form_id = self.pool.get('ir.model.data').read(cr, uid, form_ids, fields=['res_id'], context=context)[0][
                'res_id']
            return {
                'domain': [('state', '=', 'get_office')],
                'name': '核保申请单',
                'view_type': 'form',
                'view_mode': 'tree,form',
                'res_model': 'credit.sj.guarantee.application',
                'views': [(False, 'tree'), (form_id, 'form')],
                'type': 'ir.actions.act_window',
            }
        else:
            raise osv.except_osv(_(u'提醒'), _(u'此核保单不能进行退回操作！'))

    def copy(self, cr, uid, id, default=None, context=None):
        """
            复制方法重写
        """
        default.update({
            'name': self.pool.get('ir.sequence').get(cr, uid, 'credit.sj.guarantee.application'),
            'submit_time': False,
            'guarantee_user': False,
            'guarantee_result': False,
            'guarantee_result_note':False,
            'route_line':False
        })
        return super(credit_sj_guarantee_application, self).copy(cr, uid, id, default=default, context=context)


credit_sj_guarantee_application()


def creat_route(self, cr, uid, ids, route_dic=None):
    """
        批量生成核保路线
        route_dic:{ (目的地，计划核保日期，授信规模起始日期，路线编号) : {核保申请单id:[id],计数num:数量} }
    """
    if route_dic:
        route_model = self.pool.get("credit.sj.guarantee.route")
        for route in route_dic.keys():
            # 根据route_dic创建核保路线
            route_id = route_model.create(cr, uid, {
                'destination': route[0],
                "plan_check_date": route[1],
                'credit_start_date': route[2],
                'name': route[3],
                "guarante_total_number": route_dic[route]['num'],
            }, context=None)
            self.write(cr, uid, route_dic[route]['ids'], {'route_line': route_id, 'state': 'wait_officer'},
                       context=None)
    return True
    # vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: