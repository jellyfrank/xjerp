# -*- coding: utf-8 -*-
###########################################################################################
#
#    module name for OpenERP
#    Copyright (C) 2014 Jinan Shangjie Technology CO.,LTD. (<http://www.jnshangjie.com/>).
#
###########################################################################################

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


class credit_sj_guarantee_route(osv.Model):
    """
        分配核保专员
    """
    _name = 'credit.sj.guarantee.route'
    _description = "credit.sj.guarantee.route"
    _order = 'name desc'

    _columns = {
        'name': fields.char(u"路线编号", size=20),
        'credit_start_date': fields.date(u"授信规模起始日期", size=20),
        'destination': fields.char(u"目的地", size=20),
        'plan_check_date': fields.date(u"计划核保日期", size=20),
        'check_staff': fields.many2one('res.users', u'核保专员'),
        'guarante_total_number': fields.integer(u'总核保单个数', size=3),
        'guarante_complete_number': fields.integer(u'已完成核保单个数', size=3),
        'line': fields.one2many('credit.sj.guarantee.application', 'route_line', u'申请单信息'),
        'state': fields.selection([('wait_officer', u'待分配核保专员'),
                                   ('get_officer', u'已分配核保专员'),
                                   ('done', u'核保结果已反馈'),],
                                  u'状态', ),
    }

    # 设置默认值
    _defaults = {
        'state': lambda *a: 'wait_officer',
        'guarante_complete_number': lambda *a: 0,
    }

    def btn_submit(self, cr, uid, ids, context=None):
        """
            校验分配专员并修改状态
        """
        state = 'get_officer'   # 核保路线状态
        state_requisition = 'get_office'   # 核保申请单状态
        rec = self.read(cr, uid, ids, ['check_staff'], context=context)
        guarantee_user = rec[0].get('check_staff')
        # 校验是否填写上核保专员
        if guarantee_user == False:
            raise osv.except_osv(_(u'提醒'), _(u'请点击‘编辑’按钮，填写核保专员'))
        return set_request_states(self, cr, uid, ids, states=state, states_requisition=state_requisition, guarantee_user=guarantee_user[0], context=None)

    def unlink(self, cr, uid, ids, context=None):
        test = self.browse(cr,uid,ids[0])
        print '**********'
        print test.state.id

        """
            删除时校验路线中存在核保单
        """
        for rec in self.browse(cr, uid, ids, context=context):
            if rec.guarante_total_number != 0:
                raise osv.except_osv(_(u'提醒'), _(u'只能删除空的路线'))
        return super(credit_sj_guarantee_route, self).unlink(cr, uid, ids, context=context)

credit_sj_guarantee_route()


def set_request_states(self, cr, uid, route_id, states=None, states_requisition=None, guarantee_user=None, context=None):
    """
        修改制定路线的状态并修改路线下核保申请单的状态
        route_id:核保路线id
        states:需要修改成核保路线的目标状态
        states1:需要修改核保申请单的目标状态
        guarantee_user:获取页面上核保专员
    """
    up_dic = {'state': states_requisition}  #存放更新核保申请单信息的字典
    if guarantee_user:
        up_dic['guarantee_user'] = guarantee_user
    request_model = self.pool.get('credit.sj.guarantee.application')
    ids = request_model.search(cr, uid, [('route_line', '=', route_id[0] )], context=context)
    # 修改核保申请单
    request_model.write(cr, uid, ids, up_dic, context=context)
    # 修改核保申请路线
    self.write(cr, uid, route_id, {'state': states}, context=context)
    return True

class credit_sj_guarantee_route_user(osv.Model):
    _inherit = 'res.users'

    _columns = {
        'job': fields.selection([('guarantee_manager', u'客户经理'),
                                 ('guarantee_officer', u'核保专员'),
                                 ('guarantee_team', u'核保团队'), ],
                                u'职务', required=True),
    }
credit_sj_guarantee_route_user()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
