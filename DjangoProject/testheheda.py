from CrawlerXYZG.CrawlerManager import HtmlLoaderManager
import json

if __name__ == '__main__':
    HttpClient = HtmlLoaderManager.HtmlDownloader()
    url = "http://192.168.1.121:8000/creditChina/"
    jsdata = {"朋哥": "hehed朋哥123"}
    jsonStr = json.dumps(jsdata, ensure_ascii=False).encode("utf-8").decode("latin-1")
    res = HttpClient.downloadHtmlwithParam(url, jsonStr)
    print(res)
