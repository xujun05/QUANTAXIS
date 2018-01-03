# coding:utf-8
#
# The MIT License (MIT)
#
# Copyright (c) 2016-2017 yutiansut/QUANTAXIS
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import datetime
import random
import threading
import time

import pandas as pd

from QUANTAXIS.QAUtil import QA_util_log_info, QA_util_to_json_from_pandas


"""
重新定义bid模式



"""


class QA_QAMarket_bid():
    def __init__(self, price=16, date='2015-01-05', datetime='2015-01-05 09:01:00', sending_time='2015-01-05 09:01:00', transact_time='', amount=10,
                 towards=1, code='000001', user='root', strategy='example01', btype='0x01', bid_model='strategy', amount_model='amount',
                 order_id=str(random.random()), trade_id='', status='100'):
        self.price = price
        self.date = date
        self.datetime = datetime
        self.sending_time = sending_time  # 下单时间
        self.transact_time = transact_time
        self.amount = amount
        self.towards = towards  # side
        self.code = code
        self.user = user
        self.strategy = strategy
        self.type = btype  # see below
        self.bid_model = strategy
        self.amount_model = amount_model
        self.order_id = order_id
        self.trade_id = trade_id
        self.status = status

    def stock_day(self):
        self.type = '0x01'
        return self

    def stock_min(self):
        self.type = '0x02'
        return self

    def index_day(self):
        self.type = '0x03'
        return self

    def index_min(self):
        self.type = '0x04'
        return self

    def stock_transaction(self):
        self.type = '0x05'
        return self

    def index_transaction(self):
        self.type = '0x06'
        return self

    def future_day(self):
        self.type = '1x01'
        return self

    def show(self):
        return vars(self)

    def to_df(self):
        return pd.DataFrame([vars(self), ])

    def to_dict(self):
        return vars(self)

    def from_dict(self, bid):
        try:
            self.price = bid['price']
            self.date = bid['date']
            self.datetime = bid['datetime']
            self.sending_time = bid['sending_time']  # 下单时间
            self.transact_time = bid['transact_time']
            self.amount = bid['amount']
            self.towards = bid['towards']
            self.code = bid['code']
            self.user = bid['user']
            self.strategy = bid['strategy']
            self.type = bid['type']
            self.bid_model = bid['bid_model']
            self.amount_model = bid['amount_model']
            self.order_id = bid['order_id']
            self.trade_id = bid['trade_id']
            return self
        except:
            QA_util_log_info('Failed to tran from dict')

    def from_dataframe(self, dataframe):
        bid_list = []
        for item in QA_util_to_json_from_pandas(dataframe):
            bid_list.append(self.from_dict(item))
        return bid_list

    def apply(self, bid):
        try:
            self.price = bid['price']
            self.date = bid['date']
            self.datetime = bid['datetime']
            self.sending_time = bid['sending_time']  # 下单时间
            self.transact_time = bid['transact_time']
            self.amount = bid['amount']
            self.towards = bid['towards']
            self.code = bid['code']
            self.user = bid['user']
            self.strategy = bid['strategy']
            self.type = bid['type']
            self.bid_model = bid['bid_model']
            self.amount_model = bid['amount_model']
            self.order_id = bid['order_id']
            self.trade_id = bid['trade_id']
            return self
        except:
            QA_util_log_info('Failed to tran from dict')


class QA_QAMarket_bid_list():   # also the order tree
    """
    一个待成交列表

    """

    def __init__(self):
        self.list = []

    def from_dataframe(self, dataframe):
        self.list = [QA_QAMarket_bid().from_dict(item)
                     for item in QA_util_to_json_from_pandas(dataframe)]
        return self.list


if __name__ == '__main__':
    ax = QA_QAMarket_bid().stock_day()

    print(ax.show())
    print(ax.to_df())
