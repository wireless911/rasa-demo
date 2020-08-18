# #!/usr/bin/env python
# # coding: utf-8
import socket
ip = socket.gethostbyname(socket.gethostname())
# 根据ip环境切换
if ip == "10.69.0.15":  # test01 服务器
    MODE = "state"
elif ip in ["10.69.0.4","10.69.0.14"]: # app01,mgr02
    MODE = "product"
else:
    MODE = "state"

TL_URL = "http://www.tuling123.com/openapi/api"
TL_KEY = "696bcaae670341729adf68c831a3634e"


# FAQ
CHAT_URL = 'http://faq.jaxcx.com/product/chat/dm'
CHAT_REQ_TIMEOUT = 5
CHAT_CONN_TIMEOUT = 5



# bz_sdk settings
# AES encrypt decrypt
# AES_BASE_URL = 'http://10.69.0.5:8086'  # app02服务器
AES_BASE_URL = 'http://39.98.163.51:8010' if MODE == "state" else 'http://10.69.0.5:8086'
AES_CONN_TIMEOUT = 3


# 宝尊借口 测试
BAOZUN_API_PREFIX = "https://stage.yslbeautycn.com" if MODE == "state" else "https://www.yslbeautycn.com"
# 宝尊接口 生产
# BAOZUN_API_PREFIX = "https://www.yslbeautycn.com"
BZ_CONN_TIMEOUT = 5


# context接口 生产
# CONTEXT_API_PREFIX = "https://wxminiec.yslbeautycn.com"
# context接口 测试
CONTEXT_API_PREFIX = "https://wxminiec-dev.lancome.com.cn" if MODE == "state" else "https://wxminiec.yslbeautycn.com"
CONTEXT_CONN_TIMEOUT = 5

# 默认未找到时产品图片
DEFAULT_IMAGE = 'https://chat-bot.lorealchina.com/yslSource/backend/image/default.jpg'

# 小程序appid
APPID = "wx074c09c855452600" if MODE == "state" else "wxc7be3122a3b2dda9"