#coding:utf-8
from config.api_config import *
from public.common.common import *
from public.requests_handle import *
from public.xlrd_handle import *
from public.api_test.api_global import *
from public.api_test.api_main import *
from scripts.single_scripts.divine_budget import  *
from public.report.report_currency import *

#接口轮询
#api_currency_requests()
#print currency
#api_common_requests()

#神力值
divine_budget_main()

#aaa = [[1,2,'aaaa',['abc',234,['1a','3b']]],['[3]',[4,5,6]]]
#aaa = 1
#print set_table_value(aaa, 1)
