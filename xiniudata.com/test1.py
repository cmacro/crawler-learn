import requests
from py_mini_racer import py_mini_racer

cookies = {
    # 'btoken': 'INK2SU787XF2EVG4UUBHZT7LPU414077',
    # 'hy_data_2020_id': '18da368ff49542-0e5729deefc832-1e525637-5089536-18da368ff4a12c1',
    # 'hy_data_2020_js_sdk': '%7B%22distinct_id%22%3A%2218da368ff49542-0e5729deefc832-1e525637-5089536-18da368ff4a12c1%22%2C%22site_id%22%3A211%2C%22user_company%22%3A105%2C%22props%22%3A%7B%7D%2C%22device_id%22%3A%2218da368ff49542-0e5729deefc832-1e525637-5089536-18da368ff4a12c1%22%7D',
    # 'sajssdk_2020_cross_new_user': '1',
    # 'Hm_lvt_42317524c1662a500d12d3784dbea0f8': '1707843584',
    # 'Hm_lpvt_42317524c1662a500d12d3784dbea0f8': '1707843708',
}

headers = {
    'authority': 'www.xiniudata.com',
    'accept': 'application/json',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    'content-type': 'application/json',
    # 'cookie': 'btoken=INK2SU787XF2EVG4UUBHZT7LPU414077; hy_data_2020_id=18da368ff49542-0e5729deefc832-1e525637-5089536-18da368ff4a12c1; hy_data_2020_js_sdk=%7B%22distinct_id%22%3A%2218da368ff49542-0e5729deefc832-1e525637-5089536-18da368ff4a12c1%22%2C%22site_id%22%3A211%2C%22user_company%22%3A105%2C%22props%22%3A%7B%7D%2C%22device_id%22%3A%2218da368ff49542-0e5729deefc832-1e525637-5089536-18da368ff4a12c1%22%7D; sajssdk_2020_cross_new_user=1; Hm_lvt_42317524c1662a500d12d3784dbea0f8=1707843584; Hm_lpvt_42317524c1662a500d12d3784dbea0f8=1707843708',
    'origin': 'https://www.xiniudata.com',
    'pragma': 'no-cache',
    'referer': 'https://www.xiniudata.com/industry/newest?from=data',
    'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
}

json_data = {
    'payload': 'LBc3V0I6ZGB5bXsxTCQnPRBuBAQVcDhbICcmb2x3AjI=',
    'sig': 'CE704F132C4E47B31E91773020275904',
    'v': 1,
}

response = requests.post(
    'https://www.xiniudata.com/api2/service/x_service/person_industry_list/list_industries_by_sort',
    cookies=cookies,
    headers=headers,
    json=json_data,
)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"payload":"LBc3V0I6ZGB5bXsxTCQnPRBuBAQVcDhbICcmb2x3AjI=","sig":"CE704F132C4E47B31E91773020275904","v":1}'
#response = requests.post(
#    'https://www.xiniudata.com/api2/service/x_service/person_industry_list/list_industries_by_sort',
#    cookies=cookies,
#    headers=headers,
#    data=data,
#)

# print(response.text)

l=response.json()['d']

ctx = py_mini_racer.MiniRacer()
with open('./xiniudata.com/test1.js', 'r', encoding='utf-8') as file:
    js_code = file.read()
ctx.eval(js_code)
result = ctx.call('decode', l)

print(result)