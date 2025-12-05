from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

'''封装基础方法'''


class Base:

    def __init__(self, driver):
        self.driver = driver
        self.timeout = 10
        self.poll = 0.5

    # 定位单个元素
    def findElement(self, loc):
        # 定位到元素返回元素对象，没定位到超时返回错误
        if not isinstance(loc, tuple):
            print('loc参数类型错误，必须返回元组类型: loc=("id", "value1")')
        else:
            print('正在定位元素：%s' % loc)
            # 显示等待
            return WebDriverWait(self.driver, self.timeout, self.poll).until(EC.presence_of_element_located(loc))

    # 定位一组元素
    def findElements(self, loc):
        if not isinstance(loc, tuple):
            print('loc参数类型错误，必须返回元组类型: loc=("id", "value1")')
        else:
            print('正在定位元素：%s' % loc)
            return WebDriverWait(self.driver, self.timeout, self.poll).until(EC.presence_of_all_elements_located(loc))

    # 填写数据
    def sendKeys(self, loc, text):
        ele = self.findElement(loc)
        ele.send_keys(text)

    # 点击元素
    def click(self, loc):
        ele = self.findElement(loc)
        ele.click()

    # 清空输入框
    def clear(self, loc):
        ele = self.findElement(loc)
        ele.clear()

    # 判断元素是否被选中
    def isSelected(self, loc):
        ele = self.findElement(loc)
        return ele.is_selected()

    # 判断元素是否存在
    def isElementExists(self, loc):
        try:
            self.findElement(loc)
            return True
        except:
            return False

    # 判断标题是否等于指定标题
    def isTitle(self, title=""):
        '''返回布尔值'''
        try:
            result = WebDriverWait(self.driver, self.timeout, self.poll).until(EC.title_is(title))
            return result
        except:
            return False

    # 判断标题是否包含某关键字
    def isTitleContains(self, title=""):
        '''返回布尔值'''
        try:
            result = WebDriverWait(self.driver, self.timeout, self.poll).until(EC.title_contains(title))
            return result
        except:
            return False

    # 指定文本是否在某元素中
    def isTextInElement(self, loc, text):
        if not isinstance(loc, tuple):
            print('loc参数类型错误，必须返回元组类型: loc=("id", "value1")')
            try:
                result = WebDriverWait(self.driver, self.timeout, self.poll).until(
                    EC.text_to_be_present_in_element(loc, text))
                return result
            except:
                return False

    # 指定值是否在某元素中
    def isValueInElement(self, loc, value):
        if not isinstance(loc, tuple):
            print('loc参数类型错误，必须返回元组类型: loc=("id", "value1")')
            try:
                result = WebDriverWait(self.driver, self.timeout, self.poll).until(
                    EC.text_to_be_present_in_element_value(loc, value))
                return result
            except:
                return False

    # 判断是否弹出警告框
    def isAlert(self, timeout=3):
        try:
            result = WebDriverWait(self.driver, timeout, self.poll).until(EC.alert_is_present())
            return result
        except:
            return False

    # 获取当前页面的url
    def getTitle(self):
        return self.driver.title

    # 获取元素文本
    def getText(self, loc):
        try:
            return self.findElement(loc).text
        except:
            print("获取元素文本失败,返回''")
            return ""

    # 获取元素属性值
    def getAttribute(self, loc, name):
        try:
            return self.findElement(loc).get_attribute(name)
        except:
            print("获取元素属性值失败,返回''" % name)
            return ""

    # 聚焦元素
    def js_focus_element(self, loc):
        ele = self.findElement(loc)
        self.driver.execute_script("arguments[0].scrollIntoView();", ele)

    # 滚动到顶部
    def js_scroll_top(self):
        js = "window.scrollTo(0,0)"
        self.driver.execute_script(js)

    # 滚动到底部
    def js_scroll_bottom(self, x=0):
        js = "window.scrollTo(%s,document.body.scrollHeight)" % x
        self.driver.execute_script(js)

    # 通过索引获取元素
    def select_by_index(self, loc, index=0):
        ele = self.findElement(loc)  # 定位下拉框元素
        Select(ele).select_by_index(index)

    # 通过value值获取元素
    def select_by_value(self, loc, value):
        ele = self.findElement(loc)
        Select(ele).select_by_value(value)

    # 通过文本值获取元素
    def select_by_text(self, loc, text):
        ele = self.findElement(loc)
        Select(ele).select_by_visible_text(text)

