import requests
from cfmz.settings import API_KEY


class YunPian(object):

    def __init__(self, api_key):
        self.api_key = api_key
        self.single_send_url = 'https://sms.yunpian.com/v2/sms/single_send.json'

    def send_message(self, phone, code):
        params = {
            'apikey': self.api_key,
            'mobile': phone,
            'text': f"【善杰test】正在进行登录操作，您的验证码是{code}"
        }

        resp = requests.post(self.single_send_url, data=params)
        print(params)
        print(resp)



