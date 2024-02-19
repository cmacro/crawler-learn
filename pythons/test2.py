# 假设 data 是你的字节字符串字典
data = {
    b'\xe5\xa7\x93\xe5\x90\x8d': b'\xe5\xbc\xa0\xe4\xb8\x89', 
    b'\xe4\xbd\x8f\xe5\x9d\x80': b'\xe5\x8c\x97\xe4\xba\xac', 
    b'\xe7\x88\xb1\xe5\xa5\xbd': b'\xe8\xb6\xb3\xe7\x90\x83'}
# 转换为有效字符串
decoded_data = {key.decode('utf-8'): value.decode('utf-8') for key, value in data.items()}
# 输出转换后的用户信息
print("插入数据后的用户信息:", decoded_data)