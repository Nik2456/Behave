Feature: Login functionality

Scenario: Successful login with valid credentials
Given  user is on login page
When  user enters valid username and password
And  click on login button
Then user should be navigate to th product page