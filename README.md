# crawler-learn


level | name | note  
:--:|----|---  
1 | XHR debug | [乌海市公共资源交易中心/政策法规 whggzy.xhr](whggzy.xhr/readme.md) 
2 | 标准加密 AES decrypy,查找`decrypy(`关键字定位 | [万宏源证券 swhysc.com](swhysc.com/readme.md)   
2 | 非标加密 返回内部json数据关键字比较特殊，直接使用查找定位 | [企名片 qimingpian.com](qimingpian.com/readme.md)
2 | 没解密或数据关键字，尝试`JSON.parse` 定位代码 | [烯牛数据 xiniudata.com](xiniudata.com/readme.md)
2 | 头部参数加密，查找`headers`或`api path`进行定位 ｜ [DKLink oklink.com](https://www.oklink.com/cn/btc/tx-list)


## Q&A

**Q：** Python requests库处理SSL错误的方法


忽略证书警告信息，并在请求是增加 verify=False方法不验证证书


```python
import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

requests.get('https://translate.google.com', verify=False)
```

