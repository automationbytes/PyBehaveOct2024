Feature: To test Sauce Demo website

  Scenario: Login Scenario
    Given the user launches the application
    Then the user verifies the application is loaded
    When the user enters the valid credentials
    And the user verifies the home page