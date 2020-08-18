#!/usr/bin/env python
# coding:utf-8
import random
import re
from typing import Text, Dict, Any, List
from rasa_sdk import Tracker, Action
from rasa_sdk.events import AllSlotsReset
from rasa_sdk.executor import CollectingDispatcher
from sanic.log import logger as _logger

from .common.async_http import AsyncHttP
from .settings.messages import *


class Greetings(Action):
    """打招呼"""

    def name(self):
        return 'greetings'

    def is_async(self):
        return False

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        at = AsyncHttP()
        msg = random.choice(HI_MSGS)
        dispatcher.utter_message(msg)
        return ([AllSlotsReset()])


class Bye(Action):
    """拜拜"""

    def name(self):
        return 'bye'

    def is_async(self):
        return False

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        msg = random.choice(BYE_MSGS)
        dispatcher.utter_message(msg)
        return ([AllSlotsReset()])


class Thanks(Action):
    """谢谢"""

    def name(self):
        return 'thanks'

    def is_async(self):
        return False

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        msg = random.choice(THANKS_MSGS)
        dispatcher.utter_message(msg)
        return ([AllSlotsReset()])


class StoresQuery(Action):
    """门店查询"""

    def name(self):
        return 'stores_query'

    def is_async(self):
        return False

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        msg = """亲，您可以通过以下方式查询柜台信息，了解活动，{store_url}，前往专柜查询页面""".format(
            store_url="<a href='https://www.yslbeautycn.com/stores'>点击此处</a>")

        dispatcher.utter_message(msg)

        return ([AllSlotsReset()])


class CertifiedSourceQuery(Action):
    """正品渠道咨询"""

    def name(self):
        return 'certified_source_query'

    def is_async(self):
        return False

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        msg = """亲爱的，YSL精品商城小程序是正规的官方正品渠道哦~除此之外，YSL官网，YSL天猫旗舰店、线下专柜也是官方购买渠道"""

        dispatcher.utter_message(msg)

        return ([AllSlotsReset()])


class ActivityConsultation(Action):
    """活动咨询"""

    def name(self):
        return 'activity_consultation'

    def is_async(self):
        return False

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        msg = "活动咨询啊"
        dispatcher.utter_message(msg)
        return ([AllSlotsReset()])


class LetteringService(Action):
    """刻字服务"""

    def name(self):
        return 'lettering_service'

    def is_async(self):
        return False

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # msg = """亲爱的，7月1日-7月31日期间，全场满600免费刻字~<br>目前部分彩妆及香水支持刻字，具体商品请以页面为准。刻字产品将在订单提交后5个工作日内发货。<br>★温馨提示：<br>①请注意除产品质量或破损问题外，刻字产品不接受退换货。<br>②请确保您填写的刻字信息准确性，提交订单后无法进行修改哦~<br>③一份礼盒内的多个单品会默认镌刻相同刻字内容，如有特殊需求请注明在备注中。"""
        msg = """亲爱的，8月全场免费刻字~<br>目前部分彩妆及香水支持刻字，具体商品请以页面为准。刻字产品将在订单提交后5个工作日内发货。<br>★温馨提示：<br>①请注意除产品质量或破损问题外，刻字产品不接受退换货。<br>②请确保您填写的刻字信息准确性，提交订单后无法进行修改哦~<br>③一份礼盒内的多个单品会默认镌刻相同刻字内容，如有特殊需求请注明在备注中。"""
        dispatcher.utter_message(msg)
        return ([AllSlotsReset()])


class PromotionCode(Action):
    """促销代码"""

    def name(self):
        return 'promotion_code'

    def is_async(self):
        return False

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        msg = """亲爱的Y粉，促销代码相关问题建议您{artificial_service}联系人工客服，或拔打YSL官网热线：400-820-6362，我们将竭诚为您服务~"""
        dispatcher.utter_message(msg)
        return ([AllSlotsReset()])


class JointAgentQuery(Action):
    """加盟代理"""

    def name(self):
        return 'joint_agent_query'

    def is_async(self):
        return False

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        msg = """非常感谢您对YSL品牌的喜爱，目前YSL品牌已经有固定合作伙伴，暂不接受加盟代理，请您谅解。如果今后有机会，我们很高兴与您合作，再次感谢您对我们的支持"""
        dispatcher.utter_message(msg)
        return ([AllSlotsReset()])


class ComplaintFiling(Action):
    """投诉"""

    def name(self):
        return 'complaint_filing'

    def is_async(self):
        return False

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        msg = """很抱歉给您带来不便，投诉建议您可{artificial_service}联系人工客服，或拔打YSL官网热线：400-820-6362，我们将竭诚为您服务~"""
        dispatcher.utter_message(msg)
        return ([AllSlotsReset()])


class ArtificialService(Action):
    """人工客服"""

    def name(self):
        return 'artificial_service'

    def is_async(self):
        return False

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        msg = """{artificial_service}联系人工客服，或拔打YSL官网热线：400-820-6362，我们将竭诚为您服务~"""
        dispatcher.utter_message(msg)
        return ([AllSlotsReset()])


class ExpressStoreHouse(Action):
    """快递仓库查询"""

    def name(self):
        return 'express_store_hose'

    def is_async(self):
        return False

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        msg = """亲爱的，店铺正装商品订单使用「顺丰陆运」从苏州包邮寄出，顺丰无法到达区域，将会用其他承运快递公司发出。（无法指定快递发出）"""
        dispatcher.utter_message(msg)
        return ([AllSlotsReset()])
