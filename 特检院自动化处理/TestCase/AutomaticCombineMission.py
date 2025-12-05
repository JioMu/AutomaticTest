# 自动处理没有合并的任务
from selenium.common import StaleElementReferenceException

import Utils.webDriverUtils as webDriverUtils
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
import Utils.readElement


class AutomaticCombineMission:
    def __init__(self):
        print('程序开始')
        # 初始化 WebDriver 实例
        self.web_driver_utils = webDriverUtils.WebDriverOpen("edge")
        # 获取 WebDriver 实例
        self.driver = self.web_driver_utils.driver
        # 初始化 ActionChains 实例
        self.actions = ActionChains(self.driver)
        # 初始化 WebDriverWait 实例
        self.wait = WebDriverWait(self.driver, 10)
        self.wait_longtime = WebDriverWait(self.driver, 1800, poll_frequency=0.1)
        # 打开特检院网址
        self.driver.get("http://203.93.105.5:8012/")
        self.driver.maximize_window()

    # 退出浏览器
    def quitDriver(self):
        self.driver.quit()
        print('浏览器已退出')

    # 检查webDriver是否过期
    def is_driver_active(self):
        try:
            return self.driver and self.driver.session_id
        except Exception:
            print("webDriver已过期")
            return False

    # 判断元素是否存在
    def isElementExists(self, by, loc):
        try:
            self.wait.until(EC.presence_of_element_located((by, loc)))
            print('元素存在')
            return True
        except Exception as e:
            print(f"元素不存在")
            return False

    # 长时间判断元素是否存在
    def isElementExists_longtime(self, by, loc):
        try:
            self.wait_longtime.until(EC.presence_of_element_located((by, loc)))
            print('元素存在')
            return True
        except Exception as e:
            print(f"元素不存在{e}")
            return False

    def login(self):
        try:
            # 登录特检院
            usernameInput = self.wait.until(EC.presence_of_element_located((By.XPATH, '//input[@id="userName"]')))
            usernameInput.send_keys("admin")
            passwordInput = self.wait.until(EC.presence_of_element_located((By.XPATH, '//input[@id="password"]')))
            passwordInput.send_keys("tjy2023!")
            # 点击登录按钮
            loginButton = self.wait.until(EC.presence_of_element_located((By.XPATH, '//span[text()="登 录"]')))
            if usernameInput and passwordInput:
                time.sleep(1.5)
                loginButton.click()
            else:
                print('必填项为空!')
            # 进入任务列表页面
            tasklistButton = self.wait.until(EC.presence_of_element_located(
                (By.XPATH, '//li[contains(@data-menu-id,"/taskList/TaskList")]')))

            # 进入市外手动任务列表页面
            # tasklistButton = self.wait.until(EC.presence_of_element_located(
            #     (By.XPATH, '//li[contains(@data-menu-id,"/taskList/TaskListOut")]')))

            tasklistButton.click()
            # 下拉框选择任务状态为“上传中”状态
            taskStatusSelect = self.wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@id="taskStatus"]')))
            taskStatusSelect.click()
            uploadingSelect = self.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[text()="上传中"]')))
            uploadingSelect.click()
            time.sleep(1)
        except Exception as e:
            print(f'操作失败------------------\n{e}')
        finally:
            print('登录程序结束')
            print("----------------------------------------------------------")

    def get_task_list(self):
        try:
            # 初始化 start_index 变量，记录当前处理到的行索引
            start_index = 0
            while True:  # 无限循环，直到手动退出或发生异常
                try:
                    listDiv = self.wait.until(
                        EC.visibility_of_element_located((By.XPATH, '//div[@class="ant-table-container"]')))
                    listTable = listDiv.find_element(By.TAG_NAME, "table")
                    rows = listTable.find_elements(By.TAG_NAME, 'tr')
                    if len(rows) > 0:
                        print('任务列表不为空!----------->')
                    else:
                        print('任务列表为空!')
                    # 从 start_index 开始遍历每一行
                    for index, row in enumerate(rows[start_index:], start=start_index):
                        print("------------------->", row.text)
                        if "任务流水号" in row.text or row.text == "" or "暂无数据" in row.text:
                            print('跳过此条数据!')
                            continue
                        taskDetail_button = row.find_element(By.XPATH, './/button[contains(., "查看详情")]')
                        if taskDetail_button:
                            print('点击查看详情按钮...')
                            time.sleep(1)
                            taskDetail_button.click()

                            time.sleep(1)
                            print("执行合并视频逻辑---")
                            flag = self.combine_video()
                            # 如果返回为0,说明为待上传,执行下一次循环
                            if flag == 0:
                                start_index = index + 1
                                continue
                            else:
                                back_taskList_button = self.wait.until(
                                    EC.element_to_be_clickable((By.XPATH, '//a[text()="任务列表"]')))
                                time.sleep(1)
                                back_taskList_button.click()
                                # time.sleep(1)
                                # self.driver.execute_script("window.history.back()")
                                time.sleep(1)
                                start_index = index + 1
                                break
                        else:
                            print('未找到查看详情按钮,刷新页面重试!')
                            self.driver.refresh()
                            return self.get_task_list()
                    search_button = self.wait.until(
                        EC.element_to_be_clickable((By.XPATH, '//button[@class="ant-btn css-fpg3f5 ant-btn-primary"]'))
                    )
                    time.sleep(1)
                    search_button.click()
                except StaleElementReferenceException:
                    print('表格元素已过期，正在重新获取...')
                    continue
        except Exception as e:
            print(f'操作失败-------------------\n{e}')

    def combine_video(self):
        # 返回任务列表按钮
        back_taskList_button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, '//a[text()="任务列表"]')))
        print('返回任务列表按钮获取成功!')
        try:
            # 判断任务状态是否为待上传,如果为待上传返回0,外层调用处判断是否为0self.wait.until(
            #                     EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "待上传")]')))
            if self.isElementExists(By.XPATH, '//*[contains(text(), "待上传")]'):
                print('任务状态为待上传,点击返回任务列表按钮...')
                back_taskList_button.click()
                return 0
            print("任务状态为上传中,执行合并视频逻辑...")
            listDiv = self.wait.until(
                EC.presence_of_element_located(
                    (By.XPATH, '//div[@class="ant-table-wrapper css-fpg3f5"][2]//div[@class="ant-table-body"]')))
            print("listDiv获取成功!")
            table = listDiv.find_element(By.TAG_NAME, 'table')
            print("table获取成功!")
            rows = table.find_elements(By.TAG_NAME, 'tr')
            print("rows获取成功!")
            for row in rows:
                try:
                    print("开始查找当前列视频状态")
                    video_status = row.find_element(By.XPATH, ".//td[3]//span")
                    print(f"此行视频状态为--->{video_status.text}")
                    if video_status.text == "上传中":
                        print(f"{row.text}->此行视频状态为上传中,执行合并!")
                        combine_button = row.find_element(By.XPATH, './/button[contains(., "合 并")]')
                        print("获取视频状态成功!")
                        time.sleep(1)
                        print("点击视频合并按钮...")
                        combine_button.click()
                        time.sleep(1)
                        print("等待视频合并结果...")

                        # 获取结果弹窗
                        combine_badge_isExist = self.isElementExists_longtime(By.XPATH,
                                                                              '//div[@class="ant-message-notice'
                                                                              '-content"]//span[2]')
                        print(f"获取状态的结果为{combine_badge_isExist}")
                        if combine_badge_isExist:
                            combine_badge = WebDriverWait(self.driver, 1800, poll_frequency=0.1).until(
                                EC.visibility_of_element_located(
                                    (
                                        By.XPATH,
                                        '//div[@class="ant-message-notice'
                                        '-content"]//span[2]')))
                            print(f"合并结果为--->{combine_badge.text}")
                            # 判断合并结果
                            if "合并成功" in combine_badge.text:
                                print("视频合并成功,返回任务列表页面...")
                                time.sleep(1)
                                # back_taskList_button.click()
                                break
                            elif "JDBC" in combine_badge.text or "executed" in combine_badge.text:
                                print("视频合并失败,刷新页面后重新开始执行!")
                                if self.is_driver_active():
                                    self.driver.refresh()
                                    time.sleep(1)
                                    return self.combine_video()
                                else:
                                    print("driver已关闭,请重新打开driver")
                                    return
                            elif "未全部完成" in combine_badge.text:
                                print("视频没有全部完成,请稍等...")
                                time.sleep(2)
                                continue
                        else:
                            print("未获取到结果弹窗")

                    else:
                        print('视频状态不为上传中，跳过-------------------')
                        continue
                except StaleElementReferenceException:
                    print('表格元素已过期，正在重新获取...')
                    return self.combine_video()
                except Exception as e:
                    print(f'操作失败-------------------\n{e}')
                    continue

        except Exception as e:
            print(f'操作失败-------------------\n{e}')
            back_taskList_button.click()


if __name__ == '__main__':
    automaticComb = AutomaticCombineMission()
    # 登录
    automaticComb.login()
    # 获取任务列表
    automaticComb.get_task_list()
