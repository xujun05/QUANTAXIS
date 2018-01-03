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

from QUANTAXIS.QASU import save_tdx as stdx
from QUANTAXIS.QASU import save_tdx_file as tdx_file
from QUANTAXIS.QASU import save_tushare as sts
from QUANTAXIS.QASU import save_wind as sw
from QUANTAXIS.QASU import update_tdx as utdx
from QUANTAXIS.QASU import update_tushare as uts
from QUANTAXIS.QASU import update_wind as uw
from QUANTAXIS.QAUtil import QA_Setting


def QA_SU_save_trade_date(engine, client=QA_Setting.client):
    engine = select_save_engine(engine)
    engine.QA_SU_save_trade_date(client=client)


def QA_SU_save_stock_info(engine, client=QA_Setting.client):
    engine = select_save_engine(engine)
    engine.QA_SU_save_stock_info(client=client)


def QA_SU_save_stock_list(engine, client=QA_Setting.client):
    engine = select_save_engine(engine)
    engine.QA_SU_save_stock_list(client=client)


def QA_SU_save_stock_day(engine, client=QA_Setting.client):
    engine = select_save_engine(engine)
    engine.QA_SU_save_stock_day(client=client)


def QA_SU_save_stock_min(engine, client=QA_Setting.client):
    engine = select_save_engine(engine)
    engine.QA_SU_save_stock_min(client=client)


def QA_SU_save_index_day(engine, client=QA_Setting.client):
    engine = select_save_engine(engine)
    engine.QA_SU_save_index_day(client=client)


def QA_SU_save_index_min(engine, client=QA_Setting.client):
    engine = select_save_engine(engine)
    engine.QA_SU_save_index_min(client=client)


def QA_SU_save_etf_day(engine, client=QA_Setting.client):
    engine = select_save_engine(engine)
    engine.QA_SU_save_etf_day(client=client)


def QA_SU_save_etf_min(engine, client=QA_Setting.client):
    engine = select_save_engine(engine)
    engine.QA_SU_save_etf_min(client=client)


def QA_SU_save_stock_xdxr(engine, client=QA_Setting.client):
    engine = select_save_engine(engine)
    engine.QA_SU_save_stock_xdxr(client=client)

def QA_SU_save_stock_block(engine, client=QA_Setting.client):
    engine = select_save_engine(engine)
    engine.QA_SU_save_stock_block(client=client)
def QA_SU_save_stock_day_init(startDate, engine, client=QA_Setting.client):
    engine = select_save_engine(engine)
    engine.QA_SU_save_stock_day_init(startDate, client)


def QA_SU_update_stock_day(engine, client=QA_Setting.client):
    engine = select_update_engine(engine)
    engine.QA_SU_update_stock_day(client=client)


def QA_SU_update_stock_xdxr(engine, client=QA_Setting.client):
    engine = select_update_engine(engine)
    engine.QA_SU_update_stock_xdxr(client=client)


def QA_SU_update_stock_min(engine, client=QA_Setting.client):
    engine = select_update_engine(engine)
    engine.QA_SU_update_stock_min(client=client)



def QA_SU_update_index_day(engine, client=QA_Setting.client):
    engine = select_update_engine(engine)
    engine.QA_SU_update_index_day(client=client)


def QA_SU_update_index_min(engine, client=QA_Setting.client):
    engine = select_update_engine(engine)
    engine.QA_SU_update_index_min(client=client)


def select_save_engine(engine):
    if engine in ['wind', 'Wind', 'WIND']:
        return sw
    elif engine in ['tushare', 'ts', 'Tushare']:
        return sts
    elif engine in ['tdx']:
        return stdx


def select_update_engine(engine):
    if engine in ['wind', 'Wind', 'WIND']:
        return uw
    elif engine in ['tushare', 'ts', 'Tushare']:
        return uts
    elif engine in ['tdx']:
        return utdx


def QA_SU_save_stock_min_5(file_dir, client=QA_Setting.client):
    return tdx_file.QA_save_tdx_to_mongo(file_dir, client)
