from django.shortcuts import render,HttpResponse

# Create your views here.


def data(request):
    """
    正常返回，不要对数据做处理
    """
    return HttpResponse('数据66666')


def data2(request):


    # 直接返回没有问题,但对方把数据当成未定义的变量
    # return HttpResponse('数据66666')
    # 所以,我们要配合,比如下面这样, 但这样太复杂了
    return HttpResponse('alert(111111)')

def data3(request):
    import time
    time.sleep(2)
    data_obj = 'qwertytffasdf'
    response = request.GET.get('callback')
    print(response)
    return HttpResponse('%s("%s")'%(response,data_obj))

def data5(request):

    data_obj = 'aaaaaaaaaaaaaaaa'
    response = request.GET.get('callback')
    print(response)
    return HttpResponse('%s("%s")' % (response, data_obj))
    # return HttpResponse('func("66666666")')


def cors(request):
    if request.method == 'OPTIONS':
        response = HttpResponse()
        # 设置缓存时间，在请求的十秒内，无需发送options请求预检验证，
        response['Access-Control-Max-Age'] = 10
        # 只允许这个请求访问
        # response['Access-Control-Allow-Origin'] = "http://127.0.0.1:8844"
        # 允许所有请求来访问
        response['Access-Control-Allow-Origin'] = "*"

        # 允许那些复杂的请求来访问
        response['Access-Control-Allow-Methods'] = "PUT"
        return response
    else:
        response = HttpResponse('CORS数据')
        response['Access-Control-Allow-Origin'] = "http://127.0.0.1:8844"
        return response

def cors1(request):

    return HttpResponse('最牛逼的cors中间件')