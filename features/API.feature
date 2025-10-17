Feature:API testing
Scenario:Get single user
Given: i send a Get request to "https://reqres.in/api/users/2" with api key
Then: response status code should be 200