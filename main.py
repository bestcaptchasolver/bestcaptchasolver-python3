#!/usr/bin/python3

from bestcaptchasolverapi3.bestcaptchasolverapi import BestCaptchaSolverAPI
from time import sleep

ACCESS_TOKEN = 'access_token_here'
PAGE_URL = 'page_url_here'
SITE_KEY = 'site_key_here'


# solve captcha
def test_api():
    # get access token from: https://bestcaptchasolver.com/account
    bcs = BestCaptchaSolverAPI(ACCESS_TOKEN)

    # check account balance
    # ---------------------------
    balance = bcs.account_balance()  # get account balance
    print ('Balance: {}'.format(balance))  # print balance

    # solve image captcha
    # --------------------
    print ('Solving image captcha ...')
    data = {}
    data['image'] = 'captcha.jpg'
    # data['case_sensitive'] = True #, default: False
    # data['affiliate_id'] = 'affiliate_id from /account'
    id = bcs.submit_image_captcha(data)  # submit image captcha (case_sensitive param optional)
    image_text = None
    # None is returned if completion is still in pending
    while image_text == None:
        image_text = bcs.retrieve(id)['text']  # get the image text using the ID
        sleep(5)

    print ('Captcha text: {}'.format(image_text))

    # solve recaptcha
    # ---------------
    print ('Solving recaptcha ...')
    data = {}
    data['page_url'] = PAGE_URL
    data['site_key'] = SITE_KEY

    # other parameters
    # ----------------------------------------------------------------------
    # data['type'] = 1        # 1 - regular, 2 - invisible, 3 - v3, default 1
    # data['v3_action'] = 'v3 recaptcha action'
    # data['v3_min_score'] = '0.3'
    # data['user_agent'] = 'Your user agent'
    # data['proxy'] = '123.456.678:3031'
    # data['proxy'] = 'user:pass@123.456.678:3031'
    # data['affiliate_id'] = 'affiliate_id from /account'
    captcha_id = bcs.submit_recaptcha(data)  # submit captcha first, to get ID

    # check if it's still in progress (waiting to be solved), every 10 seconds
    print ('Waiting for recaptcha to be solved ...')
    gresponse = None
    while gresponse == None:  # while it's still in progress
        resp = bcs.retrieve(captcha_id)
        gresponse = resp['gresponse']
        sleep(10)  # sleep for 10 seconds and recheck

    print ('Recaptcha response: {}'.format(gresponse))  # print google response
    # proxy_status = resp['proxy_status']                       # get status of proxy
    # bcs.set_captcha_bad(2)    # set captcha with ID 2, bad

# main method
def main():
    try:
        test_api()
    except Exception as ex:
        print ('[!] Error occured: {}'.format(ex))


if __name__ == "__main__":
    main()
