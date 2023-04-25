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

    print ('Waiting for turnstile to be solved ...')
    solution = None
    d = {'page_url': 'PAGE_URL_HERE', 'site_key': 'SITEKEY_HERE'}
    # d['action'] = 'taken from page source, optional'
    # d['cdata'] = 'taken from page source, optional'
    # d['domain'] = 'challenges.cloudflare.com'
    captcha_id = bcs.submit_turnstile(d)
    while solution is None:  # while it's still in progress
        resp = bcs.retrieve(captcha_id)
        solution = resp['solution']
        if solution:
            break
        sleep(10)  # sleep for 10 seconds and recheck
    print(solution)


# main method
def main():
    try:
        test_api()
    except Exception as ex:
        print(f'[!] Error occurred: {ex}')

if __name__ == "__main__":
    main()
