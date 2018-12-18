__author__ = 'pioc'

from page_objects import PageObject, PageElement


class LoginPage(PageObject):
    input_login = PageElement(xpath="//span[text()='Username*']/ancestor::label/input")
    input_password = PageElement(xpath="//span[text()='Password*']/ancestor::label/input")
    btn_submit_login = PageElement(xpath="//button[@class='main-button']")
    label_invalid_credentials = PageElement(xpath="//p[@class='error-message ng-binding']")