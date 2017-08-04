#encoding=utf-8

from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium import webdriver
import time

binary = FirefoxBinary('D:\\Program Files (x86)\\Mozilla Firefox\\firefox.exe')
driver = webdriver.Firefox(executable_path="c:\\geckodriver")

def visit_url(url):
    #访问url
    driver.get(url)
    print driver.current_url

def login(username, password):
    # 登录
    # 点击帐号密码登录页签
    driver.find_element_by_id("switcher_plogin").click()
    #输入帐号密码
    usernametext = driver.find_element_by_xpath("//input[@id='u']")
    passwordtext = driver.find_element_by_xpath("//input[@id='p']")
    usernametext.send_keys(username)
    passwordtext.send_keys(password)
    #点击登录按钮
    login_button = driver.find_element_by_xpath("//*[@id='login_button']")
    login_button.click()

def click_group_mail():
    #点击群邮件
    group_mail_button = driver.find_element_by_xpath("//*[.='群邮件']")
    group_mail_button.click()
    time.sleep(3)

def get_mails_titles():
    mails_titles = driver.find_elements_by_xpath("//*[@class='black']")
    mails_titles_list=[]
    for i in mails_titles:
        mails_titles_list.append(i.text)
    return mails_titles_list

if __name__ == '__main__':
    visit_url("https://mail.qq.com/")
    time.sleep(5)
    login("**********", "*************")
    click_group_mail()
    print get_mails_titles()
    driver.quit()

