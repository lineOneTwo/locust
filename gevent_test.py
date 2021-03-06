from geventhttpclient import HTTPClient
from geventhttpclient.url import URL

url = URL('http://www.baidu.com')

http = HTTPClient(url.host)

# 获取一个请求
response = http.get(url.request_uri)

# 读取状态码
print(response.status_code)

# 读取返回内容
body = response.read()

# 关闭链接
http.close()
