import pytest
import logging

from pythoncode import calculator


@pytest.fixture(scope='function')
def get_calc_object():
    logging.info("开始计算")
    calcu = calculator.Calculator()
    yield calcu
    logging.info("结束计算")


def pytest_collection_modifyitems(session, config, items: list):
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')
