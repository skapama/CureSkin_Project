# Created by kapam at 7/16/2023
Feature: CureSkin search tests

  Scenario: User can search cure product
   Given Open Cureskin main page
   When Click on search icon
   And  Input text cure
    And Click price sort button
   And Click price high to low
   Then verify filter applied