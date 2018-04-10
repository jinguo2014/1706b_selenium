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

class Shezhi1(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.baidu.com"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_shezhi1(self):
        driver = self.driver
        driver.get(self.base_url)
        time.sleep(3)
        shezhi=driver.find_element_by_link_text("设置")
        ActionChains(driver).move_to_element(shezhi).perform()
        time.sleep(3)
        # 点击高级搜索
        driver.find_element_by_link_text(u"高级搜索").click()
        time.sleep(3)
        driver.find_element_by_id("adv_keyword").clear()
        driver.find_element_by_id("adv_keyword").send_keys("ssd")
        driver.find_element_by_name("q2").clear()
        driver.find_element_by_name("q2").send_keys("ddfa")
        driver.find_element_by_name("q3").clear()
        driver.find_element_by_name("q3").send_keys("dfsasd")
        driver.find_element_by_name("q4").clear()
        driver.find_element_by_name("q4").send_keys("ddd")
        Select(driver.find_element_by_name("gpc")).select_by_visible_text(u"最近一年")
        Select(driver.find_element_by_name("ft")).select_by_visible_text(u"所有格式")
        driver.find_element_by_id("q5_1").click()
        driver.find_element_by_name("q6").clear()
        driver.find_element_by_name("q6").send_keys("baidu.com")
        driver.find_element_by_css_selector("input.advanced-search-btn").click()
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
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
