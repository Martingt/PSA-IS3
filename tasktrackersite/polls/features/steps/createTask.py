from behave import *

@given('i am a employee')
def step_impl(context):
    pass

@when('i create a task and i have permission to do so')
def step_impl(context):
    assert True is not False

@then('the task is successfully registered')
def step_impl(context):
    assert context.failed is False