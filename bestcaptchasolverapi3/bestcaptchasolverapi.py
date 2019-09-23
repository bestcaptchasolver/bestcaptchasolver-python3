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
# endpoints
# -------------------------------------------------------------------------------------------


# API class
# -----------------------------------------
class BestCaptchaSolverAPI:
    def __init__(self, access_token, timeout = 120):
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
        url = '{}/user/balance?access_token={}'.format(BASE_URL, self._access_token)
        resp = self.GET(url)
        return '${}'.format(resp['balance'])

    # solve normal captcha
    def submit_image_captcha(self, opts):
        data = {}
        data.update(self._data)

        image_path = opts['image']
        # optional parameters
        if 'case_sensitive' in opts:
            print ('case_sensitive is deprecated, use is_case instead')
            if opts['case_sensitive']: data['is_case'] = True
        if 'is_case' in opts:
            if opts['is_case']: data['is_case'] = True
        if 'is_phrase' in opts:
            if opts['is_phrase']: data['is_phrase'] = True
        if 'is_math' in opts:
            if opts['is_math']: data['is_math'] = True
        if 'alphanumeric' in opts: data['alphanumeric'] = opts['alphanumeric']
        if 'minlength' in opts: data['minlength'] = opts['minlength']
        if 'maxlength' in opts: data['maxlength'] = opts['maxlength']

        # affiliate
        if 'affiliate_id' in opts:
            if opts['affiliate_id']: data['affiliate_id'] = opts['affiliate_id']
        url = '{}/captcha/image'.format(BASE_URL)

        if os.path.exists(image_path):
            with open(image_path, 'rb') as f:
                data['b64image'] = b64encode(f.read())
        else:
            data['b64image'] = image_path  # should be b64 already

        resp = self.POST(url, data)
        return resp['id']  # return ID

    # submit recaptcha to system
    def submit_recaptcha(self, data):
        data.update(self._data)
        if 'proxy' in data: data['proxy_type'] = 'HTTP'  # add proxy, if necessary
        # make request with all data
        url = '{}/captcha/recaptcha'.format(BASE_URL)
        resp = self.POST(url, data)
        return resp['id']  # return ID

    # submit geetest to system
    def submit_geetest(self, data):
        data.update(self._data)
        if 'proxy' in data: data['proxy_type'] = 'HTTP'  # add proxy, if necessary
        # make request with all data
        url = '{}/captcha/geetest'.format(BASE_URL)
        resp = self.POST(url, data)
        return resp['id']  # return ID

    # submit capy to system
    def submit_capy(self, data):
        data.update(self._data)
        if 'proxy' in data: data['proxy_type'] = 'HTTP'  # add proxy, if necessary
        # make request with all data
        url = '{}/captcha/capy'.format(BASE_URL)
        resp = self.POST(url, data)
        return resp['id']  # return ID

    # retrieve captcha
    def retrieve(self, captcha_id = None):
        url = '{}/captcha/{}?access_token={}'.format(BASE_URL, captcha_id, self._access_token)
        resp = self.GET(url)
        try:
            if resp['status'] == 'pending': return {'text': None, 'gresponse': None, 'solution': None}
        except:
            pass

        return resp

    # set captcha bad, if given id, otherwise set the last one
    def set_captcha_bad(self, captcha_id):
        data = dict(self._data)
        url = '{}/captcha/bad/{}'.format(BASE_URL, captcha_id)
        resp = self.POST(url, data)
        return resp['status']

    def GET(self, url):
        r = self._session.get(url, headers=self._headers, timeout=self._timeout, verify=SSL_VERIFY)
        js = json.loads(r.text)
        if js['status'] == 'error': raise Exception(js['error'])
        return js

    def POST(self, url, data):
        r = self._session.post(url, data=data, headers=self._headers, timeout=self._timeout, verify=SSL_VERIFY)
        js = json.loads(r.text)
        if js['status'] == 'error': raise Exception(js['error'])
        return js
