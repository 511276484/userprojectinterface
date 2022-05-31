# 导包
import logging.handlers,os
# 新建 类
from sysconfig import curpath,now

log_path = os.path.join(curpath, "logs")


class GetLog:

    # 新建一个日志器变量
    __logger = None
    # 新建获取日志器的方法
    @classmethod
    def get_logger(cls):
        # 判断日志器为空：
        if cls.__logger is None:
            # 获取日志器
            cls.__logger = logging.getLogger()
            # 修改默认级别
            cls.__logger.setLevel(logging.INFO)
            log_filename = log_path+os.sep+now+".log"
            # 获取处理器
            th = logging.handlers.TimedRotatingFileHandler(filename=log_filename,
                                                           when="midnight",
                                                           interval=1,
                                                           backupCount=3,
                                                           encoding="utf-8")
            # 获取格式器
            fmt = "%(asctime)s %(levelname)s [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s"
            fm = logging.Formatter(fmt)
            # 将格式器添加到处理器中
            th.setFormatter(fm)
            # 将处理器添加到日志器中
            cls.__logger.addHandler(th)
        # 返回日志器
        return cls.__logger

if __name__ == '__main__':
    #创建日志对象log
    log = GetLog.get_logger()
    log.error("正在对：{} 元素执行输入:{} 操作！".format("a", "b"))
    log.info("正在对：{} 元素执行输入:{} 操作！".format("a", "b"))