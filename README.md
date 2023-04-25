BestCaptchaSolver.com python3 API wrapper
=========================================

bestcaptchasolver-python3 is a super easy to use bypass captcha python3 API wrapper for bestcaptchasolver.com captcha service

## Installation    
    git clone https://github.com/bestcaptchasolver/bestcaptchasolver-python3

## Dependencies
    pip install -r requirements.txt

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
- type (optional, defaults to 1 if not given)
  - `1` - v2
  - `2` - invisible
  - `3` - v3
  - `4` - enterprise v2
  - `5` - enterprise v3
- v3_action (optional)
- v3_min_score (optional)
- domain (optional) - i.e `www.google.com` or `recaptcha.net`
- data_s (optional)
- cookie_input (optional)
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
- api_server (optional)

```python
d = {'domain': 'DOMAIN_HERE', 'gt': 'GT_HERE', 'challenge': 'CHALLENGE_HERE'}
# d['api_server'] = 'GT_DOMAIN_HERE' # optional
captcha_id = bcs.submit_geetest(d)
```

Use captcha_id to retrieve `solution` for geetest

**GeetestV4**
- domain
- captchaid

**Important:** This is not the captchaid that's in our system that you receive while submitting a captcha. Gather this from HTML source of page with geetestv4 captcha, inside the `<script>` tag you'll find a link that looks like this: https://i.imgur.com/XcZd47y.png

```python
d = {'domain': 'https://example.com', 'captchaid': '647f5ed2ed8acb4be36784e01556bb71'}
captcha_id = bcs.submit_geetest_v4(d)
```

Use captcha_id received from service to retrieve `solution` for geetestv4

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
d = {'page_url': 'PAGE_URL_HERE', 'site_key': 'SITEKEY_HERE'}
# d['invisible'] = True
# d['payload'] = {'rqdata': 'gather from page source, unique with each submission'}
# d['domain'] = 'challenges.cloudflare.com'     # optional
captcha_id = bcs.submit_hcaptcha(d)
```

Use captcha_id to retrieve `solution` for hCaptcha

**FunCaptcha (Arkose Labs)**
- page_url
- s_url
- site_key

```python
captcha_id = bcs.submit_funcaptcha({'page_url': 'PAGE_URL_HERE', 'site_key': 'SITEKEY_HERE', 's_url': 'S_URL_HERE'})
```

**Turnstile (Cloudflare)**
- page_url
- site_key

```python
d = {'page_url': 'PAGE_URL_HERE', 'site_key': 'SITEKEY_HERE'}
# d['action'] = 'taken from page source, optional'
# d['cdata'] = 'taken from page source, optional'
# d['domain'] = 'challenges.cloudflare.com' # optional
captcha_id = bcs.submit_turnstile(d)
```

**Task**
- template_name
- page_url
- variables

```python
data = {
    'template_name': 'Login test page',
    'page_url': 'https://bestcaptchasolver.com/automation/login',
    'variables': {"username": "xyz", "password": "0000"},
     # 'proxy': '126.45.34.53:345',   # or 126.45.34.53:123:joe:password
     # 'user_agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0',    # optional
}
captcha_id = bcs.submit_task(data)
```

#### Task pushVariables
Update task variables while it is being solved by the worker. Useful when dealing with data / variables, of which
value you don't know, only after a certain step or action of the task. For example, in websites that require 2 factor
authentication code.

When the task (while running on workers machine) is getting to an action defined in the template, that requires a variable, but variable was not
set with the task submission, it will wait until the variable is updated through push.

The `bcs.task_push_variables(captcha_id, push_variables)` method can be used as many times as it is needed.

```python
bcs.task_push_variables(captcha_id, dict(tfa_code=57))
```

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

