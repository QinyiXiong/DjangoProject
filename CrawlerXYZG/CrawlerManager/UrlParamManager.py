import time


class UrlParamManager(object):
    def __init__(self):
        self.UrlParam_type = "type"
        self.UrlParam_page = "page"
        self.UrlParam_PageNum = "pageNum"
        self.UrlParam_creditType = "creditType"
        self.UrlParam_encryStr = "encryStr"
        self.UrlParam_objectType = "objectType"
        self.UrlParam_dataSource = "dataSource"
        self.UrlParam_pageSize = "pageSize"
        self.UrlParam_keyword = "keyword"
        self.UrlParam__ = "_"  # 时间戳
        self.UrlParam_name = "name"
        self.UrlParam_searchState = "searchState"
        self.UrlParam_entityType = "entityType"
        self.UrlParam_total = "total"
        self.UrlParam_totalSize = "totalSize"
        self.UrlParam_scenes = "scenes"
        self.UrlParam_source = "source"

        self.timestamp = lambda: int(round(time.time() * 1000))

    def getParam_type(self):
        return self.UrlParam_type

    def getParam_page(self):
        return self.UrlParam_page

    def getXYZGParam1(self):
        param = {
            self.UrlParam_page: 1,
            self.UrlParam_creditType: 8,
            self.UrlParam_keyword: "",
            self.UrlParam_objectType: 2,
            self.UrlParam_pageSize: 10,
            self.UrlParam__: self.timestamp()
        }
        return param

    def getXYZGParam2(self):
        param = {
            self.UrlParam_dataSource: 0,
            self.UrlParam_encryStr: "",
            self.UrlParam_pageSize: 10,
            self.UrlParam_PageNum: 1
        }
        return param

    def getXYZGParam3(self):
        param = {
            self.UrlParam_name: "",
            self.UrlParam_page: 1,
            self.UrlParam_pageSize: 10
        }
        return param

    def getXYZGParam4(self):
        param = {
            self.UrlParam_keyword: "",
            self.UrlParam_searchState: 2,
            self.UrlParam_page: 1,
            self.UrlParam_pageSize: 10,
            self.UrlParam_type: "",
            self.UrlParam_entityType: "1,4,5,6,7,8"
        }
        return param

    def getXYZGParam5(self):
        param = {
            self.UrlParam_keyword: "",
            self.UrlParam_scenes: "defaultscenario",
            self.UrlParam_entityType: "",
            self.UrlParam_searchState: 1
        }
        return param

    # source:
    # type: 重点关注
    # searchState: 1
    # entityType: 1
    # scenes: defaultscenario
    # keyword: 山东地矿股份有限公司
    # page: 1
    # pageSize: 10
    def getXYZGParam6(self):
        param = {
            self.UrlParam_source: "",
            self.UrlParam_type: "",
            self.UrlParam_searchState: 1,
            self.UrlParam_entityType: "",
            self.UrlParam_scenes: "defaultscenario",
            self.UrlParam_keyword: "",
            self.UrlParam_page: 1,
            self.UrlParam_pageSize: 10
        }
        return param

