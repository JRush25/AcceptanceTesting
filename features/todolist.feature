Feature: To-Do list manager

Scenario: Add a task to the to-do list
Given the to-do list is empty
When the user adds a task "Buy groceries"
Then the to-do list should contain "Buy groceries"

Scenario: List all tasks in the to-do list
Given the to-do list contains tasks:
|Task|
|Pay bills|
When the user lists all tasks
Then the output should contain:
"""
Tasks
1.[Pending] Buy groceries
2.[Pending] Pay bills
"""

Scenario: Mark a task as completed
Given the to-do list contains tasks2:
| Task | Status |
| Buy groceries | Pending |
When the user marks task "Buy groceries" as completed
Then the to-do list should show task "Buy groceries" as completed

Scenario: Clear the entire to-do list
Given the to-do list contains tasks3:
| Task |
| Buy groceries |
| Pay bills |
When the user clears the to-do list
Then the to-do list should be empty

Scenario: List completed tasks
  Given the to-do list contains tasks4:
    | Task          | Status   |
    | Buy groceries | Completed |
    | Pay bills     | Pending   |
  When the user lists completed tasks
  Then the output should contain completed tasks:
    """
    Completed Tasks
    1. Buy groceries
    """
