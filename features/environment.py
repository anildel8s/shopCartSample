import allure
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


def before_scenario(context, driver):
    context.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    context.driver.implicitly_wait(10)
    context.driver.get("https://testscriptdemo.com/")
    context.driver.maximize_window()


def after_scenario(context, driver):
    print()
    allure.attach(context.driver.get_screenshot_as_png(), name='Last_Step',
                  attachment_type=allure.attachment_type.PNG)
    context.driver.close()


def after_step(context, step):
    print()
    if step.status == 'failed':
        allure.attach(context.driver.get_screenshot_as_png(), name='screenshot',
                      attachment_type=allure.attachment_type.PNG)