#!/usr/bin/python2.7

from bestcaptchasolverapi3.bestcaptchasolverapi import BestCaptchaSolverAPI
from time import sleep

ACCESS_TOKEN = 'ACCESS_TOKEN_HERE'
PAGE_URL = 'PAGE_URL_HERE'
SITE_KEY = 'SITE_KEY_HERE'

# for more details check https://bestcaptchasolver.com/captchabypass-api
def test_api():
    bcs = BestCaptchaSolverAPI(ACCESS_TOKEN)        # get access token from: https://bestcaptchasolver.com/account

    # check account balance
    # ---------------------------
    balance = bcs.account_balance()                       # get account balance
    print ('Balance: {}'.format(balance))                 # print balance

    # solve recaptcha
    # ---------------
    print ('Solving recaptcha ...')
    data = {}
    data['page_url'] = PAGE_URL
    data['site_key'] = SITE_KEY

    # other parameters
    # ----------------------------------------------------------------------
    # reCAPTCHA type(s) - optional, defaults to 1
    # ---------------------------------------------
    # 1 - v2
    # 2 - invisible
    # 3 - v3
    # 4 - enterprise v2
    # 5 - enterprise v3
    #
    # data['type'] = 1
    #
    #data['v3_action'] = 'v3 recaptcha action'
    #data['v3_min_score'] = '0.3'
    #data['domain'] = 'www.google.com'
    #data['data_s'] = 'recaptcha data-s parameter used in loading reCAPTCHA'
    #data['cookie_input'] = 'a=b;c=d'
    #data['user_agent'] = 'Your user agent'
    #data['proxy'] = '123.45.67.89:3031'
    #data['proxy'] = 'user:pass@123.45.67.89:3031'
    #data['affiliate_id'] = 'affiliate_id from /account'
    captcha_id = bcs.submit_recaptcha(data)        # submit captcha first, to get ID

    # check if it's still in progress (waiting to be solved), every 10 seconds
    print ('Waiting for recaptcha to be solved ...')
    gresponse = None
    while gresponse == None:    # while it's still in progress
        resp = bcs.retrieve(captcha_id)
        gresponse = resp['gresponse']
        sleep(10)               # sleep for 10 seconds and recheck

    print ('Recaptcha response: {}'.format(gresponse))         # print google response

    # proxy_status = resp['proxy_status']                      # get status of proxy
    # bcs.set_captcha_bad(2)    # set captcha with ID 2, bad

# main method
def main():
    try:
        test_api()
    except Exception as ex:
        print ('[!] Error occured: {}'.format(ex))

if __name__ == "__main__":
    main()
