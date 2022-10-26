Feature: Add to Cart

  Scenario: Add to Cart
    Given url 'https://www.demoblaze.com/index.html' opened
    When open login link
    When fill login form with 'fgordaliza' and '123456'
    When open laptop section
    When open item 'Sony vaio i7'
    When add item to cart
