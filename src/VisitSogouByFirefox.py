#encoding=utf-8
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium import webdriver
import unittest

class VisitSogouByFirefox(unittest.TestCase):

    def setUp(self):
        #binary = FirefoxBinary('D:\\FirefoxPortable\\Firefox.exe')
        # 启动Firefox浏览器
        self.driver = webdriver.Firefox(executable_path = "c:\\geckodriver")

    def test_visitSogou(self):
        # 访问搜索首页
        self.driver.get("http://www.sogou.com")
        # 打印当前网页的网址
        print self.driver.current_url

    def tearDown(self):
        # 退出firefox浏览器
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
