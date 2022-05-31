import unittest2
from unittestreport import ddt, json_data
from sysconfig import curpath
from common.get_log import GetLog
from  common.configHttp import ConfigHttp
log = GetLog.get_logger()
import os

# 动态获取测试用例文件的路径
jsonpath = os.path.join(curpath,"cases","login.json")

@ddt
class testlogin(unittest2.TestCase):

    @classmethod
    def setUpClass(cls):
        # 创建网络请求对象
        cls.ch = ConfigHttp()

    @json_data(jsonpath)
    def testlogin(self, data):
        # 设置测试用例的标题
        log.info("======={}========".format(data.get("title")))
        self._testMethodDoc = data.get("title") # 生成测试用例标题
        # 1 设置请求url
        self.ch.set_url(data.get("url"))
        log.info("1 请求url {}  请求方式 {}".format(self.ch.get_url(), data.get("method")))

        #  2 设置请求参数
        params = {"name": data.get("name"), "pw": data.get("pw")}
        log.info("2 设置请求参数 name {}  , pw {}".format(data.get("name"), data.get("pw")))
        response = self.ch.send(data.get("method"), params)

        # 获取响应的数据
        jsondata = response.json()
        log.info("3 响应的数据 {} ".format(jsondata))
        mesage = data.get("message") # 预期结果
        re = jsondata.get("code") # 实际结果
        log.info("4 预期结果 {} : 实际结果 {}  ".format(mesage, re))
        self.assertEqual(mesage, re, data.get("error"))

if __name__ == '__main__':
    unittest2.main()



