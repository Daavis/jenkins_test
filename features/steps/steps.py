from behave import *


@when('I print {parm}')
def step_impl(context, parm):
    print(eval("context."+parm))