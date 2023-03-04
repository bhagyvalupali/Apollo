from behave import *
import time
from hamcrest import *
from features.pages.healthrecordspageclass import healthrecordspageClass
from features.utility.ConfigClass import ConfigClass
from datafiles import Excelutils


@given("Chrome is opened and app url is launched")
def step_impl(context):
    context.driver.implicitly_wait(40)
    expectedTitle = "Apollo 247 - Online Doctor Consultation & Book Lab Tests at Home"
    actualTitle = context.driver.title
    print("Page title is " + actualTitle)
    assert_that(expectedTitle, equal_to(actualTitle))


@then("Clicks on later button")
def step_impl(context):
    context.driver.implicitly_wait(40)
    LaterButton = healthrecordspageClass(context.driver)
    LaterButton.click_Later_button()


@when("User clicks on the login/signup button")
def step_impl(context):
    context.driver.implicitly_wait(40)
    loginButton = healthrecordspageClass(context.driver)
    loginButton.click_login_icon()

@then("It shows mobile number window")
def step_impl(context):
    context.driver.implicitly_wait(40)
    MWText = healthrecordspageClass(context.driver)
    expectedMWText = "Please enter your mobile number to login"
    actualMWText = MWText.check_MobileWindow_Text()
    print(actualMWText)
    assert_that(expectedMWText, equal_to(actualMWText))

@when('User enters "{number}"')
def step_impl(context,number):
    context.driver.implicitly_wait(40)
    MobileNumber = healthrecordspageClass(context.driver)
    MobileNumber.enter_mobilenumber_placeholder(number)

@step("User clicks on the next button")
def step_impl(context):
    context.driver.implicitly_wait(40)
    NextButton = healthrecordspageClass(context.driver)
    NextButton.click_next_button()

@then("It navigates to the otp window")
def step_impl(context):
    context.driver.implicitly_wait(10)
    textofotp = healthrecordspageClass(context.driver)
    expectedtext = "Now type in the OTP sent to you for authentication"
    actualtext = textofotp.check_otpWindow_Text()
    print(actualtext)
    assert_that(expectedtext, equal_to(actualtext))

@when("User enters the otp")
def step_impl(context):
    time.sleep(10)
    pass
    time.sleep(5)

@then("It navigates to the home page")
def step_impl(context):
    context.driver.implicitly_wait(40)
    username = healthrecordspageClass(context.driver)
    expectedtext = "weer"
    actualtext = username.check_User_Name()
    print(actualtext)
    assert_that(expectedtext, equal_to(actualtext))
    context.driver.implicitly_wait(10)

@when("User clicks on view health records link")
def step_impl(context):
    context.driver.implicitly_wait(40)
    vhr = healthrecordspageClass(context.driver)
    vhr.click_vhr_link()

@then("It shows health records page")
def step_impl(context):
    context.driver.implicitly_wait(40)
    abn = healthrecordspageClass(context.driver)
    expectedText = "Health Categories"
    actualText = abn.healthcat_text()
    print(actualText)
    assert_that(expectedText, equal_to(actualText))

@step("User clicks on height button")
def step_impl(context):
    context.driver.implicitly_wait(40)
    height = healthrecordspageClass(context.driver)
    height.click_height_button()


@then("It shows the update window")
def step_impl(context):
    context.driver.implicitly_wait(40)
    abc = healthrecordspageClass(context.driver)
    expectedText = "Update Height"
    actualText = abc.update_text()
    print(actualText)
    assert_that(expectedText, equal_to(actualText))


@when("User enters the {height}")
def step_impl(context,height):
    context.driver.implicitly_wait(40)
    Excelutils.get_row_count(ConfigClass.datafilepath, "Sheet1")
    data = Excelutils.read_data(ConfigClass.datafilepath, "Sheet1", 2, 1)
    dataenter = healthrecordspageClass(context.driver)
    dataenter.enter_height_placeholder(data)

@step("User  clicks on update button")
def step_impl(context):
    context.driver.implicitly_wait(40)
    updateHt = healthrecordspageClass(context.driver)
    updateHt.click_update_button()

@then("It updates the height")
def step_impl(context):
    time.sleep(3)
    updatedheight = healthrecordspageClass(context.driver)
    expectedheight = "69 cms"
    actualheight= updatedheight.text_update_data()
    print(actualheight)
    assert_that(expectedheight, equal_to(actualheight))
    time.sleep(2)
    try:
        if(expectedheight == actualheight):
            assert True
            print("Test is passed")
            Excelutils.write_data(ConfigClass.datafilepath, "Sheet1", 2, 2, "Passed")
            time.sleep(3)
        else:
            print("Test is failed")
            Excelutils.write_data(ConfigClass.datafilepath, "Sheet1", 2, 2, "Failed")
            assert False
            time.sleep(3)

    finally:
        context.driver.implicitly_wait(40)
        height = healthrecordspageClass(context.driver)
        height.click_height_button()


