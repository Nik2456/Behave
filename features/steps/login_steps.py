from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@given("user is on login page")
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://www.saucedemo.com/v1/")
    context.driver.maximize_window()
    context.driver.implicitly_wait(10)

@when ("user enters valid username and password")
def step_impl(context):
    context.driver.find_element(By.ID,"user-name").send_keys("standard_user")
    context.driver.find_element(By.ID, "password").send_keys("secret_sauce")
    time.sleep(5)

@when("click on login button")
def step_impl(context):
    context.driver.find_element(By.ID,"login-button").click()

@then("user should be navigate to th product page")
def step_impl(context):
    text=context.driver.find_element(By.CLASS_NAME,"product_label").text
    assert text == "Products",f"{text} should be 'Products'"