from CrawlerXYZG.CrawlerManager import HtmlLoaderManager
from CrawlerXYZG.CrawlerManager import UrlParamManager

import json
import uuid


class creditchina(object):
    def __init__(self):
        self.url1 = "https://public.creditchina.gov.cn/private-api/typeNameAndCountSearch"   # 第一层
        # 第二层 行政许可/行政处罚/守信激励/失信惩戒/重点关注/(资质/资格)/风险提示/其他
        self.url2 = "https://public.creditchina.gov.cn/private-api/typeSourceSearch"
        self.url3 = "https://public.creditchina.gov.cn/private-api/getTyshxydmDetailsContent"  # 第二层detail
        self.Referer1 = "https://www.creditchina.gov.cn/xinyongfuwu/"  # 黑名单Referer

        self.HttpClient = HtmlLoaderManager.HtmlDownloader()
        self.selfParam = UrlParamManager.UrlParamManager()
        self.zqlist = ["行政许可", "行政处罚", "守信激励", "失信惩戒", "重点关注", "资质", "风险提示", "其他", "资格"]
        self.F_FROM = "信用中国"

    #  获取第二层详细数据总页数
    def getTotalPageCount2(self, param):
        totalPageCount = 1
        jsonStr = self.HttpClient.downloadJson(self.url2, param, self.Referer1)
        data = json.loads(jsonStr).get("data")
        totalPageCount = data.get("totalSize")
        if totalPageCount == None:
            totalPageCount = 0
        print("第二层名单类totalPageCount:", totalPageCount)
        return totalPageCount

    #  获取第一层数据总页数
    def getTotalPageCount1(self, param):
        totalPageCount = 1
        jsonStr = self.HttpClient.downloadJson(self.url1, param, self.Referer1)
        data = json.loads(jsonStr).get("data")
        totalPageCount = data.get("totalSize")
        print("第一层totalPageCount:", totalPageCount)
        return totalPageCount

    def getJCXX(self, param):
        jsonStr = self.HttpClient.downloadJson(self.url3, param, self.Referer1)
        data = json.loads(jsonStr).get("data")
        datalist = []
        datalist.append(data)
        return datalist
        # print(data, type(data))

    def getSecondData(self, param, pageCount):
        mdlist = []
        for i in range(1, pageCount + 1):
            param.update({self.selfParam.UrlParam_page: i})
            jsonStr = self.HttpClient.downloadJson(self.url2, param, self.Referer1)
            datalist = json.loads(jsonStr).get("data").get("list")
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
            results = data.get("list")
            totalPageCount = data.get("totalSize")
            for res in results:
                F_GUID = str(uuid.uuid4()).replace("-", "")
                res.update({"F_GUID": F_GUID, "F_FROM": self.F_FROM})
                reslist.append(res)
            if totalPageCount == i:
                break
        # print(reslist)
        # self.getdetaildata(reslist)
        return reslist

    def getdetaildata(self, param):
        results = self.getfirstData(param)
        data = {}
        data.update({"第一层": results})
        for res in results:
            # print(res, type(res))
            name = res.get("name")
            F_GUID = res.get("F_GUID")
            detaildata = {}
            detaildata.update({"F_GUID": F_GUID})
            # data.update({name: detaildata, "F_FROM": self.F_FROM})
            # idCardOrOrgCode = res.get("idCardOrOrgCode")
            encryStr = res.get("entity_type")
            param2 = self.selfParam.getXYZGParam5()
            param2.update({self.selfParam.UrlParam_entityType: encryStr, self.selfParam.UrlParam_keyword: name})

            jcxxlist = self.getJCXX(param2)
            detaildata.update({"基础信息": jcxxlist})

            param3 = self.selfParam.getXYZGParam6()
            for tyStr in self.zqlist:
                param3.update({self.selfParam.UrlParam_keyword: name, self.selfParam.UrlParam_entityType: encryStr, self.selfParam.UrlParam_type: tyStr})
                pqdatalist = self.getSecondData(param3, self.getTotalPageCount2(param3))
                detaildata.update({tyStr: pqdatalist})
            data.update({name: detaildata, "F_FROM": self.F_FROM})
        return data


if __name__ == '__main__':
    spiderman = creditchina()
    param = spiderman.selfParam.getXYZGParam4()
    param.update({spiderman.selfParam.UrlParam_keyword: "中融汇银", spiderman.selfParam.UrlParam_type: "失信惩戒"})
    # getdetaildata
    # data = spiderman.getfirstData(param)
    data = spiderman.getdetaildata(param)
    hehe = json.dumps(data, ensure_ascii=False)
    print(hehe, type(hehe))
    # print(spiderman.getTotalPageCount1(param))
