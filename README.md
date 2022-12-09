# AIFT_J_PROJECT  

TEAM-J Collaborator  
* xxoznge 20201049 이소정  
* YeJiKim06 20201029 김예지  
* jinjoo-jung 20201058 정진주  

2022-2 SSWU PROJECT  
* Artificial Intelligence in Financial Trade Project  
* 손가락 하나 까딱하지 않는 주식 거래 시스템 구축 (참고)  
* Github, Slack   

## 현재 진행상황  

### 1. 키움 API 설치 및 환경설정  

> PyCharm, Anaconda Windows 64-Bit   
> CMD 관리자 권한 실행  
> 32bit 가상환경 set CONDA_FORCE_32BIT=1  
> PyQt5 필요  

### 2. 키움 API로 키움증권 로그인 ( ~ 2022.11.14 )  

> 계좌개설, 공동인증서  
 
 ```python 
self.get_ocx_instance()  
self.event_slots()  
self.signal_login_commConnect()  
```

### 3. 계좌번호  ( ~ 2022.11.14 )  

> 로그인 후 계좌번호 요청  

 ```python  
self.get_account_info()  
 ```

### 4. 예수금 정보 ( ~ 2022.11.15 )  

> opw 00001 : 예수금상세현황요청  
>trdata_slot 오류 해결 ( 자동로그인 필수 )  

 ```python  
self.detail_account_info()  
 ```

### 5. 계좌평가잔고내역, 보유 종목, 미체결 종목, 코스닥 개수, 일봉데이터 ( ~ 2022.11.16 )  

> 키움증권 모의투자로 로그인 후 매수 ( 체결 / 미체결되도록 매수 후 확인 완료 )  
> 싱글데이터로 정보 처리, 멀티데이터로 보유 종목 정보 처리  
> 코스닥 종목 일봉데이터 가져오기  
> 일봉데이터 가져오기 필요없으면 self.calculator_fnc()에 주석처리  

 ``` python  
self.detail_account_mystock()  
self.not_concluded_account()   
self.calculator_fnc()  
 ```  
 
### 6. 코스닥 일봉데이터 1604개 받기 완료 ( ~ 2022.11.17 )  

> 1604개 10시간 소요  

### 7. 포트폴리오로 종목 분석 - 이동평균선 비교 ( ~ 2022.11.17 ) 

> 최근의 일봉에서 고가와 저가를 이동평균선과 비교   
>> 그랜빌 4법칙 - 120일 이동평균선 사용  
> 이동평균선 가격 계산  
> 이동평균선보다 아래에 있는지 확인  
> 이동평균선보다 위에 위치하는 구간 구하기  
> 가장 최근 이동평균선 가격이 과거의 이동평균선 가격보다 높은지 확인  

### 8. 조건 통과한 종목 파일로 저장 ( ~ 2022.11.17 )

> 120일 이동평균선 사용으로 조건 통과 종목 적은 상태  
> 장이 끝나는 시점에 동작하도록 설정해야 함.

### 9. 이동평균선 120일 -> 20일로 변경 ( ~ 2022.11.21 )
> 조건 통과 종목이 매우 적은 상황이라 제대로 된 파일을 만들기 위해 파격적으로 20일로 변경  

### 10. 조건 통과 종목 파일 저장 오류 해결 ( ~ 2022.11.26 )  
>  드디어 해결을 했습니다 .... 

### 11. 보유 종목, 미체결 종목, 분석된 종목을 하나의 딕셔너리로 구성 ( ~ 2022.11.29 )   
> portfolio_stock_dict 에서 계속 오류    

 ``` python  
def read_code(self):  
def merge_dict(self):  
def screen_number_setting(self):  
 ```  
 
 ###  12. 장 시간 체크 이벤트 등록, 종목 실시간 등록 스크린 번호 사용, 종목 정보 실시간 체크 ( ~ 2022.11.29 )  
   
  ``` python  
 def realdata_slot(self, sCode, sRealType, sRealData):   
 ```  
### 13. 지정가로 종목 매수하기, 미체결 수량 매수 취소하기, 시장가로 종목 매도하기 ( ~ 2022.11.30 )  
  
  ``` python  
 def realdata_slot(self, sCode, sRealType, sRealData):   
 ``` 
 
