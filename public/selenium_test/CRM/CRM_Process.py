#coding:utf-8
import unittest
from time import sleep
from config.selenium_config import *
from public.selenium_test.selenium_except import driver_process_except

class CRM_Process(unittest.TestCase):

    driver = driver

    def __init__(self,methodName='runTest'):
        super(CRM_Process, self).__init__(methodName)

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    #浏览器打开CRM
    def test_open_url(self):
        driver_process_except('driver.get(\'http://crm.guxiansheng.cn/\')')
        self.assertEqual(status_tag['status'], 1)

    #CRM登录
    def test_login(self):
        self.assertEqual(status_tag['status'], 1)
        driver_process_except('driver.find_element_by_xpath(".//*[@id=\'app\']/div/div/form/div[1]/input").clear()')
        driver_process_except('driver.find_element_by_xpath(".//*[@id=\'app\']/div/div/form/div[1]/input").send_keys(\'admin\')')
        driver_process_except('driver.find_element_by_xpath(".//*[@id=\'app\']/div/div/form/div[2]/input").clear()')
        driver_process_except('driver.find_element_by_xpath(".//*[@id=\'app\']/div/div/form/div[2]/input").send_keys(\'123456\')')
        driver_process_except('driver.find_element_by_xpath(".//*[@id=\'app\']/div/div/form/div[3]/button").click()')
        self.assertEqual(status_tag['status'], 1)

    #CRM权限管理
    def test_power_manager(self):
        self.assertEqual(status_tag['status'], 1)
        driver_process_except('driver.find_element_by_css_selector(".show-nav" and \'[data-title="权限管理"]\').click()')
        driver_process_except('driver.find_element_by_css_selector(\'[class="examine-query jur-add"]\').click()')
        driver_process_except('driver.find_element_by_css_selector(".layui-input.username").clear()')
        driver_process_except('driver.find_element_by_css_selector(".layui-input.username").send_keys("test权限组".decode("utf-8"))')
        driver_process_except('driver.find_element_by_css_selector(".layui-textarea.description").clear()')
        driver_process_except('driver.find_element_by_css_selector(".layui-textarea.description").send_keys("就是个描述".decode("utf-8"))')

        driver_process_except('driver.find_element_by_css_selector(".child-select").click()')
        driver_process_except('driver.find_element_by_css_selector(".squaredFour>label").click()')
        driver_process_except('driver.find_element_by_css_selector(".examine-query.add-jur-save").click()')
        driver_process_except('driver.find_element_by_xpath(".//*[@id=\'app\']/div/div[1]/table/tbody/tr[1]/td[4]/a[3]").click()')
        driver_process_except('driver.find_element_by_css_selector(".layui-layer-btn1").click()')
        driver_process_except('driver.find_element_by_xpath(".//*[@id=\'header\']/div[1]/div[2]/a[2]").click()')
        self.assertEqual(status_tag['status'], 1)


    def test_driver_close(self):
        sleep(5)
        driver_process_except(\'driver.close()\')
        self.assertEqual(status_tag['status'], 1)
