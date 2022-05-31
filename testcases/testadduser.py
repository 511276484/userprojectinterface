import token

import unittest2
from unittestreport import ddt, json_data
from sysconfig import curpath
from common.get_log import GetLog
from common.configHttp import ConfigHttp
import os
from common.tokenunit import get_token

log = GetLog.get_logger()
# 动态获取测试用例文件的路径
jsonpath = os.path.join(curpath, "cases", "adduser.json")

@ddt
class testadduser(unittest2.TestCase):

    @classmethod
    def setUpClass(cls):
        # 创建网络请求对象
        cls.ch = ConfigHttp()
        cls.token = get_token()  # 获取token

    @json_data(jsonpath)
    def testadduser(self, data):
        # 设置测试用例的标题
        log.info("======={}========".format(data.get("title")))
        self._testMethodDoc = data.get("title")  # 生成测试用例标题
        # 1 设置请求url
        self.ch.set_url(data.get("url"))
        log.info("1 请求url {}  请求方式 {}".format(self.ch.get_url(), data.get("method")))

        #  2 设置请求参数
        action = data.get("action")
        name = data.get("name")
        address = data.get("address")
        phone = data.get("phone")
        params = {"action": action,
                  "name": name,
                  "token": self.token,
                  "address": address,
                  "phone": phone
                  }
        log.info("2 设置请求参数 action {} , name {},address {},phone {},token {}".format(action, name, address, phone,token))
        response = self.ch.send(data.get("method"), params)

        # 获取响应的数据
        jsondata = response.json()
        log.info("3 响应的数据 {} ".format(jsondata))
        mesage = data.get("message")  # 预期结果
        re = jsondata.get("code")  # 实际结果
        log.info("4 预期结果 {} : 实际结果 {}  ".format(mesage, re))
        self.assertEqual(mesage, re, data.get("error"))


if __name__ == '__main__':
    unittest2.main()
