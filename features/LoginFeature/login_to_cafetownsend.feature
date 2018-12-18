# Created by piotrochojski at 2018-12-18
Feature: Login to CafeTownsend

Background:
Given user opens CafeTownsend application website


Scenario: Login with valid credentials
When user fills form with "valid" login and "valid" password
And user clicks Login button
Then user is redirected to application main page
And users username is shown

Scenario Outline: Trying to login with invalid credentials
When user fills form with "<loginIsValid>" login and "<passwordIsValid>" password
And user clicks Login button
Then invalid username or password label is shown
And user is redirected to login page

  Examples:
| loginIsValid | passwordIsValid |
| valid        | invalid         |
| invalid      | valid           |
| invalid      | invalid         |

Scenario Outline: Trying to login with empty credentials input
When user fills form with "<loginIsValid>" login and "<passwordIsValid>" password
And user clicks Login button
Then user is redirected to login page

  Examples:
| loginIsValid | passwordIsValid |
| valid        | empty           |
| empty        | empty           |
| empty        | valid           |