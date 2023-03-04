import time
from behave import *
from hamcrest import *
from features.pages.viewhealthrecordsClass import ViewHealthRecordsClass

@when("Clicks on view health records link")
def step_impl(context):
    context.driver.implicitly_wait(40)
    vhr = ViewHealthRecordsClass(context.driver)
    vhr.click_vhr_link()


@then("It shows the health records page")
def step_impl(context):
    context.driver.implicitly_wait(40)
    abn = ViewHealthRecordsClass(context.driver)
    expectedText = "Health Categories"
    actualText = abn.healthcat_text()
    print(actualText)
    assert_that(expectedText, equal_to(actualText))


@step("Clicks on height button")
def step_impl(context):
    context.driver.implicitly_wait(40)
    height = ViewHealthRecordsClass(context.driver)
    height.click_height_button()


@then("It shows update height window")
def step_impl(context):
    context.driver.implicitly_wait(40)
    abc = ViewHealthRecordsClass(context.driver)
    expectedText = "Update Height"
    actualText = abc.update_text()
    print(actualText)
    assert_that(expectedText, equal_to(actualText))


@step("Clicks on clinical documents link")
def step_impl(context):
    time.sleep(2)
    clinicalDocs = ViewHealthRecordsClass(context.driver)
    clinicalDocs.click_clinicaldocuments_link()

# step defenitions

@then("It shows reload page with clinical documents window")
def step_impl(context):
    context.driver.implicitly_wait(40)
    expectedTitle = ''
    actualTitle = context.driver.title
    print(actualTitle)
    assert_that(expectedTitle, equal_to(actualTitle))

@when(u'User enters {height}')
def step_impl(context,height):
    context.driver.implicitly_wait(40)
    heightNum = ViewHealthRecordsClass(context.driver)
    heightNum.enter_height_placeholder(height)


@step("Clicks on update button")
def step_impl(context):
    context.driver.implicitly_wait(40)
    updateHt = ViewHealthRecordsClass(context.driver)
    updateHt.click_update_button()

@then("It updates the data")
def step_impl(context):
    time.sleep(2)
    dataUpdate = ViewHealthRecordsClass(context.driver)
    expecteddata = "123 cms"
    actualdata  = dataUpdate.text_update_data()
    print(actualdata)
    assert_that(expecteddata, equal_to(actualdata))

@then("It shows error message")
def step_impl(context):
    context.driver.implicitly_wait(40)
    error = ViewHealthRecordsClass(context.driver)
    expectedText = "Invalid Input"
    actualText = error.text_error_msg()
    print(actualText)
    assert_that(expectedText, equal_to(actualText))











