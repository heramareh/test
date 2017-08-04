# encoding=utf-8
import ConfigParser
import random
import sys
import MySQLdb
import time
from flask import json
import GloableData

class ConfigManage(object):
    u"""读取配置文件"""
    configManage = ConfigParser.SafeConfigParser(allow_no_value=True)
    configManage.read("config.ini")

    @classmethod
    def getDefault(cls, options):
        u"""获取Default的子项目"""
        return ConfigManage.configManage.get("DEFAULT", options)

    @classmethod
    def getDataBase(cls):
        u"""获取要连接的数据库"""
        return ConfigManage.getDefault("database")

    @classmethod
    def getDb(cls, option):
        u"""获取连接数据库信息"""
        return ConfigManage.configManage.get(ConfigManage.getDataBase(), option)

    @classmethod
    def getTenantId(cls):
        u"""获取tenant_id"""
        return ConfigManage.getDefault("tenant_id")

class MysqlManage(object):
    u"""Mysql数据库操作类"""

    def __init__(self, db=ConfigManage.getDb("db_db"), sid=ConfigManage.getDataBase()):
        self.section = sid
        self.host = ConfigManage.getDb("db_host")
        self.port = int(ConfigManage.getDb("db_port"))
        self.username = ConfigManage.getDb("db_user")
        self.password = ConfigManage.getDb("db_pass")
        self.db = db
        self.charset = ConfigManage.getDb("db_charset")
        self.conn = None
        self.cursor = None

    def connect(self):
        u"""连接数据库"""
        try:
            self.conn = MySQLdb.connect(
                host=self.host,
                port=self.port,
                user=self.username,
                passwd=self.password,
                db=self.db,
                charset=self.charset)
            # print u"连接数据库：" + self.db + "成功！"
        except Exception, e:
            print u"连接数据库：" + self.db + "失败：" + str(e)
            assert 1 == 2, u"连接数据库：" + self.db + "失败：" + str(e)

    def usr_database(self, db):
        self.execute_sql("use " + db + ";")
        # print u"切换数据库：" + db + "成功！"

    def get_cursor(self):
        self.cursor = self.conn.cursor()
        return self.cursor

    def create_database(self, dbname):
        u"""创建库"""
        try:
            self.connect()
            self.get_cursor()
            self.cursor.execute(
                "CREATE DATABASE IF NOT EXISTS " + dbname + " DEFAULT CHARSET utf8 COLLATE utf8_general_ci;")
            # print u"创建数据库：" + dbname + "成功！"
        except Exception, e:
            print u"创建数据库：" + dbname + "失败：" + str(e)
            raise Exception(u"创建数据库：" + dbname + u"失败：" + str(e))
        finally:
            self.close()

    def execute_sql(self, sql):
        u"""执行sql语句"""
        try:
            self.cursor.execute(sql)
            # print u"执行sql语句成功！"
        except MySQLdb.Error, e:
            print u"Mysql Error %d: %s" % (e.args[0], e.args[1])
            raise Exception(u"Mysql Error %d: %s" % (e.args[0], e.args[1]))

    def executemany_sql(self, sql, datas):
        u"""执行sql语句"""
        try:
            self.cursor.executemany(sql, datas)
            # print u"执行sql语句成功！"
        except MySQLdb.Error, e:
            print u"Mysql Error %d: %s" % (e.args[0], e.args[1])
            raise Exception(u"Mysql Error %d: %s" % (e.args[0], e.args[1]))

    def update(self, sql):
        u"""执行update语句"""
        try:
            self.execute_sql(sql)
            # print u"执行update语句成功！"
            self.commit()
        except MySQLdb.Error, e:
            print u"Mysql Error %d: %s" % (e.args[0], e.args[1])
            raise Exception(u"Mysql Error %d: %s" % (e.args[0], e.args[1]))
        finally:
            self.close()

    def update_many(self, sql, datas):
        u"""执行sql语句"""
        try:
            self.executemany_sql(sql, datas)
            # print u"执行sql语句成功！"
            self.commit()
        except MySQLdb.Error, e:
            print u"Mysql Error %d: %s" % (e.args[0], e.args[1])
            raise Exception(u"Mysql Error %d: %s" % (e.args[0], e.args[1]))
        finally:
            self.close()

    def get_content(self):
        u"""获取查询结果"""
        try:
            res = self.cursor.fetchone()
            # print u"获取查询结果成功！"
            return res
        except MySQLdb.Error, e:
            print u"Mysql Error %d: %s" % (e.args[0], e.args[1])
            raise Exception(u"Mysql Error %d: %s" % (e.args[0], e.args[1]))

    def get_content_all(self):
        u"""获取所有查询结果"""
        try:
            resSet = self.cursor.fetchall()
            # print u"获取所有查询结果成功！"
            return resSet
        except MySQLdb.Error, e:
            print u"Mysql Error %d: %s" % (e.args[0], e.args[1])
            raise Exception(u"Mysql Error %d: %s" % (e.args[0], e.args[1]))

    def get_content_by_line(self, lines):
        u"""获取指定条数的数据"""
        try:
            resTuple = self.cursor.fetchmany(lines)
            # print u"获取指定条数的数据成功！"
            return resTuple
        except MySQLdb.Error, e:
            print u"Mysql Error %d: %s" % (e.args[0], e.args[1])
            raise Exception(u"Mysql Error %d: %s" % (e.args[0], e.args[1]))
        finally:
            self.close()

    def commit(self):
        u"""提交事务"""
        try:
            self.conn.commit()
            # print u"提交事务成功！"
        except MySQLdb.Error, e:
            print u"Mysql Error %d: %s" % (e.args[0], e.args[1])
            raise Exception(u"Mysql Error %d: %s" % (e.args[0], e.args[1]))

    def close(self):
        u"""断开连接"""
        try:
            if None == self.cursor:
                pass
            else:
                self.cursor.close()
                self.conn.close()
                # print u"断开连接成功！"
        except MySQLdb.Error, e:
            print u"断开连接失败：" + str(e)
            raise Exception(u"断开连接失败：" + str(e))

