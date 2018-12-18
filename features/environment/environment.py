__author__ = 'pioc'

from features.environment.browser import Browser

def before_all(context):
    print('before all execution \n')


def after_all(context):
    print('\nfinished')
    Browser.driver.close()