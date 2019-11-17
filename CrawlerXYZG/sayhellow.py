import socket
import json
from CrawlerXYZG.CrawlerManager import HtmlLoaderManager


def sayHellowToPen():
    print("123")
    myIP = get_host_ip()
    myUrl = "http://"+myIP+":8000/creditChina/"
    print(myUrl)
    reqParam = {"ip": myUrl}
    requrl = "http://192.168.2.27:8080/sxcx/search"
    htmlClient = HtmlLoaderManager.HtmlDownloader()
    requestRes = htmlClient.downloadHtml(requrl, reqParam)
    print(requestRes)





def get_host_ip():
    """
    查询本机ip地址
    :return:
    """
    global s
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()
    return ip


# sayHellowToPen()