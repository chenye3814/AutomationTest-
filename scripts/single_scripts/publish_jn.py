#coding:utf-8
import random
from public.requests_handle import requests_handle
from public.common.common import *

#锦囊body内容
need_config = {
    'jn_class':str(random.choice([88, 89, 90])),
    'plan_rate':str(random.choice([3, 5])),
    'plan_time':str(random.choice([1, 3, 5, 10])),
    'price':str(0.01),
    'stock_price':'',
    'intro':'锦囊研究分析',
    'vice_title':'Title' + str(random.randint(0, 99))
}
#实例化requests_handle对象
r_h = requests_handle()

#账号配置
member_config = [
    {'mobile':'',
    'password':get_md5('')}
]

#股票搜索方式
stock_sort = {
    "pageNo": [str(i) for i in range(10)],
    "pageSize": ['20','50','80','100'],
    # sortField可配置:
    # CRAT涨幅，CVAL涨跌，HPRI最高价，LPRI最低价，NPRI最新价,"CVAL","HPRI","LPRI","NPRI"
    "sortField": ["CRAT"]
}

#获取member_id和key
def get_member_key(member_config = member_config, r_h = r_h):
    method = 'post'
    url = r'https://login.api.guxiansheng.cn/index.php?c=user&a=login'
    body = {
        'username':member_config['mobile'],
        'password':member_config['password']
    }
    headers = {
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
    }

    r_h.set_requests_para(method, url, body, headers)
    result_str = r_h.exc_requests()
    result_json = str_to_json(result_str)
    result_filter = dict_filter_columns(result_json, ['data','code','message'])


    if result_filter is not False:
        if result_filter['code'] == 1:
            need_config['member_id'] = str(result_filter['data']['member_id'])
            need_config['key'] = str(result_filter['data']['key'])
        else:
            logging.info(result_filter['message'])
            return False


#按搜索方式，随机获取锦囊任意支股票
def get_stock(num = 1, stock_sort = stock_sort, r_h = r_h):

    pageNo = random.choice(stock_sort['pageNo'])
    pageSize = random.choice(stock_sort['pageSize'])
    sortField = random.choice(stock_sort['sortField'])

    url = r'http://mk2.api.guxiansheng.cn/?mod=quote&a=get&c=stk_sort&pageNo=' + pageNo + '&pageSize=' + pageSize + '&sortField=' + sortField
    requestMethod = 'get'


    r_h.set_requests_para(requestMethod,url)
    result_str = r_h.exc_requests()
    result_json = str_to_json(str(result_str)[3:])
    result_filter = dict_filter_columns(result_json, ['data'])

    if result_filter is not False:
        if num < len(result_filter['data']):
            print 'Return to satisfy the conditional stock : ' + str(num)
            return random.sample(result_filter['data'], num)
        else:
            print 'Return to satisfy the conditional stock : ' + str(len(result_filter['data']))
            return result_filter['data']

    else:
        logging.info('get_stock Aborted!!!')
        return False

def set_jn_config(stock_value):
    need_config['stock_code'] = str(stock_value['FCOD'])
    need_config['stock_name'] = str(stock_value['SNAM'])
    need_config['fist_buy_price'] = str(round(float(stock_value['PPRI']) * 1.01, 2))
    need_config['second_buy_price'] = str(round(float(stock_value['PPRI']) * 0.97, 2))
    need_config['fist_win_rate'] = str(round(float(stock_value['PPRI']) * 1.03, 2))
    need_config['second_win_rate'] = str(round(float(stock_value['PPRI']) * 1.05, 2))
    need_config['fist_lose_rate'] = str(round(float(stock_value['PPRI']) * 0.95, 2))
    need_config['second_lose_rate'] = str(round(float(stock_value['PPRI']) * 0.9, 2))


def publish_jn(stock_list, r_h = r_h):

    url = r'https://seller.api.guxiansheng.cn/index.php?c=jn&a=postJn'
    requestMethod = 'post'
    headers = {
        "Content-Type":r"application/x-www-form-urlencoded; charset=UTF-8"
    }
    for stock_value in (stock_list):
        set_jn_config(stock_value)
        body = {
            "member_id":need_config['member_id'],
            "key":need_config['key'],
            "stock_code":need_config['stock_code'],
            "stock_name":need_config['stock_name'],
            "fist_buy_price":need_config['fist_buy_price'],
            "second_buy_price":need_config['second_buy_price'],
            "fist_win_rate":need_config['fist_win_rate'],
            "second_win_rate":need_config['second_win_rate'],
            "fist_lose_rate":need_config['fist_lose_rate'],
            "second_lose_rate":need_config['second_lose_rate'],
            "jn_class":need_config['jn_class'],
            "plan_rate":need_config['plan_rate'],
            "plan_time":need_config['plan_time'],
            "price":need_config['price'],
            "vice_title":need_config['vice_title'],
            "intro":need_config['intro'],
            "stock_price":''
        }

        r_h.set_requests_para(requestMethod, url,body,headers)
        result_str = r_h.exc_requests()
        result_json = str_to_json(result_str)
        result_filter = dict_filter_columns(result_json,['code','message'])

        if result_filter is not False:
            if result_filter['code'] == 1:
                print 'Success!!!' + need_config['stock_name']
            else:
                print 'Fail! ' + need_config['stock_name'] + ' '+ result_filter['message']
        else:
            logging.info('publish_jn Aborted!!!')


def create_jn(num = 1, member_config = member_config):
    if type(num) is not int or num < 1:
        logging.info('create_jn Aborted!!!')
    else:
        for member_password in member_config:
            if get_member_key(member_password) is not False:
                print 'Current create jn mobile : ' + str(member_password['mobile'])
                return_stock_list = get_stock(num)
                if return_stock_list is not False:
                    publish_jn(return_stock_list)

