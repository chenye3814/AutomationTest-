#coding:utf-8
from selenium import webdriver
import os
import re
import datetime
import logging


#流程状态控制
status_tag = {
    "status" : 1
}

driver = webdriver.Firefox()
driver.implicitly_wait(10)
#logging.basicConfig(level=logging.INFO)


# 设置快照和报告路径
date_str = re.sub('[- :]', '', str(datetime.datetime.now()).split('.')[0])
snapshot_path = os.getcwd() + '\\pictures\\CRM\\CRM' + date_str
report_file_path = os.getcwd() + '\\report\\HTMLReport' + date_str + '.html'

