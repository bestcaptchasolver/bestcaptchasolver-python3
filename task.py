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

    print ('Waiting for task to be solved ...')
    solution = None
    data = {
        'template_name': 'Login test page',
        'page_url': 'https://bestcaptchasolver.com/automation/login',
        'variables': {"username": "xyz", "password": "0000"},
        # 'proxy': '126.45.34.53:345',   # or 126.45.34.53:123:joe:password
        # 'user_agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0',    # optional
    }
    captcha_id = bcs.submit_task(data)

    # submit pushVariables while task is being solved by the worker
    # very helpful, for e.g. in cases of 2FA authentication
    # bcs.task_push_variables(captcha_id, dict(tfa_code=57))

    while solution is None:  # while it's still in progress
        resp = bcs.retrieve(captcha_id)
        solution = resp['solution']
        sleep(10)  # sleep for 10 seconds and recheck
    print (solution)

    # bcs.set_captcha_bad(2)    # set captcha with ID 2, bad


# main method
def main():
    try:
        test_api()
    except Exception as ex:
        print ('[!] Error occured: {}'.format(ex))


if __name__ == "__main__":
    main()
