import gevent.pool
import json

from geventhttpclient import HTTPClient
from geventhttpclient.url import URL

Token = '<go to http://www.baidu.com and copy the access token>'

url = URL('http://www.baidu.com')
url['access_token'] = Token

http = HTTPClient.from_url(url, concurrency=10)

response = http.get(url.request_uri)

assert response.status_code == 200

data = json.loads(response)['data']


def print_friend_username(http, friend_id):
    friend_url = URL('/' + str(friend_id))
    friend_url['access_token'] = Token


    # 在链接之前，线程会处于阻塞状态
    response = http.get(friend_url.request_uri)
    assert response.status_code == 200

    friend = json.load(response)

    # 判断是否存在username
    if friend.has_key('username'):
        print(f"{friend_url['username']} :{friend['name']}")

    else:
        print(f"{friend['name']}")

    # 设置一次运行20个线程
    pool = gevent.pool.Pool(20)

    # 循环读取
    for item in data:
        friend_id = item['id']
        pool.spawn(print_friend_username, http, friend_id)

    pool.json()
    # 关闭
    http.close()



