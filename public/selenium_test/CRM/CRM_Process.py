#coding:utf-8
import unittest
import re
import datetime
from time import sleep
from config.selenium_config import selenium_config
import sys
import os
#from selenium import webdriver

class CRM_Process(unittest.TestCase):
    #流程控制
    status_tag = {
        "status": 1
    }
    #driver = webdriver.Firefox()

    def __init__(self, methodName):
        super(CRM_Process,self).__init__(methodName)

    def driver_process_except(self, driver_process_str, driver = selenium_config['driver'], loop_num=10, sleep_time=1):
        if self.status_tag['status'] == 1:
            print 'Current Process : ' + str(driver_process_str).decode('utf-8')
            num = 0
            while num < loop_num:
                try:
                    exec ('temp_result = ' + driver_process_str)
                except Exception, e:
                    print e
                else:
                    break
                finally:
                    num += 1
                    sleep(sleep_time)
            if num == loop_num:
                self.status_tag['status'] = 0
                return False
            else:
                return temp_result


    @classmethod
    def setUpClass(cls):
        #设置测试Hosts
        #modify_hosts(hosts_config['Intranet'])
        #设置快照目录
        os.makedirs(selenium_config['snapshot_path'])

    @classmethod
    def tearDownClass(cls):
        #恢复Hosts
        #modify_hosts(hosts_config['Extranet'])
        #杀掉geckodriver.exe或者chromedriver.exe进程
        if selenium_config['browser'] == 'Firefox':
            os.system('taskkill -f -im geckodriver.exe')
        elif selenium_config['browser'] == 'Chrome':
            os.system('taskkill -f -im chromedriver.exe')

    def check_process_status(self):
        self.assertEqual(self.status_tag['status'], 1)

    #保存快照
    def save_snapshot(self, name):
        sleep(1)
        self.driver_process_except('driver.save_screenshot(r"' + selenium_config['snapshot_path'] + '\\' + str(name).split('test_')[1] + '_' + re.sub('[:]', '', str(datetime.datetime.now()).split(' ')[1].split('.')[0]) + '.png")')

    #浏览器打开CRM
    def test_open_url(self):
        '''打开CRM系统'''
        self.driver_process_except('driver.get("http://crm.guxiansheng.cn/")')
        self.driver_process_except('driver.set_window_size(1440, 900)')
        self.check_process_status()

    #CRM登录
    def test_login(self):
        '''CRM登录流程执行'''
        self.check_process_status()
        self.driver_process_except('driver.find_element_by_xpath(".//*[@id=\'app\']/div/div/form/div[1]/input").clear()')
        #self.driver_process_except('driver.find_element_by_xpath(".//*[@id=\'app\']/div/div/form/div[1]/input").send_keys(\'18784527410\')')
        self.driver_process_except('driver.find_element_by_xpath(".//*[@id=\'app\']/div/div/form/div[1]/input").send_keys(\'13888888888\')')
        self.driver_process_except('driver.find_element_by_xpath(".//*[@id=\'app\']/div/div/form/div[2]/input").clear()')
        #self.driver_process_except('driver.find_element_by_xpath(".//*[@id=\'app\']/div/div/form/div[2]/input").send_keys(\'527410\')')
        self.driver_process_except('driver.find_element_by_xpath(".//*[@id=\'app\']/div/div/form/div[2]/input").send_keys(\'123456\')')
        self.save_snapshot(sys._getframe().f_code.co_name)
        self.driver_process_except('driver.find_element_by_xpath(".//*[@id=\'app\']/div/div/form/div[3]/button").click()')
        self.save_snapshot(sys._getframe().f_code.co_name)
        self.check_process_status()

    #CRM权限管理
    def test_power_manager(self):
        '''权限管理流程执行'''
        self.check_process_status()
        self.driver_process_except('driver.find_element_by_css_selector(".show-nav" and \'[data-title="权限管理"]\').click()')
        self.save_snapshot(sys._getframe().f_code.co_name)
        self.driver_process_except('driver.find_element_by_css_selector(\'[class="examine-query jur-add"]\').click()')
        self.driver_process_except('driver.find_element_by_css_selector(".layui-input.username").clear()')
        self.driver_process_except('driver.find_element_by_css_selector(".layui-input.username").send_keys("testpowergroup".decode("utf-8"))')
        self.driver_process_except('driver.find_element_by_css_selector(".layui-textarea.description").clear()')
        self.driver_process_except('driver.find_element_by_css_selector(".layui-textarea.description").send_keys("就是个描述".decode("utf-8"))')
        self.driver_process_except('driver.find_element_by_css_selector(".child-select").click()')
        self.save_snapshot(sys._getframe().f_code.co_name)
        self.driver_process_except('driver.find_element_by_css_selector(".squaredFour>label").click()')
        self.driver_process_except('driver.find_element_by_css_selector(".examine-query.add-jur-save").click()')
        self.driver_process_except('driver.find_element_by_css_selector(".layui-input").clear()')
        self.driver_process_except('driver.find_element_by_css_selector(".layui-input").send_keys("testpowergroup".decode("utf-8"))')
        self.driver_process_except('driver.find_element_by_css_selector(".examine-query").click()')
        self.assertEqual(self.driver_process_except('driver.find_element_by_xpath(".//*[@id=\'app\']/div/div[1]/table/tbody/tr/td[1]").text'), 'testpowergroup')
        self.driver_process_except('driver.find_element_by_xpath(".//*[@id=\'app\']/div/div[1]/table/tbody/tr[1]/td[4]/a[3]").click()')
        self.save_snapshot(sys._getframe().f_code.co_name)
        self.driver_process_except('driver.find_element_by_css_selector(".layui-layer-btn1").click()')
        sleep(10)
        self.driver_process_except('driver.find_element_by_xpath(".//*[@id=\'header\']/div[1]/div[2]/a[2]").click()')
        self.save_snapshot(sys._getframe().f_code.co_name)
        #self.driver_process_except('driver.refresh()')
        self.check_process_status()

    #CRM账号管理,文件上传模拟
    def test_account_manager(self):
        '''账号管理流程执行'''
        self.check_process_status()
        self.driver_process_except('driver.find_element_by_css_selector(".show-nav" and \'[data-title="账号管理"]\').click()')
        self.save_snapshot(sys._getframe().f_code.co_name)
        self.driver_process_except('driver.find_element_by_xpath(".//*[@id=\'app\']/div/div[1]/form/div/div/div[11]/a[1]").click()')
        self.driver_process_except('driver.find_element_by_css_selector("#fileUp").click()')
        #AutoIt实现windows操作模拟
        if selenium_config['browser'] == 'Chrome':
            self.driver_process_except('os.system("C:\Users\Administrator\Desktop\Bbb.exe")')
        elif selenium_config['browser'] == 'Firefox':
            self.driver_process_except('os.system("C:\Users\Administrator\Desktop\FileUp.exe")')
        self.save_snapshot(sys._getframe().f_code.co_name)
        self.assertEqual(self.driver_process_except('driver.find_element_by_css_selector(".file-btn").text'), '修改')
        self.driver_process_except('driver.find_element_by_css_selector(".ok").click()')
        self.save_snapshot(sys._getframe().f_code.co_name)
        self.driver_process_except('driver.find_element_by_css_selector(".cancel").click()')
        self.driver_process_except('driver.find_element_by_xpath(".//*[@id=\'header\']/div[1]/div[2]/a[2]").click()')
        self.save_snapshot(sys._getframe().f_code.co_name)
        #self.driver_process_except('driver.refresh()')
        self.check_process_status()

    def test_message_manager(self):
        '''消息管理流程执行'''
        self.check_process_status()
        self.driver_process_except('driver.find_element_by_xpath(".//*[@id=\'header\']/div[2]/div[1]/ul/li[1]/a").click()')
        self.check_process_status()
        self.driver_process_except('driver.find_element_by_xpath(".//*[@id=\'app\']/div[2]/div[2]/div[1]/ul/li[2]").click()')
        sleep(3)
        self.save_snapshot(sys._getframe().f_code.co_name)
        self.driver_process_except('driver.find_element_by_xpath(".//*[@id=\'app\']/div[2]/div[2]/div[1]/ul/li[3]").click()')
        sleep(3)
        self.save_snapshot(sys._getframe().f_code.co_name)
        self.driver_process_except('driver.find_element_by_xpath(".//*[@id=\'app\']/div[2]/div[2]/div[1]/ul/li[1]").click()')
        sleep(3)
        self.save_snapshot(sys._getframe().f_code.co_name)
        self.driver_process_except('driver.find_element_by_xpath(".//*[@id=\'header\']/div[1]/div[2]/a[2]").click()')
        self.save_snapshot(sys._getframe().f_code.co_name)
        self.check_process_status()

    def test_driver_close(self):
        '''浏览器窗口关闭'''
        sleep(5)
        self.save_snapshot(sys._getframe().f_code.co_name)
        self.driver_process_except('driver.close()')
        self.check_process_status()
