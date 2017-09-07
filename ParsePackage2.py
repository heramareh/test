#encoding=utf-8

import json
from ExcelManage2 import ExcelManage2
titles = ["No.", "APIName", "APIProtocol", "RequestURL", "RequestMethod", "ParamsInfo", "APITestCase", "Active", "UserName", "Data", "Result", "status"]
keys = ["No.", "APIName", "APIProtocol", "url", "type", "contentType", "APITestCase", "Active", "user", "param", "result", "status"]
data_file_name = "all_result.txt"
result_file_name = "all_result.xlsx"

def read_file(file_name):
    with open(data_file_name) as fp:
        content = fp.read()
    return content

def json_str_to_dict(json_str):
    return json.loads(json_str)

def parse(data):
    all = []
    for id, i in enumerate(data, 1):
        result = {}
        result['No.'] = str(id)
        result['APIProtocol'] = "HTTP"
        result['APITestCase'] = str(id)
        result['Active'] = 'n'
        for k,v in i.items():
            result[k] = str(v)
        all.append(result)
    return all

def write_in_excel(all, file_name):
    em = ExcelManage2()
    em.append_datas(titles)
    for result in all:
        em.append_datas([result[key] if result.has_key(key) else None for key in keys])
    em.save(file_name)

if __name__ == "__main__":
    # 读取文件内容
    content = read_file(data_file_name)
    # 江读取到的json串转成字典组成的列表
    datas = json_str_to_dict(content)
    # 对数据进行解析
    results = parse(datas)
    # 将解析结果写入excel文件
    write_in_excel(results, result_file_name)
