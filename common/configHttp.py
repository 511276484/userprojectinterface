#封装requests
import requests
import common
from common.get_log import GetLog
log = GetLog.get_logger()

# 网络请求类
class ConfigHttp():

    def __init__(self):
        self.url = ""  # 请求基本路径
        self.headers = {}
        self.params = {}
        self.data = {}
        self.files = {}
        self.state = 0

    def set_url(self, url):
        """
        设置请求路径
        :param url:
        :return:
        """
        self.url = common.baseurl + url

    def get_url(self):
        """
        设置请求路径
        :param url:
        :return:
        """
        return self.url

    def set_headers(self, header={}):
        """
        设置头部
        :param header:
        :return:
        """
        self.headers = header

    def set_params(self, param):
        """
        设置请求参数 get
        :param param:
        :return:
        """
        self.params = param

    def set_data(self, data):
        """
        设置请求参数 post
        :param data:
        :return:
        """
        self.data = data

    def get(self):
        """
        get请求
        :return:
        """
        try:
            response = requests.get(self.url, headers=self.headers, params=self.params, timeout=float(common.tm))
        except BaseException as e:
            log.error("连接超时 {}".format(e))
            return None
        return response

    def post(self):
        """
       post请求
        :return:
        """
        try:
            response = requests.post(self.url, headers=self.headers, data=self.data, timeout=float(common.tm))
        except BaseException as e:
            log.error("连接超时 {}".format(e))
            return None
        return response

    def send(self, method, params):
        if method == "post":
            # 3 设置请求参数
            self.set_data(params)
            response = self.post()
        elif method == "get":
            self.set_params(params)
            response = self.get()
        return response

# if __name__ == '__main__':
#     url = "/LoginServlet"
#     # 1 创建网络请求对象
#     cf = ConfigHttp()
#     # 2 设置请求url
#     cf.set_url(url)
#     # 3 请求参数
#     payload = {'name': 'admin',
#                'pw': '123'}
#     cf.set_data(payload)
#
#     # 发起请求
#     r = cf.post()
#     print(r.json()["code"])
