Feature: View Health Records
Background:
          Given Chrome is opened and apollo247 app is opened
                Then Click on later button
                When User clicks on login/signUp button
                Then It shows the Mobile number window
                When User enter "7013064769"
                And User clicks on Next button
                Then It navigates to OTP window
                When User enters otp
                And User clicks on Next button
                Then It navigates to Home page
                When Clicks on view health records link
                Then It shows the health records page


   Scenario:To validate view health records is clickable


   Scenario:To validate Height field is clickable
     And Clicks on height button
     Then It shows update height window

   Scenario: To validate clinical documents link is clickable
    And Clicks on clinical documents link
    Then It shows reload page with clinical documents window

  Scenario Outline: To validate the Height with valid data
       And Clicks on height button
       Then It shows update height window
       When User enters <height>
       And Clicks on update button
       Then It updates the data
    Examples:
      | height |
      |   123  |

  Scenario Outline: To validate the Height with invalid data
      And Clicks on height button
      Then It shows update height window
      When User enters <height>
      Then It shows error message
    Examples:
      | height |
      |   1234 |
      |   as@  |










