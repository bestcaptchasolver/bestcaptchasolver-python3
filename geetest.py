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
    print(f'Balance: {balance}')

    solution = None
    d = {'domain': 'DOMAIN_HERE', 'gt': 'GT_HERE', 'challenge': 'CHALLENGE_HERE'}
    # d['api_server'] = 'GT_DOMAIN_HERE' # optional
    captcha_id = bcs.submit_geetest(d)
    print ('Waiting for geetest to be solved ...')
    while solution is None:    # while it's still in progress
        resp = bcs.retrieve(captcha_id)
        solution = resp['solution']
        sleep(10)               # sleep for 10 seconds and recheck
    print (solution)

    # bcs.set_captcha_bad(2)    # set captcha with ID 2, bad

# main method
def main():
    try:
        test_api()
    except Exception as ex:
        print(f'[!] Error occurred: {ex}')

if __name__ == "__main__":
    main()