class DataBaseInfo(object):
    u"""读取数据库信息"""

    def __init__(self):
        self.tenant_id = ConfigManage.getTenantId()

    def conn(self):
        u"""连接数据库，获取游标"""
        self.mm = MysqlManage()
        self.mm.connect()
        self.mm.get_cursor()

    def close(self):
        u"""断开数据库连接"""
        self.mm.close()

    def get_shop_names(self):
        u"""获取当前用户所有平台类型为淘宝的店铺名"""
        sql = "SELECT shop_name FROM shop WHERE shop.platform_type = 1 and shop.tenant_id = " + self.tenant_id + ";"
        self.mm.execute_sql(sql)
        shop_names = self.mm.get_content_all()
        return [x[0] for x in shop_names]

    def get_seller_nick(self):
        u"""获取所有平台类型为淘宝的店铺的seller_nick"""
        sql = "select seller_nick from shop where shop.platform_type = 1 and tenant_id = " + self.tenant_id + ";"
        self.mm.execute_sql(sql)
        seller_nick = self.mm.get_content_all()
        return [x[0] for x in seller_nick]

    def get_all_city_of_province(self, province_id):
        u"""获取省的所有市"""
        sql = "select city_id, city_name from city where province_id = " + str(province_id) + ";"
        self.mm.execute_sql(sql)
        all_city_name = self.mm.get_content_all()
        cities = {}
        for x in all_city_name:
            cities[x[0]] = x[1]
        return cities

    def get_province_name(self, province_id):
        u"""获取省的名称"""
        sql = "SELECT province_name FROM province where province_id = " + str(province_id) + ";"
        self.mm.execute_sql(sql)
        content = self.mm.get_content_all()
        return [x[0] for x in content]

    def get_all_district_by_city(self, city_id):
        u"""获取市的所有区"""
        sql = "select district_id, district_name from district where city_id = " + str(city_id) + ";"
        self.mm.execute_sql(sql)
        content = self.mm.get_content_all()
        districts = {}
        for x in content:
            districts[x[0]] = x[1]
        return districts

    def get_all_addresses(self):
        u"""获取所有地址"""
        sql = "SELECT p.province_name,c.city_name,d.district_name FROM province p LEFT JOIN city c ON p.`province_id` = c.`province_id` LEFT JOIN district d ON d.`city_id` = c.`city_id` ORDER BY p.`province_id`;"
        self.mm.execute_sql(sql)
        content = self.mm.get_content_all()
        return [x for x in content if x[1] and x[2]]

    def get_stockout_goods(self):
        u"""获取缺货的商品"""
        # sql = "SELECT v.sku_id, v.sku_no, v.product_no, v.product_name, v.pic, c1.name, c2.name, p.num_iid, p.platform_sku_id FROM (SELECT * FROM v_stock WHERE tenant_id = " + self.tenant_id + " AND sale_number <= 0 and platform_type != null) v LEFT JOIN (SELECT * FROM customer_dict WHERE tenant_id = " + self.tenant_id + ") c1 ON v.size_type = c1.code AND c1.type = 'size_type' LEFT JOIN (SELECT * FROM customer_dict WHERE tenant_id = " + self.tenant_id + ") c2 ON v.color_type = c2.code AND c2.type = 'color_type' left join (select * from platform_product_match WHERE tenant_id = " + self.tenant_id + ") p on v.sku_id = p.sku_id;"
        # sql = "SELECT sku_id, sku_no FROM v_stock;"
        self.mm.execute_sql(GloableData.SQL % (self.tenant_id,self.tenant_id,"<=",self.tenant_id,self.tenant_id))
        content = self.mm.get_content_all()
        return list(content)

    def get_stockin_goods(self):
        u"""获取有存货的商品"""
        # sql = "SELECT v.sku_id, v.sku_no, v.product_no, v.product_name, v.pic, c1.name, c2.name, p.num_iid, p.platform_sku_id FROM (SELECT * FROM v_stock WHERE tenant_id = " + self.tenant_id + " AND sale_number > 0 and platform_type != null) v LEFT JOIN (SELECT * FROM customer_dict WHERE tenant_id = " + self.tenant_id + ") c1 ON v.size_type = c1.code AND c1.type = 'size_type' LEFT JOIN (SELECT * FROM customer_dict WHERE tenant_id = " + self.tenant_id + ") c2 ON v.color_type = c2.code AND c2.type = 'color_type' left join (select * from platform_product_match WHERE tenant_id = " + self.tenant_id + ") p on v.sku_id = p.sku_id;"
        # sql = "SELECT sku_id, sku_no FROM v_stock WHERE tenant_id = " + self.tenant_id + " AND sale_number > 0;"
        self.mm.execute_sql(GloableData.SQL % (self.tenant_id,self.tenant_id,">",self.tenant_id,self.tenant_id))
        content = self.mm.get_content_all()
        return list(content)

class RandomDatas(object):
    u"""随机数据生成"""

    @classmethod
    def get_nowtime(cls):
        u"""获取当前时间"""
        return u'' + time.strftime("%Y-%m-%d %H:%M:%S")

    @classmethod
    def random_digits(cls, length):
        u"""随机指定长度的数字字符串"""
        return random.randint(int('1' + '0' * (length - 1)), int('9' * length))

    @classmethod
    def random_mobile(cls):
        u"""随机手机号"""
        return str(random.randint(13500000000, 13999999999))

    @classmethod
    def random_address(cls, all_addresses):
        u"""随机收获地址：（省，市，区/县）"""
        return random.choice(all_addresses)

    @classmethod
    def random_detail_address(cls, address):
        u"""随机详细地址"""
        return address[0] + address[1] + address[2] + str(random.randint(1, 500)).zfill(3) + u"街道" + str(
            random.randint(1, 300)).zfill(3) + u"号"

    @classmethod
    def random_trade_key(cls):
        u"""随机一级key"""
        random_trade_dict = dict.fromkeys(GloableData.RANDOM_TRADE_KEY)
        random_trade_dict[u'tid'] = RandomDatas.random_digits(7)
        random_trade_dict[u'buyer_message'] = random.choice(GloableData.BUYER_MESSAGE)
        random_trade_dict[u'buyer_nick'] = u'nick_' + str(random_trade_dict[u'tid'])
        random_trade_dict[u'created'] = random_trade_dict[u'modified'] = random_trade_dict[u'pay_time']= RandomDatas.get_nowtime()
        random_trade_dict[u'payment'] = str(random.randint(50,500))
        address = RandomDatas.random_address(GloableData.ALL_ADDRESS)
        province, city, district = address
        detail_address = RandomDatas.random_detail_address(address)
        random_trade_dict[u'receiver_address'] = detail_address
        random_trade_dict[u'receiver_state'] = province
        random_trade_dict[u'receiver_city'] = city
        random_trade_dict[u'receiver_district'] = random_trade_dict[u'receiver_town'] = district
        random_trade_dict[u'receiver_mobile'] = random_trade_dict[u'receiver_phone'] = RandomDatas.random_mobile()
        random_trade_dict[u'receiver_name'] = u'王小贝_' + str(random_trade_dict[u'tid'])
        random_trade_dict[u'seller_flag'] = random.randint(0, 5)
        random_trade_dict[u'seller_memo'] = random.choice(GloableData.SELLER_MEMO)
        random_trade_dict[u'seller_mobile'] = RandomDatas.random_mobile()
        random_trade_dict[u'seller_name'] = u"杨明_" + str(random_trade_dict[u'tid'])
        random_trade_dict[u'seller_nick'] = random.choice(GloableData.SELLER_NICK)
        random_trade_dict[u'status'] = random.choice(GloableData.STATUS)
        random_trade_dict[u'title'] = random.choice(GloableData.SHOP_NAME)
        random_trade_dict[u'total_fee'] = str(random.randint(50,500))
        return random_trade_dict

    @classmethod
    def random_order_key(cls):
        u"""随机order的key"""
        random_order_dict = dict.fromkeys(GloableData.RANDOM_ORDER_KEY)
        random_order_dict[u'cid'] = RandomDatas.random_digits(8)
        # random_order_dict[u'num'] = random.randint(1, 3)
        random_order_dict[u'oid'] = RandomDatas.random_digits(8)
        random_order_dict[u'price'] = str(random.randint(50, 500))
        random_order_dict[u'refund_status'] = random.choice(GloableData.REFUND_STATUS)
        random_order_dict[u'status'] = random.choice(GloableData.STATUS)
        random_order_dict[u'total_fee'] = str(random.randint(50, 500))
        good = random.choice(GloableData.STOCKOUT_GOODS + GloableData.STOCKIN_GOODS)
        sku_id, sku_no, product_no, product_name, pic, size, color, num_iid, platform_sku_id = good
        random_order_dict[u'num_iid'] = int(num_iid)
        random_order_dict[u'outer_iid'] = product_no
        random_order_dict[u'outer_sku_id'] = sku_no
        random_order_dict[u'pic_path'] = pic if pic else ''
        random_order_dict[u'sku_id'] = platform_sku_id
        random_order_dict[u'sku_properties_name'] = u"颜色:" + color + ";尺码:" + size
        random_order_dict[u'title'] = product_name
        return dict(random_order_dict.items() + GloableData.DEFAULT_ORDER_KEY.items())

    @classmethod
    def random_one_order_one_goods(cls):
        u"""随机一单一货订单的order"""
        random_order_dict = RandomDatas.random_order_key()
        random_order_dict[u'num'] = 1
        return {u'order' : [random_order_dict]}

    @classmethod
    def random_one_order_more_goods(cls):
        u"""随机一单多货订单的order"""
        random_order_dicts = []
        for i in xrange(random.randint(1,4)):
            random_order_dict = RandomDatas.random_order_key()
            random_order_dict[u'num'] = random.randint(2,5)
            random_order_dicts.append(random_order_dict)
        return {u'order' : random_order_dicts}

class CreateDatas(object):
    u"""生成数据"""

    @classmethod
    def json_to_dict(cls, json_str):
        u"""json串转字典"""
        return json.loads(json_str)

    @classmethod
    def dict_to_json(cls, json_dict):
        u"""字典转json串"""
        return json.dumps(json_dict, ensure_ascii=False, sort_keys=True, separators=(',', ':'))

    @classmethod
    def create_one_order_one_goods_json(cls):
        u"""生成一单一货json串"""
        orders = {"orders" : RandomDatas.random_one_order_one_goods()}
        json_dict = dict(GloableData.DEFAULT_TRADE_KEY.items() + RandomDatas.random_trade_key().items() + orders.items())
        return {"trade_fullinfo_get_response": {"trade": json_dict}}

    @classmethod
    def create_one_order_more_goods_json(cls):
        u"""生成一单多货json串"""
        orders = {"orders" : RandomDatas.random_one_order_more_goods()}
        json_dict = dict(GloableData.DEFAULT_TRADE_KEY.items() + RandomDatas.random_trade_key().items() + orders.items())
        return {"trade_fullinfo_get_response": {"trade": json_dict}}

    @classmethod
    def create_jsons(cls):
        jsons = []
        for i in xrange(int(ConfigManage.getDefault("one_order_one_goods_count"))):
            jsons.append(CreateDatas.create_one_order_one_goods_json())
        for j in xrange(int(ConfigManage.getDefault("one_order_more_goods_count"))):
            jsons.append(CreateDatas.create_one_order_more_goods_json())
        return jsons

    def create_order(self):
        u"""生成order"""
        order = dict.fromkeys(GloableData.ORDER_KEY-GloableData.DEFAULT_ORDER_KEY.keys())
        return order

    def create_orders(self, num=1):
        u"""生成orders"""
        orders = {"order": []}
        for i in xrange(num):
            orders["order"].append(self.create_order())
        return orders

    @classmethod
    def get_database_datas(cls):
        u"""获取数据库中的数据"""
        dbi = DataBaseInfo()
        dbi.conn()
        GloableData.ALL_ADDRESS = dbi.get_all_addresses()
        GloableData.SHOP_NAME = dbi.get_shop_names()
        GloableData.SELLER_NICK = dbi.get_seller_nick()
        GloableData.STOCKIN_GOODS = dbi.get_stockin_goods()
        GloableData.STOCKOUT_GOODS = dbi.get_stockout_goods()
        dbi.close()

class ImportDatas(object):
    u"""导入数据"""

    @classmethod
    def insert_json_to_sql_order(cls):
        u"""向数据库jdp_tb_trade表插入数据"""
        content = []
        for json_dict in CreateDatas.create_jsons():
            child = json_dict['trade_fullinfo_get_response']['trade']
            tid = child['tid']
            status = child['status']
            type = child['type']
            seller_nick = child['seller_nick']
            buyer_nick = child['buyer_nick']
            created = modified = jdp_created = jdp_modified = RandomDatas.get_nowtime()
            jdp_hashcode = str(RandomDatas.random_digits(9))
            jdp_response = CreateDatas.dict_to_json(json_dict)
            # print jdp_response
            content.append((tid, status, type, seller_nick, buyer_nick, created, modified, jdp_hashcode, jdp_response,
                            jdp_created, jdp_modified))
        sql = "insert into jdp_tb_trade values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        ImportDatas.update_data(sql, content)

    @classmethod
    def update_data(cls, sql, content):
        u"""向sys_info数据库中插入数据"""
        mm = MysqlManage('sys_info')
        mm.connect()
        mm.get_cursor()
        mm.executemany_sql(sql, content)
        mm.commit()
        mm.close()

if __name__ == '__main__':
    dbi = DataBaseInfo()
    dbi.conn()
    all_addresses = dbi.get_all_addresses()
    dbi.close()
    # for index in xrange(int(ConfigManage.getCreateOrderCount())):
    #     province, city, district = RandomDatas.random_address(all_addresses)
    #     print province+city+district+str(random.randint(1,500)).zfill(3)+u"街道"+str(random.randint(1,300)).zfill(3)+u"号"
    for k, v in CreateDatas().create_orders().items():
        print k, v
