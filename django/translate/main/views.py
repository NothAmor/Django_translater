from django.shortcuts import render
from django.http import HttpResponse

import urllib
import time, json, random, hashlib

# Create your views here.

def index(request):
    return render(request, 'main.html')

def return_result(request):
    content = request.POST.get("content")
    url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"
    data = {}

    u = 'fanyideskweb'
    d = content
    f = str(int(time.time() * 1000) + random.randint(1, 10))
    c = 'rY0D^0\'nM0}g5Mm1z%1G4'
    sign = hashlib.md5((u + d + f + c).encode('utf-8')).hexdigest()

    data = {'i': content,
            'from': 'AUTO',
            'to': 'AUTO',
            'smartresult': 'dict',
            'client': 'fanyideskweb',
            'doctype': 'json',
            'version': '2.1',
            'keyfrom': 'fanyi.web',
            'action': 'FY_BY_REALTIME',
            'typoResult': 'false'}
    data = urllib.parse.urlencode(data).encode('utf-8')
    req = urllib.request.Request(url, data)
    response = urllib.request.urlopen(req)

    res = response.read().decode('utf-8')
    res = json.loads(res)
    res = res["translateResult"]
    #print(res[0][0]['tgt'])
    return HttpResponse(res[0][0]['tgt'])