# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
# 引入 ActionChains 类
from selenium.webdriver.common.action_chains import ActionChains



class YiduwangAddcart(unittest.TestCase):
    def setUp(self):
        #加载谷歌浏览器驱动
        self.driver = webdriver.Chrome()
        #隐式等待
        self.driver.implicitly_wait(30)
        #主页地址
        self.base_url = "http://www.gole123.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_yiduwang_addcart(self):
        driver = self.driver
        #请求主页
        driver.get(self.base_url + "/")
        #把浏览器屏幕放到最大
        driver.maximize_window()
        # 定位到要鼠标悬停到上装区元素
        above = driver.find_element_by_xpath("//div[@id='header']/div[3]/div/div[2]/ul/li[2]/a/span")
        # 对定位到的元素执行鼠标悬停操作
        ActionChains(driver).move_to_element(above).perform()

        time.sleep(3)
        driver.find_element_by_xpath(u"(//a[contains(text(),'套裙')])[4]").click()

        #点击完套裙页面往上滚一些
        js = "window.scrollTo(0,600);"
        driver.execute_script(js)
        time.sleep(3)

        #点击其中一件套裙
        driver.find_element_by_id("SubCategory_rptProducts_ctl00_ctl00_Common_ProductThumbnail1").click()
        time.sleep(3)

        #此处应该有一个窗口切换
        all_handles = driver.window_handles
        #切换到第二个窗口
        driver.switch_to.window(all_handles[1])

        time.sleep(3)
        js = "window.scrollTo(0,300);"
        driver.execute_script(js)
        time.sleep(3)
        driver.find_element_by_id('skuValueId_18_159').click()

        time.sleep(3)
        driver.find_element_by_id("skuValueId_17_154").click()
        time.sleep(3)
        driver.find_element_by_css_selector("div[name=\"spAdd\"] > span").click()
        time.sleep(3)
        driver.find_element_by_css_selector("#addcartButton > img").click()
        time.sleep(3)
        driver.find_element_by_css_selector("a.btn-viewcart").click()
        time.sleep(3)
        driver.find_element_by_id("ShoppingCart_btnCheckout").click()
        time.sleep(3)
        driver.find_element_by_id("textfieldusername").clear()
        driver.find_element_by_id("textfieldusername").send_keys("jinguo1988")
        time.sleep(3)
        driver.find_element_by_id("textfieldpassword").clear()
        driver.find_element_by_id("textfieldpassword").send_keys("123456")
        time.sleep(3)
        driver.find_element_by_id("btnLoginAndBuy").click()

        time.sleep(10)
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        # self.driver.quit()
        self.driver.close()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
