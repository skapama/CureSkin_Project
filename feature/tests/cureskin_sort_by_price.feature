# Created by kapam at 7/16/2023
 Feature: Search product cureskin tests
   Scenario: User can search product on cureskin
    Given Opens Cureskin Search page
    When Searches for the cure
    And Selects sort by price, high to low
    Then Verifies filter applied