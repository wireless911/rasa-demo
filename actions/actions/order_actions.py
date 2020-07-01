#!/usr/bin/env python
# coding:utf-8
import random
import re
from typing import Text, Dict, Any, List
from rasa_sdk import Tracker, Action
from rasa_sdk.events import AllSlotsReset
from rasa_sdk.executor import CollectingDispatcher
from sanic.log import logger as _logger





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