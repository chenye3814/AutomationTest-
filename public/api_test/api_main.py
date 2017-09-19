#coding:utf-8
from config.api_config import *
from public.requests_handle import *
from public.xlrd_handle import *
from api_global import *
from public.common.common import *

def api_requests():
    
    #实例化requests_handle
    api_requests = requests_handle()

    #实例化xlrd_handle
    api_currency = xlrd_handle(excel_data['path'], excel_data['currency_sheet_name'])

    api_currency.open_workbook()
    api_currency.open_sheet()
    #获取currency中的全部数据
    api_currency_value = api_currency.value_to_array()

    #返回数据大于1行，则处理数据；否则判断currency返回数据无通用接口数据
    if len(api_currency_value) > 1:
        request_value = {}
        for i in range(1, len(api_currency_value)):
            request_value['instruction ']       = api_currency_value[i][0]
            request_value['tag']                = api_currency_value[i][1]
            request_value['interfacestatus']    = api_currency_value[i][2]
            request_value['method']             = api_currency_value[i][3]
            request_value['url']                = api_currency_value[i][4]
            request_value['body']               = str_to_json(var_convert_para(api_currency_value[i][5]))
            request_value['headers']            = str_to_json(api_currency_value[i][6])
            request_value['checkpoint']         = api_currency_value[i][7]

            api_requests.set_requests_para(request_value['method'],request_value['url'],request_value['body'],request_value['headers'])
            return_data = str_to_json(api_requests.exc_requests())
            if request_value['tag'] in ('00000001'):
                if request_value['tag'] == '00000001':
                    currency['member_id'] = return_data['data']['member_id']
                    currency['key'] = return_data['data']['key']
            else:
                pass


            
        
        


 
