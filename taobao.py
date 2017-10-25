#encoding=utf-8
import re
import traceback

import GloableData
from ExcelManage2 import ExcelManage2
from createOrders import *
import requests
import json

if __name__ == '__main__':
    # CreateDatas.get_database_datas()
    # ImportDatas.insert_json_to_sql_order()
    # date={}
    # login = requests.post(url="https://login.taosj.com/?redirectURL=http%3A%2F%2Fwww.taosj.com%2F", data={'loginCode':'18910438805','loginPassword':'123456789'},timeout=60)
    # print login.cookies
    # url = requests.get(url="http://www.taosj.com/industry/index.html#/data/hotshops/?cid=50000436&pcid=2&brand=&type=ALL&date=&pageNo=1", cookies = login.cookies)
    # print login.status_code
    # result = requests.get("http://www.taosj.com/industry/index.html#/data/hotshops/?cid=50000436&pcid=2&brand=&type=ALL&date=&pageNo=1")
    # print result.content

    em = ExcelManage2()
    em.append_datas([u"店铺", u"卖家", u"地址", u"销售量", u"宝贝数量"])

    # # 女装
    # filename = u"女装_"
    # url = "https://shopsearch.taobao.com/search?app=shopsearch&q=%E5%A5%B3%E8%A3%85&js=1&initiative_id=staobaoz_20170822&ie=utf8&loc=%E6%9D%AD%E5%B7%9E&s="
    # 男装
    filename = u"男装_"
    url = "https://shopsearch.taobao.com/search?app=shopsearch&ie=utf8&initiative_id=staobaoz_20170822&js=1&q=%E7%94%B7%E8%A3%85&suggest=0_1&_input_charset=utf-8&wq=nan&suggest_query=nan&source=suggest&loc=%E6%9D%AD%E5%B7%9E&s="
    for i in xrange(5000/20):
        # print requests.get(url + str(i*20)).content
        try:
            results = re.findall(r'"uid":"\d*","title":"(.*?)","nick":"(.*?)","provcity":"(.*?)","totalsold":(\d*),"procnt":(\d*),', requests.get(url + str(i*20)).content)
            for result in results:
                em.append_datas(list(result))
        except Exception, e:
            print "error:"+str(e)
            continue
    em.save("d:\\" + filename + time.strftime("%Y-%m-%d") + ".xlsx")
