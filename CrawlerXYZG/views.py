from django.shortcuts import render
import time
import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from CrawlerXYZG.CreditChinaCrawlerZG import CreditChinaService2

# Create your views here.


def hello(request):
    print(request)
    print("heheda")
    return HttpResponse("Hello world ! ")

@csrf_exempt
def getCreditChinaData(request):
    jsonstr = request.body.decode("utf-8")
    print(jsonstr)
    data = json.loads(jsonstr)
    timeParam = data.get("time")   # 0,1
    companyParam = data.get("company")  # 集合
    typeParam = data.get("type")

    spiderman = CreditChinaService2.creditchina()
    allData = []
    param = spiderman.selfParam.getXYZGParam4()
    for company in companyParam:
        param.update({spiderman.selfParam.UrlParam_keyword: company, spiderman.selfParam.UrlParam_type: typeParam})
        if timeParam == "0":
            allData.append(spiderman.getfirstData(param))
        else:
            allData.append(spiderman.getdetaildata(param))
    rspdata = json.dumps(allData, ensure_ascii=False).encode("utf-8").decode("utf-8")
    print(rspdata)
    return HttpResponse(rspdata)
