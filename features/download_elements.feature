Feature: Download elements
As a user I want to download current folder

    Scenario: Download current folder
        Given I'm logged in user
        When I select current folder
        And I click on submit download button
        Then the current folder is dwonloaded