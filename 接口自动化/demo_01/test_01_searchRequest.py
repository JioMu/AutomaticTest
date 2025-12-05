# import pytest


# loginInfo = {"account":"20200444",
#              "password":"meehoo2012",
#              "rememberMe":False,
#              "code":"1",
#              "uuid":"b849668f49d246fd9b7ff447d1d46361"}


# def test_login_success(api_client, assert_util):
#     response = api_client.post("/api/login/userLogin", 
#                                json=loginInfo)
#     assert_util.assert_status_code(response, 200)
#     assert_util.assert_json_containsKey(response, "account", "admin")
#     # assert_util.assert_json_containsValue(response, "admin")

