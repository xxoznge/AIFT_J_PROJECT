import logging.config
import datetime
class Logging():
    def __init__(self, config_path='config/logging.conf', log_path='log'): # 270p
        self.logger = logging.getLogger(__name__)

        format = logging.Formatter("%(asctime)s | %(filename)s | %(lineno)s | %(levelname)s -> %(message)s")

        streamHandler = logging.StreamHandler()
        streamHandler.setFormatter(format)
        self.logger.addHandler(streamHandler)

        d_time = datetime.datetime.now()
        d_str = d_time.strftime("%Y-%m-%d")
        fileHandler = logging.FileHandler("log/"+d_str+".log", encoding="utf-8")
        fileHandler.setFormatter(format)
        self.logger.addHandler(fileHandler)

        self.logger.setLevel(level=logging.DEBUG)

        self.config_path = config_path
        self.log_path = log_path
        
    #로그설정
    def kiwoom_log(self):
        fh = logging.FileHandler(self.log_path+'/{:%Y-%m-%d}.log'.format(datetime.now()), encoding="utf-8")
        formatter = logging.Formatter('[%(asctime)s] I %(filename)s | %(name)s-%(funcName)s-%(lineno)04d I %(levelname)-8s > %(message)s')

        fh.setFormatter(formatter)
        self.logger.addHandler(fh)