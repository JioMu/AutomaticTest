import allure
import pytest

class TestHomePage:
    @allure.feature("首页")
    @allure.story("查询消息总数")
    @pytest.mark.normal
    def test_query_message_totals(self, assert_util, api_client, auth_token):
        allure.step("查询消息总数")
        response = api_client.get("/api/notification/queryMessageTotals", token=auth_token)
        assert_util.assert_status_code(response, 200)
        assert_util.assert_json_containsValue(response, "totals")

