import logging

class AssertUtils:
    def __init__(self):
        pass
        
    @staticmethod
    def assert_status_code(response, expected_code):
        assert response.status_code == expected_code, \
            f"响应码错误，期望值：{expected_code}，实际值：{response.status_code}"
        logging.info(f"响应码正确，期望值：{expected_code}，实际值：{response.status_code}")
    
    @staticmethod
    def assert_json_containsKey(response, key, value=None):
        '''断言json结果中包含key,可以将value为期望值'''
        json_data = response.json()

        def find_value_in_nested_dict(data, target_key):
            """在嵌套字典中查找指定的key"""
            # print("查看data.items()---->",data)
            if isinstance(data, dict):
                if target_key in data:
                    return data[target_key]
                for k, v in data.items():
                    result = find_value_in_nested_dict(v, target_key)
                    if result is not None:
                        return result
            elif isinstance(data, list):
                for item in data: 
                    result = find_value_in_nested_dict(item, target_key)
                    if result is not None:
                        return result
            return None
        
        actual_value = find_value_in_nested_dict(json_data, key)
        assert actual_value is not None, f"响应结果中不存在key：{key}"

        # 删除这行导致错误的代码: assert key in json_data

        if value is not None:
            assert actual_value == value, \
                f"响应结果中key：{key}的值错误，期望值：{value}，实际值：{actual_value}"
            logging.info(f"响应结果中key：{key}的值正确，期望值：{value}，实际值：{actual_value}")
    
    @staticmethod
    def assert_json_containsValue(response, value):
        '''断言json中value是否包含value,可以将expected_value为期望值'''
        json_data = response.json()

        def find_value_in_nested_dict(data, target_value):
            
            """在嵌套字典中查找指定值"""
            if isinstance(data, dict):
                if target_value in data.values():
                    return True
                for v in data.values():
                    if find_value_in_nested_dict(v, target_value):
                        return True
            elif isinstance(data, list):
                for item in data: 
                    if find_value_in_nested_dict(item, target_value):
                        return True
            elif data == target_value:
                return True
            return False

        actual_value = find_value_in_nested_dict(json_data, value)
        assert actual_value, \
            f"响应结果中不存在value：{value}"
        
    @staticmethod
    def extract_value_by_key(response, key):
        """提取json结果中指定key的值"""
        json_data = response.json()
        def find_value_in_nested_dict(data, target_key):
            """在嵌套字典中查找指定的key"""
            # print("查看data.items()---->",data)
            if isinstance(data, dict):
                if target_key in data:
                    return data[target_key]
                for k, v in data.items():
                    result = find_value_in_nested_dict(v, target_key)
                    if result is not None:
                        return result
            elif isinstance(data, list):
                for item in data: 
                    result = find_value_in_nested_dict(item, target_key)
                    if result is not None:
                        return result
            return None
        return find_value_in_nested_dict(json_data, key)

