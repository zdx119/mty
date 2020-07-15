import pytest

from config.conf import GY_DB_QA
from tools.api import request_tool
from tools.data.mysql_tool import mysql_db


def login():
    method = "POST"  # 请求方法，全部大写
    uri = "/login"  # 接口地址
    # post请求json数据，注意数据格式为字典或者为json串 为空写None
    json_data = '''
            {
          "pwd": "qwe123",
          "userName": "853vZE"
        }
            '''
    status_code = 200  # 响应状态码
    expect = "2000"  # 预期结果
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r = request_tool.request(method=method, url=uri, pub_data=pub_data, json_data=json_data, status_code=status_code,
                             expect=expect)
    return r.json()["data"]["token"]


@pytest.fixture(scope='session')                            
def pub_data():
    data = {'token':login()}
    return data

@pytest.fixture()
def db():
    return mysql_db(**GY_DB_QA)
