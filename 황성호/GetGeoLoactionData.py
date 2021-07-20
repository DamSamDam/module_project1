import urllib.request
import json

def get_request_url(url):
    pass

def GetGeoLoactionData(addr):
    baseUrl = "https://naveropenapi.apigw.ntruss.com/map-geocode/v2/geocode"
    paraData = "?query=%s" % urllib.parse.quote(addr)
    resultUrl = baseUrl + paraData

    resultData = get_request_url(resultUrl)

    tempData = []

    if(resultData == None): # 결과가 있는지 없는지 확인
        return "Data가 없습니다."
    else:
        tempData = json.loads(resultData) # 데이터를 정형으로 변경함 
    
    if 'addresses' in tempData.keys():
        xdata = tempData['addresses'][0]['x']
        ydata = tempData['addresses'][0]['y']

    return xdata,ydata


def Main():
    addr = ""
    xdata,ydata = GetGeoLoactionData(addr)
    
   
if __name__ == '__main__':
    Main()
