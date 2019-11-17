from CrawlerXYZG.CrawlerManager import HtmlLoaderManager
from CrawlerXYZG.CrawlerManager import UrlParamManager
from CrawlerXYZG.CrawlerManager import UrlManager
import json
import time
import uuid


class creditchina(object):
    def __init__(self):
        self.url1 = "https://www.creditchina.gov.cn/api/credit_info_search"   # 第一层
        self.url2 = "https://www.creditchina.gov.cn/api/record_param"  # 第二层 黑名单，红名单，重点关注名单
        self.url3 = "https://www.creditchina.gov.cn/api/credit_info_detail"  # 第二层detail
        self.url4 = "https://www.creditchina.gov.cn/api/pub_permissions_name"   # 第二层行政许可
        self.url5 = "https://www.creditchina.gov.cn/api/pub_penalty_name"  # 行政处罚
        self.Referer1 = "https://www.creditchina.gov.cn/xinyongfuwu/"  # 黑名单Referer

        self.HttpClient = HtmlLoaderManager.HtmlDownloader()
        self.selfParam = UrlParamManager.UrlParamManager()
        self.F_FROM = "信用中国"
        self.creditTypeList = ["2", "4", "8"]

    #  获取第二层行政许可（行政处罚）数据总页数
    def getTotalPageCount3(self, param, url):
        totalPageCount = 1
        jsonStr = self.HttpClient.downloadJson(url, param, self.Referer1)
        data = json.loads(jsonStr).get("result")
        totalPageCount = data.get("totalPageCount")
        print("第二层行政许可类totalPageCount:", totalPageCount)
        return totalPageCount

    #  获取第二层名单类（黑名单，红名单，重点关注名单）数据总页数
    def getTotalPageCount2(self, param):
        totalPageCount = 1
        jsonStr = self.HttpClient.downloadJson(self.url2, param, self.Referer1)
        totalPageCount = json.loads(jsonStr).get("totalPageCount")
        print("第二层名单类totalPageCount:", totalPageCount)
        return totalPageCount

    #  获取第一层数据总页数
    def getTotalPageCount1(self, param):
        totalPageCount = 1
        jsonStr = self.HttpClient.downloadJson(self.url1, param, self.Referer1)
        data = json.loads(jsonStr).get("data")
        totalPageCount = data.get("totalPageCount")
        print("第一层totalPageCount:", totalPageCount)
        return totalPageCount

    def getJCXX(self, param):
        jsonStr = self.HttpClient.downloadJson(self.url3, param, self.Referer1)
        data = json.loads(jsonStr).get("result")
        datalist = []
        datalist.append(data)
        return datalist
        # print(data, type(data))

    def getXZXX(self, param, pageCount, url):
        xzxklist = []
        for i in range(1, pageCount + 1):
            param.update({self.selfParam.UrlParam_page: i})
            jsonStr = self.HttpClient.downloadJson(url, param, self.Referer1)
            results = json.loads(jsonStr).get("result").get("results")
            xzxklist.append(results)
            # print(results, type(results))
        return xzxklist

    def getMD(self, param, pageCount):
        mdlist = []
        for i in range(1, pageCount + 1):
            param.update({self.selfParam.UrlParam_PageNum: i})
            jsonStr = self.HttpClient.downloadJson(self.url2, param, self.Referer1)
            datalist = json.loads(jsonStr).get("result")
            print(datalist, type(datalist))
            mdlist.append(datalist)
        return mdlist


    # 获取第一层数据
    def getfirstData(self, param):
        reslist = []
        for i in range(1, 6):
            param.update({self.selfParam.UrlParam_page: i})
            jsonStr = self.HttpClient.downloadJson(self.url1, param, self.Referer1)
            data = json.loads(jsonStr).get("data")
            results = data.get("results")
            totalPageCount = data.get("totalPageCount")
            for res in results:
                F_GUID = str(uuid.uuid4()).replace("-", "")
                res.update({"F_GUID": F_GUID})
                reslist.append(res)
            if totalPageCount == i:
                break
        # print(reslist)
        # self.getdetaildata(reslist)
        return reslist

    def getdetaildata(self, param):
        results = self.getfirstData(param)
        data = {}
        for res in results:
            # print(res, type(res))
            name = res.get("name")
            F_GUID = res.get("F_GUID")
            detaildata = {}
            detaildata.update({"F_GUID": F_GUID})
            # data.update({name: detaildata, "F_FROM": self.F_FROM})
            # idCardOrOrgCode = res.get("idCardOrOrgCode")
            encryStr = res.get("encryStr")
            param2 = self.selfParam.getXYZGParam2()
            param2.update({self.selfParam.UrlParam_encryStr: encryStr})

            jcxxlist = self.getJCXX(param2)
            detaildata.update({"0": jcxxlist})

            param3 = self.selfParam.getXYZGParam3()
            param3.update({self.selfParam.UrlParam_name: name})

            xzxklist = self.getXZXX(param3, self.getTotalPageCount3(param3, self.url4), self.url4)
            detaildata.update({"1": xzxklist})

            xzcflist = self.getXZXX(param3, self.getTotalPageCount3(param3, self.url5), self.url5)
            detaildata.update({"3": xzcflist})

            for creditType in self.creditTypeList:
                param2.update({self.selfParam.UrlParam_creditType: creditType})
                mdlist = self.getMD(param2, self.getTotalPageCount2(param2))
                detaildata.update({creditType: mdlist})
            data.update({name: detaildata, "F_FROM": self.F_FROM})
        return data


if __name__ == '__main__':
    spiderman = creditchina()
    timestamp = lambda: int(round(time.time() * 1000))
    param = {
        spiderman.selfParam.UrlParam_page: 1,
        spiderman.selfParam.UrlParam_creditType: 8,
        spiderman.selfParam.UrlParam_keyword: "上海普联",
        spiderman.selfParam.UrlParam_objectType: 2,
        spiderman.selfParam.UrlParam_pageSize: 10,
        spiderman.selfParam.UrlParam__: timestamp(),
    }
    data = spiderman.getfirstData(param)
    hehe = json.dumps(data, ensure_ascii=False)
    print(hehe, type(hehe))
    # print(spiderman.getTotalPageCount1(param))
