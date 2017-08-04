#encoding=utf-8
import json

s = """{
    "trade_fullinfo_get_response": {
        "trade": {
            "adjust_fee": "0.00",
            "alipay_id": 2089112345692104,
            "alipay_no": "2016061231451001480256872104",
            "alipay_point": 0,
            "available_confirm_fee": "323.58",
            "buyer_alipay_no": "1334642104@qq.com",
            "buyer_area": "陕西联通",
            "buyer_cod_fee": "0.00",
            "buyer_email": "1334642104@qq.com",
            "buyer_ip": "MASwLjEwNS4xNxyuZxQ:",
            "buyer_message": "周末配送 ",
            "buyer_nick": "采购004",
            "buyer_obtain_point_fee": 0,
            "buyer_rate": false,
            "cod_fee": "0.00",
            "cod_status": "NEW_CREATED",
            "commission_fee": "0.00",
            "created": "2017-07-28 14:18:32",
            "discount_fee": "10.42",
            "has_post_fee": true,
            "has_yfx": false,
            "is_3D": false,
            "is_brand_sale": false,
            "is_daixiao": false,
            "is_force_wlb": false,
            "is_lgtype": false,
            "is_part_consign": false,
            "is_sh_ship": false,
            "is_wt": false,
            "modified": "2017-07-28 14:18:32",
            "orders": {
                "order": [
                    {
                        "adjust_fee": "5.00",
                        "buyer_rate": false,
                        "cid": 50010222,
                        "discount_fee": "10.00",
                        "divide_order_fee": "86.20",
                        "is_daixiao": false,
                        "is_oversold": false,
                        "num": 1,
                        "num_iid": 100018587597,
                        "oid": 500001083,
                        "order_from": "WAP,WAP",
                        "outer_iid": "B-C352-F301-",
                        "outer_sku_id": "B-C352-F301-356M",
                        "part_mjz_discount": "0.00",
                        "payment": "100.00",
                        "pic_path": "https://gd4.alicdn.com/bao/uploaded/i4/TB1SqW2MVXXXXXEaXXXXXXXXXXX_!!0-item_pic.jpg_400x400.jpg",
                        "price": "100.00",
                        "refund_status": "NO_REFUND",
                        "seller_rate": false,
                        "seller_type": "B",
                        "sku_id": "5000000017",
                        "sku_properties_name": "颜色:黑色;尺码:L",
                        "snapshot_url": "g:865383121623375_1",
                        "status": "WAIT_SELLER_SEND_GOODS",
                        "title": "正常001",
                        "total_fee": "85.00"
                    },
                    {
                        "adjust_fee": "11.00",
                        "buyer_rate": false,
                        "cid": 50010221,
                        "discount_fee": "30.00",
                        "divide_order_fee": "117.77",
                        "is_daixiao": false,
                        "is_oversold": false,
                        "num": 1,
                        "num_iid": 100018587598,
                        "oid": 500001084,
                        "order_from": "WAP,WAP",
                        "outer_iid": "B-C352-F302-",
                        "outer_sku_id": "B-C352-F302-357M",
                        "part_mjz_discount": "0.00",
                        "payment": "100.00",
                        "pic_path": "https://gd4.alicdn.com/bao/uploaded/i4/TB1SqW2MVXXXXXEaXXXXXXXXXXX_!!0-item_pic.jpg_400x400.jpg",
                        "price": "100.00",
                        "refund_status": "NO_REFUND",
                        "seller_rate": false,
                        "seller_type": "B",
                        "sku_id": "5000000018",
                        "sku_properties_name": "颜色:黑色;尺码:L",
                        "snapshot_url": "k:1368678412452047_1",
                        "status": "WAIT_SELLER_SEND_GOODS",
                        "title": "正常001",
                        "total_fee": "109.00"
                    }
                ]
            },
            "pay_time": "2017-07-28 14:18:32",
            "payment": "323.58",
            "pcc_af": 0,
            "point_fee": 0,
            "post_fee": "0.00",
            "promotion_details": {
                "promotion_detail": [
                    {
                        "promotion_name": "收藏先发货",
                        "promotion_id": "Tmall$tmallItemPromotion-1513716101_9422588990",
                        "id": 1368678412452030,
                        "promotion_desc": "收藏先发货:省10.00元",
                        "discount_fee": "10.00"
                    }
                ]
            },
            "real_point_fee": 0,
            "received_payment": "0.00",
            "receiver_address": "陕西省西安市新城区解放路100   ",
            "receiver_city": "西安市",
            "receiver_district": "新城区",
            "receiver_mobile": "13312343069",
            "receiver_name": "王小贝10048",
            "receiver_phone": "029-8989999",
            "receiver_state": "陕西省",
            "receiver_town": "新城区",
            "receiver_zip": "710000 ",
            "seller_alipay_no": "wanglu12@163.com",
            "seller_can_rate": false,
            "seller_cod_fee": "0.00",
            "seller_email": "wanglu12@163.com",
            "seller_flag": 3,
            "seller_memo": "改为发顺丰",
            "seller_mobile": "15521261518",
            "seller_name": "杨明",
            "seller_nick": "淘宝店铺003_100018",
            "seller_rate": false,
            "service_tags": {
                "logistics_tag": [
                    {
                        "logistic_service_tag_list": {
                            "logistic_service_tag": [
                                {
                                    "service_type": "FAST",
                                    "service_tag": "origAreaId:350582;lgType:-4"
                                }
                            ]
                        },
                        "order_id": "1368678412452073"
                    }
                ]
            },
            "shipping_type": "express",
            "snapshot_url": "k:1368678412452073_1",
            "status": "WAIT_SELLER_SEND_GOODS",
            "tid": 500001084,
            "title": "淘宝店铺003",
            "total_fee": "488.00",
            "trade_from": "WAP,WAP",
            "type": "fixed"
        }
    }
}"""

