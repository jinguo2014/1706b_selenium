# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
import  HTMLTestRunner

class AssertLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "http://www.gole123.com"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_assert_login(self):
        driver = self.driver
        driver.get(self.base_url + "/login.aspx")
        time.sleep(5)
        driver.find_element_by_id("login_txtUserName").clear()
        driver.find_element_by_id("login_txtUserName").send_keys("jinguo1988")
        driver.find_element_by_id("login_txtPassword").clear()
        driver.find_element_by_id("login_txtPassword").send_keys("123456")
        time.sleep(2)
        driver.find_element_by_id("login_btnLogin").click()
        time.sleep(5)

        user_name_element=driver.find_element_by_xpath("html/body/div[2]/div[2]/div[2]/div[1]/div[1]/div[2]/p/b")

        user_name=user_name_element.text

        # 如果我预期的登录名和我真实登录后的名字一样，就说明我登录成功了！
        self.assertEqual("jinguo1998",user_name,"用户名不一样")
        time.sleep(2)
        driver.get_screenshot_as_file("E:\\foo.png")
        time.sleep(5)

    
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

if __name__ == "assert_login":
    # unittest.main()
    my_test_suite=unittest.TestSuite()
    my_test_suite.addTest(AssertLogin("test_assert_login"))
    unittest.TextTestRunner().run(my_test_suite)

    # fp=open("assert_login_result.html","wb")
    #
    # h_t_runner=HTMLTestRunner.HTMLTestRunner(stream=fp, title='test result', description=u'result:')
    #
    # h_t_runner.run(my_test_suite)
    #
    # fp.close()

