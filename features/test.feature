Feature: Full On Net


  Scenario: Navigate on Full On Net
    Given a webpage 'http://www.full-on-net.com'
    When Accept cookies
    And open contact page
    Then Check we are here text


  Scenario Outline: Navigate on Full On Net
    Given a webpage '<url>'
    When Accept cookies
    """
    aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
    """
    And open contact page
      | column1 | column2 |
      | value1  | value2  |
      | value3  | value4  |
    Then Check we are here text is '<text>'

    Examples:
      | url                        | text        |
      | http://www.full-on-net.com | We are here |
#      | http://www.full-on-net.com    | We are here fail |
#      | http://www.full-on-netttt.com | We are here fail |