# -*- coding: utf-8 -*-
###########################################################################################

#    Guarantee Route name for OpenERP
#    Copyright (C) 2014 Jinan Shangjie Technology CO.,LTD. (<http://www.jnshangjie.com/>).

###########################################################################################

{
    'name': 'Guarantee Route', #模块名称
    'summary': 'Verify Guarantee', #摘要
    'version': '1.1', #版本
    'category': 'Accounting & Finance', #分类
    'author': 'Jinan Shangjie Technology', #作者
    'website': 'http://www.jnshangjie.com/', #网址
    'depends': ['base'], #关联模块
    'data': [
        'credit_sj_guarantee_route_view.xml',
        'credit_sj_guarantee_route_repport.xml',
        'report/credit_sj_guarantee_route_report.rml'
    ], #更新XML,CSV
    'installable': True, #是否可安装
    'application': True, #是否认证
    'auto_install': False, #是否自动安装
    'description': """
核保系统-核保任务管理/核保任务接收
""",
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:

