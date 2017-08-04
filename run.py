#encoding=utf-8
import GloableData
from createOrders import *

if __name__ == '__main__':
    CreateDatas.get_database_datas()
    ImportDatas.insert_json_to_sql_order()