import datetime

from QUANTAXIS.QAFetch.QATdx import (QA_fetch_get_stock_day,
                                     QA_fetch_get_stock_min,
                                     QA_fetch_get_stock_transaction,
                                     QA_fetch_get_stock_xdxr)
from QUANTAXIS.QAFetch.QATushare import QA_fetch_get_stock_time_to_market
from QUANTAXIS.QASU.save_tdx import QA_SU_save_stock_xdxr
from QUANTAXIS.QAUtil import (QA_Setting, QA_util_log_info,
                              QA_util_to_json_from_pandas, trade_date_sse)


"""
该模块已经废弃

目前都在save_tdx中 增量更新

"""


def QA_SU_update_stock_day(client=QA_Setting.client):
    def save_stock_day(code, start, end, coll):
        QA_util_log_info('##JOB01 Now Updating STOCK_DAY==== %s' % (str(code)))
        data = QA_util_to_json_from_pandas(
            QA_fetch_get_stock_day(str(code), start, end, '00'))

        if len(data) > 0:
            coll.insert_many(data)
        else:
            pass
    coll_stock_day = client.quantaxis.stock_day
    for item in QA_fetch_get_stock_time_to_market().index:

        if coll_stock_day.find({'code': str(item)[0:6]}).count() > 0:
            # 加入这个判断的原因是因为如果股票是刚上市的 数据库会没有数据 所以会有负索引问题出现

            start_date = str(coll_stock_day.find({'code': str(item)[0:6]})[
                coll_stock_day.find({'code': str(item)[0:6]}).count() - 1]['date'])
            print('*' * 20)
            end_date = str(now_time())[0:10]
            start_date = trade_date_sse[trade_date_sse.index(
                start_date) + 1]
            QA_util_log_info(' UPDATE_STOCK_DAY \n Trying updating %s from %s to %s' %
                             (item, start_date, end_date))

            save_stock_day(item, start_date, end_date, coll_stock_day)

        else:
            save_stock_day(item, '1990-01-01',
                           str(now_time())[0:10], coll_stock_day)

    QA_util_log_info('Done == \n')


def QA_SU_update_stock_xdxr(client=QA_Setting.client):
    client.quantaxis.drop_collection('stock_xdxr')
    QA_SU_save_stock_xdxr()


def QA_SU_update_stock_min(client=QA_Setting.client):
    """
    stock_min 分三个库 type区分
    1. 1min_level 库
    2. 5min_level 库
    3. 15min_level 库
    """


def QA_SU_update_index_day(client=QA_Setting.client):
    pass


def QA_SU_update_index_min(client=QA_Setting.client):
    pass


if __name__ == '__main__':
    QA_SU_update_stock_day()
    # QA_SU_update_stock_xdxr()
