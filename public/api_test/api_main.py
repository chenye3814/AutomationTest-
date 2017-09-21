#coding:utf-8
from config.api_config import *
from public.requests_handle import *
from public.xlrd_handle import *
from api_global import *
from public.common.common import *

def api_requests():
    
    #实例化requests_handle
    api_requests = requests_handle()


    current_sheet_value = excel_sheet_value(excel_data['path'], excel_data['common_sheet_name'])


    print  current_sheet_value

    #返回数据大于1行，则处理数据；否则判断currency返回数据无通用接口数据
    if  current_sheet_value != False and len(current_sheet_value) > 1:
        for i in range(1, len(current_sheet_value)):

            request_value = excel_row_handle(current_sheet_value[i])

            if request_value != False:

                api_requests.set_requests_para(request_value['method'],request_value['url'],request_value['body'],request_value['headers'])
                return_data = str_to_json(api_requests.exc_requests())
                if request_value['tag'] in ('00000001'):
                    if request_value['tag'] == '00000001':
                        currency['member_id'] = return_data['data']['member_id']
                        currency['key'] = return_data['data']['key']
                else:
                    pass


            
        
        


 
