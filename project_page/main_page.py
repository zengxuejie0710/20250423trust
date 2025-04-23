import time

import yaml
from selenium.webdriver.chrome import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By

from project_page.add_member import AddMemberPage
from project_page.contact_page import ContactPage


class MainPageObject:
    # 跳转通讯录页面的功能
    def goto_contact_page(self):
        return  ContactPage()
        pass
    # 跳转添加成员页面的功能
    def goto_add_member_page(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(3)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        cookies = yaml.safe_load(open("../data/cookie.yaml"))
        # 修复：检查文件是否存在且内容有效
        try:
            with open("../data/cookie.yaml", "r") as f:
                cookies = yaml.safe_load(f)
                if cookies is None:
                    self.fail("cookie.yaml 文件内容为空或格式错误")
        except FileNotFoundError:
            self.fail("cookie.yaml 文件不存在，请先运行 test_get_cookies")

        # 添加 cookie
        for c in cookies:
            self.driver.add_cookie(c)
        time.sleep(3)
        # 刷新页面验证登录状态
        self.driver.refresh()
        self.driver.get("http://work.weixin.qq.com/wework_admin/frame")
        return AddMemberPage()