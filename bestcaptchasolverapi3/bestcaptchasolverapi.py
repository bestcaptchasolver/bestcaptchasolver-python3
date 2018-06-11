try:
    from requests import session
    import requests
except:
    raise Exception('requests package not installed, try with: \'pip2.7 install requests\'')

import os, json
from base64 import b64encode

USER_AGENT = 'pythonClient'
BASE_URL = 'https://bcsapi.xyz/api'
SSL_VERIFY = False
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
    def submit_image_captcha(self, image_path, case_sensitive = False):
        data = dict(self._data)
        url = '{}/captcha/image'.format(BASE_URL)
        if os.path.exists(image_path):
            with open(image_path, 'rb') as f:
                data['b64image'] = b64encode(f.read())
        else:
            data['b64image'] = image_path       # should be b64 already

        if case_sensitive: data['case_sensitive'] = '1'

        resp = self.POST(url, data)
        return resp['id']       # return ID

    # submit recaptcha to system
    # SET PROXY AS WELL
    # -------------------
    # ----------------------------------
    # ------------------------------
    def submit_recaptcha(self, page_url, site_key, proxy = None):
        # data parameters
        data = dict(self._data)
        data['page_url'] = page_url
        data['site_key'] = site_key

        # check proxy and set dict (request params) accordingly
        if proxy:   # if proxy is given, check proxytype
            # we have both proxy and type at this point
            data['proxy'] = proxy
            data['proxytype'] = 'HTTP'

        # make request with all data
        url = '{}/captcha/recaptcha'.format(BASE_URL)
        resp = self.POST(url, data)
        return resp['id']  # return ID

    # retrieve captcha
    def retrieve(self, captcha_id = None):
        url = '{}/captcha/{}?access_token={}'.format(BASE_URL, captcha_id, self._access_token)
        resp = self.GET(url)
        try:
            if resp['status'] == 'pending': return None
        except:
            pass
        try:
            return resp['gresponse']
        except:
            return resp['text']

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
