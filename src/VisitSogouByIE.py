#encoding=utf-8
from selenium import webdriver
import unittest

class VisitSogouByIE(unittest.TestCase):

    def setUp(self):
        # 启动IE浏览器
        self.driver = webdriver.Ie(executable_path = "c:\\IEDriverServer")

    def test_visitSogou(self):
        # 访问搜索首页
        self.driver.get("http://www.sogou.com")
        # 打印当前网页的网址
        print self.driver.current_url

    def tearDown(self):
        # 退出IE浏览器
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
