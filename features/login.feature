Feature: Login functionality

@smoke
Scenario: Successful login with valid credentials
Given  user is on login page
When  user enters valid username and password
And  click on login button
Then user should be navigate to the product page

@regression @negative
Scenario: Successful login with invalid credentials
Given  user is on login page
When  user enters invalid username and password
And  click on login button
Then user should be not navigate to the product page