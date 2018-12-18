__author__ = 'pioc'

from behave import *
from features.pages.LoginPage import *
from features.pages.MainPage import *
from features.environment.browser import Browser
from main import testsConfig as config


driver = Browser.driver
login_page = LoginPage(driver)
main_page = EmployeeListPage(driver)

class LoginPageStepsClass:

    ### GIVEN section #################################################################################################

    @given('user opens CafeTownsend application website')
    def step(self):
        driver.get(config.environmentLink)

    ### WHEN section #################################################################################################

    @when('user clicks Login button')
    def step(self):
        login_page.btn_submit_login.click()

    @when('user fills form with "{loginIsValid}" login and "{passwordIsValid}" password')
    def steps(self, loginIsValid, passwordIsValid):
        if loginIsValid == 'valid':
            login_page.input_login.send_keys(config.credentials['login'])
        elif loginIsValid == 'empty':
            login_page.input_login.send_keys('')
        elif loginIsValid == 'invalid':
            login_page.input_login.send_keys('abcdefgh123')

        if passwordIsValid == 'valid':
            login_page.input_password.send_keys(config.credentials['password'])
        elif passwordIsValid == 'empty':
            login_page.input_password.send_keys('')
        elif passwordIsValid == 'invalid':
            login_page.input_password.send_keys('abcdefgh123')

    ### THEN section #################################################################################################

    @then('user is redirected to application main page')
    def steps(self):
        assert 'Create' in main_page.actions_label.text
        assert main_page.btn_logout

    @then('users username is shown')
    def steps(self):
        assert main_page.label_welcome.text == 'Hello ' + (config.credentials['login'])

    @then('invalid username or password label is shown')
    def steps(self):
        assert login_page.label_invalid_credentials.text == 'Invalid username or password!'

    @then('user is redirected to login page')
    def steps(self):
        assert login_page.input_login and login_page.input_password and login_page.btn_submit_login
        if not main_page.label_welcome: raise AssertionError