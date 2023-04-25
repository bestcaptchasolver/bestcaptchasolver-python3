try:
    from requests import session
    import requests
except:
    raise Exception('requests package not installed, try with: \'pip2.7 install requests\'')

import os, json
from base64 import b64encode

USER_AGENT = 'python3Client'
BASE_URL = 'https://bcsapi.xyz/api'
SSL_VERIFY = True


# API class
class BestCaptchaSolverAPI:
    def __init__(self, access_token, timeout=120):
        self._access_token = access_token
        self._data = {
            'access_token': access_token
        }

        self._timeout = timeout
        self._session = session()       # init a new session

        self._headers = {               # use this user agent
            'User-Agent' : USER_AGENT
        }

    # get account balance
    def account_balance(self):
        url = f'{BASE_URL}/user/balance?access_token={self._access_token}'
        resp = self.GET(url)
        return f"${resp['balance']}"

    # solve classic image captcha
    def submit_image_captcha(self, opts):
        data = {}
        data.update(self._data)

        image_path = opts['image']
        # optional parameters
        if 'case_sensitive' in opts:
            print ('case_sensitive is deprecated, use is_case instead')
            if opts['case_sensitive']: data['is_case'] = True
        if 'is_case' in opts and opts['is_case']:
            data['is_case'] = True
        if 'is_phrase' in opts and opts['is_phrase']:
            data['is_phrase'] = True
        if 'is_math' in opts and opts['is_math']:
            data['is_math'] = True
        if 'alphanumeric' in opts: data['alphanumeric'] = opts['alphanumeric']
        if 'minlength' in opts: data['minlength'] = opts['minlength']
        if 'maxlength' in opts: data['maxlength'] = opts['maxlength']

        # affiliate
        if 'affiliate_id' in opts and opts['affiliate_id']:
            data['affiliate_id'] = opts['affiliate_id']
        url = f'{BASE_URL}/captcha/image'

        if os.path.exists(image_path):
            with open(image_path, 'rb') as f:
                data['b64image'] = b64encode(f.read())
        else:
            data['b64image'] = image_path  # should be b64 already

        resp = self.POST(url, data)
        return resp['id']  # return ID

    # submit recaptcha to system
    def submit_task(self, data):
        data.update(self._data)
        url = f'{BASE_URL}/captcha/task'
        resp = self.POST(url, data)
        return resp['id']  # return ID

    # submit recaptcha to system
    def task_push_variables(self, captcha_id, push_variables: dict):
        d = dict(pushVariables=push_variables)
        d.update(self._data)
        url = f'{BASE_URL}/captcha/task/pushVariables/{captcha_id}'
        resp = self.POST(url, d)
        if 'error' in resp:
            raise Exception(resp['error'])
        return True

    # submit recaptcha to system
    def submit_recaptcha(self, data):
        data.update(self._data)
        url = f'{BASE_URL}/captcha/recaptcha'
        resp = self.POST(url, data)
        return resp['id']  # return ID

    def submit_turnstile(self, data):
        data.update(self._data)
        url = f'{BASE_URL}/captcha/turnstile'
        resp = self.POST(url, data)
        return resp['id']  # return ID

    # submit geetest to system
    def submit_geetest(self, data):
        data.update(self._data)
        url = f'{BASE_URL}/captcha/geetest'
        resp = self.POST(url, data)
        return resp['id']  # return ID
    
    # submit geetest v4 to system
    def submit_geetest_v4(self, data):
        data.update(self._data)
        url = f'{BASE_URL}/captcha/geetestv4'
        resp = self.POST(url, data)
        return resp['id']  # return ID

    # submit capy to system
    def submit_capy(self, data):
        data.update(self._data)
        url = f'{BASE_URL}/captcha/capy'
        resp = self.POST(url, data)
        return resp['id']  # return ID

    # submit hcaptcha to system
    def submit_hcaptcha(self, data):
        data.update(self._data)
        url = f'{BASE_URL}/captcha/hcaptcha'
        resp = self.POST(url, data)
        return resp['id']  # return ID

    # submit funcaptcha to system
    def submit_funcaptcha(self, data):
        data.update(self._data)
        url = f'{BASE_URL}/captcha/funcaptcha'
        resp = self.POST(url, data)
        return resp['id']  # return ID

    # retrieve captcha
    def retrieve(self, captcha_id = None):
        url = f'{BASE_URL}/captcha/{captcha_id}?access_token={self._access_token}'
        resp = self.GET(url)
        try:
            if resp['status'] == 'pending': return {'text': None, 'gresponse': None, 'solution': None}
        except:
            pass

        return resp

    # set captcha bad, if given id, otherwise set the last one
    def set_captcha_bad(self, captcha_id):
        data = dict(self._data)
        url = f'{BASE_URL}/captcha/bad/{captcha_id}'
        resp = self.POST(url, data)
        return resp['status']

    def GET(self, url):
        r = self._session.get(url, headers=self._headers, timeout=self._timeout, verify=SSL_VERIFY)
        js = json.loads(r.text)
        if js['status'] == 'error': raise Exception(js['error'])
        return js

    def POST(self, url, data):
        if 'proxy' in data: data['proxy_type'] = 'HTTP'  # add proxy, if necessary
        r = self._session.post(url, json=data, headers=self._headers, timeout=self._timeout, verify=SSL_VERIFY)
        js = json.loads(r.text)
        if js['status'] == 'error': raise Exception(js['error'])
        return js
