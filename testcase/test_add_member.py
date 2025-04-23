from project_page.main import MainPageObject


class TestAddMember:
    def test_add_member(self):
        #
        main= MainPageObject()
        # 跳转到添加成员页面
        # addmember的操作
        # 获取到通讯录的成员列表
        # 断言实际结果与预期结果
        mem_list = main.goto_add_member_page().add_member().get_member_list()
        assert  "" in  mem_list
