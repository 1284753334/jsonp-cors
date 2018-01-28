from django.shortcuts import render,HttpResponse
import requests
# Create your views here.


def jsonp1(request):
    """
    正常的用requests没有问题
    """
    data = requests.get('http://127.0.0.1:8033/data/')
    print(data.text)
    return render(request,'request的方式.html',{"data":data})

def jsonp2(request):

    return render(request,'jsonp2.html')


def test1(request):
    return HttpResponse('一切OK')


def cors(request):
    import platform
    print(platform.node())

    return render(request, 'cors.html')