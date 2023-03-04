import time
from behave import *
from hamcrest import *
from features.pages.loginpage import  LoginPageClass

#step defenitions

@given("Chrome is opened and apollo247 app is opened")
def step_impl(context):
    context.driver.implicitly_wait(40)
    expectedTitle = "Apollo 247 - Online Doctor Consultation & Book Lab Tests at Home"
    actualTitle = context.driver.title
    print("Page title is " + actualTitle)
    assert_that(expectedTitle, equal_to(actualTitle))

@then("Click on later button")
def step_impl(context):
    context.driver.implicitly_wait(40)
    LaterButton = LoginPageClass(context.driver)
    LaterButton.click_Later_button()

@when("User clicks on login/signUp button")
def step_impl(context):
    context.driver.implicitly_wait(40)
    loginButton = LoginPageClass(context.driver)
    loginButton.click_login_icon()


@then("It shows the Mobile number window")
def step_impl(context):
    context.driver.implicitly_wait(40)
    MWText = LoginPageClass(context.driver)
    expectedMWText = "Please enter your mobile number to login"
    actualMWText = MWText.check_MobileWindow_Text()
    print(actualMWText)
    assert_that(expectedMWText, equal_to(actualMWText))


@when('User enter "{number}"')
def step_impl(context,number):
    context.driver.implicitly_wait(40)
    MobileNumber = LoginPageClass(context.driver)
    MobileNumber.enter_mobilenumber_placeholder(number)

@step("User clicks on Next button")
def step_impl(context):
    context.driver.implicitly_wait(40)
    NextButton = LoginPageClass(context.driver)
    NextButton.click_next_button()


@then("It navigates to OTP window")
def step_impl(context):
    context.driver.implicitly_wait(10)
    textofotp  = LoginPageClass(context.driver)
    expectedtextofotpText = "Now type in the OTP sent to you for authentication"
    actualtextofotpText = textofotp.check_otpWindow_Text()
    print(actualtextofotpText)
    assert_that(expectedtextofotpText, equal_to(actualtextofotpText))

@when("User enters otp")
def step_impl(context):
    time.sleep(10)
    pass
    time.sleep(5)

@then("It navigates to Home page")
def step_impl(context):
    context.driver.implicitly_wait(40)
    username = LoginPageClass(context.driver)
    expectedusernameText = "weer"
    actualusernameText = username.check_User_Name()
    print(actualusernameText)
    assert_that(expectedusernameText, equal_to(actualusernameText))
    context.driver.implicitly_wait(10)

