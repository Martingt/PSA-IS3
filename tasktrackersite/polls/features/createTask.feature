Feature: creating a task

  Scenario: add a simple task
     Given i am a employee
      When i create a task and i have permission to do so
      Then the task is successfully registered