# 自动化脚本的入口
import unittest2
import os
import unittestreport
from sysconfig import curpath
from common.tokenunit import set_token

#测试用例的路径
casepath = os.path.join(curpath,"testcases")
# 报告路径
resultpath = os.path.join(curpath,"results")

def start():

    #设置token
    set_token()

    suits = unittest2.defaultTestLoader.discover(casepath, pattern='test*.py')
    # 2、创建一个用例运行程序
    runner = unittestreport.TestRunner(suits,
                                       tester='测试人员—deng',
                                       filename="用户管理系统测试报告",
                                       report_dir=resultpath,
                                       title='这里设置报告标题',
                                       desc='用户管理',
                                       templates=3
                                       )

    # 3、测试用例
    runner.run(thread_count=2)

start()
