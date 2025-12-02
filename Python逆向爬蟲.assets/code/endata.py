import requests
import execjs

headers = {
    'Accept': 'text/plain, */*; q=0.01',
    'Accept-Language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7,ja;q=0.6',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Origin': 'https://www.endata.com.cn',
    'Pragma': 'no-cache',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '"Chromium";v="142", "Google Chrome";v="142", "Not_A Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
}

data = {
    'pageIndex': '2',
    'pageSize': '12',
    'SceneID': '2',
    'TagID': '',
    'MethodName': 'Data_ReportListNew',
}

response = requests.post('https://www.endata.com.cn/API/GetData.ashx', headers=headers, data=data)

with open("endata.js", 'r', encoding='utf-8') as f:
    js_code = f.read()
ctx = execjs.compile(js_code)
result = ctx.call('decrypt_data', response.text)
print(result)