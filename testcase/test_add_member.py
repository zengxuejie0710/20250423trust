
from project_page.main_page import MainPageObject

class TestAddMember:

    def setup_class(self):
        """
        用例执行前的准备工作
        :return:
        """
        self.main = MainPageObject()

    def  teardown_class(self):
        """
        退出driver
        :return:
        """
        pass
    def test_add_member(self):
        #明天再继续
        main= MainPageObject()
        # 跳转到添加成员页面
        # addmember的操作
        # 获取到通讯录的成员列表
        # 断言实际结果与预期结果
        self.main.goto_add_member_page().add_member()
        # assert  "" in  mem_list
        print("直接指向主分支")