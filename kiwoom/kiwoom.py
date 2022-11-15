from PyQt5.QAxContainer import *
from PyQt5.QtCore import *
from config.errorCode import *
from PyQt5.QtTest import *
from config.kiwoomType import *
from config.log_class import *

class Kiwoom(QAxWidget):
    def __init__(self):
        super().__init__()
        self.realType = RealType()
        self.logging = Logging()

        self.logging.logger.debug("Kiwoom() class start.")

        ####### event loop를 실행하기 위한 변수모음
        self.login_event_loop = QEventLoop() # 예수금 118p / 로그인 요청용 이벤트 루프
        #########################################

        ########### 전체 종목 관리
        self.all_stock_dict = {}
        ###########################


        ####### 계좌 관련된 변수 118p
        self.account_num = None
        self.deposit = 0 # 예수금
        self.use_money = 0
        self.use_money_percent = 0.5
        self.output_deposit = 0 # 출력 가능 금액
        self.account_stock_dict = {}
        self.not_account_stock_dict = {}
        ########################################

        ######## 종목 정보 가져오기
        self.portfolio_stock_dict = {}
        self.jango_dict = {}
        ########################

        ########### 종목 분석 용
        self.calcul_data = []
        ##########################################


        ####### 요청 스크린 번호
        self.screen_start_stop_real = "1000" #장 시작/종료 실시간 스크린번호
        self.screen_my_info = "2000" # 계좌 관련 스크린 번호 118p
        ########################################

        ######### 초기 셋팅 함수들 바로 실행
        self.get_ocx_instance() #Ocx 방식을 파이썬에 사용할 수 있게 변환해 주는 함수 실행
        self.event_slots() #키움과 연결하기 위한 signal / slot 모음 함수 실행
        self.signal_login_commConnect() #로그인 시도 함수 실행
        self.get_account_info() #계좌번호 가져오기
        self.detail_account_info()
        self.trdata_slot()


        self.condition_event_slot()
        self.condition_signal()
        #########################################

    def get_ocx_instance(self):
        self.setControl("KHOPENAPI.KHOpenAPICtrl.1")


    def event_slots(self):  # 121p 
        self.OnEventConnect.connect(self.login_slot)  # 로그인 관련 이벤트
        self.OnReceiveTrData.connect(self.trdata_slot)  # TR 관련 이벤트



    def signal_login_commConnect(self):
        self.dynamicCall("CommConnect()")

        self.login_event_loop = QEventLoop()
        self.login_event_loop.exec_()

    def login_slot(self, err_code):

        self.logging.logger.debug(errors(err_code)[1])

        self.login_event_loop.exit()


    def get_account_info(self):  # 계좌번호 가져오기 111p
        account_list = self.dynamicCall("GetLoginInfo(QString)", "ACCNO")
        account_num = account_list.split(';')[0]
        self.account_num = account_num

        # self.logging.logger.debug("계좌번호 : %s" % account_num)
        print("계좌번호 : %s" % account_num)

    def detail_account_info(self, sPrevNext = "0"):   # 예수금 118p
        print("예수금을 요청하는 부분")
        self.dynamicCall("SetInputValue(QString, QString)", "계좌번호", self.account_num)
        self.dynamicCall("SetInputValue(QString, QString)", "비밀번호", "0000")
        self.dynamicCall("SetInputValue(QString, QString)", "비밀번호입력매체구분", "00")
        self.dynamicCall("SetInputValue(QString, QString)", "조회구분", "2")
        self.dynamicCall("CommRqData(QString, QString, int, QString)", "예수금상세현황요청", "opw00001", sPrevNext, self.screen_my_info)
        
      

    def trdata_slot(self, sScrNo, sRQName, sTrCode,sRecordName, sPrevNext): # 예수금 122p # 오류
        if sRQName == "예수금상세현황요청":
            print("dd")
            deposit = self.dynamicCall("GetCommData(QString, QString, int, QString)", sTrCode, sRQName, 0, "예수금")
            self.deposit = int(deposit)
            use_money = float(self.deposit) * self.use_money_percent
            self.use_money = int(use_money)
            self.use_money = self.use_money / 4
            

            output_deposit = self.dynamicCall("GetCommData(QString, QString, int, QString)", sTrCode, sRQName, 0, "출금가능금액")
            self.ouput_deposit = int(output_deposit)
            
            print("예수금 : %s" % self.output_deposit)
            self.stop_screen_cancel(self.screen_my_info)




    def stop_screen_cancel(self, sScrNo=None):
        self.dynamicCall("DisconnectRealData(QString)", sScrNo)

    #송수신 메세지 get
    def msg_slot(self, sScrNo, sRQName, sTrCode, msg):
        self.logging.logger.debug("스크린: %s, 요청이름: %s, tr코드: %s --- %s" %(sScrNo, sRQName, sTrCode, msg))

    #조건검색식 이벤트 모음
    def condition_event_slot(self):
        self.OnReceiveConditionVer.connect(self.condition_slot)
        self.OnReceiveTrCondition.connect(self.condition_tr_slot)
        self.OnReceiveRealCondition.connect(self.condition_real_slot)


    # 어떤 조건식이 있는지 확인
    def condition_slot(self, lRet, sMsg):
        self.logging.logger.debug("호출 성공 여부 %s, 호출결과 메시지 %s" % (lRet, sMsg))

        condition_name_list = self.dynamicCall("GetConditionNameList()")
        self.logging.logger.debug("HTS의 조건검색식 이름 가져오기 %s" % condition_name_list)

        condition_name_list = condition_name_list.split(";")[:-1]

        for unit_condition in condition_name_list:
            index = unit_condition.split("^")[0]
            index = int(index)
            condition_name = unit_condition.split("^")[1]

            self.logging.logger.debug("조건식 분리 번호: %s, 이름: %s" % (index, condition_name))

            ok  = self.dynamicCall("SendCondition(QString, QString, int, int)", "0156", condition_name, index, 1) #조회요청 + 실시간 조회
            self.logging.logger.debug("조회 성공여부 %s " % ok)



    # 조건식 로딩 하기
    def condition_signal(self):
        self.dynamicCall("GetConditionLoad()")

    # 나의 조건식에 해당하는 종목코드 받기
    def condition_tr_slot(self, sScrNo, strCodeList, strConditionName, index, nNext):
        self.logging.logger.debug("화면번호: %s, 종목코드 리스트: %s, 조건식 이름: %s, 조건식 인덱스: %s, 연속조회: %s" % (sScrNo, strCodeList, strConditionName, index, nNext))

        code_list = strCodeList.split(";")[:-1]
        self.logging.logger.debug("코드 종목 \n %s" % code_list)

    # 조건식 실시간으로 받기
    def condition_real_slot(self, strCode, strType, strConditionName, strConditionIndex):
        self.logging.logger.debug("종목코드: %s, 이벤트종류: %s, 조건식이름: %s, 조건명인덱스: %s" % (strCode, strType, strConditionName, strConditionIndex))

        if strType == "I":
            self.logging.logger.debug("종목코드: %s, 종목편입: %s" % (strCode, strType))

        elif strType == "D":
            self.logging.logger.debug("종목코드: %s, 종목이탈: %s" % (strCode, strType))

