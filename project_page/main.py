from project_page.add_member import AddMemberPage
from project_page.contact_page import ContactPage


class MainPageObject:
    # 跳转通讯录页面的功能
    def  goto_contact_page(self):
        return  ContactPage()
        pass
    # 跳转添加成员页面的功能
    def goto_add_member_page(self):
        return AddMemberPage()