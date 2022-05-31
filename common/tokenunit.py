# 作者： deng
# 时间： 2022/5/30 16:29 
# 版本： v1.0
# 描述： 负责获取token
from common.configHttp import ConfigHttp
from sysconfig import curpath
import os
import common
tokenfilepath = os.path.join(curpath,"common","token.txt") # token文件的路径

def set_token():
    """
    设置token
    :return:
    """
    # 1 创建请求对象
    cf = ConfigHttp()
    cf.set_url("/LoginServlet")
    #  2 设置请求参数
    params = {"name":common.name, "pw": common.pw}
    # 3 发起请求
    response = cf.send("post", params)
    # 4 获取响应的数据
    jsondata = response.json()
    # common/token.txt
    with open(tokenfilepath,"w") as f:
        f.write(jsondata.get("token"))

def get_token():
    """
    获取token
    :return:
    """
    with open(tokenfilepath) as f:
        return f.read()


if __name__ == '__main__':
    # set_token()
    print(get_token())
