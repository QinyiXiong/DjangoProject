import time

import requests
import json


class HtmlDownloader(object):

    def setHeaders(self, url):
        if url is None:
            return None

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36',
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Content-Type': 'application/json',
            'Referer': url
        }
        return headers

    def downloadHtml(self, url, param):
        if url is None:
            return None
        r = requests.get(url, params=param, headers=self.setHeaders(url))
        if r.status_code == 200:
            r.encoding = 'utf-8'
            return r.text
        elif r.status_code == 403:
            return r.status_code
        else:
            return None

    def downloadHtmlwithParam(self, url, jsondata):
        # param = {
        #     "type": "black"
        # }
        if url is None:
            return None

        r = requests.post(url, data=jsondata, headers=self.setHeaders(url))

        return r.text

    def is_json(self, myjson):
        try:
            json_object = json.loads(myjson, encoding='utf-8')
        except ValueError:
            return False
        return True

    def downloadJson(self, url, param, Referer):
        if url is None:
            return None
        time.sleep(1)
        jsonStr = ''
        r = requests.get(url, params=param, headers=self.setHeaders(Referer))
        if r.status_code == 200:
            r.encoding = 'utf-8'
            jsonStr = r.text
            if self.is_json(jsonStr):
                return jsonStr
            else:
                print("not jsonStr:", jsonStr)
                jsonStr = self.downloadJson(url, param, Referer)
                return jsonStr
        else:
            if r.status_code == 403:
                return r.status_code
            print(jsonStr, "状态码：", r.status_code)
            jsonStr = self.downloadJson(url, param, Referer)
            return jsonStr