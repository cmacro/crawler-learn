# crawler

## 爬虫基础教程

### 定位技巧

- 接口定位
  - 字体定位
  - Unicode
  - 数据加密 
- JS逆向
  - 主要的加密(解密)方法或函数 

### 初步JS

- 混淆 
- 无混淆js
  - 关键字搜索 
    - 解密搜 decrypt 加密搜 encrypt
      - 适用方法 
      - decrypt(需要被解密的内容) 
      - 对称加密算法 AES DES 
    - ajax渲染 JSON.parse 
      - JSON.parse(函数或方法(密文)) 
      - a = 函数或方法(密文) JSON.parser(a)
    - 接口自带关键字 
      - 特点：方法或函数（密文数据） 
  - XHR断点 
  - 路径断点（搜索） 
  - 跟栈 
  - hook 

### JS逆向

- 数据加密 
- 请求头加密 
  - 获取生成的方法 
  - 服务器也不知道具体是什么东西？ 
  - 原文内容 
    - 被加密之前的数据 
  - 爬虫 模仿服务器的加密方法 
- 表单加密 
  - 生成规则：模拟生成规则 在被加密前是什么数据 
  - 
- 参数加密 
- cookie加密 

## 技巧分析

- 爬虫的认知 
- 加密定位技巧解析 
  - 请求堆栈分析
    - 正常栈 
      - 红人点集逆向登陆
      - 烯牛请求sig 
    - 回掉异步栈 
      - 点点数据 
  - 关键字搜索
    - 唯一艺术 sig.data 
    - 

## JS逆向基础

- 标准算法 
  - 对称加密算法 
    - AES 
      - 查表法 白盒AES
      - 128密钥 4 10 
      - 192 6 12 
      - 256 8 14 
    - key iv 加密模式 填充方式pad 
    - 巨潮 https://webapi.cninfo.com.cn/#/marketDataDate 
    - 服务器返回密文数据  
    - 采招网 https://search.bidcenter.com.cn/search?keywords=%E9%87%87%E8%B4%AD%E8%B6%85%E5%A3%B0%E6%B3%A2%E5%88%80&mod=0&page=2 
  - 非对称加密算法 
  - 消息摘要算法 
- 魔改算法 
- 混淆技术 
- AST 

## 涉及的内容

- 对称加密算法(DES AES) 
- 非对称加密算法 
- 消息摘要算法 
  - MD5 
- 数字签名算法 

## python包 

- requests 
- execjs pyexecjs2
