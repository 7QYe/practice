'''
测试文件
'''
import allure
import yaml
import pytest


def get_datas():
    with open('./datas/calc.yml') as f:
        datas = yaml.safe_load(f)
    return datas


@allure.feature("计算器")
class Test:

    # 加法运算
    @allure.feature("相加正常情况")
    @pytest.mark.parametrize("a,b,expect", get_datas()['add_normal'],
                             ids=get_datas()['ids_normal'])
    def test_add_normal(self, get_calc_object, a, b, expect):
        assert expect == get_calc_object.add(a, b)

    @allure.feature("相加浮点数情况")
    @pytest.mark.parametrize("a,b,expect", get_datas()['add_float'],
                             ids=get_datas()['ids_float'])
    def test_add_float(self, get_calc_object, a, b, expect):
        assert expect == round(get_calc_object.add(a, b), 1)

    @allure.feature("相加字符串情况")
    @pytest.mark.parametrize("a,b,expect", get_datas()['add_error'],
                             ids=get_datas()['ids_type'])
    def test_add_error(self, get_calc_object, a, b, expect):
        try:
            expect == get_calc_object.add(a, b)
        except TypeError:
            print("只能数字相加")

    # # 除法运算
    @allure.feature("相除正常情况")
    @pytest.mark.parametrize("a, b, expect", get_datas()['div_normal'], ids=get_datas()['ids_normal'])
    def test_div_normal(self, get_calc_object, a, b, expect):
        assert expect == get_calc_object.div(a, b)

    @allure.feature("相除浮点情况")
    @pytest.mark.parametrize("a,b,expect", get_datas()['div_float'],
                             ids=get_datas()['ids_float'])
    def test_div_float(self, get_calc_object, a, b, expect):
        assert expect == round(get_calc_object.div(a, b), 1)

    @allure.feature("相除异常情况")
    @pytest.mark.parametrize("a,b,expect", get_datas()['div_error'],
                             ids=get_datas()['ids_zero'])
    def test_div_error(self, get_calc_object, a, b, expect):
        try:
            expect == get_calc_object.div(a, b)
        except ZeroDivisionError:
            print("除数不能为0")
