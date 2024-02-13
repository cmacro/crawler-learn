# -*- coding: utf-8 -*-

# Code Runner: Run in current directory

import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# requests.packages.urllib3.disable_warnings()

cookies = {
    # '_ga': 'GA1.3.1337939758.1696224876',
    # '__Secure-ENID': '16.SE=TyjltHXFk_5F5GGxkqs8WJjntRAjLmR49OAEhWXOY4603xBypCV5m-2AJlPhQJeJuaLgcUGD4CFP1d__1k26Lv-8dQzsLGjLE-VCPNyFVQXHrA0FGxbJDnGaczwd6SpGRUeT2QST8gmi23UjrppknkzK0oZVSOxKez3fJaSti-mYleVpdQ',
    # 'SID': 'fQjl68KW1ZvaAnGd9qHUPwU0hVHIttdMPkhpwgIElb5VbPeWjBiTiBUyTDeBqXI549QTNQ.',
    # '__Secure-1PSID': 'fQjl68KW1ZvaAnGd9qHUPwU0hVHIttdMPkhpwgIElb5VbPeW0T9lX6Vi7Zz43sxcw8Y4pg.',
    # '__Secure-3PSID': 'fQjl68KW1ZvaAnGd9qHUPwU0hVHIttdMPkhpwgIElb5VbPeWRznaD9W3HPbfQrEtWfHDOA.',
    # 'HSID': 'AcW5p8XYgMV_dsRcT',
    # 'SSID': 'A43xyuGa97brOZwUD',
    # 'APISID': 'OSMnIemd21QU9kcF/AWHubHTtMVcQpnMB1',
    # 'SAPISID': 'fMJt-UHAhe7boPcD/AHsBVB6nY2ApwCG0j',
    # '__Secure-1PAPISID': 'fMJt-UHAhe7boPcD/AHsBVB6nY2ApwCG0j',
    # '__Secure-3PAPISID': 'fMJt-UHAhe7boPcD/AHsBVB6nY2ApwCG0j',
    # 'AEC': 'Ae3NU9O4_eu7q-k7UhZFt9Gfjfr9aJZzFqyrBGfkWlbq4GQCi5bY1JCtTQ',
    # 'OTZ': '7420441_24_24__24_',
    # '1P_JAR': '2024-02-10-12',
    # 'NID': '511=vZVVH60pzDbZ3z_On2jar7TlOJM4SBDtC4BlU97c_vXn_fueq3K8k7e41sac6317CxwLUattyuAI9-HTfGR9Z9GO5D3eeGQ8jcTL8SKSje6eC39rrivvnoykZPkykwaTQyJOwdzr7mAWqmvg7TuyY0YWTuG0D_3zAbGf9dpQHiVPneybX1a-APmIFDpgMAhXF3tgqSKExviIu08f1YLcG8u0t8LL6CIGb7S2Io7DCt4oETp9KN1c1c31HmDbDYscYeG0KJb4cJxt2u9VuWjLicuSWUKHMavJsro2cPrjFOYgylvxMLU_BKd_1uy_DKBf70f7GZk0079FNDbP0Ajen3ESKIu_oUfuwAJfRXYpaRiYfNrppisX9O_yEcx1Nf43HsMaITFEjdPD8KD3H_q30FEm5MBLAip6w_x32INk7ExKjrAfwfbZEm3A4VhP9rAg9pnTEf6ToisdZI3PAgaQ9-yUkH2z_FTlYZGp3iquyylKAxLxok7CsbTD2c8K4f2XArOw-9sUVFyP5Rf4r4Fbc3uKtSMwYzkd0dmMOt2WF9-wurRcfJcWMNXHFyAwUaO9dltS6-mI9nzJ7rP4qwqV5r9QNtNH36MpFj9PTr9T68ksRMmNYbTQd7-sB_n_k3dhVCnvb6JEoDxMLJpWjV5l_jsu29kMmbcZU-h241v9_KuXS2TmiVp4vDY3fjE2Gy38',
    # '__Secure-1PSIDTS': 'sidts-CjIBPVxjSlrOUHfzhfIWXb_FG4B-ovOCtLHs8tAxxGVjfryV2KMz8UAwd5nzDksQOFxQlhAA',
    # '__Secure-3PSIDTS': 'sidts-CjIBPVxjSlrOUHfzhfIWXb_FG4B-ovOCtLHs8tAxxGVjfryV2KMz8UAwd5nzDksQOFxQlhAA',
    # 'SIDCC': 'ABTWhQFoVIbG-0DsewdsDed5CveQHjE86jS3Jk-_LXex3pcNwwSfFcvq-N_sAJZbzJe_bFfYASQ',
    # '__Secure-1PSIDCC': 'ABTWhQEDL-WeHSmmNxXO-shA7kQHgLIXZDxBf0FlYVNu7X5hebv-kLpSvHIZanVHQpc1l070dxl8',
    # '__Secure-3PSIDCC': 'ABTWhQGl85FpAOBQcR6UUhN5mfYkjmK0lfm4eyj8X6ALoterpScCEsL9tzeILDKTg3jPwhDYoXs',
}

