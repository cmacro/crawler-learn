import time
import requests
import execjs


timestamp = int(time.time() * 1000)

with open('./oklink.com/test1.js', 'r', encoding='utf-8') as file:
    js_code = file.read()
context = execjs.compile(js_code)
xapikey = context.call("getApiKey")

cookies = {}

headers = {
    'authority': 'www.oklink.com',
    'accept': 'application/json',
    'accept-language': 'zh-CN,zh;q=0.9',
    'app-type': 'web',
    'cache-control': 'no-cache',
    # 'cookie': 'aliyungf_tc=6e9b3b0704339018ddcd4aa063d068a0a501fa9ee6726da889860b03f4790cb2; locale=zh_CN; browserVersionLevel=v5.6ad2a8e37c01; devId=8803249d-7332-4f6d-b650-d9dc37b474b9; okg.currentMedia=xl; _monitor_extras={"deviceId":"1qQvmDv8H5pFoKVwmgqm-k","eventId":12,"sequenceNumber":12}; amp_d77757=0ekYKoTqlWG0NVcpHlx2pK...1hmj5ckkf.1hmj5f0fh.b.0.b; ok-ses-id=e5kolvhUfiivW1bVr8kwXalAG7kA7Qm8TVYorBb2mWMQDo3b6xzky8HI4dF+cEF2vdQtagxHNtR9kN/88NTp/jakm1zN5QBlj/jNDecQmKbitPLLUtqMkaGeOVETij5+',
    'devid': '8803249d-7332-4f6d-b650-d9dc37b474b9',
    'pragma': 'no-cache',
    'referer': 'https://www.oklink.com/cn/btc/tx-list/page/3',
    # 'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
    # 'sec-ch-ua-mobile': '?0',
    # 'sec-ch-ua-platform': '"macOS"',
    # 'sec-fetch-dest': 'empty',
    # 'sec-fetch-mode': 'cors',
    # 'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
    # 'x-apikey': 'LWIzMWUtNDU0Ny05Mjk5LWI2ZDA3Yjc2MzFhYmEyYzkwM2NjfDI4MTkwMDc5NDc0NjY2Nzg=',
    'x-apikey': xapikey,
    'x-cdn': 'https://static.oklink.com',
    'x-locale': 'zh_CN',
    'x-site-info': '[object Object]',
    'x-utc': '8',
    'x-zkdex-env': '0',
}

params = {
    't': f'{timestamp}',
    'offset': '40',
    'txType': '',
    'limit': '20',
    'curType': '',
}

response = requests.get(
    'https://www.oklink.com/api/explorer/v1/btc/transactionsNoRestrict',
    params=params,
    cookies=cookies,
    headers=headers,
)
print(response.text)
print(response.status_code)