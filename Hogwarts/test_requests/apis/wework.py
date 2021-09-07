"""
author : QY
"""
from test_requests.apis.base_api import BaseApi


class WeWork(BaseApi):
    def __init__(self, corpid, corpsecret):
        self.token = self.get_access_token(corpid, corpsecret)

    def get_access_token(self, corpid, corpsecret):
        # 完成access_token的获取
        # 请求的地址
        url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecret}"
        # 把接口信息封装到字典中
        req = {
            "method": "GET",
            "url": url
        }
        r = self.send_api(req)
        token = r.json()["access_token"]
        return token


