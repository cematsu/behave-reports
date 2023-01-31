from random import random, randrange
from time import sleep

from behave import given, when, then


@given('I generate a test report')
def step_impl(context):
    pass


@given('I generate another test report')
def step_impl(context):
    pass


@when('I wait {seconds} sec')
def step_impl(context, seconds):
    sleep(int(seconds))


@then('I fail the test')
def step_impl(context):
    assert int(randrange(0, 100)) % 2 == 0, "ERROR"
