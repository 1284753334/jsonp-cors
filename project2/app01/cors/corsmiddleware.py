from django.utils.deprecation import MiddlewareMixin


class CorsMiddleware(MiddlewareMixin):
    """
    为解决跨域问题，所建立的中间件
    """

    def process_response(self, request, response):
        """
        :param response: server端向client端返回的json数据
        :return: 添加响应头
        """
        response["Access-Control-Allow-Methods"] = "POST,GET,OPTIONS,PUT"
        response['Access-Control-Allow-Origin'] = '*'
        response["Access-Control-Max-Age"] = '100000'
        response['Access-Control-Allow-Headers'] = "content-type"
        return response


