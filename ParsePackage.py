#encoding=utf-8

import json
import re
from ExcelManage2 import ExcelManage2
foundData = None

def _findData(sourceDict, find):
    global foundData
    u"""在字典对象中递归查找需要被存储的数据"""
    if foundData is not None:
        return
    if isinstance(sourceDict, dict):
        if sourceDict.has_key(find):
            foundData = sourceDict[find]
        else:
            for v in sourceDict.values():
                _findData(v, find)
    else:
        return

def findData(sourceDict, find):
    global foundData
    foundData = None
    _findData(sourceDict, find)
    if foundData:
        return foundData
    else:
        return None

def getData(sourceDict, find):
    if sourceDict.has_key(find):
        return sourceDict[find]
    else:
        return None

with open("packages.txt") as fp:
    content = fp.read()
# content = re.sub(r"\\x3c", r"<", content)
# content = re.sub(r"\\x3e", r">", content)
# content = re.sub(r"\\x3FF", r"", content)
# content = re.sub(r"\\x26([a-zA-Z]{2,6});", r"&\1;", content)
# packages_list = json.loads(content)
content = re.sub(r"null", r"None",content)
content = re.sub(r"\\/", r"/",content)
# content = re.sub(r"\\r\\n", r"\n",content)
packages_list = eval(content)
print len(packages_list)
# for i in packages_list:
#     print type(i)
titles = ["No.", "APIProtocol", "RequestURL", "RequestMethod", "ParamsInfo", "Data", "frame.number", "http.response_in", "http.request_in", "http.next_request_in", "http.next_response_in", "http.prev_request_in", "http.prev_response_in"]
result_keys = ['No', "frame.coloring_rule.name", "http.request.full_uri", "http.request.method", "http.content_type", "http.file_data", "frame.number", "http.response_in", "http.request_in", "http.next_request_in", "http.next_response_in", "http.prev_request_in", "http.prev_response_in"]
em = ExcelManage2()
em.append_datas(titles)
for id, i in enumerate(packages_list, 1):
    result = {}
    result['No'] = id
    source = i["_source"]["layers"]
    if source.has_key("frame"):
        frame = source['frame']
        for key in ["frame.number", "frame.coloring_rule.name"]:
            result[key] = getData(frame, key)
    if source.has_key("http"):
        http = source['http']
        for key in ["_ws.expert.message", "http.request.method"]:
            result[key] = findData(http, key)
        for key in ["http.response_in", "http.request_in", "http.next_request_in", "http.next_response_in", "http.prev_request_in", "http.prev_response_in", "http.request.full_uri", "http.host", "http.content_type", "http.file_data"]:
            result[key] = getData(http, key)
    em.append_datas([result[key] for key in result_keys])
em.save("d:\\ParseResult.xlsx")