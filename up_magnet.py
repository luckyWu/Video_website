import json
import requests

#{"请求载荷（payload）":{"EDITOR_CONFIG":{"text":"magnet:?xt=urn:btih:732111d1b2f373a3eaf74e5f0d16001658ac6ef1&dn=[www.domp4.com]狼殿下.第21集.HD1080p.国语中字.mp4","mode":"text/plain"}}}
headers = {
    "Host": "47.104.165.92:8000",
    # "TE":"Trailers",
    "accept": "application/json, text/plain, */*",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "zh,en;q=0.9,zh-CN;q=0.8",
    "Connection":"keep-alive",
    # "X-Requested-With":"XMLHttpRequest",
    # "Content-Type": "application/json;charset=utf-8",
    "Referer": "http://47.104.165.92:8000/",
    "user-agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:68.0) Gecko/20100101 Firefox/68.0"
}


def up_magnet(magnet):
    data = bytes(magnet, encoding="utf-8")
    url = "http://47.104.165.92:8000/api/magnet"
    try:
        res = requests.post(url, headers=headers, data=data, verify=False)
        res.encoding = "utf-8"
        return res.status_code, res.text
    except Exception as e:
        return -1, e

def test(url):
    res = requests.get(url)
    print(res.status_code)
    print(res.text)
    # print(res.headers)


if __name__ == "__main__":
    # magnet = "magnet:?xt=urn:btih:45dcbd62c4de1fe2ad516c94f376658f4ebcb804&dn=[www.domp4.com]狼殿下.第26集.HD1080p.国语中字.mp4"
    # # magnet = 'https://www.baidu.com'
    # code, msg = up_magnet(magnet)
    # print(code, msg)
    url = "http://47.104.165.92:8000/"
    test(url)
    #print()