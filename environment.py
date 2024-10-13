#before all - only once
#before scenario - before each scenario
#before step - before each step
import allure
from selenium import webdriver
#afterall - only once
#afterscenario
#afterstep
from PageObjects.LoginPage import  LoginPage
from PageObjects.HomePage import HomePage
def before_all(context):
    print("Before All")


def before_scenario(context,scenario):
    print("Before Scenario")


def before_step(context,step):
    print("Before Step")


def after_all(context):
    print("After All")


def after_scenario(context,scenario):
    print("After Scenario")
    hp = HomePage(context.driver)
    hp.clickLogout()

def after_step(context,step):
    print("After Step")
    #context.driver = webdriver.Chrome()
    #if you add this allure attach inside the if condition it will capture only for failure cases
    allure.attach(context.driver.get_screenshot_as_png(), name=step.name,
                  attachment_type=allure.attachment_type.PNG)
    # if step.status == "failed":
    #     allure.attach(context.driver.get_screenshot_as_png(), name=step.name,
    #                   attachment_type=allure.attachment_type.PNG)
    #
    #     print("failed")
    #     context.driver.get_screenshot_as_file(step.name+".png") #document purpose not needed