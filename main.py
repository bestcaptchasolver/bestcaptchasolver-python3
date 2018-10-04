#!/usr/bin/python3

from bestcaptchasolverapi3.bestcaptchasolverapi import BestCaptchaSolverAPI
from time import sleep

ACCESS_TOKEN = 'your_access_token'
PAGE_URL = 'your_page_url'
SITE_KEY = 'your_site_key'


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
    # works with URL as well, if authenticated with token
    print ('Solving image captcha ...')
    id = bcs.submit_image_captcha('captcha.jpg', False)  # submit image captcha (case_sensitive param optional)
    image_text = None
    # None is returned if completion is still in pending
    while image_text == None:
        image_text = bcs.retrieve(id)['text']  # get the image text using the ID
        sleep(5)

    print ('Captcha text: {}'.format(image_text))

    # solve recaptcha
    # -----------------------------------------------------------------------------------------------
    print ('Solving recaptcha ...')
    captcha_id = bcs.submit_recaptcha(PAGE_URL, SITE_KEY)  # submit captcha first, to get ID
    # check if it's still in progress (waiting to be solved), every 10 seconds
    print ('Waiting for recaptcha to be solved ...')
    gresponse = None
    while gresponse == None:  # while it's still in progress
        resp = bcs.retrieve(captcha_id)
        gresponse = resp['gresponse']
        sleep(10)  # sleep for 10 seconds and recheck

    print ('Recaptcha response: {}'.format(gresponse))  # print google response
    #proxy_status = resp['proxy_status']                       # get status of proxy

    # bcs.submit_image_captcha('captcha.jpg', True)    # case sensitive captcha image solving
    # bcs.submit_recaptcha(PAGE_URL, SITE_KEY, '123.45.67.89:3012')   # solve through proxy
    # bcs.submit_recaptcha(PAGE_URL, SITE_KEY, 'user:pass@123.45.67.89:3012')  # solve through proxy with auth
    # bcs.set_captcha_bad(2)    # set captcha with ID 2, bad


# main method
def main():
    try:
        test_api()
    except Exception as ex:
        print ('[!] Error occured: {}'.format(ex))


if __name__ == "__main__":
    main()
