
class UrlManager(object):

    def __init__(self):
        self.urls1 = set()  # 第一层请求地址
        self.urls2 = set()  # 第二层请求地址
        self.urls3 = set()  # 第三层请求地址

        self.urlsDict = dict()  # 地址字典

    def addUrlsDict(self, key, value):
        self.urlsDict[key] = value

    def hasUrls1(self):
        return self.urls1Size() != 0

    def hasUrls2(self):
        return self.urls2Size() != 0

    def hasUrls3(self):
        return self.urls3Size() != 0

    def getUrls1(self):
        new_url = self.urls1.pop()
        return new_url

    def getUrls2(self):
        new_url = self.urls2.pop()
        return new_url

    def getUrls3(self):
        new_url = self.urls3.pop()
        return new_url

    def addUrl1(self, url):
        if url is None:
            return
        if url not in self.urls1:
            self.urls1.add(url)

    def addUrl2(self, url):
        if url is None:
            return
        if url not in self.urls2:
            self.urls2.add(url)

    def addUrl3(self, url):
        if url is None:
            return
        if url not in self.urls3:
            self.urls3.add(url)

    def addUrls1(self, urls):
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.addUrl1(url)

    def addUrls2(self, urls):
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.addUrl2(url)

    def addUrls3(self, urls):
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.addUrl3(url)

    def urls1Size(self):
        return len(self.urls1)

    def urls2Size(self):
        return len(self.urls2)

    def urls3Size(self):
        return len(self.urls3)
