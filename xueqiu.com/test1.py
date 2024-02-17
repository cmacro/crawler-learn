import requests

from py_mini_racer import py_mini_racer
import re
from datetime import datetime, timedelta

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Referer': 'https://xueqiu.com/today',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
}

response = requests.get(r'https://xueqiu.com/today', headers=headers)
with open(r'./fristresponse.html', 'w', encoding='utf-8') as f:
    f.write(response.text)
print(response.status_code)

# 使用正则表达式提取 arg1 参数的值
html_content = response.text
match = re.search(r"var arg1='([^']*)';", html_content)
if match:
    arg1_value = match.group(1)
    print("arg1 value:", arg1_value)
else:
    print("failed arg1 parameter not found.")

# arg1 = '1E4D9885F310E251757FBEB071E4DC082A525D0F'
ctx = py_mini_racer.MiniRacer()
with open(r'./xueqiu.com/test1.js', 'r', encoding='utf-8') as file:
    js_code = file.read()
ctx.eval(js_code)
acw_sc__v2 = ctx.call('decode', arg1_value)
print(acw_sc__v2)


# 增加 3600 秒（1小时）
expire_date = datetime.now() + timedelta(seconds=3600)
expire_date_str = expire_date.strftime('%a, %d %b %Y %H:%M:%S GMT')


cookies = {
    'acw_sc__v2': acw_sc__v2,
    'max-age':'3600',
    'expires': expire_date_str,
    'path':'/'
}

# cookies = {
#     'acw_tc': '2760826517080122888794310ef576e9e81683655a4307c6cce99273a085a1',
#     'acw_sc__v2': '65ce33002863da5cb783ea29aebf8ebad0c631f9',
#     'xq_a_token': 'f5e826d5be1c4265b380bc7d743963f24729480d',
#     # 'xqat': 'f5e826d5be1c4265b380bc7d743963f24729480d',
#     # 'xq_r_token': '276e026a754b9a09bd76b733aa3ae41ab08ac00b',
#     # 'xq_id_token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1aWQiOi0xLCJpc3MiOiJ1YyIsImV4cCI6MTcwOTc3MjM1MSwiY3RtIjoxNzA4MDE0MDEwODU2LCJjaWQiOiJkOWQwbjRBWnVwIn0.aOcmySRNWJAYMptqbF0DWB9jOFbsfAXh5zEdoHBDgF9iwE8aHN7HCmMKDC-ErXqF18vE-gOECblINgrXYg7EU0QpEYaSAFmXz19eyC9zK-cllyMDunafoaxVr0yRGMmCo47QOSddS2LaSbRQKBErf60IJ_5LrFWEcvY3ThgSxwf1-RuSVMHFyXP4Zx1G1xyEtjIS5J-uvzGzfO2hUnskSjDSPdhb_lFJVFsWiBIrMv3yKQLkGg1PMzaX607GaVzhZp2jt-k0DtTIkoNhTApXWtNTUi1ec0WPK_QviDUTj5KYXeGq7JtEu9JLNRUdwZp6vBxsstmuh10-arDMd3JJpQ',
#     # 'cookiesu': '631708014049985',
#     'u': '631708014049985',
# }

response = requests.get(r'https://xueqiu.com/today', headers=headers, cookies=cookies)
with open(r'./secondresponse.html', 'w', encoding='utf-8') as f:
    f.write(response.text)


# print(response.text)
