__author__ = 'pioc'

from page_objects import PageObject, PageElement

class EmployeeListPage(PageObject):
    label_welcome = PageElement(xpath="//p[@id='greetings']")
    actions_label = PageElement(xpath="//ul[@id='sub-nav']")
    btn_logout = PageElement(xpath="//p[@class='main-button']")