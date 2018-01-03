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

from QUANTAXIS.QAARP.QAAccount import QA_Account
from QUANTAXIS.QAARP.QARisk import QA_Risk
from QUANTAXIS.QAARP.QAPortfolio import QA_Portfolio

from QUANTAXIS.QAARP.QARisk import (QA_risk_account_freeCash_currentAssest,
                                    QA_risk_account_freeCash_frozenAssest,
                                    QA_risk_account_freeCash_initAssest, QA_risk_eva_account)


class QA_ARP():
    def __init__(self):
        pass

    def QA_ARP_A2R(self, QA_Account, QA_Risk):

        pass

    def QA_ARP_R2P(self, QA_Risk, QA_Portfolio):
        pass

    def QA_ARP_P2R(self, QA_Risk, QA_Portfolio):
        pass

    def QA_ARP_R2A(self, QA_Account, QA_Risk):
        pass
