from behave import *
from main import Task, ToDoListManager

to_do_list_manager = ToDoListManager()
# Step 1: Given the to-do list is empty
@given('the to-do list is empty')
def step_impl(context):
    to_do_list_manager.clear_tasks()

# Step 2: When the user adds a task "{task}"
@when('the user adds a task "{task}"')
def step_impl(context, task):
    to_do_list_manager.add_task(task)

# Step 3: Then the to-do list should contain "{task}"
@then('the to-do list should contain "{task}"')
def step_impl(context, task):
    to_do_list_manager.list_tasks()
    assert task in [task_obj.description for task_obj in to_do_list_manager.tasks], f'Task "{task}" not found in the to-do list'

# Step 4: Given the to-do list contains tasks:
@given('the to-do list contains tasks')
def step_impl(context):
    for row in context.table:
        task_description = row['Task']
        to_do_list_manager.add_task(task_description)

# Step 5: When the user lists all tasks
@when('the user lists all tasks')
def step_impl(context):
    context.output = to_do_list_manager.list_tasks().strip()

# Step 6: Then the output should contain:
@then('the output should contain')
def step_impl(context):
    expected_output = context.text.strip()
    print(expected_output)
    print(context.output)
    assert expected_output == context.output, f'Expected output not found:\nExpected:\n{expected_output}\nActual:\n{context.output}'


# Step: Given the to-do list contains tasks2:
@given('the to-do list contains tasks2')
def step_impl(context):
    for row in context.table:
        task_description = row['Task']
        task_status = True if row['Status'].lower() == 'completed' else False
        to_do_list_manager.add_task(Task(task_description, task_status))


# Step: When the user marks task "{task}" as completed
@when('the user marks task "{task}" as completed')
def step_impl(context, task):
    to_do_list_manager.complete_task(task)

# Step: Then the to-do list should show task "{task}" as completed
@then('the to-do list should show task "{task}" as completed')
def step_impl(context, task):
    task_list = to_do_list_manager.list_tasks()
    assert f"[Completed] {task}" in task_list, f'Task "{task}" not marked as completed in the to-do list'


# Step: Given the to-do list contains tasks3:
@given('the to-do list contains tasks3')
def step_impl(context):
    for row in context.table:
        task_description = row['Task']
        to_do_list_manager.add_task(Task(task_description))

# Step: When the user clears the to-do list
@when('the user clears the to-do list')
def step_impl(context):
    to_do_list_manager.clear_tasks()


# Step: Then the to-do list should be empty
@then('the to-do list should be empty')
def step_impl(context):
    assert to_do_list_manager.tasks == [], 'To-do list is not empty'


# Step: Given the to-do list contains tasks:
@given('the to-do list contains tasks4')
def step_impl(context):
    for row in context.table:
        task_description = row['Task']
        task_status = True if row['Status'].lower() == 'completed' else False
        to_do_list_manager.add_task(Task(task_description, task_status))

# Step: When the user lists completed tasks
@when('the user lists completed tasks')
def step_impl(context):
    context.output = to_do_list_manager.list_completed_tasks()

# Step: Then the output should contain completed tasks:
@then('the output should contain completed tasks')
def step_impl(context):
    expected_output = context.text.strip()
    assert expected_output == context.output, f'Expected completed tasks output not found:\nExpected:\n{expected_output}\nActual:\n{context.output}'
