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
import pymongo
import re
import datetime
import time
import motor
import asyncio
from motor import motor_asyncio
from motor.motor_asyncio import (AsyncIOMotorCollection, AsyncIOMotorClient, AsyncIOMotorDatabase,
                                 AsyncIOMotorCommandCursor)
from .QALogs import QA_util_log_info


def QA_util_sql_mongo_setting(host='127.0.0.1', port=27017, user_name="admin", user_pwd="test", db_name="quantaxis"):
    uri = "mongodb://{username}:{password}@{host}:{port}/{db_name}?authMechanism=SCRAM-SHA-1".format(username=user_name,
                                                                                                    password=user_pwd,
                                                                                                    host=host,
                                                                                                    port=port,
                                                                                                    db_name=db_name)
    QA_sql_mongo_client = pymongo.MongoClient(uri)
    QA_util_log_info('host:{},port:{}'.format(str(host), str(port)))
    return QA_sql_mongo_client

# async


def QA_util_sql_async_mongo_setting(ip='127.0.0.1', port=27017):
    QA_sql_async_mongo_client = AsyncIOMotorClient(ip, int(port))
    QA_util_log_info('ip:{},port{}'.format(str(ip),str(port)))
    return QA_sql_async_mongo_client


if __name__=='__main__':
    # test async_mongo
    client=QA_util_sql_async_mongo_setting().quantaxis.stock_day
    print(client)