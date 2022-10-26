Feature: Sign Up

  Scenario: Sign Up
    Given url 'https://www.demoblaze.com/index.html' opened
    When open signup link
    When fill signup form with 'fgordaliza' and '123456'
    Then check signup confirmation