#获取项目的路径
import os,time

# __file__当前文件
#curpath 当前工程的路径
curpath = os.path.dirname(os.path.realpath(__file__))
now = time.strftime("%Y-%m-%d", time.localtime(time.time()))


