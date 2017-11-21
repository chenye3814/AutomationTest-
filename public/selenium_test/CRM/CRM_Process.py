#coding:utf-8
import unittest
import re
import datetime
from time import sleep
from config.selenium_config import *
from public.selenium_test.selenium_except import driver_process_except
from config.selenium_config import snapshot_path
from config.selenium_config import date_str
from config.api_config import hosts_config
from public.common.common import modify_hosts
import sys
import os


class CRM_Process(unittest.TestCase):

    driver = driver

    def __init__(self,methodName='runTest'):
        super(CRM_Process, self).__init__(methodName)

    @classmethod
    def setUpClass(cls):
        #设置测试Hosts
        #modify_hosts(hosts_config['Intranet'])
        #设置快照目录
        os.makedirs(snapshot_path)

    @classmethod
    def tearDownClass(cls):
        #恢复Hosts
        #modify_hosts(hosts_config['Extranet'])
        #杀掉geckodriver.exe进程
        os.system('taskkill -f -im geckodriver.exe')
        #pass

    def check_process_status(self):
        self.assertEqual(status_tag['status'], 1)

    def save_snapshot(self, name):
        sleep(1)
        driver_process_except('driver.save_screenshot(r"' + snapshot_path + '\\' + str(name).split('test_')[1] + '_' + re.sub('[:]', '', str(datetime.datetime.now()).split(' ')[1].split('.')[0]) + '.png")')

    #浏览器打开CRM
    def test_open_url(self):
        '''打开CRM系统'''
        driver_process_except('driver.get("http://crm.guxiansheng.cn/")')
        self.check_process_status()

    #CRM登录
    def test_login(self):
        '''CRM登录流程执行'''
        self.check_process_status()
        driver_process_except('driver.find_element_by_xpath(".//*[@id=\'app\']/div/div/form/div[1]/input").clear()')
        driver_process_except('driver.find_element_by_xpath(".//*[@id=\'app\']/div/div/form/div[1]/input").send_keys(\'admin\')')
        driver_process_except('driver.find_element_by_xpath(".//*[@id=\'app\']/div/div/form/div[2]/input").clear()')
        driver_process_except('driver.find_element_by_xpath(".//*[@id=\'app\']/div/div/form/div[2]/input").send_keys(\'123456\')')
        self.save_snapshot(sys._getframe().f_code.co_name)
        driver_process_except('driver.find_element_by_xpath(".//*[@id=\'app\']/div/div/form/div[3]/button").click()')
        self.save_snapshot(sys._getframe().f_code.co_name)
        self.check_process_status()

    #CRM权限管理
    def test_power_manager(self):
        '''权限管理流程执行'''
        self.check_process_status()
        driver_process_except('driver.find_element_by_css_selector(".show-nav" and \'[data-title="权限管理"]\').click()')
        self.save_snapshot(sys._getframe().f_code.co_name)
        driver_process_except('driver.find_element_by_css_selector(\'[class="examine-query jur-add"]\').click()')
        driver_process_except('driver.find_element_by_css_selector(".layui-input.username").clear()')
        driver_process_except('driver.find_element_by_css_selector(".layui-input.username").send_keys("testpowergroup".decode("utf-8"))')
        driver_process_except('driver.find_element_by_css_selector(".layui-textarea.description").clear()')
        driver_process_except('driver.find_element_by_css_selector(".layui-textarea.description").send_keys("就是个描述".decode("utf-8"))')
        driver_process_except('driver.find_element_by_css_selector(".child-select").click()')
        self.save_snapshot(sys._getframe().f_code.co_name)
        driver_process_except('driver.find_element_by_css_selector(".squaredFour>label").click()')
        driver_process_except('driver.find_element_by_css_selector(".examine-query.add-jur-save").click()')
        driver_process_except('driver.find_element_by_css_selector(".layui-input").clear()')
        driver_process_except('driver.find_element_by_css_selector(".layui-input").send_keys("testpowergroup".decode("utf-8"))')
        driver_process_except('driver.find_element_by_css_selector(".examine-query").click()')
        self.assertEqual(driver_process_except('driver.find_element_by_xpath(".//*[@id=\'app\']/div/div[1]/table/tbody/tr/td[1]").text'), 'testpowergroup')
        driver_process_except('driver.find_element_by_xpath(".//*[@id=\'app\']/div/div[1]/table/tbody/tr[1]/td[4]/a[3]").click()')
        self.save_snapshot(sys._getframe().f_code.co_name)
        driver_process_except('driver.find_element_by_css_selector(".layui-layer-btn1").click()')
        sleep(5)
        driver_process_except('driver.find_element_by_xpath(".//*[@id=\'header\']/div[1]/div[2]/a[2]").click()')
        self.save_snapshot(sys._getframe().f_code.co_name)
        #driver_process_except('driver.refresh()')
        self.check_process_status()

    #CRM账号管理,文件上传模拟
    def test_account_manager(self):
        '''账号管理流程执行'''
        self.check_process_status()
        driver_process_except('driver.find_element_by_css_selector(".show-nav" and \'[data-title="账号管理"]\').click()')
        self.save_snapshot(sys._getframe().f_code.co_name)
        driver_process_except('driver.find_element_by_xpath(".//*[@id=\'app\']/div/div[1]/form/div/div/div[11]/a[1]").click()')
        driver_process_except('driver.find_element_by_css_selector("#fileUp").click()')
        #AutoIt实现windows操作模拟
        driver_process_except('os.system("C:\Users\Administrator\Desktop\FileUp.exe")')
        self.save_snapshot(sys._getframe().f_code.co_name)
        self.assertEqual(driver_process_except('driver.find_element_by_css_selector(".file-btn").text'), '修改')
        driver_process_except('driver.find_element_by_css_selector(".ok").click()')
        self.save_snapshot(sys._getframe().f_code.co_name)
        driver_process_except('driver.find_element_by_css_selector(".cancel").click()')
        driver_process_except('driver.find_element_by_xpath(".//*[@id=\'header\']/div[1]/div[2]/a[2]").click()')
        self.save_snapshot(sys._getframe().f_code.co_name)
        #driver_process_except('driver.refresh()')
        self.check_process_status()

    def test_driver_close(self):
        '''浏览器窗口关闭'''
        sleep(5)
        self.save_snapshot(sys._getframe().f_code.co_name)
        driver_process_except('driver.close()')
        self.check_process_status()
