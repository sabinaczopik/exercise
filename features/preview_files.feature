Feature:Preview files
As a user I want to preview selected files

    Scenario: Preview selected files
        Given I'm logged in user
        When I choose preview selected files
        Then I see preview
