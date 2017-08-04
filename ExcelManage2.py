#encoding=utf-8

from openpyxl import Workbook, load_workbook
import random, os


class ExcelManage2(object):
    def __init__(self, sheet_name = None):
        self.wb = Workbook()
        self.sheet_name = sheet_name
        if self.sheet_name == None:
            self.ws = self.wb.active
        else:
            self.ws = self.wb.get_sheet_by_name(self.sheet_name)

    def create_datas_goods(self, nick_list, outer_id, lens, file_path):
        size = ['SS', 'S', 'M', 'L', 'XL', 'XXL', 'XXXL']
        # 设置第一行标题
        self.ws.append(['nick', 'num_iid', 'skus-sku-outer_id', 'skus-sku-sku_id'])
        # 生成随机数
        for i in xrange(lens):
            self.ws.append([random.choice(nick_list), str(random.randint(int('1'+'0'*11), int('9'*12))), outer_id+str(random.randint(100, 200))+random.choice(size), str(random.randint(int('1'+'0'*12), int('9'*13)))])
        self.wb.save(file_path)

    def append_datas(self, datas):
        u"""按行插入数据"""
        self.ws.append(datas)

    def save(self, file_path):
        u"""保存文件"""
        self.wb.save(file_path)

if __name__ == '__main__':
    # em = ExcelManage2()
    # nick_list = [u'淘宝店铺001_100071', u'123321_100071', u'999999_100071', u'22222_100071', u'淘宝店铺002_100071']
    # goods_file_path = os.path.join(ConfigManage.get_input_path(), "test01_Basic_Files", u"test01_004_002_input.xlsx")
    # file_path = os.path.join(ConfigManage.get_input_path(), "test02_Order_Manage", u"test02_001_002_input.xlsx")
    # # em.create_datas_goods(nick_list, 'D-C301_T146-',10,file_path)
    # em.create_datas_orders(goods_file_path, file_path)
    pass