### 14. 실시간 체결정보 확인, 체결 정보 데이터 받기, 변경된 잔고내역 데이터 받기, 서버에서 메세지 받기 ( ~ 2022.11.30 ) 

  ``` python  
 def realdata_slot(self, sCode, sRealType, sRealData):   
 def chejan_slot(self, sGubun, nItemCnt, sFidList):  
 def msg_slot(self, sScrNo, sRQName, sTrCode, msg):  
 ``` 
 
### 15. 장 종료 후 - 연결 끊기, 종목 분석, 프로그램 종료 ( ~ 2022.11.30 )  


  ``` python  
 def realdata_slot(self, sCode, sRealType, sRealData):   
 def file_delete(self):   
 ``` 
 ### 16. 로깅, 슬랙메세지 ( ~ 2022.11.30 ) 
> 로깅 / 슬랙메세지 (노트북, 핸드폰 알람) 확인  
* 슬랙메세지  
>> https://api.slack.com/apps에서 토큰받기  
>> slcak.py -> 토큰 복사  
>> requests 모듈 설치 -> pip install requests  
* config file  
>> log_class.py / slack.py  
>  
> * 슬랙메세지  
> https://api.slack.com/apps에서 토큰받기  
> slcak.py -> 토큰 복사  
> requests 모듈 설치 -> pip install requests  
>  
> * config file  
> log_class.py / slack.py  

### 17. 매수매도 오류 ( 2022.12.01 )
> 로그 파일 확인 : 모의투자 정정 / 취소할 수량이 없습니다.  

### 18. 매수매도 수정 ( 2022.12.02 )
> 수정은 했지만 장 시간 종료로 확인 X ( 2022.12.04 까지 )  
> 12 / 05에도 장 종료돼서 확인 못함 ( 학교 수업 )  

  ``` python   
  def real_event_slots(self):  
    self.OnReceiveRealData.connect(self.realdata_slot) # 실시간 이벤트 연결    
    self.OnReceiveChejanData.connect(self.chejan_slot)  # 종목 주문체결 관련한 이벤트   
 ```  

   ``` python   
def realdata_slot(self, sCode, sRealType, sRealData):  
def chejan_slot(self, sGubun, nItemCnt, sFidList):   
 ```  
 
### 19. 매수매도 수정 후 오류 / 해결 ( 2022.12.06 )  
> 수정 후 잘 돌아가다가 오류  
> 로그 파일 확인 : 종목 관련 정보 반복 출력  
> 깃허브 데스크탑 Revert 후 12/2 코드로 다시 돌려놓기 - 오류 해결  
> 모의투자 정정 / 취소할 수량이 없습니다. - 오류 해결  
  
### 20. 매도 성공 ( 2022.12.06 )  
> 보유하고 있는 종목 ( 삼성전자 ) : 매도조건에 맞아서 매도 성공  

### 21. 미체결 종목 매수취소 성공 ( 2022.12.07 )  
> 다른 가격으로 매수 -> 매수 취소 전달 성공  

### 22. 매수 조건 ( 등락율 ) 수정 ( 2022.12.07 )  
> 조건에 맞는 종목 아예 없음  
> 등락율 d > 2.0 -> d > 1.0 수정
> 최종 조건 : 이동평균선 5일, 등락율 d > 1.0  

 ``` python 
elif d > 1.0 and sCode not in self.jango_dict:  
                self.logging.logger.debug("매수조건 통과 %s " % sCode)
 ```  

### 23. 매수 결과 ( 2022.12.08 )
> 과거 일봉데이터 가져오면 가격이 안맞아서 매수 성공 후 매수 최소 전달됨.  
> 매수 오류는 없으나 조건 통과 종목이 없어서 매수 불가능.    
> 장 종료(주말)로 인해 12/11일까지 매수 불가능. 

### 23. 8시 30분 자동 실행( 2022.12.09 )  
> 작업스케쥴러 이용  
> 아침 8시 30분마다 프로그램 자동으로 실행하도록 설정  
