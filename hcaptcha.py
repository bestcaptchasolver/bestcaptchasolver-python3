#!/usr/bin/python2.7

from bestcaptchasolverapi3.bestcaptchasolverapi import BestCaptchaSolverAPI
from time import sleep

ACCESS_TOKEN = 'ACCESS_TOKEN_HERE'

# for more details check https://bestcaptchasolver.com/captchabypass-api
def test_api():
    bcs = BestCaptchaSolverAPI(ACCESS_TOKEN)        # get access token from: https://bestcaptchasolver.com/account

    # check account balance
    # ---------------------------
    balance = bcs.account_balance()                       # get account balance
    print ('Balance: {}'.format(balance))                 # print balance

    print ('Waiting for hCaptcha to be solved ...')
    solution = None
    captcha_id = bcs.submit_hcaptcha({'page_url': 'PAGE_URL_HERE', 'site_key': 'SITEKEY_HERE'})
    while solution == None:  # while it's still in progress
        resp = bcs.retrieve(captcha_id)
        solution = resp['solution']
        sleep(10)  # sleep for 10 seconds and recheck
    print (solution)

# main method
def main():
    try:
        test_api()
    except Exception as ex:
        print ('[!] Error occured: {}'.format(ex))

if __name__ == "__main__":
    main()
