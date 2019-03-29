# coding=utf-8
import requests
import ssl
import random
import json


def get_salary(page):
    USER_AGENTS = [
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
        "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
        "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
        "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
        "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5"
    ]

    user_agent = random.choice(USER_AGENTS)

    proxies = {
        "http": "http://10.10.1.10:3128",
        "https": "http://127.0.0.1:1080",
    }

    url = "https://www.lagou.com/jobs/positionAjax.json"

    querystring = {"city": "重庆", "needAddtionalResult": "false"}

    payload = "first=true&pn=" + str(page) + "&kd=%E6%B5%8B%E8%AF%95%E5%B7%A5%E7%A8%8B%E5%B8%88&undefined="
    headers = {
        'Accept': "application/json, text/javascript, */*; q=0.01",
        'Accept-Encoding': "gzip, deflate, br",
        'Accept-Language': "zh-CN,zh;q=0.9",
        'Connection': "keep-alive",
        'Content-Length': "64",
        'Content-Type': "application/x-www-form-urlencoded",
        # 'Cookie': "WEBTJ-ID=20190103115448-16811d96d4f1ff-0e9af096bc567c-b781636-2073600-16811d96d51321; _ga=GA1.2.1875377608.1546487689; _gid=GA1.2.1639064321.1546487689; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1546487689,1546487700; user_trace_token=20190103115501-5868be88-0f0b-11e9-b0e4-5254005c3644; LGUID=20190103115501-5868c346-0f0b-11e9-b0e4-5254005c3644; X_HTTP_TOKEN=160336272d2a0476774c2734ba28aa5d; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2216811d9b86921f-0e06bb6cbd7051-b781636-2073600-16811d9b86af%22%2C%22%24device_id%22%3A%2216811d9b86921f-0e06bb6cbd7051-b781636-2073600-16811d9b86af%22%7D; sajssdk_2015_cross_new_user=1; LG_LOGIN_USER_ID=85eeea5088bb645c15125c5395a4323195359f9aba6138553535d0ec0f26f68b; _putrc=6A2A9583A67EE1EF123F89F2B170EADC; JSESSIONID=ABAAABAAAGGABCB3411EABF40F0A601E533CBE524C47D6E; login=true; unick=%E4%BD%95%E7%BE%8E%E5%BB%BA; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; hasDeliver=8; gate_login_token=c2958f4761ee0c9b17b16b6aef324815fa534525051d5fcb33474148b23cdb69; index_location_city=%E5%85%A8%E5%9B%BD; LGSID=20190103140452-7c63a781-0f1d-11e9-b0e4-5254005c3644; PRE_UTM=; PRE_HOST=; PRE_SITE=https%3A%2F%2Fwww.lagou.com%2F; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Fjobs%2Flist_%25E6%25B5%258B%25E8%25AF%2595%25E5%25B7%25A5%25E7%25A8%258B%25E5%25B8%2588%3FlabelWords%3Dsug%26fromSearch%3Dtrue%26suginput%3Dceshi; _gat=1; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1546497065; LGRID=20190103143106-26338adb-0f21-11e9-b0e4-5254005c3644; SEARCH_ID=d98fe3376a334dc18d5343dc54292ff0",
        'Host': "www.lagou.com",
        'Origin': "https://www.lagou.com",
        'Referer': "https://www.lagou.com/jobs/list_%E6%B5%8B%E8%AF%95%E5%B7%A5%E7%A8%8B%E5%B8%88?city=%E9%87%8D%E5%BA%86&cl=false&fromSearch=true&labelWords=&suginput=",
        'User-Agent': user_agent,
        'X-Anit-Forge-Code': "0",
        'X-Anit-Forge-Token': "None",
        'X-Requested-With': "XMLHttpRequest",
        'cache-control': "no-cache"

    }

    # verify：忽略证书 proxies：设置代理，便于fiddler 监听
    #response = requests.post(url, data=payload, headers=headers, params=querystring, verify=False, proxies=proxies)
    response=requests.post(url,data=payload, headers=headers, params=querystring,verify =  False)

    jsons = json.loads(response.text, encoding='utf-8')

    print response.text
    pageSize = jsons['content']['pageSize']
    salarys = []
    lens = len(jsons['content']['positionResult']['result'])
    for i in range(int(lens)):
        salary = jsons['content']['positionResult']['result'][i]['salary']
        salarys.append(salary)
    return salarys


def write_data(data):
    with open('test.txt', 'a') as fp:
        fp.writelines(json.dumps(data))
        fp.writelines('\n')


if __name__ == '__main__':
    i = 0
    while (True):
        salarys = get_salary(i)
        if salarys == []:
            break
        else:
            print salarys
            for salary in salarys:
                write_data(salary)
        i += 1
