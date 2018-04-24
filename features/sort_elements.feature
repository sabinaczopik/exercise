Feature: Sort elements by name
As a user I want to sort visiable elements by name

    Scenario: Sort elements ascending by name
        Given I'm logged in user
        When I choose sort by "Name" data
        And I choose "Ascending" order
        Then elements are sorted by "Ascending" name

    Scenario: Sort elements descending by name
        Given I'm logged in user
        When I choose sort by "Name" data
        And I choose "Descending" order
        Then elements are sorted by "Descending" name
