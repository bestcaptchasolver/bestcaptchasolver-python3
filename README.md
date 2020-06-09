BestCaptchaSolver.com python3 API wrapper
=========================================

bestcaptchasolver-python3 is a super easy to use bypass captcha python3 API wrapper for bestcaptchasolver.com captcha service

## Installation    
    git clone https://github.com/bestcaptchasolver/bestcaptchasolver-python3

## Dependencies
    pip install requests

## Usage
    # make sure you've changed access_key, page_url, etc in main.py
    python3 main.py  

## How to use?

Simply require the module, set the auth details and start using the captcha service:

``` python
from bestcaptchasolverapi3.bestcaptchasolverapi import BestCaptchaSolverAPI
```
Set access_token for authentication

``` python
access_token = 'access_token_here'
# get your access token from https://bestcaptchasolver.com/account
bcs = BestCaptchaSolverAPI(ACCESS_TOKEN)
```

Once you've set your authentication details, you can start using the API

**Get balance**

``` python
balance = bcs.account_balance()                 
```

**Submit image captcha**

``` python
data = {}
data['image'] = 'captcha.jpg'

# optional parameters
data['is_case'] = if case sensitive set to True, default: False
data['is_phrase'] = if phrase, set to True, default: False
data['is_math'] = True if captcha is math, default: False
data['alphanumeric'] = 1 (digits only) or 2 (letters only), default: all characters
data['minlength'] = minimum length of captcha text, default: any
data['maxlength'] = maximum length of captcha text, default: any

bcs.submit_image_captcha(data)
```
The image submission works with both files and b64 encoded strings.
For setting the affiliate_id, set the `affiliate_id` parameter

**Submit recaptcha details**

For recaptcha submission there are two things that are required.
- page_url
- site_key
- type (optional)
- v3_action (optional)
- v3_min_score (optional)
- data_s (optional)
- user_agent (optional)
- affiliate_id (optional)
- proxy (optional)

``` python
bcs.submit_recaptcha({'page_url': 'page_url_here', 'site_key': 'sitekey_here')   
```

This method returns a captchaID. This ID will be used next, to retrieve the g-response, once workers have 
completed the captcha. This takes somewhere between 10-80 seconds.

**Geetest**
- domain
- gt
- challenge

```python
captcha_id = bcs.submit_geetest({'domain': 'DOMAIN_HERE', 'gt': 'GT_HERE', 'challenge': 'CHALLENGE_HERE'})
```

Use captcha_id to retrieve `solution` for geetest

**Capy**
- page_url
- site_key

```python
captcha_id = bcs.submit_capy({'page_url': 'PAGE_URL_HERE', 'site_key': 'SITEKEY_HERE'})
```

Use captcha_id to retrieve `solution` for capy

**hCaptcha**
- page_url
- site_key

```python
captcha_id = bcs.submit_hcaptcha({'page_url': 'PAGE_URL_HERE', 'site_key': 'SITEKEY_HERE'})
```

Use captcha_id to retrieve `solution` for hCaptcha

**Retrieve captcha response (all captchas)**

```
image_text = bcs.retrieve(captcha_id)['text']
gresponse = bcs.retrieve(recaptcha_id)['gresponse']
solution = bcs.retrieve(captcha_id)['solution']
```

**If submitted with proxy, get proxy status**
```
proxy_status = bcs.retrieve(recaptcha_id)['proxy_status']
```


**Set captcha bad**

When a captcha was solved wrong by our workers, you can notify the server with it's ID,
so we know something went wrong.

``` python
bcs.set_captcha_bad(captcha_id)
```

## Examples
Check main.py

## License
API library is licensed under the MIT License

## More information
More details about the server-side API can be found [here](https://bestcaptchasolver.com/api )


<sup><sub>captcha, bypasscaptcha, decaptcher, decaptcha, 2captcha, deathbycaptcha, anticaptcha, 
bypassrecaptchav2, bypassnocaptcharecaptcha, bypassinvisiblerecaptcha, captchaservicesforrecaptchav2, 
recaptchav2captchasolver, googlerecaptchasolver, recaptchasolverpython, recaptchabypassscript, bestcaptchasolver</sup></sub>

