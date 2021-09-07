"""
author : QY
"""
from test_requests.apis.wework import WeWork
from test_requests.testcase.utils import Utils


class Tag(WeWork):
    def creat_tag(self, data):
        '''
        创建标签
        :param data:
        :return:
        '''
        creat_url = f"https://qyapi.weixin.qq.com/cgi-bin/tag/create?access_token={self.token}"
        req = {
            "method": "POST",
            "url": creat_url,
            "json": data
        }
        r = self.send_api(req)
        return r.json()

    def update_tag(self, data):
        '''
        更新标签
        :param data:
        :return:
        '''
        update_url = f"https://qyapi.weixin.qq.com/cgi-bin/tag/update?access_token={self.token}"
        req = {
            "method": "POST",
            "url": update_url,
            "json": data
        }
        r = self.send_api(req)
        return r.json()

    def delete_tag(self, tag_id):
        '''
        删除标签
        :param data:
        :return:
        '''
        delete_url = f"https://qyapi.weixin.qq.com/cgi-bin/tag/delete?access_token={self.token}&tagid={tag_id}"
        req = {
            "method": "GET",
            "url": delete_url
        }
        r = self.send_api(req)
        return r.json()

    def get_tags(self):
        '''
        获取标签列表
        :param data:
        :return:
        '''
        get_url = f"https://qyapi.weixin.qq.com/cgi-bin/tag/list?access_token={self.token}"
        req = {
            "method": "POST",
            "url": get_url,
        }
        r = self.send_api(req)
        return r.json()

    def add_tag_user(self, data):
        '''
        获取标签成员
        :return:
        '''
        add_user_url = f"https://qyapi.weixin.qq.com/cgi-bin/tag/addtagusers?access_token={self.token}"
        req = {
            "method": "POST",
            "url": add_user_url,
            "json": data
        }
        r = self.send_api(req)
        return r.json()

    def get_tag_user(self, tag_id):
        '''
        获取标签成员
        :param tag_id:
        :return:
        '''
        get_user_url = f"https://qyapi.weixin.qq.com/cgi-bin/tag/get?access_token={self.token}&tagid={tag_id}"
        req = {
            "method": "GET",
            "url": get_user_url
        }
        r = self.send_api(req)
        return r.json()

    def delete_tag_user(self, data):
        '''
        删除标签成员
        :return:
        '''
        delete_user_url = f"https://qyapi.weixin.qq.com/cgi-bin/tag/deltagusers?access_token={self.token}"
        req = {
            "method": "POST",
            "url": delete_user_url,
            "json": data
        }
        r = self.send_api(req)
        return r.json()

    def clear_tag(self):
        '''
        清理已经存在的标签信息
        :return:
        '''
        # 获取当前存在标签名
        tag_list = self.get_tags()
        print(tag_list)
        # 提取所有的部门id
        tagid_list = Utils.base_jsonpath(tag_list, "$..tagid")
        print(tagid_list)
        if tagid_list is not False:
            for i in tagid_list:
                self.delete_tag(i)
                i += 1
        else:
            print("该列表为空")
