
# 安装 py_mini_racer 库
# pip install py_mini_racer

# py_mini_racer 和 PyExecJS  JavaScript代码的库，但它们之间有一些区别。 
# - PyExecJS 兼容性高 为通用型js解析器能支持包括 Node.js、PhantomJS、Apple JavaScriptCore 等
# - py_mini_racer 执行效率高 是专为js优化过效率比较高，使用v8引擎

# import execjs
from py_mini_racer import py_mini_racer
import requests

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Origin': 'https://www.qimingpian.com',
    'Pragma': 'no-cache',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'cross-site',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
}

data = {
    'time_interval': '',
    'tag': '',
    'tag_type': '',
    'province': '',
    'lunci': '',
    'page': '1',
    'num': '20',
    'unionid': '',
}

response = requests.post('https://vipapi.qimingpian.cn/DataList/productListVip', headers=headers, data=data)
# print(response.text)
encrypt_data=response.json()['encrypt_data']

# # 读取JavaScript文件内容
# with open('./qimingpian.com/test2.js', 'r', encoding='utf-8') as file:
#     js_code = file.read()
# context = execjs.compile(js_code)
# result = context.call("s", encrypt_data)

with open('./qimingpian.com/test2.js', 'r', encoding='utf-8') as file:
    js_code = file.read()
    
ctx = py_mini_racer.MiniRacer()
ctx.eval(js_code)
result = ctx.call('s', encrypt_data)

# 打印结果
print(result)