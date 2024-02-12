import time
import requests

timestamp = int(time.time() * 1000)

handler = {
    "Accept": "application/json, text/plain, */*",
    "X-Requested-With": "XMLHttpRequest",
    "Content-Type": "application/json;charset=utf-8",
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'
}
data = '{"pageNo":2,"pageSize":15,"categoryCode":"GovernmentProcurement","_t":%d}' % (timestamp)

url = 'http://www.whggzy.com/portal/category'
response = requests.post(url, headers=handler, data=data)
print(response.text)
print(response.status_code)