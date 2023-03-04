Feature: View Health Records

  Scenario: To validate the height  field with valid data
    Given Chrome is opened and app url is launched
    Then Clicks on later button
    When User clicks on the login/signup button
    Then It shows mobile number window
    When User enters "7013064769"
    And User clicks on the next button
    Then It navigates to the otp window
    When User enters the otp
    And  User clicks on the next button
    Then It navigates to the home page
    When User clicks on view health records link
    Then It shows health records page
    And User clicks on height button
    Then It shows the update window
    When User enters the height
    And User  clicks on update button
    Then It updates the height