headers = {
    'authority': 'translate.google.com',
    'accept': '*/*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
    # 'cookie': '_ga=GA1.3.1337939758.1696224876; __Secure-ENID=16.SE=TyjltHXFk_5F5GGxkqs8WJjntRAjLmR49OAEhWXOY4603xBypCV5m-2AJlPhQJeJuaLgcUGD4CFP1d__1k26Lv-8dQzsLGjLE-VCPNyFVQXHrA0FGxbJDnGaczwd6SpGRUeT2QST8gmi23UjrppknkzK0oZVSOxKez3fJaSti-mYleVpdQ; SID=fQjl68KW1ZvaAnGd9qHUPwU0hVHIttdMPkhpwgIElb5VbPeWjBiTiBUyTDeBqXI549QTNQ.; __Secure-1PSID=fQjl68KW1ZvaAnGd9qHUPwU0hVHIttdMPkhpwgIElb5VbPeW0T9lX6Vi7Zz43sxcw8Y4pg.; __Secure-3PSID=fQjl68KW1ZvaAnGd9qHUPwU0hVHIttdMPkhpwgIElb5VbPeWRznaD9W3HPbfQrEtWfHDOA.; HSID=AcW5p8XYgMV_dsRcT; SSID=A43xyuGa97brOZwUD; APISID=OSMnIemd21QU9kcF/AWHubHTtMVcQpnMB1; SAPISID=fMJt-UHAhe7boPcD/AHsBVB6nY2ApwCG0j; __Secure-1PAPISID=fMJt-UHAhe7boPcD/AHsBVB6nY2ApwCG0j; __Secure-3PAPISID=fMJt-UHAhe7boPcD/AHsBVB6nY2ApwCG0j; AEC=Ae3NU9O4_eu7q-k7UhZFt9Gfjfr9aJZzFqyrBGfkWlbq4GQCi5bY1JCtTQ; OTZ=7420441_24_24__24_; 1P_JAR=2024-02-10-12; NID=511=vZVVH60pzDbZ3z_On2jar7TlOJM4SBDtC4BlU97c_vXn_fueq3K8k7e41sac6317CxwLUattyuAI9-HTfGR9Z9GO5D3eeGQ8jcTL8SKSje6eC39rrivvnoykZPkykwaTQyJOwdzr7mAWqmvg7TuyY0YWTuG0D_3zAbGf9dpQHiVPneybX1a-APmIFDpgMAhXF3tgqSKExviIu08f1YLcG8u0t8LL6CIGb7S2Io7DCt4oETp9KN1c1c31HmDbDYscYeG0KJb4cJxt2u9VuWjLicuSWUKHMavJsro2cPrjFOYgylvxMLU_BKd_1uy_DKBf70f7GZk0079FNDbP0Ajen3ESKIu_oUfuwAJfRXYpaRiYfNrppisX9O_yEcx1Nf43HsMaITFEjdPD8KD3H_q30FEm5MBLAip6w_x32INk7ExKjrAfwfbZEm3A4VhP9rAg9pnTEf6ToisdZI3PAgaQ9-yUkH2z_FTlYZGp3iquyylKAxLxok7CsbTD2c8K4f2XArOw-9sUVFyP5Rf4r4Fbc3uKtSMwYzkd0dmMOt2WF9-wurRcfJcWMNXHFyAwUaO9dltS6-mI9nzJ7rP4qwqV5r9QNtNH36MpFj9PTr9T68ksRMmNYbTQd7-sB_n_k3dhVCnvb6JEoDxMLJpWjV5l_jsu29kMmbcZU-h241v9_KuXS2TmiVp4vDY3fjE2Gy38; __Secure-1PSIDTS=sidts-CjIBPVxjSlrOUHfzhfIWXb_FG4B-ovOCtLHs8tAxxGVjfryV2KMz8UAwd5nzDksQOFxQlhAA; __Secure-3PSIDTS=sidts-CjIBPVxjSlrOUHfzhfIWXb_FG4B-ovOCtLHs8tAxxGVjfryV2KMz8UAwd5nzDksQOFxQlhAA; SIDCC=ABTWhQFoVIbG-0DsewdsDed5CveQHjE86jS3Jk-_LXex3pcNwwSfFcvq-N_sAJZbzJe_bFfYASQ; __Secure-1PSIDCC=ABTWhQEDL-WeHSmmNxXO-shA7kQHgLIXZDxBf0FlYVNu7X5hebv-kLpSvHIZanVHQpc1l070dxl8; __Secure-3PSIDCC=ABTWhQGl85FpAOBQcR6UUhN5mfYkjmK0lfm4eyj8X6ALoterpScCEsL9tzeILDKTg3jPwhDYoXs',
    'origin': 'https://translate.google.com',
    'pragma': 'no-cache',
    'referer': 'https://translate.google.com/',
    # 'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
    # 'sec-ch-ua-arch': '"x86"',
    # 'sec-ch-ua-bitness': '"64"',
    # 'sec-ch-ua-full-version': '"121.0.6167.160"',
    # 'sec-ch-ua-full-version-list': '"Not A(Brand";v="99.0.0.0", "Google Chrome";v="121.0.6167.160", "Chromium";v="121.0.6167.160"',
    # 'sec-ch-ua-mobile': '?0',
    # 'sec-ch-ua-model': '""',
    # 'sec-ch-ua-platform': '"macOS"',
    # 'sec-ch-ua-platform-version': '"14.0.0"',
    # 'sec-ch-ua-wow64': '?0',
    # 'sec-fetch-dest': 'empty',
    # 'sec-fetch-mode': 'cors',
    # 'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
    # 'x-client-data': 'CI+2yQEIpLbJAQipncoBCJKLywEIlKHLAQj8qswBCOmYzQEIhqDNAQje680BCKjuzQEIg/DNAQjW8c0BCIHyzQEInvbNAQi5980BGKfqzQEYyvjNAQ==',
    # 'x-goog-batchexecute-bgr': '[";0824zZXQAAYXgN6QN4BfYeu456KGNkMmADQBEArZ1CqDPEb7czWA8ziqOmb66RT61MU04S3o23byg7F9xGrVM_Y4HQWM_3ZW4xaA38aSHwAAAC5PAAAAAnUBB4QDSajq9UQX8i-8NOCjfdOkA4YhigD7zgdeSx_mweL7CpPSn-QL160Rqraog2vAoWUUFvUvfAhv8m2Qkczz2LJtoqe0CyDIrZXsdO_OBflO5o_gdzuDjn2e-pqTUg6Ne1TxRSWHSemgbxN0wWiHD5zaNGFD_0ppgR1rg--lITIIQ3eDYwqxCk9xi2HR1nN_9-ad230Y9D11gqa6QdpQMVAa3d7oSE8MhU0DLaR9mvhgLPbZqhGoKWWoaf7Ztk7R7jA2alobPdSShEoKW8QGmcfY0U0lp9BbJol7IpBGnPdxaB3jAL3DU4ePJGOldMRvkIEiL20z56jJI-yibB_Y5DBGQJnh0hhXbumtG7xK_q1cWQcWt3Jvhgva4Q68H8GwU_jlIa9A2VJknuEbcqiJwpEubuLBnej-dag2UgCr67l8bTwB8gAiSpIh2LaamoE92LDqRmaUwYmwR1Nj-RwTecyzhrRoTJ4ZzcqoIhZCoXbBMBT37aGkgvd7d5QVRlGZOETn5Ikx1MuR4TVxeyO1Tz8A1dGlL4TeLnhwa9eOvbYZuu0blSVcgLlf_egcxVPknAhvLByOU3Dry2yEBYH9blQXsNmgtObZirtAj0LV1BteHjRzgUtg4vOKR762iJOSHOBdH-gy4FZxnzBdLE-jw6xzdJAGjJWoPEHPfM69FMsXQU1pmDTOiMxHFoA1wHWYMZcr3v-ZCCfg8k_oX4cxDSkqrvnIl2FHKEOMdMDfZW8T2fNNpg_raU4Fq761S-pKdUWu_DpwXDNa5qZWkt-A55UTNoVNvDCZbHRTBvFt5tQlMKexdspt3dlKKl7PBqTC5v6Y0xvXv279a8JQqbKaFhs5ths93KvvCRN_ccyavPY2AIJUxDG0unDjOu5FBka9_iKVH6LqdE_M-Xav5PDPD7pyWBrSVzml0A0l8tRMiLc9dJ8bTv94Tgjl7QE58oh-UQcv9Skz2Wj9VzU36DuGR3Lxg_eHdYl4iUfCHkR90nBvWzzU0Ufytbgig-p6cBjfkVFWjjhO1vywk1R1E8yXw1GFI7KfKGtC1q3MuFrY54uNZ7tfOEIYXqFpNgSo3ysQpf8YO2SYPzqrfnDywr5ccZe3RUZCe22H0FpabdE",null,null,3,null,null,null,0,"2"]',
    # 'x-goog-ext-174067345-jspb': '[[1]]',
    # 'x-same-domain': '1',
}

params = {
    'rpcids': 'AVdN8',
    'source-path': '/',
    'f.sid': '-3763781673604600076',
    'bl': 'boq_translate-webserver_20240207.06_p0',
    'hl': 'zh-CN',
    'soc-app': '1',
    'soc-platform': '1',
    'soc-device': '1',
    '_reqid': '7270378',
    'rt': 'c',
}
# &at=AFS6QyiomdWGugr0K5xnmn3LtWo8%3A1707564777164&
data = 'f.req=%5B%5B%5B%22AVdN8%22%2C%22%5B%5C%22learn%5C%22%2C%5C%22en%5C%22%2C%5C%22zh-CN%5C%22%5D%22%2Cnull%2C%22generic%22%5D%5D%5D'

response = requests.post(
    'https://translate.google.com/_/TranslateWebserverUi/data/batchexecute',
    params=params,
    cookies=cookies,
    headers=headers,
    data=data,
    verify=False,
)

with open('./translatelearn.txt', 'w', encoding='utf-8') as f:
    f.write(response.text)

print(response.text)
print(response.status_code)