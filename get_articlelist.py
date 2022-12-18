import requests
import json
import urllib3


def single_page(headers, searchword, url, page):
    data = {
        "newsearch": 'true',
        "queryText": searchword,
        "pageNumber": str(page),
    }
    res = requests.post(url=url, data=json.dumps(data), headers=headers, verify=False)
    dic_obj = res.json()
    return dic_obj


def airtcle_list(searchword):
    headers = {
        'Accept': 'application/json,text/plain,*/*',
        'Accept-Encoding': 'gzip,deflate,br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Connection': 'keep-alive',
        'Content-Length': '147',
        'Content-Type': 'application/json',
        'Referer': 'https://ieeexplore.ieee.org/search/searchresult.jsp?newsearch=true',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 '
                      'Safari/537.36 Edg/108.0.1462.46',
    }
    url = 'https://ieeexplore.ieee.org/rest/search'
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    dic_obj = single_page(headers, searchword, url, 1)
    totalpage = int(dic_obj["totalPages"])
    totalrecords = int(dic_obj["totalRecords"])
    print('搜索关键词:' + searchword)
    print('共检索到' + str(totalrecords) + '篇文章')
    result_list = []    # 存储文章序号
    for i in range(1, totalpage + 1):
        dic_obj = single_page(headers, searchword, url, i)
        for dic_obj in dic_obj["records"]:
            result_list.append(dic_obj["articleNumber"])

    return result_list
