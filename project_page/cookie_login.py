#

import time
import unittest
import yaml
from selenium import webdriver


class TestCookieLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_get_cookies(self):
        self.driver.get("http://work.weixin.qq.com/wework_admin/frame")
        time.sleep(20)
        cookies = self.driver.get_cookies()
        print(cookies)
        # 修复：正确写入文件，使用 with 确保文件关闭
        with open("../data/cookie.yaml", "w") as f:
            yaml.safe_dump(cookies, f)  # 正确写法：yaml.safe_dump(数据, 文件对象)