print json.loads(s)


"""{
    "trade_fullinfo_get_response": {
        "trade": {
            "adjust_fee": "0.00",
            "alipay_id": 2089112345692104,
            "alipay_no": "2016061231451001480256872104",
            "alipay_point": 0,
            "available_confirm_fee": "323.58",
            "buyer_alipay_no": "1334642104@qq.com",
            "buyer_area": "陕西联通",
            "buyer_cod_fee": "0.00",
            "buyer_email": "1334642104@qq.com",
            "buyer_ip": "MASwLjEwNS4xNxyuZxQ:",
            "buyer_message": "周末配送 ",             随机
            "buyer_nick": "采购004",                  随机:nick_平台单号(tid)
            "buyer_obtain_point_fee": 0,
            "buyer_rate": false,
            "cod_fee": "0.00",
            "cod_status": "NEW_CREATED",
            "commission_fee": "0.00",
            "created": "2017-07-28 14:18:32",       当前时间
            "discount_fee": "10.42",
            "has_post_fee": true,
            "has_yfx": false,
            "is_3D": false,
            "is_brand_sale": false,
            "is_daixiao": false,
            "is_force_wlb": false,
            "is_lgtype": false,
            "is_part_consign": false,
            "is_sh_ship": false,
            "is_wt": false,
            "modified": "2017-07-28 14:18:32",      当前时间
            "orders": {
                "order": [
                    {
                        "adjust_fee": "5.00",
                        "buyer_rate": false,
                        "cid": 50010222,            随机：8位
                        "discount_fee": "10.00",
                        "divide_order_fee": "86.20",
                        "is_daixiao": false,
                        "is_oversold": false,
                        "num": 1,                   随机
                        "num_iid": 100018587597,    数据库good  num_iid
                        "oid": 500001083,           随机：8位
                        "order_from": "WAP,WAP",
                        "outer_iid": "B-C352-F301-",    数据库good  product_no
                        "outer_sku_id": "B-C352-F301-356M",     数据库good  sku_no
                        "part_mjz_discount": "0.00",
                        "payment": "100.00",
                        "pic_path": "https://gd4.alicdn.com/bao/uploaded/i4/TB1SqW2MVXXXXXEaXXXXXXXXXXX_!!0-item_pic.jpg_400x400.jpg",      数据库good  pic
                        "price": "100.00",      随机：50-500
                        "refund_status": "NO_REFUND",           列表
                        "seller_rate": false,
                        "seller_type": "B",
                        "sku_id": "5000000017",         数据库good  platform_sku_id
                        "sku_properties_name": "颜色:黑色;尺码:L",    数据库good  c1.name, c2.name
                        "snapshot_url": "g:865383121623375_1",
                        "status": "WAIT_SELLER_SEND_GOODS",         列表
                        "title": "正常001",              数据库good  product_name
                        "total_fee": "85.00"    随机：50-500
                    },
                    {
                        "adjust_fee": "11.00",
                        "buyer_rate": false,
                        "cid": 50010221,
                        "discount_fee": "30.00",
                        "divide_order_fee": "117.77",
                        "is_daixiao": false,
                        "is_oversold": false,
                        "num": 1,
                        "num_iid": 100018587598,
                        "oid": 500001084,
                        "order_from": "WAP,WAP",
                        "outer_iid": "B-C352-F302-",
                        "outer_sku_id": "B-C352-F302-357M",
                        "part_mjz_discount": "0.00",
                        "payment": "100.00",
                        "pic_path": "https://gd4.alicdn.com/bao/uploaded/i4/TB1SqW2MVXXXXXEaXXXXXXXXXXX_!!0-item_pic.jpg_400x400.jpg",
                        "price": "100.00",
                        "refund_status": "NO_REFUND",
                        "seller_rate": false,
                        "seller_type": "B",
                        "sku_id": "5000000018",
                        "sku_properties_name": "颜色:黑色;尺码:L",
                        "snapshot_url": "k:1368678412452047_1",
                        "status": "WAIT_SELLER_SEND_GOODS",
                        "title": "正常001",
                        "total_fee": "109.00"
                    }
                ]
            },
            "pay_time": "2017-07-28 14:18:32",      当前时间
            "payment": "323.58",                    随机：50-500
            "pcc_af": 0,
            "point_fee": 0,
            "post_fee": "0.00",
            "promotion_details": {
                "promotion_detail": [
                    {
                        "promotion_name": "收藏先发货",
                        "promotion_id": "Tmall$tmallItemPromotion-1513716101_9422588990",
                        "id": 1368678412452030,
                        "promotion_desc": "收藏先发货:省10.00元",
                        "discount_fee": "10.00"
                    }
                ]
            },
            "real_point_fee": 0,
            "received_payment": "0.00",
            "receiver_address": "陕西省西安市新城区解放路100   ",   数据库 detail_address
            "receiver_city": "西安市",           数据库city,
            "receiver_district": "新城区",      数据库 district,
            "receiver_mobile": "13312343069",   随机手机号
            "receiver_name": "王小贝10048",     随机：王小贝+tid
            "receiver_phone": "029-8989999",    随机电话号码
            "receiver_state": "陕西省",         数据库province,
            "receiver_town": "新城区",          数据库 district,
            "receiver_zip": "710000 ",          
            "seller_alipay_no": "wanglu12@163.com",
            "seller_can_rate": false,
            "seller_cod_fee": "0.00",
            "seller_email": "wanglu12@163.com",
            "seller_flag": 3,                   随机：0-5
            "seller_memo": "改为发顺丰",        客服备注：列表
            "seller_mobile": "15521261518",     随机
            "seller_name": "杨明",              随机：杨明+tid
            "seller_nick": "淘宝店铺003_100018",        列表seller_nick
            "seller_rate": false,
            "service_tags": {
                "logistics_tag": [
                    {
                        "logistic_service_tag_list": {
                            "logistic_service_tag": [
                                {
                                    "service_type": "FAST",
                                    "service_tag": "origAreaId:350582;lgType:-4"
                                }
                            ]
                        },
                        "order_id": "1368678412452073"
                    }
                ]
            },
            "shipping_type": "express",
            "snapshot_url": "k:1368678412452073_1",
            "status": "WAIT_SELLER_SEND_GOODS",     列表
            "tid": 500001084,                       随机:7位
            "title": "淘宝店铺003",                 列表
            "total_fee": "488.00",                  随机：50-500
            "trade_from": "WAP,WAP",
            "type": "fixed"
        }
    }
}"""