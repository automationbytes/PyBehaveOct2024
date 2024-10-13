@Demo @Smoke
Feature: To test Sauce Demo website

  Background: Login Scenario
    Given the user launches the application
    Then the user verifies the application is loaded
    When the user enters the valid credentials
    And the user verifies the home page


  Scenario Outline: To Verify Filter Option
    And the user verifies the home page
    Then the user filters "<filter>"
    Examples:
      | filter |
#    |Name (Z to A)|
     |Price (low to high)|
#    |Price (high to low)|
#
#  Scenario: Logout
#    #And the user verifies the home page
#    Then the user logouts from the application
