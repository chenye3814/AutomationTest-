#coding:utf-8
from public.common.common import *

common_data = {
        'mobile':'18511903584',
        'password':'654321'
    }


excel_data = {
        'path':r'API_Test.xlsx',
        'currency_sheet_name':'currency',
        'common_sheet_name':'common'
    }


currency = {
        'member_id':'',
        'key':'',
        'hashkey':''        
    }


hosts_config = { "Intranet":"# APP inner web\n\
192.168.10.205 static.guxiansheng.cn\n\
192.168.10.205 login.api.guxiansheng.cn\n\
192.168.10.205 u.api.guxiansheng.cn\n\
192.168.10.205 content.api.guxiansheng.cn\n\
192.168.10.205 trade.api.guxiansheng.cn\n\
192.168.10.205 h5api.api.guxiansheng.cn\n\
192.168.10.205 h5.api.guxiansheng.cn\n\
192.168.10.205 tpsadmin.guxiansheng.cn #第三方内网\n\
192.168.10.205 tps.api.guxiansheng.cn #第三方内网\n\
192.168.10.205 pay.api.guxiansheng.cn\n\
192.168.10.205 managertps.guxiansheng.cn\n\
192.168.10.205 merchants.guxiansheng.cn\n\
192.168.10.205 newh5.guxiansheng.cn\n\
192.168.0.96 manager.tps.cn\n\
192.168.10.205   zb.gukezhibo.com#直播\n\
192.168.10.205   gkadmin.gukezhibo.com\n\
192.168.10.205   gkcustomer.gukezhibo.com\n\
192.168.10.205   static.guxiansheng.cn\n\
192.168.10.205	wxlgd.guxiansheng.cn\n\
192.168.10.205 front.caixuetang.cn\n\
120.76.180.146 mk2.api.guxiansheng.cn\n\
192.168.10.205 www.guxiansheng.cn\n\
192.168.10.205 m.guxiansheng.cn\n\
192.168.10.243 cfzx.testtg.com\n\
192.168.10.205 clb.api.guxiansheng.cn\n\
192.168.10.205 seller.api.guxiansheng.cn\n\
192.168.10.205 hegui.guxiansheng.cn #合规后台\n\
192.168.10.205 compliance.api.guxiansheng.cn\n\
192.168.10.205 www.guxiansheng.cn\n\
120.76.180.146 mk.api.guxiansheng.cn\n\
192.168.10.205 admin.caixuetang.cn\n\
192.168.10.205 api.caixuetang.cn\n\
192.168.10.205 zhifu.caixuetang.cn\n\
192.168.10.205 front.caixuetang.cn\n\
192.168.10.205 doc.caixuetang.cn\n\
192.168.10.205 edu.caixuetang.cn",
                 "Extranet":""
}