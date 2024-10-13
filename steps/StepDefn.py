from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By

from PageObjects.LoginPage import  LoginPage
from PageObjects.HomePage import HomePage

driver = webdriver.Chrome()
driver.implicitly_wait(30)
driver.maximize_window()
hp = HomePage(driver)
lp = LoginPage(driver)


@given(u'the user launches the application')
def the_user_launches_the_application(context):
    context.driver = driver
    context.driver.get("https://www.saucedemo.com/")


@then(u'the user verifies the application is loaded')
def the_user_verifies_the_application_is_loaded(context):
    context.driver = driver
    logo = context.driver.find_element(By.CLASS_NAME,"login_logo").is_displayed()
    assert logo is True

@when(u'the user enters the valid credentials')
def the_user_enters_the_valid_credentials(context):
    context.driver = driver
    lp.enterUsername("standard_user")
    lp.enterPassword("secret_sauce")
    lp.clickLogin()

@when(u'the user verifies the home page')
def the_user_verifies_the_home_page(context):
    context.driver = driver
    assert hp.verifyLogo() is True


@then(u'the user filters \"{str}\"')
def step_impl(context,str):
    hp.selectFilterDropdown(str)


@then(u'the user logouts from the application')
def logout(context):
    hp.clickLogout()