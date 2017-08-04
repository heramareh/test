#encoding=utf-8

from selenium import webdriver
import unittest
import time
# 导入显示等待类
from selenium.webdriver.support.ui import WebDriverWait
# 导入期望场景类
from selenium.webdriver.support import expected_conditions as EC

class LoginMail(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox(executable_path='D:\\geckodriver')
        self.driver.implicitly_wait(20)
        self.driver.maximize_window()

    def test_login_mail(self):
        self.login_126_mail('jq0002', '11111q')

    def tearDown(self):
        self.driver.quit()

    def login_126_mail(self, username, password):
        self.driver.get('http://mail.126.com')
        login_by_mail_tab = self.driver.find_element_by_xpath("//div[@class='loginFuncNormal']")
        login_by_mail_tab.click()
        self.driver.switch_to.frame('x-URS-iframe')
        mail_input_text = self.driver.find_element_by_name("email")
        mail_input_text.send_keys(username)
        password_input_text = self.driver.find_element_by_name("password")
        password_input_text.send_keys(password)
        time.sleep(3)
        login_btn = self.driver.find_element_by_xpath("//a[@id='dologin']")
        login_btn.click()
        bind_phone_btn = self.driver.find_element_by_xpath("//a[text()='继续登录']")
        bind_phone_btn.click()
        time.sleep(3)
        self.driver.switch_to.default_content()
        assert u'退出' in self.driver.page_source
        print u'登录成功'
        logout_btn = self.driver.find_element_by_xpath("//a[text()='退出']")
        logout_btn.click()
        wait = WebDriverWait(self.driver, 20, 1)
        wait.until(EC.title_is(u"网易邮箱 - 您已成功退出邮箱"))
        print self.driver.title
        assert u'您已成功退出邮箱' in self.driver.title
        print u'退出成功'

if __name__ == '__main__':
    unittest.main()
