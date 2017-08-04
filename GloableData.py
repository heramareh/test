# encoding=utf-8

# json串中所有一级key
TRADE_KEY = (u'seller_email', u'promotion_details', u'alipay_id', u'is_sh_ship', u'point_fee', u'receiver_mobile',
             u'seller_can_rate', u'seller_memo', u'is_lgtype', u'available_confirm_fee', u'buyer_cod_fee',
             u'seller_alipay_no', u'has_post_fee', u'pay_time', u'modified', u'shipping_type', u'receiver_address',
             u'is_daixiao', u'orders', u'cod_fee', u'is_force_wlb', u'receiver_district', u'receiver_city', u'title',
             u'buyer_message', u'has_yfx', u'snapshot_url', u'real_point_fee', u'is_3D', u'pcc_af', u'post_fee', u'tid',
             u'seller_cod_fee', u'seller_mobile', u'receiver_phone', u'seller_nick', u'status', u'is_part_consign',
             u'receiver_zip', u'total_fee', u'seller_rate', u'commission_fee', u'seller_flag', u'buyer_email',
             u'cod_status', u'buyer_rate', u'is_wt', u'trade_from', u'payment', u'buyer_nick', u'buyer_area',
             u'buyer_alipay_no', u'seller_name', u'created', u'discount_fee', u'type', u'adjust_fee', u'buyer_ip',
             u'is_brand_sale', u'service_tags', u'receiver_town', u'buyer_obtain_point_fee', u'received_payment',
             u'receiver_state', u'alipay_point', u'receiver_name', u'alipay_no')
# 需要随机的一级key
RANDOM_TRADE_KEY = (
u'buyer_message', u'buyer_nick', u'created', u'modified', u'pay_time', u'payment', u'receiver_address',
u'receiver_city', u'receiver_district', u'receiver_mobile', u'receiver_name', u'receiver_phone', u'receiver_state',
u'receiver_town', u'seller_flag', u'seller_memo', u'seller_mobile', u'seller_name', u'seller_nick', u'status', u'tid',
u'title', u'total_fee')
# 取默认值的一级key
DEFAULT_TRADE_KEY = {u'adjust_fee': u'0.00', u'alipay_id': 2089112345692104L,
                     u'alipay_no': u'2016061231451001480256872104', u'alipay_point': 0,
                     u'available_confirm_fee': u'323.58', u'buyer_alipay_no': u'1334642104@qq.com',
                     u'buyer_area': u'山西联通', u'buyer_cod_fee': u'0.00', u'buyer_email': u'1334642104@qq.com',
                     u'buyer_ip': u'MASwLjEwNS4xNxyuZxQ:', u'buyer_obtain_point_fee': 0, u'buyer_rate': False,
                     u'cod_fee': u'0.00', u'cod_status': u'NEW_CREATED', u'commission_fee': u'0.00',
                     u'discount_fee': u'10.42', u'has_post_fee': True, u'has_yfx': False, u'is_3D': False,
                     u'is_brand_sale': False, u'is_daixiao': False, u'is_force_wlb': False, u'is_lgtype': False,
                     u'is_part_consign': False, u'is_sh_ship': False, u'is_wt': False, u'pcc_af': 0, u'point_fee': 0,
                     u'post_fee': u'0.00', u'promotion_details': {u'promotion_detail': [
        {u'discount_fee': u'10.00', u'promotion_id': u'Tmall$tmallItemPromotion-1513716101_9422588990',
         u'promotion_desc': u'收藏先发货:省10.00元', u'promotion_name': u'收藏先发货', u'id': 1368678412452030L}]},
                     u'real_point_fee': 0, u'received_payment': u'0.00', u'receiver_zip': u'710000 ',
                     u'seller_alipay_no': u'wanglu12@163.com', u'seller_can_rate': False, u'seller_cod_fee': u'0.00',
                     u'seller_email': u'wanglu12@163.com', u'seller_rate': False, u'service_tags': {u'logistics_tag': [
        {u'order_id': u'1368678412452073', u'logistic_service_tag_list': {
            u'logistic_service_tag': [{u'service_type': u'FAST', u'service_tag': u'origAreaId:350582;lgType:-4'}]}}]},
                     u'shipping_type': u'express', u'snapshot_url': u'k:1368678412452073_1', u'trade_from': u'WAP,WAP',
                     u'type': u'fixed'}
