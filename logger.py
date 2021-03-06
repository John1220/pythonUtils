# -*-coding:utf-8-*-
"""
配置 log
"""
import logging
from logging import handlers


class Logger(object):
    # 日志级别关系映射
    level_relations = {
        'DEBUG': logging.DEBUG,
        'INFO': logging.INFO,
        'WARNING': logging.WARNING,
        'ERROR': logging.ERROR,
        'CRITICAL': logging.CRITICAL
    }

    def __init__(self, filename, level='INFO', when='D', backCount=3,
                 fmt='%(levelname)s:%(asctime)s:[line:%(lineno)d]: %(message)s'):
        # fmt='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'
        self.logger = logging.getLogger()
        format_str = logging.Formatter(fmt)  # 设置日志格式
        self.logger.setLevel(self.level_relations.get(level))  # 设置日志级别
        sh = logging.StreamHandler()  # 往屏幕上输出
        sh.setFormatter(format_str)  # 设置屏幕上显示的格式
        th = handlers.TimedRotatingFileHandler(filename=filename, when=when, backupCount=backCount,
                                               encoding='utf-8')  # 往文件里写入#指定间隔时间自动生成文件的处理器
        # 实例化TimedRotatingFileHandler
        # interval是时间间隔，backupCount是备份文件的个数，如果超过这个个数，就会自动删除，when是间隔的时间单位，单位有以下几种：
        # S 秒
        # M 分
        # H 小时、
        # D 天、
        # W 每星期（interval==0时代表星期一）
        # midnight 每天凌晨
        th.setFormatter(format_str)  # 设置文件里写入的格式
        th.setLevel(self.level_relations.get(level))
        # 清除存在的handlers, 防止重复打印, 写入日志
        if self.logger.hasHandlers():
            self.logger.handlers.clear()
        # 把对象加到logger
        self.logger.addHandler(sh)
        self.logger.addHandler(th)

    def get_log(self):
        return self.logger


if __name__ == '__main__':
    log = Logger('all.log', level='DEBUG')
    log.logger.debug('debug')
    log.logger.info('info')
    log.logger.warning('警告')
    log.logger.error('报错')
    log.logger.critical('严重')
    log2 = Logger('error.log', level='ERROR')
    log2.logger.error('error')
