import requests
import logging
import sys
import os


from demo_01.config.setting import load_config

config = load_config()

class RequestUtils:
    def __init__(self):
        self.baseUrl = config['base']['baseUrl']
        self.timeout = config['base']['timeout']
        # 创建session
        self.session = requests.Session()

    def request(self, method, endUrl, **kwargs):
        """发送请求
        
        Args:
            method: HTTP方法 (GET/POST/PUT/DELETE等)
            endUrl: API端点路径
            **kwargs: 其他请求参数，可包含:
                - json: 请求体数据 (dict)
                - token: 认证token (str)
                - headers: 额外头部信息 (dict)
                - 其他requests支持的参数 (timeout, params等)
        """
        url = f"{self.baseUrl}{endUrl}"
        kwargs.setdefault("timeout", self.timeout)
        
        # 处理认证token
        if 'token' in kwargs:
            token = kwargs.pop('token')  # 取出token并从kwargs中移除
            headers = kwargs.get('headers', {})  # 获取已有的headers或新建空dict
            headers['Token'] = token
            kwargs['headers'] = headers
        
        # 日志记录
        logging.info(f"请求方法 -> {method.upper()}")
        if 'json' in kwargs:
            logging.info(f"请求参数 -> {kwargs['json']}")
        if 'headers' in kwargs and 'Authorization' in kwargs['headers']:
            logging.debug("携带认证token")  # 安全考虑，不直接记录token内容
        
        # 发送请求
        response = self.session.request(method, url, **kwargs)
        
        # 记录响应
        logging.info(f"响应状态码 -> {response.status_code}")
        logging.debug(f"响应内容 -> {response.text}")
        
        return response
        
    def get(self, endUrl, **kwargs):
        """发送get请求"""
        return self.request("get", endUrl, **kwargs)
    
    def post(self, endUrl, **kwargs):
        """发送post请求"""
        return self.request("post", endUrl, **kwargs)
    
    def put(self, endUrl, **kwargs):
        """发送put请求"""
        return self.request("put", endUrl, **kwargs)
    
    def delete(self, endUrl, **kwargs):
        """发送delete请求"""
        return self.request("delete", endUrl, **kwargs)