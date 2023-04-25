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
    d = {'domain': 'https://example.com', 'captchaid': '647f5ed2ed8acb4be36784e01556bb71'}
    # d['user_agent'] = 'your user agent'
    # d['proxy'] = 'user:pass@123.45.67.89:3031'
    # d['affiliate_id'] = 'your affiliate id'
    captcha_id = bcs.submit_geetest_v4(d)
    print('Waiting for geetestv4 to be solved ...')
    while solution is None:    # while it's still in progress
        resp = bcs.retrieve(captcha_id)
        solution = resp['solution']
        sleep(10)               # sleep for 10 seconds and recheck
    print(solution)

    # bcs.set_captcha_bad(2)    # set captcha with ID 2, bad


# main method
def main():
    try:
        test_api()
    except Exception as ex:
        print(f'[!] Error occurred: {ex}')


if __name__ == "__main__":
    main()
