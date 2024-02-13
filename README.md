# crawler-learn


level | name | note  
:--:|----|---  
1 | XHR debug | [乌海市公共资源交易中心/政策法规 whggzy.xhr](whggzy.xhr/readme.md) 
2 | 标准加密 AES decrypy | [万宏源证券 swhysc.com](swhysc.com/readme.md)   
2 | 数据关键字 非标加密 decrypy 扣取解密代码 | [企名片 qimingpian.com](qimingpian.com/readme.md)
2 | 没解密或数据关键字，尝试JSON.parse 定位代码 | [烯牛数据 xiniudata.com](xiniudata.com/readme.md)

## Q&A

**Q：** Python requests库处理SSL错误的方法


忽略证书警告信息，并在请求是增加 verify=False方法不验证证书


```python
import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

requests.get('https://translate.google.com', verify=False)
```