# json串中所有orders['order'][i]下的key
ORDER_KEY = (u'sku_id', u'refund_status', u'seller_type', u'num', u'outer_sku_id', u'outer_iid', u'is_daixiao',
             u'sku_properties_name', u'part_mjz_discount', u'title', u'snapshot_url', u'order_from', u'status',
             u'price', u'oid', u'buyer_rate', u'payment', u'divide_order_fee', u'seller_rate', u'cid', u'discount_fee',
             u'adjust_fee', u'num_iid', u'is_oversold', u'total_fee', u'pic_path')
# 需要随机的order的key
RANDOM_ORDER_KEY = (
    u'cid', u'num', u'num_iid', u'oid', u'outer_iid', u'outer_sku_id', u'pic_path', u'price', u'refund_status',
    u'sku_id',
    u'sku_properties_name', u'status', u'title', u'total_fee')
# orders['order'][i]下取默认值的key
DEFAULT_ORDER_KEY = {u'adjust_fee': u'5.00', u'buyer_rate': False, u'discount_fee': u'10.00',
                     u'divide_order_fee': u'86.20', u'is_daixiao': False, u'is_oversold': False,
                     u'order_from': u'WAP,WAP', u'part_mjz_discount': u'0.00', u'payment': u'100.00',
                     u'seller_rate': False, u'seller_type': u'B', u'snapshot_url': u'g:865383121623375_1'}
# 订单状态
# STATUS = [u"TRADE_NO_CREATE_PAY", u"WAIT_BUYER_PAY", u"SELLER_CONSIGNED_PART", u"WAIT_SELLER_SEND_GOODS", u"WAIT_BUYER_CONFIRM_GOODS", u"TRADE_BUYER_SIGNED", u"TRADE_FINISHED", u"TRADE_CLOSED", u"TRADE_CLOSED_BY_TAOBAO", u"PAY_PENDING", u"WAIT_PRE_AUTH_CONFIRM"]
STATUS = [u"WAIT_SELLER_SEND_GOODS"]
# 退款状态
# REFUND_STATUS = [u"NO_REFUND", u"WAIT_SELLER_AGREE", u"WAIT_BUYER_RETURN_GOODS", u"WAIT_SELLER_CONFIRM_GOODS", u"SELLER_REFUSE_BUYER", u"CLOSED", u"SUCCESS"]
REFUND_STATUS = [u"NO_REFUND"]
# 买家留言
BUYER_MESSAGE = [u"发圆通快递", u"发顺丰快递", u"发申通快递", u"发韵达快运", u""]
# 客服备注
SELLER_MEMO = [u"圆通", u"正常发货", u"发顺丰", u"不改", u"", u"", u"", u"", u""]
# sql
SQL = """SELECT v.sku_id,v.sku_no,v.product_no,v.product_name,v.pic,c1.name,c2.name,v.num_iid,v.platform_sku_id FROM (SELECT vs.sku_id,vs.sku_no,vs.product_name,vs.product_no,vs.pic,vs.color_type,vs.size_type,p.num_iid,p.platform_sku_id FROM v_stock vs, (SELECT * FROM platform_product_match WHERE tenant_id = %s) p WHERE vs.tenant_id = %s AND vs.sale_number %s 0 AND vs.sku_id = p.sku_id) v LEFT JOIN (SELECT * FROM customer_dict WHERE tenant_id = %s) c1 ON v.size_type = c1.code AND c1.type = 'size_type' LEFT JOIN (SELECT * FROM customer_dict WHERE tenant_id = %s) c2 ON v.color_type = c2.code AND c2.type = 'color_type' ;"""
# 从数据库查询的数据
# 所有地址：（省，市，区/县）
ALL_ADDRESS = []
# 店铺名称
SHOP_NAME = []
# seller_nick
SELLER_NICK = []
# 缺货的商品
STOCKOUT_GOODS = []
# 有货的商品
STOCKIN_GOODS = []

if __name__ == "__main__":
    print len(TRADE_KEY)
    print len(DEFAULT_TRADE_KEY.keys())
    print len(RANDOM_TRADE_KEY)
    print len(ORDER_KEY)
    print len(DEFAULT_ORDER_KEY.keys())
    print len(RANDOM_ORDER_KEY)