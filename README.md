# AIFT_J_PROJECT

2022-2 SSWU PROJECT  
* Artificial Intelligence in Financial Trade Project  
* 손가락 하나 까딱하지 않는 주식 거래 시스템 구축 (참고)  
 
## 현재 진행상황  

### 1. 키움 API 설치 및 환경설정  

> PyCharm, Anaconda Windows 64-Bit   
> CMD 관리자 권한 실행  
> 32bit 가상환경 set CONDA_FORCE_32BIT=1  
> PyQt5 필요  

### 2. 키움 API로 키움증권 로그인 ( ~ 2022.11.14 )  

> 계좌개설, 공동인증서  

'''python 
self.get_ocx_instance()  
self.event_slots()  
self.signal_login_commConnect()  
'''
 
 ```
python 
self.get_ocx_instance()  
self.event_slots()  
self.signal_login_commConnect()  
```

### 3. 계좌번호  ( ~ 2022.11.14 )  

> 로그인 후 계좌번호 요청  

 '''python  
self.get_account_info()  
'''

### 4. 예수금 정보 ( ~ 2022.11.15 )  

> opw 00001 : 예수금상세현황요청  
>trdata_slot 오류 해결 ( 자동로그인 필수 )  

'''python  
self.detail_account_info()  
'''

### 5. 계좌평가잔고내역, 보유 종목, 미체결 종목, 코스닥 개수, 일봉데이터 ( ~ 2022.11.16 )  

> 키움증권 모의투자로 로그인 후 매수 ( 체결 / 미체결되도록 매수 후 확인 완료 )  
> 싱글데이터로 정보 처리, 멀티데이터로 보유 종목 정보 처리  
> 코스닥 종목 일봉데이터 가져오기  

''' python  
self.detail_account_mystock()  
self.not_concluded_account()   
self.calculator_fnc()  
'''
