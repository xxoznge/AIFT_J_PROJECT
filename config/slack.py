import requests

class MyMsg():
    def send_msg(self, msg=""):
        response = requests.post(
            'https://slack.com/api/chat.postMessage',
            headers={
                'Authorization': 'Bearer '+'xoxb-4384492639233-4456863566545-JQMWJozEkTKEfGtg2rGI83WJ'
            },
            data={
                'channel':'#realmessage',
                'text':msg
            }
        )
        print(response)

MyMsg().send_msg(msg="슬랙으로 전송하기")