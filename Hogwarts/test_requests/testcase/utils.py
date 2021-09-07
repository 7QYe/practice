"""
author : QY
"""
import yaml
from jsonpath import jsonpath


class Utils:
    @classmethod
    def get_data_yaml(cls, file_path):
        '''
        获取yaml数据信息
        :param file_path: yaml文件路径
        :return:
        '''
        with open(file_path, encoding="utf-8") as f:
            datas = yaml.safe_load(f)
        return datas

    @classmethod
    def base_jsonpath(cls, obj, json_path):
        '''
        封装jsonpath断言方法
        :param obj: 响应的内容
        :param json_path: jsonpath表达式
        :return: 断言的结果
        '''
        return jsonpath(obj, json_path)
