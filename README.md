# Simple package with fake user agents for your requests.

## Installation
    pip install fake-usrag-bor

## Usage

### 1. Initialization:
    from fake_usrag_bor import FakeUserAgentBOR
    ua = FakeUserAgentBOR()

### 2. Some examples:
    #Random user agent
    ua.random_user_agent()
    >> Mozilla/5.0 (Windows; U; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727)
    
    #Random Google Chrome user agent
    ua.random_chrome_user_agent()
    >> Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.815.0 Safari/535.1
   
    #Simple header with random user agent
    ua.simple_header()
    >> {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.0; en-US; rv:1.8.1.4) Gecko/20070509 Firefox/2.0.0'}
    
    #Simple header with Opera user agent
    ua.simple_header(ua.random_opera_user_agent)
    >> {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.0; Windows XP) Opera 6.04  [fr]'}
    
## Notes

###### This package working without Internet, it's mean, that you shouldn't make request to different sites to take some user agents.

## Release history
* 0.1.36 Description fixes
* 0.1.3 Some bug fixes for Unix systems
* 0.1.2 Removed tested strings from main file
* 0.1.1 Added description to README
* 0.1 Released