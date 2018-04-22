Feature: Login
As a user I can login to the service

    Scenario: Login with correct password
        Given the main page is open
        When I enter "correct" password
        And I submit it
        Then I'm logged in user

    Scenario: Login with incorrect password
        Given the main page is open
        When I enter "incorrect" password
        And I submit it
        Then the validation mesage appers
