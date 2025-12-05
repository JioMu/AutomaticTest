# 此版本为初始版本，reqeuestUtil中没有添加baseUrl,添加baseUrl后,初始版本已注释
'''
import pytest
from .config.setting import load_config

config = load_config()

@pytest.fixture(scope="session")
def baseUrl():
    """获取base_url"""
    return config['base']['baseUrl']

@pytest.fixture(autouse=True)
def auto_apply_baseUrl(baseUrl, request):
    """自动添加baseUrl到请求头"""
    if "baseUrl" in request.fixturenames:
        return baseUrl
'''

import pytest
import logging
import sys
import os
# 添加项目根目录到Python路径
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)

from demo_01.commonUtils.requestUtil import RequestUtils
from demo_01.commonUtils.assertUtil import AssertUtils

# 配置日志
# logging.basicConfig(
#     level=logging.INFO,
#     format='%(asctime)s - %(levelname)s - %(message)s',
#     handlers=[
#         logging.StreamHandler(),
#         logging.FileHandler('test.log')
#     ]
# )

@pytest.fixture(scope="session")
def api_client():
    '''创建api请求对象'''
    return RequestUtils()

@pytest.fixture(scope="session")
def assert_util():
    '''创建断言对象'''
    return AssertUtils()

def pytest_addoption(parser):
    parser.addoption(
        "--env", 
        action="store", 
        default="test", 
        help="Environment to run tests against: dev, test, prod"
        )

@pytest.fixture(scope="session")
def env(request):
    """获取环境"""
    return request.config.getoption("--env")

@pytest.fixture(scope="session")
def auth_token(api_client, assert_util, login_info):
    """获取授权token"""
    response = api_client.post("/api/login/userLogin", json=login_info)
    assert_util.assert_status_code(response, 200)
    token = assert_util.extract_value_by_key(response, "token")
    if token is None:
        token = assert_util.extract_value_by_key(response, "jwt")
    print("获取到的token为：", token)
    assert token is not None, "获取token失败"
    return token

@pytest.fixture(scope="session")
def login_info():
    """获取登录信息"""
    loginInfo = {"account":"20200444",
             "password":"meehoo2012",
             "rememberMe":False,
             "code":"1",
             "uuid":"b849668f49d246fd9b7ff447d1d46361"}
    return loginInfo

