#coding:utf-8
from config.api_config import *
from ..common.log import *
from ..common.common import *


#将excel中获取的包含在||内的变量转成对应参数，替换参数均统一保存在common_data字典中
def var_convert_para(need_convert):

    try:
        temp_str = str(need_convert)
    except:
        logging.error('变量转换参数失败.转为str类型处理失败'.decode('utf-8'))
        return False

    #将str以'|'为分隔符，转成list
    temp_list = temp_str.split('|')

    #list长度大于1时，开始转换
    if len(temp_list) > 1:
        for i in range(0, len(temp_list)):
            #所有待替换的变量位置均为list的基数位
            if i % 2 == 1:
                try:
                    temp_list[i] = common_data[temp_list[i]]
                except:
                    logging.error('参数替换失败./n/t替换的变量为:\t'.decode('utf-8') + str(temp_list[i]))
                    return False
        #将替换好的str返回
        return ''.join(temp_list)
                
    else:
        return temp_str
        

