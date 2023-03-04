
import time
from features.utility.UtilityClass import UtilityClass
from selenium.webdriver.support.wait import WebDriverWait

def before_scenario(context, driver):
    UtilityClass.launch_browser(context)
    context.driver.implicitly_wait(10)
    UtilityClass.launch_app(context)
    context.driver.implicitly_wait(5)
    UtilityClass.Maximize_browser(context)


def after_scenario(context, driver):
    context.driver.implicitly_wait(5)
    UtilityClass.close_browser(context)
