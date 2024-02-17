import requests
from py_mini_racer import py_mini_racer

cookies = {
    'acw_tc': '2760826517080122888794310ef576e9e81683655a4307c6cce99273a085a1',
    'acw_sc__v2': '65ce33002863da5cb783ea29aebf8ebad0c631f9',
    'xq_a_token': 'f5e826d5be1c4265b380bc7d743963f24729480d',
    # 'xqat': 'f5e826d5be1c4265b380bc7d743963f24729480d',
    # 'xq_r_token': '276e026a754b9a09bd76b733aa3ae41ab08ac00b',
    # 'xq_id_token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1aWQiOi0xLCJpc3MiOiJ1YyIsImV4cCI6MTcwOTc3MjM1MSwiY3RtIjoxNzA4MDE0MDEwODU2LCJjaWQiOiJkOWQwbjRBWnVwIn0.aOcmySRNWJAYMptqbF0DWB9jOFbsfAXh5zEdoHBDgF9iwE8aHN7HCmMKDC-ErXqF18vE-gOECblINgrXYg7EU0QpEYaSAFmXz19eyC9zK-cllyMDunafoaxVr0yRGMmCo47QOSddS2LaSbRQKBErf60IJ_5LrFWEcvY3ThgSxwf1-RuSVMHFyXP4Zx1G1xyEtjIS5J-uvzGzfO2hUnskSjDSPdhb_lFJVFsWiBIrMv3yKQLkGg1PMzaX607GaVzhZp2jt-k0DtTIkoNhTApXWtNTUi1ec0WPK_QviDUTj5KYXeGq7JtEu9JLNRUdwZp6vBxsstmuh10-arDMd3JJpQ',
    # 'cookiesu': '631708014049985',
    'u': '631708014049985',
}

headers = {
    'Accept': '*/*',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    # 'Cookie': 'acw_tc=2760826517080122888794310ef576e9e81683655a4307c6cce99273a085a1; acw_sc__v2=65ce33002863da5cb783ea29aebf8ebad0c631f9; xq_a_token=f5e826d5be1c4265b380bc7d743963f24729480d; xqat=f5e826d5be1c4265b380bc7d743963f24729480d; xq_r_token=276e026a754b9a09bd76b733aa3ae41ab08ac00b; xq_id_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1aWQiOi0xLCJpc3MiOiJ1YyIsImV4cCI6MTcwOTc3MjM1MSwiY3RtIjoxNzA4MDE0MDEwODU2LCJjaWQiOiJkOWQwbjRBWnVwIn0.aOcmySRNWJAYMptqbF0DWB9jOFbsfAXh5zEdoHBDgF9iwE8aHN7HCmMKDC-ErXqF18vE-gOECblINgrXYg7EU0QpEYaSAFmXz19eyC9zK-cllyMDunafoaxVr0yRGMmCo47QOSddS2LaSbRQKBErf60IJ_5LrFWEcvY3ThgSxwf1-RuSVMHFyXP4Zx1G1xyEtjIS5J-uvzGzfO2hUnskSjDSPdhb_lFJVFsWiBIrMv3yKQLkGg1PMzaX607GaVzhZp2jt-k0DtTIkoNhTApXWtNTUi1ec0WPK_QviDUTj5KYXeGq7JtEu9JLNRUdwZp6vBxsstmuh10-arDMd3JJpQ; cookiesu=631708014049985; u=631708014049985',
    'Pragma': 'no-cache',
    'Referer': 'https://xueqiu.com/today',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    # 'elastic-apm-traceparent': '00-1d49e7c315b32504084237b43869d6bf-53e76bef781b7120-00',
    # 'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
    # 'sec-ch-ua-mobile': '?0',
    # 'sec-ch-ua-platform': '"macOS"',
}

params = {
    'since_id': '-1',
    'max_id': '-1',
    'size': '15',
}



# response = requests.get('https://xueqiu.com/statuses/hot/listV2.json', params=params, cookies=cookies, headers=headers)

# print(response.text)