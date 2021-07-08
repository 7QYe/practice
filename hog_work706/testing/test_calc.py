'''
测试文件
'''
import logging
from decimal import Decimal
from decimal import getcontext
from pythoncode import calculator

import pytest


class Test:

    def setup_class(self):
        logging.info("setup_class 开始计算")
        self.calc = calculator.Calculator()

    def teardown_class(self):
        logging.info("teardown_class结束计算")

    def setup(self):
        logging.info("开始计算")

    def teardown(self):
        logging.info("结束计算")

    # 加法运算
    @pytest.mark.parametrize("a,b,expect", [
        (1, 1, 2), (-1, -2, -3), (-2, 4, 2), (0.1, 0.1, 0.2), (-0.2, -0.4, -0.6), (0.3, -0.2, 0.1), (1, 0.3, 1.3),
        (1, 0, 1)], ids=["posInt", "minusInt", "pos&minusInt", "minusFloat", "negFloat", "pos&minusFloat", "int&float",
                         "zero"])
    def test_add(self, a, b, expect):
        getcontext().prec = 1
        if isinstance(a, int) and isinstance(b, int):
            assert expect == self.calc.add(a, b)
        elif isinstance(a, float) and isinstance(b, float):
            assert expect == float(self.calc.add(Decimal(a), Decimal(b)))
        else:
            assert expect == float(Decimal(self.calc.add(a, b)))

    # # 除法运算
    @pytest.mark.parametrize("a, b, expect", [
        (3, 1, 3), (-3, -1, 3), (-3, 1, -3), (0.1, 0.1, 1), (-0.2, -0.1, 2), (-0.2, 0.1, -2.0), (0.2, 1, 0.2), (1, 0, 0)
    ], ids=["posInt", "minusInt", "pos&minusInt", "minusFloat", "negFloat", "pos&minusFloat", "int&float", "zero"])
    def test_div(self, a, b, expect):
        getcontext().prec = 1
        if b == 0:
            logging.info("除数不能为0")
        elif isinstance(a, int) and isinstance(b, int):
            assert expect == self.calc.div(a, b)
        elif isinstance(a, float) and isinstance(b, float):
            assert expect == float(self.calc.div(Decimal(a), Decimal(b)))
        else:
            assert expect == float(Decimal(self.calc.div(a, b)))
