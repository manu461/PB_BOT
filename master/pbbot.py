PATTERN = r'(recommendation|trade to make|action to take||currency pick)'

from pycookiecheat import chrome_cookies
from bs4 import BeautifulSoup
import requests, http, json, re
url='https://www.palmbeachgroup.com/monthly-issues/?filter=pbo'

c = {'__cfduid': 'd4a33ebdfc95b8a12f88ccb6ab57886841515154167', '_ga': 'GA1.2.2000975722.1515154173', '_gid': 'GA1.2.1023872585.1522049805', 'GSIDBrxgIoIXfWCS': 'd9858b51-7338-4352-b5b6-b761c3e73b60', 'STSID243866': '417c47f9-d035-4349-88e9-cf973110c791', 'seerses': 'e', '_gat_UA-87443958-1': '1', '_gat': '1', '__attag': '%22lio%3Aall1%2Clio%3Apalm_beach_research_group_master%2Clio%3Aly_unknown_email%2Clio%3Aly_frequent_user%2Clio%3Asmt_new%2Clio%3Aall%22', '__atuvc': '2%7C12', '_hjIncludedInSample': '1', 'PHPSESSID': 'puk8m0upsbsso2ticdrlm277a7', 'wordpress_logged_in_5bc136f5a92deb57afbec1e72c54cb76': 'danusmarke33%40gmail.com%7C1522222684%7CSV2SWJrEMrZb7adkjgAztzHVoVPYmPhQhVq5MIdexQT%7C9e52e03624df9a5e7b1288bb5913c42b567da6ba3533eb203f44685598cd3f76', 'wordpress_test_cookie': 'WP+Cookie+check', 'ly_segs': '%7B%22all1%22%3A%22all1%22%2C%22palm_beach_research_group_master%22%3A%22palm_beach_research_group_master%22%2C%22ly_unknown_email%22%3A%22ly_unknown_email%22%2C%22ly_frequent_user%22%3A%22ly_frequent_user%22%2C%22smt_power%22%3A%22smt_power%22%2C%22all%22%3A%22all%22%7D', 'AWSALB': 'eujy/KHJgmePH4TrKTzCuI/xuXx1WGIThsyJj3NaNLoNwNgUl9x8Zb6LAJe3PpV3V8pCjEXTsRbELBeKWDDcB9wIL5pqXYoGPKuF4qHrgQFWxPo4K7vMVhJyxi61', 'PathforaPageView': '95', 'seerid': '0dbbfae8e8d211fef2e88fa5c33617e6'}
r=requests.get(url,cookies=c)
data=r.content
soup = BeautifulSoup(data,'html.parser')

links = [post.a.get('href') for post in soup.find_all('div', class_='post-entry-wrapper')]

for article_link in links:
    r=requests.get(article_link, cookies=c)
    soup = BeautifulSoup(r.content, 'html.parser')
    print(article_link)
    for h2 in soup.find_all('h2'):
        if (re.match(r'\s*bringing\s*it\s*all\s*together', h2.text, re.IGNORECASE)) is None:
            continue
        h2['id'] = "BIAT"
        candidates = soup.select('#BIAT ~ * > strong')[:5]
        for candidate in candidates:
            if re.match(PATTERN, candidate.text, re.IGNORECASE) is None:
                continue
            print(article_link, "MATCH", candidate.next_sibling)
            break
