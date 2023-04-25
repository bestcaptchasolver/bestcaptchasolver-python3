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

    print ('Solving image captcha ...')
    data = {'image': '../captcha.jpg'}
    # optional parameters
    # -------------------
    # data['is_case'] = True, default: False
    # data['is_phrase'] = True, default: False
    # data['is_math'] = True, default: False
    # data['alphanumeric'] = 1 (digits only) or 2 (letters only), default: all characters
    # data['minlength'] = minimum length of captcha text, default: any
    # data['maxlength'] = maximum length of captcha text, default: any
    # data['affiliate_id'] = 'affiliate_id from /account'

    id = bcs.submit_image_captcha(data)  # submit image captcha (case_sensitive param optional)
    image_text = None
    # None is returned if completion is still in pending
    while image_text is None:
        image_text = bcs.retrieve(id)['text']  # get the image text using the ID
        sleep(5)

    print(f'Captcha text: {image_text}')

# main method
def main():
    try:
        test_api()
    except Exception as ex:
        print(f'[!] Error occurred: {ex}')

if __name__ == "__main__":
    main()
