#coding=utf-8

import time
import os.path
import traceback
import requests
from selenium import webdriver
from ExcelManage2 import ExcelManage2
category_urls = [(u"配饰配件/皮带/帽子/围巾", "50010404"),
                 (u"流行男鞋", "50011740"),
                 (u"箱包皮具/热销女包/男包", "50006842"),
                 (u"女士内衣/男士内衣/家居服", "1625"),
                 (u"女鞋", "50006843"),
                 (u"男装", "30"),
                 (u"女装/女士精品", "16")]

def switch_window(driver, window_title):
    u"""切换窗口"""
    try:
        all_windows = driver.window_handles
        for window in all_windows:
            driver.switch_to_window(window)
            if (window_title in driver.title):
                break
    except Exception, e:
        print u"切换窗口失败："

if __name__ == "__main__":
    # get_download_url("http://a.holaworld.cn/theme/v1/themes?cw=100&cw2=233&psize=500","d:\\download_url.txt")
    # download_file("d:\\failed.txt","d:\\success.txt","Chrome")
    try:
        chrome_options = webdriver.ChromeOptions()
        prefs = {"profile.managed_default_content_settings.images": 2}
        chrome_options.add_experimental_option("prefs", prefs)
        driver = webdriver.Chrome(executable_path='d:\\chromedriver', chrome_options=chrome_options)
        driver.maximize_window()
        driver.get("https://login.taosj.com/?redirectURL=http%3A%2F%2Fwww.taosj.com%2F")
        driver.find_element_by_xpath("//input[@name='loginCode']").send_keys("18910438805")
        driver.find_element_by_xpath("//input[@name='loginPassword']").send_keys("123456789")
        driver.find_element_by_xpath(".//*[@id='T_Login']").click()
        for k,v in category_urls:
            em = ExcelManage2()
            em.append_datas([u"行业：", u"服装鞋包", u"子行业", k, u"分类", u"全部"])
            em.append_datas([u"店铺", u"主营", u"掌柜", u"地址", u"开店时间", u"好评率", u"销售量", u"销售金额"])
            urls = []
            for i in xrange(1, 50):
                driver.get("http://www.taosj.com/industry/index.html#/data/hotshops/?cid=" + v + "&pcid=2&brand=&type=ALL&date=&pageNo=" + str(i))
                time.sleep(1)
                elements = driver.find_elements_by_xpath("//a[text()='查看详情']")
                for id, element in enumerate(elements):
                    a = driver.find_elements_by_xpath("//a[text()='查看详情']/parent::*/parent::*/parent::td/preceding-sibling::td[4]")[id].text.strip()
                    b = driver.find_elements_by_xpath("//a[text()='查看详情']/parent::*/parent::*/parent::td/preceding-sibling::td[3]")[id].text.strip()
                    c = driver.find_elements_by_xpath("//a[text()='查看详情']/parent::*/parent::*/parent::td/preceding-sibling::td[2]")[id].text.strip()
                    url = element.get_attribute("href")
                    # print url,a,b,c
                    urls.append((url,a,b,c))
                # driver.find_element_by_xpath("//a[@class='J_page_jump page-one page-pn ui-page-no ui-page-next']").click()
                # time.sleep(2)
            for url,a,b,c in urls:
                driver.get(url)
                time.sleep(0.6)
                try:
                    driver.find_element_by_xpath("//a[@class='ui_close']").click()
                    time.sleep(0.5)
                    continue
                except:
                    pass
                if driver.title == u"淘数据_店铺搜索":
                    try:
                        driver.find_element_by_xpath("//a[@class='ui_close']").click()
                        time.sleep(0.5)
                    except:
                        pass
                    continue
                try:
                    datas = []
                    for title in ["店铺", "主营", "掌柜", "地址", "开店时间"]:
                        element = driver.find_element_by_xpath("//div[@class='J_Shop_Info shop_homepage_detail_index']//span[contains(text(),'" + title + "')]/following-sibling::span[1]")
                        datas.append(element.text.strip())
                    #     print element.text,
                    # print
                    em.append_datas(datas+[a,b,c])
                except:
                    continue
            em.save(u"d:\\服装鞋包-" + k.replace('/', '_') + "-热销店铺排行.xlsx")
    except:
        # print "error"
        print traceback.format_exc()
