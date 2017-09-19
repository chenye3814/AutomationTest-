#coding:utf-8
from config.api_config import *
from public.common.common import *
from public.requests_handle import *
from public.xlrd_handle import *
from public.api_test.api_global import *
from public.api_test.api_main import *

'''
test = xlrd_handle(r'API_Test.xlsx','currency')
test.open_workbook()
test.open_sheet()

excel_value = test.value_to_array()

body_value = var_convert_para(excel_value[1][5])

body_value_json = str_to_json(body_value)

print body_value_json

header_value = str_to_json(excel_value[1][6])

method_value = excel_value[1][3]

url_value = excel_value[1][4]

request_result = requests_handle(method_value,url_value,body_value_json,header_value)

print request_result.exc_requests()
'''
api_requests()

print currency
