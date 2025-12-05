import sys
import os

# 获取当前脚本所在目录作为项目根目录
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(current_dir)
sys.path.insert(0, project_root)

import pytest

def check_and_run_tests():
    """检查并运行测试"""
    print(f"项目根目录: {project_root}")
    print(f"当前目录: {current_dir}")
    
    # 优先运行整个目录
    test_dir_path = current_dir
    if os.path.exists(test_dir_path):
        print(f"运行测试目录: {test_dir_path}")
        return pytest.main(["-s", "-v", test_dir_path])
    else:
        print(f"测试目录不存在: {test_dir_path}")
        
    # 如果目录不存在，尝试运行特定文件
    test_file_path = os.path.join(current_dir, "test_01_searchRequest.py")
    if os.path.exists(test_file_path):
        print(f"运行测试文件: {test_file_path}")
        return pytest.main(["-s", "-v", test_file_path])
    else:
        print(f"测试文件不存在: {test_file_path}")
        return 4  # ExitCode.USAGE_ERROR

if __name__ == '__main__':
    exit_code = check_and_run_tests()
    sys.exit(exit_code)