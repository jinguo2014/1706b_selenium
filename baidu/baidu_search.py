# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class Baidu(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.baidu.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_baidu(self):
        driver = self.driver
        driver.get(self.base_url + "/")


        driver.find_element_by_id("kw").click()#获取到百度输入框进行点击操作
        driver.find_element_by_id("kw").clear()#获取到百度输入框进行清理操作
        driver.find_element_by_id("kw").send_keys(u"周帅")#获取到百度输入框输入要查询的东西
        # driver.find_element_by_id("su").click()#获取到“百度一下”按钮进行点击操作
        # driver.find_element_by_xpath("//input[@id='su']").click()
        # driver.find_element_by_xpath(".//*[@id='su']").click()
        time.sleep(5)
        driver.set_window_size(480, 800)

        button=driver.find_element(By.XPATH,".//*[@id='su']")
        num=button.size
        text=button.text
        value=button.get_attribute("maxlength")
        isd=button.is_displayed()

        print(num,text,value,isd)
        driver.find_element_by_id("kw").submit()#模拟回车键
        time.sleep(5)
        driver.refresh()
        time.sleep(5)
        driver.back()
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
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
